import my_functions  # Ohne .py

if __name__ == "__main__":
    person  = my_functions.build_person("Bundschuh","Justin", "Male", 21)
    experiment = my_functions.build_experiment("Test","23.03.2025", "John", "running")
    print(person)
    print(experiment)
