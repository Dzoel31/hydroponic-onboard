import pytest
from pydantic import ValidationError


def test_level_2_schema_sensor_menerima_data_valid():
    from schemas.sensor import SensorData

    data = SensorData(temperature=25, humidity=60, moisture=40)

    assert data.temperature == 25
    assert data.humidity == 60
    assert data.moisture == 40


def test_level_2_schema_sensor_menolak_persen_di_luar_range():
    from schemas.sensor import SensorData

    with pytest.raises(ValidationError):
        SensorData(temperature=25, humidity=101, moisture=40)

    with pytest.raises(ValidationError):
        SensorData(temperature=25, humidity=60, moisture=-1)


def test_level_2_schema_sensor_wajib_punya_tiga_field_utama():
    from schemas.sensor import SensorData

    with pytest.raises(ValidationError):
        SensorData(temperature=25, humidity=60)
