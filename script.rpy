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
    # inisialisasi karakter
    image ketos :
        "laki/mc biasa.png"
        zoom 3
    image waketos :
        "laki/figuran cowo 2.png"
        zoom 2


define ketos = Character("udin")
define waketos = Character("sule")


# The game starts here.

label start:

    scene bg sekolah 

    show waketos

    waketos "pagi [ketos]"

    ketos "Pagi [waketos]"

    waketos "kita jadi ngadain pentas kan? Udah ditanyain banyak orangg nihh"

    ketos "jadii [waketos], sabar yaa, plan kasarnya udah jadi. Nanti tolong sampain ke temen temen untuk rapat besok!."

    waketos "Siap paketuuu, nanti langsung gue sampaiin ke temen-temen, besok tinggal cus rapat deh."

    waketos "Makasih yaa [waketos]."


    return
