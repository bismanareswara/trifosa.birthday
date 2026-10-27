import tkinter as tk
import random
import math
import os
from PIL import Image, ImageTk, ImageDraw, ImageOps

# ==========================================
# HAPPY BIRTHDAY TRIFOSA SEKAR ARUM
# ==========================================

W, H = 900, 760

root = tk.Tk()
root.title("Happy Birthday Trifosa Sekar Arum")
root.geometry(f"{W}x{H}")
root.resizable(False, False)
root.configure(bg="#FFF4F7")

canvas = tk.Canvas(
    root,
    width=W,
    height=H,
    bg="#FFF4F7",
    highlightthickness=0
)
canvas.pack()

# Warna pastel
pink = "#F6B7CE"
purple = "#C9B8F0"
cream = "#FFE6B8"
blue = "#C5E5F5"
green = "#C9EAD8"
text_color = "#8D6687"

# ==========================================
# BACKGROUND PASTEL
# ==========================================

top = (255, 244, 248)
bottom = (239, 234, 255)

background = Image.new("RGB", (W, H))
pixels = background.load()

for y in range(H):
    t = y / H
    color = tuple(
        int(top[i] * (1 - t) + bottom[i] * t)
        for i in range(3)
    )
    for x in range(W):
        pixels[x, y] = color

bg_photo = ImageTk.PhotoImage(background)
canvas.create_image(
    0, 0,
    image=bg_photo,
    anchor="nw"
)

# Dekorasi sudut
canvas.create_oval(
    -100, -100, 180, 180,
    fill="#FCE0EC", outline=""
)
canvas.create_oval(
    740, -100, 1000, 180,
    fill="#E6DFFF", outline=""
)
canvas.create_oval(
    -100, 640, 160, 880,
    fill="#DDF3E8", outline=""
)
canvas.create_oval(
    750, 650, 1000, 900,
    fill="#FFF0D1", outline=""
)

# Bintik dekorasi pastel
for i in range(40):
    x = random.randint(10, W - 10)
    y = random.randint(10, H - 10)
    r = random.randint(2, 4)

    canvas.create_oval(
        x-r, y-r, x+r, y+r,
        fill=random.choice(
            [pink, purple, cream, blue, green]
        ),
        outline=""
    )

# ==========================================
# JUDUL DAN TEKS
# ==========================================

canvas.create_text(
    450, 38,
    text="♡  A SPECIAL DAY FOR YOU  ♡",
    font=("Helvetica", 11, "bold"),
    fill="#B17D9C"
)

canvas.create_text(
    450, 77,
    text="Happy Birthday",
    font=("Georgia", 31, "bold"),
    fill="#D77FA4"
)

canvas.create_text(
    450, 116,
    text="Trifosa Sekar Arum",
    font=("Georgia", 25, "bold"),
    fill="#987DC4"
)

canvas.create_text(
    450, 148,
    text="a special day for you",
    font=("Helvetica", 13, "italic"),
    fill=text_color
)

# ==========================================
# FOTO PRIBADI DI TENGAH
# ==========================================

try:
    # Simpan foto dengan nama trifosa.jpg
    # di folder yang sama dengan file Python.

    photo_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "trifosa.jpg"
    )

    photo = Image.open(photo_path).convert("RGB")

    # Crop foto menjadi persegi
    photo = ImageOps.fit(
        photo,
        (250, 250),
        method=Image.Resampling.LANCZOS,
        centering=(0.58, 0.42)
    )

    # Membuat sudut foto membulat
    mask = Image.new("L", (250, 250), 0)

    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, 249, 249),
        radius=30,
        fill=255
    )

    photo_rgba = photo.convert("RGBA")
    photo_rgba.putalpha(mask)

    photo_tk = ImageTk.PhotoImage(photo_rgba)

    # Bingkai foto
    canvas.create_rectangle(
        315, 174, 585, 444,
        fill="#FFFFFF",
        outline="#F3B8D0",
        width=5
    )

    canvas.create_image(
        450, 309,
        image=photo_tk
    )

    # Menjaga foto agar tetap tampil
    canvas.photo_tk = photo_tk

