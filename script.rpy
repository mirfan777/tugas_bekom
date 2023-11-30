# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Inisialisi asset
init :
    image bg sekolah : 
        "sekolah.png" 
        zoom 3
    image bg dalam_kelas :
        "dalam kelas.jpg"
        zoom 3
    image bg lorong_kelas :
        "lorong kelas.jpeg"
        zoom 3
    image bg ruang_rapat :
        "ruang rapat.jpg"
        zoom 3
    image bg rumah :
        "bg rumah.jpg"
        zoom 2
    image bg dalam_rumah :
        "dalam rumah.jpeg"
        zoom 3
    # inisialisasi karakter
    image ketos :
        "laki/mc biasa.png"
        zoom 3
    image waketos :
        "laki/figuran cowo 2.png"
        zoom 2
    image ibu :
        "ibu senyum.png"
        zoom 3


define ketos = Character("udin")
define waketos = Character("sule")
define ibu = Character("ibu")


# The game starts here.

label start:
# scene 1
    scene bg sekolah 

    show waketos

    waketos "pagi [ketos]"

    ketos "Pagi [waketos]"

    waketos "kita jadi ngadain pentas kan? Udah ditanyain banyak orangg nihh"

    ketos "jadii [waketos], sabar yaa, plan kasarnya udah jadi. Nanti tolong sampain ke temen temen untuk rapat besok!."

    waketos "Siap paketuuu, nanti langsung gue sampaiin ke temen-temen, besok tinggal cus rapat deh."

    waketos "Makasih yaa [waketos]."

# scene 2
    scene bg rumah

    ketos "..."

    scene bg dalam_rumah

    ketos "Assalamualaikum"

    ibu "Waalaikumsalam, anak ibu sudah pulang"

    ketos "Eh ibu lagi sakit ko bebersih(?). Sinii bu, sini biar aku aja."

# scene 3
    scene bg rumah

    with fade

    show ketos

    ketos "Kenalin, aku [ketos]. Aku adalah seorang anak tunggal di keluarga ku. Aku tinggal bersama orang tua ku, namun kondisi ibuku saat ini sedang sakit parah."
    
    ketos "Ayahku adalah seorang buruh tani sehingga kami cukup kesulitan untuk memberikan perawatan yang cukup untuk ibuku."

    ketos "Aku juga seorang ketua osis di SMA X jadi aku tidak punya waktu untuk nongkrong atau bermain seperti anak SMA pada umumnya."

    ketos "Aku selalu ingin membantu orang tuaku dengan bekerja paruh waktu, namun ayahku selalu melarangnya."

    ketos "Dia bilang aku harus fokus pada sekolahku agar kelak aku dapat menjadi orang yang sukses karena aku adalah satu satunya harapan mereka."

# scene 4
    
    return
