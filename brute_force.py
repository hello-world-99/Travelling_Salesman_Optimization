import itertools
import datetime
from util import City, read_cities, write_cities_and_return_them, generate_cities, path_cost, visualize_tsp

start_time = datetime.datetime.now()


class BruteForce:

    def __init__(self, cities):
        self.cities = cities

    def run(self):
        self.cities = min(itertools.permutations(self.cities), key=lambda path: path_cost(path))
        return path_cost(self.cities)


if __name__ == "__main__":
    brute = BruteForce(read_cities(12))
    print(brute.run())
    end_time = datetime.datetime.now() - start_time
    print("--- %s seconds ---" % (end_time.total_seconds()))
    visualize_tsp('Brute force TSP', brute.cities)
