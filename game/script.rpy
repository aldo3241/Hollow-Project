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
        jump walk_or_not

label walk_or_not:
    mc "berjalan perlahan lahan sambil berpegangan pada pohon pohon besar yang ada sambil memperhatikan langkahnya."
    mc "Lamanya berjalan, ia mulun mulai mengingat ngingat apa yang terjadi padanya hingga terdampar ke hutan ini"
    mc "kenapa juga aku bisa ada disini, diculik? Jika benar kenapa di damparkan ke hutan? Mungkin bukan…"
    mc "dia pun Masih berfikir sambil mengatur nafas nya yang terengah engah"
    mc "tersesat? Aku tidak ingat apa yang terakhir aku lakukan sebelum bangun"
    mc "sepertinya aku terbentur cukup keras, kepala ku sakit sekali seperti di pukul besi"
    "Setelah istirahat dan mengumpulkan energy dia pun berdiri lagi untuk melanjutkan perjalanannya di dalam kegelapan."
    "Saat berjalan ia mulai bisa melihat ke depan, ternyata bulan muncul namun tidak seperti bulan yang ia tau."
    mc "bulan?... tapi kenapa terang sekali?"
    mc "permukaannya terlihat!"
    "Dia pun berjalan lebih cepat agar bisa keluar dari hutan yang luas ini."
    mc"Aku yang aneh atau memang hutan ini sangatlah luas?"
    "aku bahkan tak bisa menemukan area tanpa pohon"
    mc"tenggorokan ku kering, aku harus minum jika ingin melanjutkan perjalanan"
    "Saat berjalan ke depan, ia melihat bangunan besar dari kejauhan"
    mc"Bangunan?, Di tengah hutan?"
    "Ia pun berjalan mendekat ke bangunan tersebut"
    mc"halo… apakah ada orang Disini?"
    "Dia pun masuk ke dalam bangunan tersebut, dari dalam sangat terlihat bahwa bangunan ini sudah lama ditinggalkan, hanya tersisa debu dan jaring laba laba dimana mana"
    mc"apakah ini hanya bangunan kosong?"
    mc"mungkin aku bisa beristirahat disini, tapi makanan dan air belum juga ketemu"
    "Sambil berkeliling ia juga mencari sesuatu yang bisa dimakan atau minum"
    "sialan, tak ada apapun disini selain furnitur rusak dan debu"
    mc"untuk sekarang tidur saja di tempat ini, setidaknya lebih aman dari pada di luar…"
    mc"Sambil menahan lapar dan haus, dia pun tertidur"
    "…."
    "“krekk…. Tap tap tap ” suara ranting patah dan langkah kaki mendekat "
    "Belum sempat bermimpi sang anak manusia pun terbangun dan merasakan hawa yang tidak enak, badannya bergetar kepanikan mendengar suara langkah yang mendekat, dia pun menutup mulut nya agar tidak terdengar"
    "“*********!!!!” ucap makhluk yang mendekat sambil mengacungkan bilah tajam"
menu:
    "apa yang harus ku lakukan"

    "lari":
        jump run_from_monster
    "bersembunyi dari monster":
        jump hide_from_monster
        


label run_from_monster:
    "sang manusia pun berlari ke luar bangunan dan dikejar oleh mahkluk yang belum pernah ia lihat sebelumnya"
    "Saat di tengah pelarian ia pun terjatuh karena tidak memperhatikan langkahnya "
    mc "akhhhh…. Kenapa di waktu yang gak tepat gini"
    "Saat mencoba berdiri ia pun tersungkur lagi karena kaki yang sakit "
    mc "akhh kaki ku, makhluk sialan, kau tak bisa menangkap ku"
    mc "hahaha… akhhh"
    "Ia pun terjatuh ke depan dengan darah yang mengucur"
    mc "hooekk…"
    "Sesaat ia merasakan rasa sakit yang ekstrim di perutnya, ia menyadari benda hitam yang menembus badannya"
    mc "akhhh… ukkh… se-sejak kapan?..."
    "Makhluk tersebut pun mengangkat bilah nya ke atas dan membuat rasa sakit yang dirasakan bertambah"
    mc "AAKKHHHH… TOLONG… si-SIAPA SAJA…"
    "Makhluk tersebut hanya menikmati teriakan dan penderitaan manusia tersebut sampai akan mati"
    mc "HAHAHAHAHA Beginikah cara ku mati di tempat seperti ini?, konyol sekali oh tuhan beginikah kau akah membunuh ku kalau begitu akan kubunuh kau dengan cara yang sama"
    "Dan dalam keputusasaan, sang anak manusia pun perlahan mati di tangan makhluk tersebut secara perlahan"
    "THIS IS THE END OF THE GAME"

label hide_from_monster:
    "sang manusia pun bersembunyi di dalam bangunan"
    "beberapa sesaat kemudian makhluk itu pergi disaat itu lah dia berlari ke luar bangunan"
    mc "apa apa an itu tadi apa yang akan terjadi jika dia menemukan ku?, aku sangat lapar sekali"
    "setelah berjalan kesana kemari ia pun tidak mendapatkan makanan dan minuman sama sekali"
    mc "aku tidak tahu sudah berjalan selama apa tapi perut kusemakin lapar"
    "di saat dia akan berjalan lagi dia langsung ambruk "
    mc "aku sudah tidak kuat lagi kenapa pula aku bisa disini apa yang terjadi padaku, "
    "dia pun mengeluh dan menangis lalu terkapar sampai memejamkan mata"
    "sampai akhir hayat nya "
    "THIS IS THE END OF THE GAME"

    
   