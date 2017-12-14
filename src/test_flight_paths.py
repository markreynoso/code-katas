"""Test flight paths."""


def test_flight_path_when_no_path():
    """Test flight path when no path exists."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Garowe', 'Hargeisa')
    assert output == 'There is no path between these cities'


def test_flight_path_returns_correct_path_and_distance_one_city():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Juba', 'Khartoum')
    assert output == (['Juba', 'Khartoum'], 743.328584586253)


def test_flight_path_returns_correct_path_and_distance_three_cities():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Juba', 'Amsterdam')
    assert output == (['Juba', 'Kigali', 'Amsterdam'], 4513.677071138924)


def test_flight_path_returns_correct_path_and_distance_four_cities():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Juba', 'Vancouver')
    assert output == (['Juba', 'Cairo', 'Amsterdam', 'Vancouver'],
                      8576.329728079483)


def test_flight_path_returns_correct_path_and_distance_to_seattle():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Juba', 'Seattle')
    assert output == (['Juba', 'Cairo', 'Munich', 'Seattle'],
                      8637.558154892897)


def test_flight_path_returns_correct_path_and_distance_houston_to_seattle():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Seattle', 'Houston')
    assert output == (['Seattle', 'Anchorage', 'Houston'], 4702.33921690171)


def test_flight_path_returns_correct_path_and_distance_seattle_to_bogata():
    """Test flight path returns correct path and distance."""
    from flight_paths import find_path_between_cities
    output = find_path_between_cities('Seattle', 'London')
    assert output == (['Seattle', 'Anchorage', 'Vancouver', 'London'],
                      7488.286376146534)
