from typing import Dict

first_experiment_id = []

creation_date = "13.03.2025"

namen = ("Noah", "Justin", "Jonathan", "Samuel", "Moritz", "Niklas", "Mappelmann", "Olivia", "Julius", "Magnus" )

supervisor = "Alex"

 

def validate_id(Id_Nummer:int) -> bool:

    try:

        int(Id_Nummer)

        return True

    except:

        print ("Id_Nummer muss eine ganze Zahl sein und im Bereich  von 1 bis 10 liegen")

        return False

 

for i in range(1, 11):

    if validate_id(i):

        experiment: Dict[str, object] = {

            "supervisor": supervisor,

            "creation-date": creation_date,

            "Id_Nummer": i,

            "Name": namen[i-1]

        }

 

        first_experiment_id.append(experiment)

for Experiment in first_experiment_id:

    if Experiment["Id_Nummer"] > 5:

            break

    print(Experiment)

gerade_id = sum(Id_Nummer % 2 == 0 for Id_Nummer in range(1, 11))

print("Die Anzahl der geraden Nummern von der Liste Beträgt:", gerade_id)