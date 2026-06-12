from fastapi.routing import APIRoute

from conftest import get_fastapi_app


def test_level_1_main_memiliki_fastapi_app():
    app = get_fastapi_app()

    assert app.title, "FastAPI app sebaiknya punya title agar mudah dikenali di /docs."


def test_level_1_app_memasang_route_api_sensors():
    app = get_fastapi_app()

    sensor_routes = [
        route
        for route in app.routes
        if isinstance(route, APIRoute) and route.path == "/api/sensors"
    ]

    assert sensor_routes, (
        "Belum ada route `/api/sensors`. "
        "Clue: buat router di folder routes, lalu pasang router itu di main.py."
    )

    methods = set().union(*(route.methods for route in sensor_routes))
    assert "GET" in methods, (
        "Route `/api/sensors` harus bisa menerima GET. "
        "Clue: gunakan decorator `@router.get(...)`."
    )
