<script setup lang="ts">
import { computed, onMounted, reactive, ref } from "vue";
import { createHydroponicData, getHydroponicData } from "./services/hydroponicApi";
import type { HydroponicCreate } from "./api/models/HydroponicCreate";
import type { HydroponicRead } from "./api/models/HydroponicRead";

const readings = ref<HydroponicRead[]>([]);
const isLoading = ref(false);
const isSaving = ref(false);
const errorMessage = ref("");

const form = reactive<HydroponicCreate>({
  moisture: 80,
  temperature: 27.1,
  humidity: 67.5,
  ph: 6.1,
  ec: 1.45,
});

const latestReading = computed(() => readings.value[0]);

async function loadReadings() {
  isLoading.value = true;
  errorMessage.value = "";

  try {
    const response = await getHydroponicData();
    readings.value = response.data;
  } catch (error) {
    errorMessage.value =
      error instanceof Error ? error.message : "Gagal mengambil data hidroponik.";
  } finally {
    isLoading.value = false;
  }
}

async function submitReading() {
  isSaving.value = true;
  errorMessage.value = "";

  try {
    const created = await createHydroponicData({ ...form });
    readings.value = [created, ...readings.value];
  } catch (error) {
    errorMessage.value =
      error instanceof Error ? error.message : "Gagal menyimpan data hidroponik.";
  } finally {
    isSaving.value = false;
  }
}

onMounted(loadReadings);
</script>

<template>
  <main class="app-shell">
    <section class="page-header">
      <div>
        <p class="eyebrow">Hydroponic Onboard</p>
        <h1>Dashboard data sensor</h1>
        <p class="intro">
          Contoh frontend kecil untuk membaca dan mengirim data hidroponik ke backend FastAPI.
        </p>
      </div>
      <button type="button" class="secondary-button" :disabled="isLoading" @click="loadReadings">
        Refresh
      </button>
    </section>

    <section class="summary-grid" aria-label="Ringkasan data terbaru">
      <article class="metric-card">
        <span>Moisture</span>
        <strong>{{ latestReading?.moisture ?? "-" }}%</strong>
      </article>
      <article class="metric-card">
        <span>Temperature</span>
        <strong>{{ latestReading?.temperature ?? "-" }} C</strong>
      </article>
      <article class="metric-card">
        <span>pH</span>
        <strong>{{ latestReading?.ph ?? "-" }}</strong>
      </article>
      <article class="metric-card">
        <span>EC</span>
        <strong>{{ latestReading?.ec ?? "-" }}</strong>
      </article>
    </section>

    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>

    <section class="content-grid">
      <form class="panel" @submit.prevent="submitReading">
        <div class="panel-header">
          <h2>Tambah data</h2>
          <p>Form ini mengirim request POST ke endpoint backend.</p>
        </div>

        <label>
          Moisture (%)
          <input v-model.number="form.moisture" type="number" min="0" max="100" required />
        </label>

        <label>
          Temperature (C)
          <input v-model.number="form.temperature" type="number" min="0" step="0.1" required />
        </label>

        <label>
          Humidity (%)
          <input v-model.number="form.humidity" type="number" min="0" max="100" step="0.1" required />
        </label>

        <label>
          pH
          <input v-model.number="form.ph" type="number" min="0" step="0.1" required />
        </label>

        <label>
          EC
          <input v-model.number="form.ec" type="number" min="0" step="0.01" required />
        </label>

        <button type="submit" class="primary-button" :disabled="isSaving">
          {{ isSaving ? "Menyimpan..." : "Simpan data" }}
        </button>
      </form>

      <section class="panel">
        <div class="panel-header">
          <h2>Riwayat pembacaan</h2>
          <p>Data dari endpoint GET ditampilkan dalam tabel sederhana.</p>
        </div>

        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>Moisture</th>
                <th>Temp</th>
                <th>Humidity</th>
                <th>pH</th>
                <th>EC</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="isLoading">
                <td colspan="5">Memuat data...</td>
              </tr>
              <tr v-else-if="readings.length === 0">
                <td colspan="5">Belum ada data.</td>
              </tr>
              <tr v-for="reading in readings" :key="reading.id">
                <td>{{ reading.moisture }}%</td>
                <td>{{ reading.temperature }} C</td>
                <td>{{ reading.humidity }}%</td>
                <td>{{ reading.ph }}</td>
                <td>{{ reading.ec }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </section>
  </main>
</template>
