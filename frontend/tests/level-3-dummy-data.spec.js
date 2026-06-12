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
    test.describe(`Dashboard Hidroponik - Dummy Data (@${member.name})`, () => {
        test('Harus menampilkan data sensor yang benar', async ({ page }) => {
            await page.route('**/api/sensors', async route => {
                await route.fulfill({
                    status: 200,
                    contentType: 'application/json',
                    body: JSON.stringify({
                    temperature: 25,
                    humidity: 60,
                    moisture: 40
                })
            });
        });

        await page.goto(member.path);

        await expect(page.locator('#data-suhu')).toHaveText('Suhu: 25°C');
        await expect(page.locator('#data-kelembaban')).toHaveText('Kelembaban: 60%');
        await expect(page.locator('#data-moisture')).toHaveText('Moisture: 40%');
        });
    });
}
