import random

def fitness_function(params, rpm, load, temp, speed):
    injection, afr, ignition, throttle = params
    base_efficiency = (100 - abs(14.7 - afr)) * (1 - abs(throttle - 50)/100) - abs(injection - 10)
    condition_penalty = abs(rpm - 2500)/1000 + abs(load - 50)/50 + abs(temp - 25)/10 + abs(speed - 60)/30
    return base_efficiency - condition_penalty

def mutate(chromosome):
    return [gene + random.uniform(-1, 1) for gene in chromosome]

def crossover(parent1, parent2):
    return [(g1 + g2) / 2 for g1, g2 in zip(parent1, parent2)]

def run_ga(inputs):
    rpm = float(inputs.get("rpm", 2500))
    load = float(inputs.get("load", 50))
    temp = float(inputs.get("temp", 25))
    speed = float(inputs.get("speed", 60))

    pop_size = 10
    generations = 50
    population = [[random.uniform(5, 15), random.uniform(12, 16), random.uniform(5, 15), random.uniform(0, 100)] for _ in range(pop_size)]

    for _ in range(generations):
        population.sort(key=lambda x: -fitness_function(x, rpm, load, temp, speed))
        next_gen = population[:2]
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:5], 2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)
        population = next_gen

    best = max(population, key=lambda x: fitness_function(x, rpm, load, temp, speed))
    return {
        "fuel_injection": round(best[0], 2),
        "air_fuel_ratio": round(best[1], 2),
        "ignition_timing": round(best[2], 2),
        "throttle_position": round(best[3], 2),
        "efficiency_score": round(fitness_function(best, rpm, load, temp, speed), 2)
    }
