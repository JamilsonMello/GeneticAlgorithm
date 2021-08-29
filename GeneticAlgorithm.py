from random import random

class GeneticAlgorithm():
    def __init__(self, Individual, population_length):
        self.length = population_length
        self.population = []
        self.genetation = 0
        self.best_individual = 0
        self.individual = Individual

    def create_genetation(self, spaces, values, space_limit):
        for i in range(self.length):
            self.population.append(self.individual(spaces, values, space_limit))
        
        self.best_individual = self.population[0]

    def __sorted_by_best_individual(self):
        self.population = sorted(self.population, key=lambda population: population.score, reverse=True)

    def __best_individual(self, individual):
        if individual.score > self.best_individual.score:
            self.best_individual = individual

    def __sum_scores_generation(self):
        sum = 0

        for individual in self.population:
            sum += individual.score
        
        return sum

    def __select_individual(self, sum_scores):
        individual = -1
        raffled_value = random() * sum_scores
        sum = 0
        counter = 0

        while counter < len(self.population) and sum < raffled_value:
            sum += self.population[counter].score
            individual = individual + 1
            counter += 1

        return individual

    def view(self):
        best = self.population[0]

        print(f"Geração: {self.population[0].generation}")
        print(f"Valor: {best.score}")
        print(f"Espaço: {best.space_used}")
        print(f"Cromossomo: {best.chromosome}")

    def builder(self, mutation_tax, generations, spaces, values, space_limit):
        self.create_genetation(spaces, values, space_limit)

        for individual in self.population:
            individual.fitness()

        self.__sorted_by_best_individual()

        self.view()

        for genetation in range(generations):
            sum_scores_generation = self.__sum_scores_generation()
            new_genetation = []
            
            for individual_created in range(0, self.length, 2):
                father = self.__select_individual(sum_scores_generation)
                mother = self.__select_individual(sum_scores_generation)

                children = self.population[father].crossover(self.population[mother])

                new_genetation.append(children[0].mutation(mutation_tax))
                new_genetation.append(children[1].mutation(mutation_tax))
            
            self.population = list(new_genetation)

            for individual in self.population:
                individual.fitness()

            self.__sorted_by_best_individual()
            self.view()
            self.__best_individual(self.population[0])

        print(f"Melhor solução: {self.best_individual.generation}")
        print(f"Melhor Valor: {self.best_individual.score}")
        print(f"Espaço: {self.best_individual.space_used}")
        print(f"Cromossomo: {self.best_individual.chromosome}")

        return self.best_individual.chromosome