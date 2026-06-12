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
    test.describe(`Dashboard Hidroponik - Format Data (@${member.name})`, () => {
        test('Harus menampilkan data suhu yang benar', async ({ page }) => {
            await page.goto(member.path);
            const teksSuhu = page.locator('#data-suhu');
            await expect(teksSuhu).toHaveText(/Suhu: \d+°C/);
        });

        test('Harus menampilkan data kelembaban yang benar', async ({ page }) => {
            await page.goto(member.path);
            const teksKelembaban = page.locator('#data-kelembaban');
            await expect(teksKelembaban).toHaveText(/Kelembaban: \d+%/);
        });

        test('Harus menampilkan data moisture yang benar', async ({ page }) => {
            await page.goto(member.path);
            const teksMoisture = page.locator('#data-moisture');
            await expect(teksMoisture).toHaveText(/Moisture: \d+%/);
        });
    });
}
