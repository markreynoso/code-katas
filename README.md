# code-katas

Day of Code Wars Challenges

Code Fellows 401 project to complete Code Wars Katas in 12 hours. 
Each Kyu is ranked as follows:
- 8th kyu: 1 
- 7th kyu: 2 
- 6th kyu: 4 
- 5th kyu: 5 
- 4th kyu: 6 
- 3rd kyu: 8 
- 2nd kyu: 9 
- 1st kyu: 10
The goal is to complete 20pts worth of Katas with any combination of Katas. 

# Completed Katas:

**Exclamation Marks Series #6 (8th kyu)**

- **Module**: `exclamation_marks_series_6.py`
- **Tests**: `test_exclamation_marks_series_6.py`
- **URL**: [challenge url](https://www.codewars.com/kata/exclamation-marks-series-number-6-remove-n-exclamation-marks-in-the-sentence-from-left-to-right/python)

**What's The Real Floor (8th kyu)**

- **Module**: `whats_the_real_floor.py`
- **Tests**: `test_whats_the_real_floor.py`
- **URL**: [challenge url](https://www.codewars.com/kata/whats-the-real-floor/python)

**Sum of Two Lowest Possible Integers (7th kyu)**

- **Module**: `sum_of_two_lowest_possible_integers.py`
- **Tests**: `test_sum_of_two_lowest_possible_integers.py`
- **URL**: [challenge url](https://www.codewars.com/kata/sum-of-two-lowest-positive-integers/python)

**List Filtering (7th kyu)**

- **Module**: `list_filtering.py`
- **Tests**: `list_filtering_test.py`
- **URL**: [challenge url](https://www.codewars.com/kata/list-filtering/python)

**Simple Pig Latin (5th kyu)**

- **Module**: `simple_pig_latin.py`
- **Tests**: `simple_pig_latin_test.py`
- **URL**: [challenge url](https://www.codewars.com/kata/simple-pig-latin/python)

**Changing Letters (7th kyu)**

- **Module**: `changing_letters.py`
- **Tests**: `changing_letters_test.py`
- **URL**: [challenge url](http://www.codewars.com/kata/changing-letters/python)

**Find the Odd Int (6th kyu)**

- **Module**: `find_the_odd_int.py`
- **Tests**: `find_the_odd_int_test.py`
- **URL**: [challenge url](http://www.codewars.com/kata/find-the-odd-int/python)

**Multiples of 3 and 5 (6th kyu)**

- **Module**: `multiples_of_3_and_5.py`
- **Tests**: `multiples_of_3_and_5_test.py`
- **URL**: [challenge url](https://www.codewars.com/kata/multiples-of-3-and-5/python)

**Sum of the first nth Term of a Series (7th kyu)**

- **Module**: `sum_of_nth_terms.py`
- **Tests**: `sum_of_nth_terms_test.py`
- **URL**: [challenge url](http://www.codewars.com/kata/sum-of-the-first-nth-term-of-series/python)

# Flight Paths

Using data found here [url](https://codefellows.github.io/sea-python-401d6/_downloads/cities_with_airports.json) and a method for calculating distance between two points using latitude and longitude, found here [url](https://codefellows.github.io/sea-python-401d6/assignments/kata_flight_paths.html), I implemented a method to calculate the shortest path and route cities to travel in order to travel between two given cities. Drawing from the Dijkstra algorithm, find_the_path_between_cities() will make a request to the supplied json data and sort through all paths from a given city until it finds the destination city or finds no route at all. It will keep track of which path will produce the shortest path and return both a list of the cities traveled and the distance from beginning to end. 

- **find_the_path_between_cities(city1, city2)** - O(n**2)

