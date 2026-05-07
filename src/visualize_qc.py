import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../results/qc_results.csv")

# GC Plot
plt.figure(figsize=(8,5))

plt.bar(df["File"], df["Average GC %"])

plt.title("GC Content")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../results/gc_content_plot.png")

print("GC plot saved")


# مهم جدًا
plt.close()


# Q30 Plot
plt.figure(figsize=(8,5))

plt.bar(df["File"], df["Average Q30 %"])

plt.title("Q30 Scores")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../results/q30_plot.png")

print("Q30 plot saved")

plt.close()