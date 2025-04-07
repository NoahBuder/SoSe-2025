import random
from datetime import date
from typing import List, Dict, Union
Names = ["Anna", "Ben", "Clara", "Justin", "Noah", "David", "Elena", "Felix", "Gina", "Hannes"]
def create_experiments(first_experiment_id: Union[int, str, float]) -> List[Dict[str, Union[int]]]:
    experiments = []
    today = date.today().isoformat()
    try:
        first_experiment_id = int(first_experiment_id)
    except ValueError:
        print("Fehler: Die ID muss eine ganze Zahl sein.")
        return[]
    for i in range(10):
        experiment = {
            "id": first_experiment_id + i,
            "Name": random.choice(Names),
            "Datum": today}
        experiments.append(experiment)
    return experiments
def display_experiments(experiments: List[Dict[str, Union[int, str]]]) -> None:
    print("Erste Zehn Experimente:")
    for experiment in experiments[:10]:
        print(experiment)
def count_even_ids(experiments: List[Dict[str, Union[int]]]) -> int:
    return sum(1 for exp in experiments if exp["id"] % 2==0)
first_experiment_id = input("Geben Sie die Start ID ein: ")
experiments = create_experiments(first_experiment_id)

if experiments:
    display_experiments(experiments)
    even_count = count_even_ids(experiments)
    print("Anzahl der Experimente mit gerader ID: {even_count}")

    #Numpy installiert
