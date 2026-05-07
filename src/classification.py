import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# قراءة البيانات
df = pd.read_csv("../results/qc_results.csv")


# تحويل الـ labels لأرقام
# case = 1
# control = 0

df["Class"] = df["Class"].map({
    "case": 1,
    "control": 0
})


# Features
X = df[[
    "Average GC %",
    "Average Length",
    "Average Q20 %",
    "Average Q30 %"
]]


# Labels
y = df["Class"]


# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# إنشاء الموديل
model = RandomForestClassifier()


# تدريب الموديل
model.fit(X_train, y_train)


# التوقع
y_pred = model.predict(X_test)


# حساب الدقة
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.2f}")


# تقرير التصنيف
print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))