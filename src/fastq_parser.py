from collections import namedtuple
from pathlib import Path
from Bio import SeqIO

# شكل منظم لكل Read
FastqRead = namedtuple(
    "FastqRead",
    ["id", "sequence", "quality_scores"]
)

# دالة قراءة FASTQ
def parse_fastq(filepath):

    filepath = Path(filepath)

    # نتأكد إن الملف موجود
    if not filepath.exists():
        raise FileNotFoundError(f"FASTQ file not found: {filepath}")

    # قراءة كل Read
    for record in SeqIO.parse(str(filepath), "fastq"):

        yield FastqRead(
            id=record.id,
            sequence=str(record.seq),
            quality_scores=record.letter_annotations["phred_quality"]
        )

# تشغيل الملف
if __name__ == "__main__":

    # مسار ملف FASTQ
    fq_path = "../data/case"

    # قراءة كل الملفات داخل case
    fastq_files = list(Path(fq_path).glob("*.fastq"))

    print(f"Found {len(fastq_files)} FASTQ files")

    # نقرأ كل ملف
    for file in fastq_files:

        print(f"\nProcessing: {file.name}")

        total = 0

        for read in parse_fastq(file):

            total += 1

            # نطبع أول 3 Reads فقط
            if total <= 3:

                avg_quality = (
                    sum(read.quality_scores)
                    / len(read.quality_scores)
                )

                print(f"Read ID: {read.id}")
                print(f"Length: {len(read.sequence)}")
                print(f"Average Quality: {avg_quality:.2f}")
                print("-" * 40)

        print(f"Total Reads: {total}")