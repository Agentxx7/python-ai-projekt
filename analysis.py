# Vi importerar pandas för att läsa CSV-filen.
import pandas as pd

# Vi importerar matplotlib för att kunna skapa en visualisering.
import matplotlib.pyplot as plt

# Vi importerar train_test_split för att dela upp datat i träningsdata och testdata.
from sklearn.model_selection import train_test_split

# Vi importerar RandomForestClassifier, som är modellen vi ska använda.
from sklearn.ensemble import RandomForestClassifier

# Här importerar vi mått för att utvärdera modellen.
from sklearn.metrics import accuracy_score, classification_report

# Här läser vi in datasetet från CSV-filen.
df = pd.read_csv("job_match_dataset.csv")

# Här skriver vi ut information om datasetet.
print("Information om datasetet:")
print(df.info())

# Här skriver vi ut grundläggande statistik.
print("\nStatistik för datasetet:")
print(df.describe())

# Här räknar vi hur många kandidater som matchar jobbet och inte matchar jobbet.
match_counts = df["job_match"].value_counts().sort_index()

# Här skapar vi ett stapeldiagram.
match_counts.plot(kind="bar")

# Här sätter vi rubrik och namn på axlarna.
plt.title("Antal kandidater som matchar jobbet eller inte")
plt.xlabel("Job match (0 = inte match, 1 = match)")
plt.ylabel("Antal kandidater")

# Här visar vi diagrammet.
plt.show()

# X innehåller all indata till modellen.
# Vi tar bort kolumnen job_match eftersom den är facit.
X = df.drop("job_match", axis=1)

# y är målvariabeln som modellen ska försöka förutsäga.
y = df["job_match"]

# Här delar vi upp datat i träningsdata och testdata.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Här skapar vi modellen.
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Här tränar vi modellen på träningsdatan.
model.fit(X_train, y_train)

# Här gör modellen förutsägelser på testdatan.
y_pred = model.predict(X_test)

# Här räknar vi ut accuracy.
accuracy = accuracy_score(y_test, y_pred)

# Här skriver vi ut resultatet.
print("\nAccuracy:", accuracy)

# Här skriver vi ut classification report.
print("\nClassification report:")
print(classification_report(y_test, y_pred))