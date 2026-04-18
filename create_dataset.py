# Vi importerar biblioteket csv så att vi kan skapa och skriva en CSV-fil.
import csv

# Vi importerar random för att kunna skapa exempeldata med lite variation.
import random

# Detta gör att samma "slumpmässiga" data skapas varje gång vi kör filen.
random.seed(42)

# Här bestämmer vi namnet på filen som ska skapas.
filename = "job_match_dataset.csv"

# Här skapar vi en lista med rubrikerna till våra kolumner i CSV-filen.
# Varje kolumn motsvarar en egenskap hos kandidaten eller facit för matchning.
headers = [
    "education_level",
    "years_experience",
    "python_skill",
    "sql_skill",
    "communication_skill",
    "english_level",
    "job_match"
]

# Här skapar vi en tom lista där alla rader i datasetet ska sparas.
rows = []

# Här bestämmer vi hur många kandidater vi vill skapa i datasetet.
# 120 rader är lagom.
for i in range(120):

    # education_level:
    # 1 = gymnasium
    # 2 = yrkesutbildning
    # 3 = högskola/universitet
    education_level = random.choice([1, 2, 3])

    # years_experience:
    # antal års erfarenhet mellan 0 och 10
    years_experience = random.randint(0, 10)

    # python_skill:
    # 0 = kandidaten kan inte Python
    # 1 = kandidaten kan Python
    python_skill = random.choice([0, 1])

    # sql_skill:
    # 0 = kandidaten kan inte SQL
    # 1 = kandidaten kan SQL
    sql_skill = random.choice([0, 1])

    # communication_skill:
    # 0 = låg/saknas
    # 1 = finns
    communication_skill = random.choice([0, 1])

    # english_level:
    # 1 = låg
    # 2 = medel
    # 3 = hög
    english_level = random.choice([1, 2, 3])

    # Här bygger vi en enkel poängmodell för att avgöra om kandidaten är en match.
    # Detta är inte maskininlärning ännu.
    # Det är bara ett sätt att skapa ett träningsdataset med ett tydligt mönster.
    score = 0

    # Högre utbildningsnivå ger lite högre poäng.
    score += education_level * 1.0

    # Fler års erfarenhet ger också högre poäng.
    score += years_experience * 0.7

    # Python är viktigt i vårt exempel, så det ger extra poäng.
    score += python_skill * 2.0

    # SQL ger också extra poäng.
    score += sql_skill * 1.5

    # Kommunikationsförmåga ger också ett litet plus.
    score += communication_skill * 1.0

    # Engelska kan spela roll, så även det ger poäng.
    score += english_level * 0.8

    # Här lägger vi till lite slumpmässig variation.
    # Det gör datat mindre mekaniskt och lite mer verklighetsnära.
    score += random.uniform(-1.0, 1.0)

    # Här sätter vi facit-kolumnen job_match.
    # Om den totala poängen är tillräckligt hög blir kandidaten en match (1),
    # annars inte en match (0).
    if score >= 8:
        job_match = 1
    else:
        job_match = 0

    # Här samlar vi alla värden för en kandidat i en rad.
    row = [
        education_level,
        years_experience,
        python_skill,
        sql_skill,
        communication_skill,
        english_level,
        job_match
    ]

    # Här lägger vi till raden i listan med alla rader.
    rows.append(row)

# Här öppnar vi filen för att skriva till den.
# "w" betyder write, alltså skriva.
# newline="" gör att vi slipper töma rader mellan dataraderna i Windows.
with open(filename, "w", newline="", encoding="utf-8") as file:

    # Här skapar vi ett skrivobjekt som kan skriva CSV-format.
    writer = csv.writer(file)

    # Här skriver vi först kolumnrubrikerna.
    writer.writerow(headers)

    # Här skriver vi sedan alla datarader.
    writer.writerows(rows)

# Här skriver vi ut ett meddelande i terminalen så att vi ser att filen skapats.
print(f"Datasetet har skapats: {filename}")
print(f"Antal rader: {len(rows)}")