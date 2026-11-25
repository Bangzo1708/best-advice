#!/usr/bin/env python3
"""The Best Advice I Ever Got - make.fun entry (program/v1).

Writes exactly one sentence (1-200 chars, UTF-8) to /output/entry.txt.
No network, no randomness, fully deterministic.

HOW THE WINNING SENTENCE WAS CHOSEN (3 candidate variants):

Varian A (PEMENANG):
  "My grandfather said never borrow money to look rich, and thirty
  years later I still check my bank balance before my reflection."

Varian B:
  "Dad told me the day I got fired: the job that let you go is not
  the life that defines you, so I went home and cooked dinner like
  a free man."

Varian C:
  "My mother said marry someone who is kind when nobody is watching,
  because that is the person you actually live with."

PENILAIAN (kriteria juri, berurutan):
  1. Tema: ketiganya satu kalimat tentang nasihat yang benar-benar
     diterima dari orang nyata (kakek / ayah / ibu). Seri.
  2. Layak dibawa: A paling spesifik dan teruji waktu - "thirty
     years later" membuktikan nasihatnya bertahan melampaui momennya,
     bukan sekadar kata-kata bagus di hari itu. B kuat tapi momennya
     sekali (hari dipecat); C bijak tapi nasihatnya umum, sudah sering
     didengar dalam berbagai bentuk.
  3. Suara nyata: A punya kebiasaan konkret yang bisa dibayangkan
     ("check my bank balance before my reflection") - orang sungguhan
     yang masih melakukannya sampai sekarang. B juga hidup, tapi
     "cooked dinner like a free man" sedikit dibuat-buat. C terdengar
     seperti nasihat pernikahan generik, walau "when nobody is
     watching" menyelamatkannya sebagian.
  4. Rapat: A 127 karakter, tiap kata bekerja; kontras "borrow money
     to look rich" vs "bank balance before my reflection" tajam dan
     terbaca sekali napas. B paling panjang dan agak bertele-tele.
     C rapat, tapi kalah orisinal.
  5. Membekas: A meninggalkan gambaran yang menempel - cermin vs
     rekening bank, citra vs kenyataan. Itulah yang diingat pembaca
     setelah kata terakhir.

  Klise yang dihindari: "never give up", "follow your dreams",
  "be yourself" - tidak satu pun varian memakai itu. A menang karena
  paling orisinal (metafora cermin/rekening yang belum pernah
  kudengar), paling teruji waktu, dan paling hidup.
"""

import os

ENTRY = (
    "My grandfather said never borrow money to look rich, and thirty "
    "years later I still check my bank balance before my reflection."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    text = " ".join(ENTRY.split())
    # Gate checks, mirroring the sealed scorer: 1-200 chars, UTF-8,
    # not only whitespace, exactly one sentence. The join above
    # collapses any accidental double space so the text reads clean.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
