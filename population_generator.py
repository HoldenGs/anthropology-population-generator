
import random



class Population:

    def __init__(self):
        reds = []
        for i in range(0, 20):
            reds += ["Red"]

        whites = []
        for i in range(0, 20):
            whites += ["White"]

        alleles = []

        while reds or whites:
            coinflip = random.randint(0, 1)
            if coinflip and reds:
                alleles += [reds.pop()]
            elif whites:
                alleles += [whites.pop()]
        
        self.population = []

        while alleles:
            ind = Individual(alleles.pop(), alleles.pop())
            self.population += [ind]
    
    def new_generation(self):
        old_population = self.population

        alleles = []
        for i in old_population:
            alleles.append(i.alleles[0])
            alleles.append(i.alleles[1])

        random.shuffle(alleles)

        new_population = []

        while alleles:
            ind = Individual(alleles.pop(), alleles.pop())
            new_population += [ind]
        
        self.population = new_population

    def remove_recessive_homozygous_white(self):
        for i in self.population:
            if i.alleles == ["White", "White"]:
                self.population.remove(i)
    
    def print_individuals(self):
        for c, i in enumerate(self.population):
            print(c + 1, i.alleles)

    def catastrophe(self, survivor_count):
        self.population = self.population[:survivor_count]



class Individual:

    def __init__(self, allele1, allele2):
        self.sex = None
        self.alleles = []
        self.alleles += [allele1]
        self.alleles += [allele2]



# Problem 1

print("\nProblem 1")

# Step 1

population0 = Population()

print("\nStep 2\n")

population0.print_individuals()


# Step 3

population0.remove_recessive_homozygous_white()

# Step 4

print("\nStep 4\n")

population0.new_generation()

population0.print_individuals()

# Step 5

print("\nStep 5\n")

for _ in range(1):
    population0.remove_recessive_homozygous_white()
    population0.new_generation()

population0.print_individuals()

# Problem 2

print("\nProblem 2")

# Step 1

print("\nStep 1\n")

population1 = Population()

population1.catastrophe(5)

population1.print_individuals()

# Step 2

print("\nStep 2\n")

population1 = Population()

population1.catastrophe(2)

population1.print_individuals()

# Problem 3

print("\nProblem 3")

# Step 1

print("\nStep 1\n")

island_1_population = []

for i in range(6):
    if i < 3:
        ind = Individual("White", "White")
    elif i < 5:
        ind = Individual("Red", "White")
    else:
        ind = Individual("Red", "Red")
    ind.sex = "M"
    island_1_population.append(ind)

print("\nStep 2\n")

island_2_population = []

for i in range(10):
    ind = Individual("Red", "Red")
    if i < 2:
        ind.sex = "M"
    else:
        ind.sex = "F"
    island_2_population.append(ind)

print("\nStep 3\n")

islands_combined_population = island_1_population + island_2_population

random.shuffle(islands_combined_population)

males = []
females = []
for i in islands_combined_population:
    if i.sex == "M":
        males.append(i)
    elif i.sex == "F":
        females.append(i)

next_generation = []
while males or females:
    male = males.pop()
    female = females.pop()

    coinflip1 = random.randint(0, 1)
    coinflip2 = random.randint(0, 1)

    ind1 = Individual(male.alleles[coinflip1], female.alleles[coinflip2])

    coinflip1 = random.randint(0, 1)
    coinflip2 = random.randint(0, 1)

    ind2 = Individual(male.alleles[coinflip1], female.alleles[coinflip2])

    next_generation.append(ind1)
    next_generation.append(ind2)

for c, i in enumerate(next_generation):
    print(c + 1, i.alleles)
