from pathlib import Path
from Bio import SeqIO
import pandas as pd

# حساب GC Content
def calculate_gc(sequence):

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100


# حساب Q20
def calculate_q20(qualities):

    q20_bases = sum(q >= 20 for q in qualities)

    return (q20_bases / len(qualities)) * 100


# حساب Q30
def calculate_q30(qualities):

    q30_bases = sum(q >= 30 for q in qualities)

    return (q30_bases / len(qualities)) * 100


# تحليل ملف FASTQ
def analyze_fastq(filepath):

    total_reads = 0

    gc_values = []
    lengths = []
    q20_values = []
    q30_values = []

    for record in SeqIO.parse(str(filepath), "fastq"):

        sequence = str(record.seq)

        qualities = record.letter_annotations["phred_quality"]

        total_reads += 1

        gc_values.append(calculate_gc(sequence))

        lengths.append(len(sequence))

        q20_values.append(calculate_q20(qualities))

        q30_values.append(calculate_q30(qualities))

    results = {

        "File": filepath.name,
        "Total Reads": total_reads,
        "Average GC %": sum(gc_values) / len(gc_values),
        "Average Length": sum(lengths) / len(lengths),
        "Average Q20 %": sum(q20_values) / len(q20_values),
        "Average Q30 %": sum(q30_values) / len(q30_values)

    }

    return results


# تشغيل البرنامج
if __name__ == "__main__":

    data_path = Path("../data")

    all_results = []

    # قراءة case + control
    for folder in ["case", "control"]:

        folder_path = data_path / folder

        fastq_files = list(folder_path.glob("*.fastq"))

        print(f"\nProcessing {folder} samples...")

        for file in fastq_files:

            print(f"Analyzing: {file.name}")

            result = analyze_fastq(file)

            result["Class"] = folder

            all_results.append(result)

    # تحويل النتائج لجدول
    df = pd.DataFrame(all_results)

    print("\nFinal QC Results:\n")

    print(df)

    # حفظ CSV
    output_path = "../results/qc_results.csv"

    df.to_csv(output_path, index=False)

    print(f"\nResults saved to: {output_path}")