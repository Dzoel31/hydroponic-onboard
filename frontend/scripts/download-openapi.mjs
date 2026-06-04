import { writeFile } from "node:fs/promises";

const openApiUrl = process.env.VITE_OPENAPI_URL ?? "http://127.0.0.1:8000/openapi.json";

const response = await fetch(openApiUrl);

if (!response.ok) {
  throw new Error(`Failed to download OpenAPI schema from ${openApiUrl}`);
}

const schema = await response.text();
await writeFile("openapi.json", schema);

console.log(`Downloaded OpenAPI schema from ${openApiUrl}`);
