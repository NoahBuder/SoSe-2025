import my_functions  # Ohne .py

if __name__ == "__main__":
    person  = my_functions.build_person("Noah","Buder", "Male", 20)
    experiment = my_functions.build_experiment("Test","21.03.2025", "Alex", "running")
    print(person)
    print(experiment)
