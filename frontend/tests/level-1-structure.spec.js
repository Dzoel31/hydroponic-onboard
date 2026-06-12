const { test, expect } = require('@playwright/test');

const members = [
    {
        name: 'Aniqah',
        path: '/aniqah/',
    },
    {
        name: 'Syahla',
        path: '/syahla/',
    },
];

for (const member of members) {
    test.describe(`Dashboard Hidroponik - Struktur Dasar (@${member.name})`, () => {
        test('Memiliki class "dashboard", header, dan judul yang sesuai', async ({ page }) => {
            await page.goto(member.path);

            const dashboard = page.locator('.dashboard');
            await expect(dashboard).toBeVisible();

            const header = dashboard.locator('.header');
            await expect(header).toBeVisible();

            const judul = header.locator('h1');
            await expect(judul).toHaveText(/Dashboard Hidroponik/);
        });

        test('Memiliki elemen untuk menampilkan data suhu, kelembaban, dan moisture', async ({ page }) => {
            await page.goto(member.path);
            await expect(page.locator('#data-suhu.sensor-card')).toBeVisible();
            await expect(page.locator('#data-kelembaban.sensor-card')).toBeVisible();
            await expect(page.locator('#data-moisture.sensor-card')).toBeVisible();
        });
    });
}