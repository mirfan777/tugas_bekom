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
        zoom 4
    image bg ruang_rapat :
        "ruang rapat.jpg"
        zoom 3
    image bg ruang_osis :
        "ruang osis.jpg"
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
    image npc_1 :
        "laki/figuran cowo 1.png"
        zoom 2
    image npc_2 :
        "laki/figuran cowo 2.png"
        zoom 2
    image npc_3 :
        "perempuan/figuran 1 cw.png"
        zoom 2
    image npc_4 :
        "perempuan/figuran 2 cw.png"
        zoom 2
    image waketos :
        "perempuan/waketos biasa.png"
        zoom 2
    image waketos senyum jahat :
        "perempuan/waketos jahat gigi.png"
        zoom 2
    image waketos jahat :
        "perempuan/waketos jahat.png"
        zoom 2
    image waketos sedih :
        "perempuan/waketos sedih.png"
        zoom 2
    image waketos senyum gigi :
        "perempuan/waketos senyum gigi.png"
        zoom 2
    image ibu senyum :
        "perempuan/ibu senyum.png"
        zoom 2
    image ibu senyum_gigi :
        "perempuan/ibu senyum gigi.png"
        zoom 2
    image ibu senyum :
        "perempuan/ibu senyum.png"
        zoom 2


define ketos = Character("sule")
define waketos = Character("rini")
define ibu = Character("ibu")
define anggota = Character("seluruh anggota")


# The game starts here.

label start:
# scene 1
    scene bg lorong_kelas

    show waketos at left

    waketos "pagi [ketos]"

    ketos "Pagi [waketos]"

    show waketos senyum gigi at left

    waketos "kita jadi ngadain pentas kan? Udah ditanyain banyak orangg nihh"

    ketos "jadii [waketos], sabar yaa, plan kasarnya udah jadi. Nanti tolong sampain ke temen temen untuk rapat besok!."

    show waketos at left

    waketos "Siap paketuuu, nanti langsung gue sampaiin ke temen-temen, besok tinggal cus rapat deh."

    show waketos senyum gigi at left

    waketos "Makasih yaa [waketos]."

# scene 2
    scene bg rumah
    with fade

    ketos "..."

    scene bg dalam_rumah

    show ibu senyum

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
    scene bg ruang_rapat

    show npc_1 at center
    show npc_3 at left 
    show npc_2 at right 

    ketos "Oke temen-temen semua. Seperti yang udah di sampein sama [waketos] kemarin, hari ini kita mau bahas tentang acara pensi yang bakal diadain 3 bulan lagi."

    ketos "Pertama-tama, kita bakal bagi-bagi seksi bidang sama tugasnya dulu ya."

    anggota "baik kak" 

    ketos "*fast forward setelah rapat*"

    scene bg ruang_rapat
    
    with fade

    show npc_1 at center
    show npc_3 at left 
    show npc_2 at right 

    ketos "Oke semuanya sudah dapat bagiannya masing masing ya. Untuk sekarang silahkan kalian diskusikan dengan koordinator masing-masing bidang dan melaporkan hasilnya ke sekretaris ya untuk dibuatkan proposal acaranya."

    ketos "Kalau ada yang ingin ditanyakan kalian bisa langsung tanya ke saya atau bertanya lewat koordinatornya. Saya akan membantu semuanya sebisa saya."

    anggota "siap ka"

# scene 5
    scene bg ruang_osis
    with fade

    "dua minggu kemudian"

    show npc_2 at center
    show npc_1 at left 
    show npc_3 at right 

    ketos "Oke temen-temen. Proposalnya baru aja di selesaiin sama sekretaris kita. Sekarang saya dan sekretaris akan mengajukan proposal ini ke kepala sekolah."

    ketos "Terima kasih atas kerja keras temen-temen semua, sekarang semoga proposal ini bisa di acc dengan cepat yaa."

    

    
    
    return