except Exception as e:
    canvas.create_text(
        450, 300,
        text=(
            "♡ FOTO TRIFOSA ♡\n\n"
            "Simpan foto dengan nama\n"
            "trifosa.jpg di folder yang sama\n"
            "dengan file Python."
        ),
        font=("Helvetica", 14),
        fill=text_color,
        justify="center"
    )

# ==========================================
# TANGGAL ULANG TAHUN
# ==========================================

canvas.create_text(
    450, 466,
    text="♡  8 November 2026  ♡",
    font=("Helvetica", 15, "bold"),
    fill="#C17FA4"
)

# ==========================================
# AYAT ALKITAB
# ==========================================

canvas.create_text(
    450, 505,
    text="AMSAL 9:11",
    font=("Helvetica", 12, "bold"),
    fill="#987DC4"
)

canvas.create_text(
    450, 529,
    text='"Karena oleh aku (hikmat) umurmu diperpanjang,',
    font=("Helvetica", 10),
    fill=text_color
)

canvas.create_text(
    450, 549,
    text='dan tahun-tahun hidupmu ditambah."',
    font=("Helvetica", 10),
    fill=text_color
)

# ==========================================
# UCAPAN DAN DOA
# ==========================================

canvas.create_text(
    450, 585,
    text="today is all about you",
    font=("Georgia", 15, "italic"),
    fill="#D77FA4"
)

canvas.create_text(
    450, 611,
    text="May your life be filled with love,",
    font=("Helvetica", 11),
    fill=text_color
)

canvas.create_text(
    450, 631,
    text="happiness, and God's blessings ♡",
    font=("Helvetica", 11),
    fill=text_color
)

# ==========================================
# NAMA PENGIRIM
# ==========================================

canvas.create_text(
    450, 674,
    text="From Bisma Nareswara",
    font=("Helvetica", 11, "bold"),
    fill="#B18AAE"
)

# ==========================================
# ANIMASI BALON DAN LOVE
# ==========================================

particles = []
colors = [pink, purple, cream, blue, green]

def create_particle():
    x = random.randint(15, W - 15)
    y = H + random.randint(10, 100)
    speed = random.uniform(1.0, 2.4)
    phase = random.random() * 6.28

    if random.random() < 0.55:
        # Membuat balon
        r = random.randint(9, 14)
        color = random.choice(colors)

        balloon = canvas.create_oval(
            x-r, y-r*1.3,
            x+r, y+r*1.3,
            fill=color,
            outline="#FFFFFF",
            width=1
        )

        string = canvas.create_line(
            x, y+r*1.3,
            x+3, y+r*2,
            fill="#C5A9C5"
        )

        particles.append({
            "kind": "balloon",
            "items": [balloon, string],
            "x": x,
            "y": y,
            "r": r,
            "speed": speed,
            "phase": phase
        })

    else:
        # Membuat hati
        size = random.randint(12, 20)

        heart = canvas.create_text(
            x, y,
            text=random.choice(["♡", "♥️", "💕"]),
            font=("Helvetica", size),
            fill=random.choice(colors)
        )

        particles.append({
            "kind": "heart",
            "items": [heart],
            "x": x,
            "y": y,
            "speed": speed,
            "phase": phase
        })

def animate():
    # Menambahkan partikel baru
    if len(particles) < 30 and random.random() < 0.7:
        create_particle()

    for p in particles[:]:
        p["y"] -= p["speed"]

        p["x"] += math.sin(
            p["y"] / 35 + p["phase"]
        ) * 0.7

        x = p["x"]
        y = p["y"]

        if p["kind"] == "balloon":
            balloon, string = p["items"]
            r = p["r"]

            canvas.coords(
                balloon,
                x-r, y-r*1.3,
                x+r, y+r*1.3
            )

            canvas.coords(
                string,
                x, y+r*1.3,
                x+3, y+r*2
            )

        else:
            canvas.coords(
                p["items"][0],
                x, y
            )

        # Menghapus balon dan hati yang sudah keluar
        if y < -50:
            for item in p["items"]:
                canvas.delete(item)

            particles.remove(p)

    root.after(30, animate)

# Jalankan animasi
animate()

# Menampilkan jendela
root.mainloop()