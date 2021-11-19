LOCUST_PLAGUE_POPULATION = 30_000_000_000
POPULATION_THRESHOLD = 1_000_000_000


def to_locust_units(population):
    return population / LOCUST_PLAGUE_POPULATION


world_population = [

    585_000_000,
    660_000_000,
    740_000_000,
    978_000_000,
    1_650_000_000,
    6_008_000_000,
    7_052_000_000,

]

my_list = [to_locust_units(i) for i in world_population if i < 1_000_000_000]

print(my_list)
