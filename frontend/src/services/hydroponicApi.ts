import { OpenAPI } from "../api/core/OpenAPI";
import type { HydroponicCreate } from "../api/models/HydroponicCreate";
import type { HydroponicListResponse } from "../api/models/HydroponicListResponse";
import type { HydroponicRead } from "../api/models/HydroponicRead";
import { HydroponicsService } from "../api/services/HydroponicsService";

OpenAPI.BASE = import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

export function getHydroponicData(): Promise<HydroponicListResponse> {
  return HydroponicsService.listHydroponicDataHydroponicsGet();
}

export function createHydroponicData(
  payload: HydroponicCreate,
): Promise<HydroponicRead> {
  return HydroponicsService.createHydroponicDataHydroponicsPost(payload);
}
