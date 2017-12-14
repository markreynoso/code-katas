"""Test flight paths."""


def test_flight_path_when_no_path():
    """Test flight path when no path exists."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Garowe', 'Hargeisa')
    assert output == 'There is no path between these cities'


def test_flight_path_returns_correct_path_and_distance():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Juba', 'Khartoum')
    print(output)
    assert output == 1000


    Juba: 20
        Nairobi: 16
        Kigal:
        Cairo: 54
            Nairobi: 16
            Asmara: 26
                Dubai: 394
                Cairo: 54
                Khartoum: 78
            Aswan:
        Dubai: 394

