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
    test.describe(`Dashboard Hidroponik - Data Real-time (@${member.name})`, () => {
        test('Dashboard memperbarui data sensor secara real-time', async ({ page }) => {
            const dummyData = [
                { temperature: 25, humidity: 60, moisture: 40 },
                { temperature: 26, humidity: 61, moisture: 42 },
                { temperature: 27, humidity: 62, moisture: 44 }
            ];

            let index = 0;

            await page.route('**/api/sensors', async route => {
                const data = dummyData[index];

                index = (index + 1) % dummyData.length;

                await route.fulfill({
                    status: 200,
                    contentType: 'application/json',
                    body: JSON.stringify(data)
                });
            });

            await page.goto(member.path);

            await expect(page.locator('#data-suhu')).toHaveText('Suhu: 25°C');

            await page.waitForTimeout(1100);
            await expect(page.locator('#data-suhu')).toHaveText('Suhu: 26°C');

            await page.waitForTimeout(1100);
            await expect(page.locator('#data-suhu')).toHaveText('Suhu: 27°C');
        });
    });
}
