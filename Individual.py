import random

class Individual():
    def __init__(self, spaces, values, limit_spaces, generation = 0):
        self.spaces = spaces
        self.values = values
        self.limit_spaces = limit_spaces
        self.generation = generation
        self.score = 0
        self.space_used = 0
        self.chromosome = self.__create_chromosome()

    def __create_chromosome(self):
        return [random.randint(0, 1) for i in range(len(self.spaces))]
    
    def fitness(self):
        score = 0
        sum_spaces = 0
        length = len(self.chromosome)

        for gene in range(length):
            if self.chromosome[gene] == 1:
                score += self.values[gene]
                sum_spaces += self.spaces[gene]

        if sum_spaces > self.limit_spaces:
            score = 1
        
        self.score = score
        self.space_used = sum_spaces
    
    def crossover(self, mother):
        cut = round(random.random() * len(self.chromosome))
        father = self.chromosome

        first_child = mother.chromosome[0:cut] + father[cut::]
        second_child = father[0:cut] + mother.chromosome[cut::]

        children = [Individual(self.spaces, self.values, self.limit_spaces, self.generation + 1),
                    Individual(self.spaces, self.values, self.limit_spaces, self.generation + 1)]

        children[0].chromosome = first_child
        children[1].chromosome = second_child

        return children

    def mutation(self, tax):
        is_a_mutation = random.random() < tax

        for gene in self.chromosome:
            if is_a_mutation:
                if self.chromosome[gene] == 1:
                    self.chromosome[gene] = 0
                else:
                    self.chromosome[gene] = 1

        return self
