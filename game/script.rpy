# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("")
define narattor = Character("")

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 0.5
    play sound "/audio/game_start.mp3"
    play music "/audio/background_play.mp3" loop
    scene expression "#000"
    with Dissolve(1.0)
    "Chapter 1"
    "Awakened In The Unknown"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    
    # These display lines of dialogue.

    #Paragraph 1
    "Malam itu, di hutan yang sangat luas seperti tidak memiliki ujung"
    "dengan cahaya dari bintang-bintang dan suasana gelap yang mencekam."
    "Bayangan nampak seolah pohon pohon itu hidup, siluet di sekujur tempat ini juga menciptakan suasana seperti berada di dalam mimpi buruk"
    "Di tempat yang seperti mimpi buruk ini, ada seorang lelaki yang tergeletak di bawah pohon dengan tubuhnya yang terluka parah dan berlumuran darah."
    "Dengan kondisinya yang seperti itu ia seharusnya sudah mati dan akan segera membusuk."
    "Tetapi secara tiba-tiba tubuhnya tertutup asap putih dan tubuhnya seketika bersih seolah ia baru saja lahir,"
    "tidak ada satupun luka atau darah yang tersisa di tubuhnya, matanya yang kosong tiba-tiba hidup kembali,"

    mc "TOLONG……"

    mc "AKKKKHHHH…."

    "“Mereka bukanlah legenda, mereka bukan lah dongeng, mereka adalah bencana itu sendiri”"

    "“Mereka menghancurkan dan membunuh apa yang bisa mereka sentuh, tertahan ribuan tahun, mahkluk yang Abadi melebihi akal manusia menyentuh tanah ini.“"

    mc "akh…."

    mc "di… dimana aku?"

    mc "hutan?"

    mc "Seorang anak manusia terbangun di tengah hutan belantara, tanpa adanya cahaya."

    mc "kenapa aku di hutan? Apa yang terjadi?” (diapun berdiri)"

    mc "Dia melihat ke sekitar untuk mengetahui di mana ia berada, saat menatap langit yang dia lihat hanya titik bintang tanpa bulan yang tertutup rindangnya daun daun pohon hutan yang menjulang tinggi"

    mc "Gelap sekali… melihat tanah saja susah"

    mc "Apa  karena bulan tak muncul?"

    mc "Bagaimana aku bisa mencari pertolongan jika gelap begini?!"

    mc "Bagaimana jika ada hewan buas yang menyergap?!"
    
menu:
    "apa yang harus ku lakukan"

    "Diam menunggu bantuan":
        "Aku harus terus bergerak"
    "Berjalan maju":
        jump run_or_not

label run_or_not:
    mc "berjalan perlahan lahan sambil berpegangan pada pohon pohon besar yang ada sambil memperhatikan langkahnya."
    mc "Lamanya berjalan, ia mulun mulai mengingat ngingat apa yang terjadi padanya hingga terdampar ke hutan ini"
    mc "kenapa juga aku bisa ada disini, diculik? Jika benar kenapa di damparkan ke hutan? Mungkin bukan…"
    mc "dia pun Masih berfikir sambil mengatur nafas nya yang terengah engah"
    mc "tersesat? Aku tidak ingat apa yang terakhir aku lakukan sebelum bangun"
    mc "sepertinya aku terbentur cukup keras, kepala ku sakit sekali seperti di pukul besi"
    "Setelah istirahat dan mengumpulkan energy dia pun berdiri lagi untuk melanjutkan perjalanannya di dalam kegelapan."
    "Saat berjalan ia mulai bisa melihat ke depan, ternyata bulan muncul namun tidak seperti bulan yang ia tau."
    mc "bulan?... tapi kenapa terang sekali?"
    # This ends the game.
