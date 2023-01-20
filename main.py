import hashlib
import random
import cv2 as cv
import os
import time
import webbrowser
from datetime import datetime
from random import choice
from re import M
from winsound import PlaySound
import pyautogui
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import re
import urllib.request
import turtle
import json
from termcolor import cprint
from googletrans import Translator
r = sr.Recognizer()

   

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem Çalışmıyor")
        return voice
        
listofman = ["adam" , "asmaca"]
listofface= ["takibi , yüz"]
def response(voice):
        if "şifre" in voice:
         text= record()
         print("Plaintext: ", text )
         i= hashlib.md5(text.encode()).hexdigest()
         print(i)
       
        if voice in listofface:   
          
            capture = cv.VideoCapture(0)

            pretrained_model = cv.CascadeClassifier("C:\\Users\Xarta\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\\haarcascade_frontalface_default.xml") 


            while True:
                boolean, frame = capture.read()
                if boolean == True:
                    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) 
                    
                    for (x,y,w,h) in coordinate_list:
                        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

                    cv.imshow("Face Detection", frame)
                    
                    if cv.waitKey(20)== ord("x"):
                        break
            capture.release()
            cv.destroyAllWindows()
    
        if "hava durumu" in voice:
    
            url = "https://www.havadurumu15gunluk.net/havadurumu/istanbul-hava-durumu-15-gunluk.html"
            site = urllib.request.urlopen(url).read().decode('utf-8')

            r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
            r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
            r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
            r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
            r_aciklama = '<img src="/havadurumu/images/trans.gif" alt="İstanbul Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

            comp_gunduz = re.compile(r_gunduz)
            comp_gece = re.compile(r_gece)
            comp_gun = re.compile(r_gun)
            comp_tarih = re.compile(r_tarih)
            comp_aciklama = re.compile(r_aciklama)

            gunduz = []
            gece = []
            gun = []
            tarih = []
            aciklama = []

            for i in re.findall(r_gunduz, site):
                gunduz.append(i)

            for i in re.findall(r_gece, site):
                gece.append(i)

            for i in re.findall(r_gun, site):
                gun.append(i)

            for i in re.findall(r_tarih, site):
                tarih.append(i)

            for i in re.findall(r_aciklama, site):
                aciklama.append(i)

            print("-" * 75)
            print("                         ISPARTA HAVA DURUMU")
            print("-" * 75)
            for i in range(0, len(gun)):
              print("{} {},\n\t\t\t\t\tgündüz: {} °C\tgece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i], aciklama[i]))
              print("-" * 75)
        
        if "bir şey sor" in voice:
            speak("yalan söylemek yok ama")
            playsound("voice/espri.mp3")
            speak("nasılsın")
            print("nasılsın ?"+id)

        listofban=["hey siri","hey alexa","cortana"]
        if voice in listofban:
            speak("sen benimle dalga mı geçiyosun "+id)
            print(":X")
            exit()

        listofgood=["naılsın","iyimisin","nasıl  gidiyor","naber","iyi misin"]
        listofanswer1=["iyiyim","iyi gidiyor","bi sorun yok",""]
        if voice in listofgood:
           selection =random.choice(listofanswer1)
           speak(selection) 


        if "benim şarkımı aç" in voice:
            webbrowser.get().open("https://www.youtube.com/watch?v=007lQf3rxn0" )

       
        if "adam " in voice:
        
                def cprint(*args, **kwargs):
                 print(*args)
           
                kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]
                 
                
                def oyun_hazirlik():
                    """Oyun için gerekli değişkenleri tanımlar"""
                    global secilen_kelime, gorunen_kelime, can
                    secilen_kelime = random.choice(kelimeler)
                    gorunen_kelime = ["-"] * len(secilen_kelime)
                    can = 5
                
                
                def harf_al():
                    """Kullanıcıdan bir harf alır, alana kadar gerekirse hata verir, birisi quit yazarsa programı kapatır"""
                    devam = True
                    while devam:
                        harf = input("Bir harf giriniz: ")
                        if harf.lower() == "quit":
                            cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                            exit()
                        elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
                            devam = False
                        else:
                            cprint("Hatalı Giriş", color="red", on_color="on_grey")
                
                    # noinspection PyUnboundLocalVariable
                    return harf.lower()
                
                
                def oyun_dongusu():
                    """Oyunun ana döngüsü, harf alır, tutarsa görünen karakterler listesi güncellenir,
                    tutmazsa can azaltılır, ve bu can bitene kadar ya da kelime bilinene kadar devam eder..."""
                    global gorunen_kelime, can
                    while can > 0 and secilen_kelime != "".join(gorunen_kelime):
                        cprint("kelime: " + "".join(gorunen_kelime), color="cyan", attrs=["bold"])
                        cprint("can   : <" + "❤" * can + " " * (5 - can) + ">", color="cyan", attrs=["bold"])
                
                        girilen_harf = harf_al()
                        pozisyonlar = harf_kontrol(girilen_harf)
                        if pozisyonlar:
                            for p in pozisyonlar:
                                gorunen_kelime[p] = girilen_harf
                        else:
                            can -= 1
                
                
                def harf_kontrol(girilen_harf):
                    """Gelen harfin seçilen kelimede nerelerde olduğunu bulur"""
                    poz = []
                    for index, h in enumerate(secilen_kelime):
                        if h == girilen_harf:
                            poz.append(index)
                    return poz
                
                
                def skor_tablosunu_goster():
                    """Skor tablosunu gösterir"""
                    veri = ayar_oku()
                    cprint("|Skor\t\tKullanıcı|", color="white", on_color="on_grey")
                    cprint("|------------------------|", color="white", on_color="on_grey")
                    for skor, kullanici in veri["skorlar"]:
                        cprint("|"+str(skor) +"\t\t"+ kullanici+" "*(9-len(kullanici))+"|", color="white", on_color="on_grey")
                    cprint("|------------------------|", color="white", on_color="on_grey")
                
                
                def skor_tablosunu_guncelle():
                    """Skor tablosunu son kullanıcının ismiyle ve skoruyla günceller"""
                    veri = ayar_oku()
                    veri["skorlar"].append((can, veri["son_kullanan"]))
                    veri["skorlar"].sort(key=lambda skor_tuplei: skor_tuplei[0], reverse=True)
                    veri["skorlar"] = veri["skorlar"][:5]
                    ayar_yaz(veri)
                
                
                def oyun_sonucu():
                    """Oyun bittiğinde kazanıp kazanamadığımızı ekrana yazar."""
                    if can > 0:
                        cprint("Kazandınız", color="yellow", on_color="on_red")
                        skor_tablosunu_guncelle()
                    else:
                        cprint("Kaybettiniz", color="red", on_color="on_yellow")
                    skor_tablosunu_goster()
                
                
                def dosyay_kontrol_et_yoksa_olustur():
                    """Ayar dosyası var mı kontrol eder, varsa sağlam mı diye bakar,
                    bozuk ya da olmayan durum için dosyayı öntanımlı değerlerle oluşturur"""
                    yaz = False
                    if os.path.exists("ayarlar.json"):
                        try:
                            ayar_oku()
                        except ValueError as e:
                            cprint("Hata: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
                            os.remove("ayarlar.json")
                            yaz = True
                    else:
                        yaz = True
                
                    if yaz:
                        ayar_yaz({"skorlar": [], "son_kullanan": ""})
                
                
                def ayar_oku():
                    """Ayarlar dosyasını okur"""
                    with open("ayarlar.json") as f:
                        return json.load(f)
                
                
                def ayar_yaz(veri):
                    """Ayarlar dosyasına gönderilen veriyi yazar"""
                    with open("ayarlar.json", "w") as f:
                        json.dump(veri, f)
                
                
                def kullanici_adini_guncelle():
                    """Kullanıcıdan isim alıp ayarlara yazdırmaya gönderir"""
                    veri = ayar_oku()
                    veri["son_kullanan"] = input("Kullanıcı Adınız: ")
                    while not veri["son_kullanan"] or len(veri["son_kullanan"]) > 9:
                        veri["son_kullanan"] = input("lykpython ile 9 karakter uzunluğunda yazın: ")
                    ayar_yaz(veri)
                
                
                def kullanici_kontrol():
                    """Bir önce giriş yapan kullanıcı ismini gösterip kullanıcıya bu siz misiniz diye sorar"""
                    veri = ayar_oku()
                    print("Son giriş yapan: " + veri["son_kullanan"])
                    if not veri["son_kullanan"]:
                        kullanici_adini_guncelle()
                    elif input("Bu siz misiniz?(e/h) ").lower() == "h":
                        kullanici_adini_guncelle()
                
                
                def main():
                    """Programın ana döngüsü, oyunun çalışmasından yükümlü"""
                    tekrar_edecek_mi = True
                    dosyay_kontrol_et_yoksa_olustur()
                    cprint("Merhaba, Adam Asmacaya hoşgeldiniz.", color="cyan", on_color="on_magenta", attrs=["bold"])
                    cprint("Yardım: Oyun sırasında quit diyerek çıkabilirsiniz", color="cyan", on_color="on_magenta", attrs=["bold"])
                    cprint("-"*30, color="cyan", on_color="on_magenta", attrs=["bold"])
                    skor_tablosunu_goster()
                    kullanici_kontrol()
                    while tekrar_edecek_mi:
                        oyun_hazirlik()
                        oyun_dongusu()
                        oyun_sonucu()
                        if input("Devam?(e/h) ").lower() == "h":
                            tekrar_edecek_mi = False
                    cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                
                    main()
        if "google'da ara" in voice:
            speak("Ne aramamı istersin")
            search = record()
            url = "https://www.google.com/search?q={}".format(search)
            webbrowser.get().open(url)
            speak("{} içi Google'da bulabildiklerim bunlar".format(search))

        if "teşekkürler" in voice:
            speak("rica ederim ")
            print("Rica ederim  <3")

        if "saat kaç" in voice:
            selection = ["Saat: ", "Hemen Bakıyorum :"]
            clock = datetime.now().strftime("%H:%M")
            selection = random.choice(selection)
            speak(selection + clock)
            print(selection," :",clock + id)

        if "youtube'da ara" in voice:
            speak("Ne Aramamı istersin"+id)
            search = record()
            url = "https://www.youtube.com/results?search_query={}".format(search)
            webbrowser.get().open(url)

        if "bizi coştur" in voice:
            webbrowser.get().open("https://www.youtube.com/watch?v=X8dlyffFTIo")
            
        if "görev yöneticisi" in voice:
            os.startfile("taskmgr.exe")
            
        if "aygıt yöneticisi" in voice:
         os.startfile("devmgmt.exe")
         
        if "büyüteç" in voice:
         os.startfile("magnify.exe ") 
         
        if "ses ayarları" in voice:
         os.startfile("mmsys.cpl") 
        
        if "ekran klavyesi" in voice:
            os.startfile("osk.exe")
            
        if "hesap makinası" in voice:
            os.startfile("calc.exe ")
            
        if "sen kimsin" in voice:
            speak("Ben arya")
            print("Ben ARYA")
            speak("kısaca hikayemi anlatmam gerekirse ben 4 üniversite arkadaşının üretimi olan bir kişisel asistanım")
           

        if "gün" in voice:
            gün = time.strftime("%A")
            gün.capitalize()
            ay = time.strftime("%B")
            ay.capitalize()
            yıl = time.strftime("%Y")
            yıl.capitalize()
            if gün == "Monday":
                gün = "Pazartesi"
            elif gün == "Tuesday":
                gün = "Salı"
            elif gün == "Wednesday":
                gün = "Çarşamba"
            elif gün == "Thursday":
                gün = "Perşembe"
            elif gün == "Friday":
                gün = "Cuma"
            elif gün == "Saturday":
                gün = "Cumartesi"
            elif gün == "Sunday":
                gün = "Pazar"
            if   ay == "January":
                ay = "Ocak"
            elif ay == "February":
                ay = "Şubat"
            elif ay == "March":
                ay = "Mart"
            elif ay == "April":
                ay = "Nisan"
            elif ay == "May":
                ay = "Mayıs"
            elif ay == "June":
                ay = "Haziran"
            elif ay == "July":
                ay = "Temmuz"
            elif ay == "August":
                ay = "Ağustos"
            elif ay == "September":
                ay = "Eylül"
            elif ay == "October":
                ay = "Ekim"
            elif ay == "November":
                ay = "Kasım"
            elif ay == "December":
                ay = "Aralık"

            speak(yıl+ay+gün+id)
            print(yıl+ay+gün)
        if "yılan oyununu aç" in voice:
            
            delay = 0.15
            
            pencere = turtle.Screen()
            pencere.title('Yılan Oyunu')
            pencere.bgcolor('lightgreen')
            pencere.setup(width=600, height=600)
            pencere.tracer(0)
            
            kafa = turtle.Turtle()
            kafa.speed(0)
            kafa.shape("square")
            kafa.color("black")
            kafa.penup()
            kafa.goto(0, 100)
            kafa.direction = "stop"
            
            yemek = turtle.Turtle()
            yemek.speed(0)
            yemek.shape("circle")
            yemek.color("red")
            yemek.penup()
            yemek.shapesize(0.80, 0.80)
            yemek.goto(0, 0)
            
            kuyruklar = []
            puan = 0
            
            yaz = turtle.Turtle()
            yaz.speed(0)
            yaz.shape("square")
            yaz.color("white")
            yaz.penup()
            yaz.hideturtle()
            yaz.goto(0, 260)
            yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
            
            def move():
                if kafa.direction == "up":
                    y = kafa.ycor()
                    kafa.sety(y + 20)
                if kafa.direction == "down":
                    y = kafa.ycor()
                    kafa.sety(y - 20)
                if kafa.direction == "right":
                    x = kafa.xcor()
                    kafa.setx(x + 20)
                if kafa.direction == "left":
                    x = kafa.xcor()
                    kafa.setx(x - 20)
            
            def go_up():
                if kafa.direction != "down":
                    kafa.direction = "up"
            def go_down():
                if kafa.direction != "up":
                    kafa.direction = "down"
             
            
            
            
            
            def go_right():
                if kafa.direction != "left":
                    kafa.direction = "right"
            def go_left():
                if kafa.direction != "right":
                    kafa.direction = "left"
            
            pencere.listen()
            pencere.onkey(go_up, "Up")
            pencere.onkey(go_down, "Down")
            pencere.onkey(go_right, "Right")
            pencere.onkey(go_left, "Left")
            
            while True:
                pencere.update()
            
                if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
                    time.sleep(1)
                    kafa.goto(0, 0)
                    kafa.direction = "stop"
            
                    for kuyruk in kuyruklar:
                        kuyruk.goto(1000, 1000)
                    kuyruklar = []
            
                    puan = 0
                    delay = 0.1
            
                    yaz.clear()
                    yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
            
                if kafa.distance(yemek) < 20:
                    x = random.randint(-250, 250)
                    y = random.randint(-250, 250)
                    yemek.goto(x, y)
            
                    yeni_kuyruk = turtle.Turtle()
                    yeni_kuyruk.speed(0)
                    yeni_kuyruk.shape("square")
                    yeni_kuyruk.color("white")
                    yeni_kuyruk.penup()
                    kuyruklar.append(yeni_kuyruk)
            
                    delay -= 0.001
            
                    puan = puan + 10
                    yaz.clear()
                    yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))
            
                for index in range(len(kuyruklar) - 1, 0, -1):
                    x = kuyruklar[index - 1].xcor()
                    y = kuyruklar[index - 1].ycor()
                    kuyruklar[index].goto(x, y)
            
                if len(kuyruklar) > 0:
                    x = kafa.xcor()
                    y = kafa.ycor()
                    kuyruklar[0].goto(x, y)
            
                move()
            
                for segment in kuyruklar:
                    if segment.distance(kafa) < 20:
                        time.sleep(1)
                        kafa.goto(0, 0)
                        kafa.direction = "stop"
                        for segment in kuyruklar:
                            segment.goto(1000, 1000)
                        kuyruklar = []
                        puan = 0
                        yaz.clear()
                        yaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
                        hiz = 0.15
            
                time.sleep(delay)

        if "fıkra" in voice:
            selection = ["adamın biri varmış ölmüş", "Hiç canım kalmadı"]
            selection = random.choice(selection)
            speak(selection)
            print(selection+":D")

        listofold=["kaç yaşındasın","sen kaç yaşındasın","yaş kaç oldu"]
        if voice in listofold:
            selection = ["asistan olacak yaştayım", "bilmem siriye sor"]
            selection = random.choice(selection)
            speak(selection+id)
            print(selection)

        listofby=["görüşürüz","bay bay","kapan"]   
        if voice in listofby:
            selection = ["bay bay :", "umarım çok sonra olur :", "görüşmeyelim olur mu :", "bence görüşmeyelim", "görüşmesekte olur"]
            selection = random.choice(selection)
            speak(selection + id)
            print(selection)
            exit()
        listofwrite=["not al"]
        if voice in listofwrite:
            speak("Dosya ismi ne olsun?")
            txtFile = record() +".txt"
            speak("Ne kaydetmek istiyorsun")
            theText = record()
            f = open(txtFile, "w", encoding="utf-8")
            f.writelines(theText)
            f.close()
            speak("işlem tamam"+id)         
                
        
        if "bilgisayarı yeniden başlat" in voice:
            print("Yeniden Başlatılıyor")
            os.system("shutdown /g")

        if "bilgisayarı kapat" in voice:
             print("Bilgisayarın kısa süre içinde kapatılacak...")
             os.system("shutdown/s")
             
        select1 = random.randint
        if "bana bir şey çiz" in voice:
            select1 = random.randint(0,100)
            if select1 <=50:
             one()
            else:
             two()
        
        if "çeviri" in voice:
            speak("Lütfen çevirmek istediğiniz cümleyi giriniz: ")
            cümle  = input("Cümle : ")
            turkish=True
            
            
            def translate(text, german=False, french=False, turkish=False):

                translation_dict = {}

                tranlator = Translator()
                if german==True:
                 result = tranlator.translate(text, dest='de')
                 translation_dict["Almanca"] = result.text

                if french==True:
                 result = tranlator.translate(text, dest='fr')
                
                 translation_dict["Fransızca"] = result.text

                if turkish==True:
                 result = tranlator.translate(text, dest='tr')
                 translation_dict["Türkçe"] = result.text

            
                return translation_dict

            if __name__ == '__main__':

                 text = cümle 
                 result = translate(text, french=True, german=True, turkish=True)

                 for language in result.items():
                        print(language)   
            
             
        if "bilgisayarı kapatma komutu iptal" in voice:
            print("Kapatma komutu iptal ediliyor...")
            os.system("shutdown/a")

        listofapp = ["pencere kapat","uygulama kapat","google sekmesini kapa"]
        if voice in listofapp:
            speak("Hangi uygulamayı kapatmamı istiyorsun")
            stopApp = record()
            stopApp = stopApp.lower()
            print(stopApp)
            
            if "sanal makina"in stopApp:
             os.system ("taskkill /f /im VirtualBox.exe")

            if "google sekmesini kapat"in stopApp:
             os.system ("taskkill /f /im chrome.exe")

        listofapp1 = ["uygulama aç"]    
        if voice in listofapp1:
            speak("Hangi uygulamayı açmamı istiyorsun")
            runApp = record()
            runApp = runApp.lower()
            print(runApp)
     
            #if runApp in listofopen:
              #os.startfile("C:\Program Files\WindowsApps\Microsoft.WindowsCamera_2021.105.10.0_x64__8wekyb3d8bbwe\WindowsCamera.exe")
             
            if "google aç" in runApp:
              os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")

            if "virtual box" in runApp:
              os.startfile("C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")
            
            if"karay metin2" in runApp:
              os.startfile("C:\KCT_GAME\KarayMt2\KarayMt2.exe")
        
        if "uyku" in voice:
            speak("1 dakika sessizlik yeter mi"+id)
            voice = record()
            print(voice)
            if "evet" in voice:
             print("Ben kaçar")
             time.sleep(60)
            else :
             print("Ben kaçar")
             time.sleep(120)
             
        listofreaad = ["not oku"]
        if voice in listofreaad:
            speak("hangi notu okumamı istersin")
            voice = record()
            with open ('{}.txt'.format(voice),'r') as dosya:
             for line in dosya.read().splitlines():
              speak(line)
              
        
def one():
	# Creating turtle  
		t = turtle.Turtle()  
		s = turtle.Screen()  
		s.bgcolor("black")  
		
		turtle.pensize(2)  
		
		# To design curve  
		def curve():  
			for i in range(200):  
				t.right(1)  
				t.forward(1)  
		
		t. speed(3)  
		t.color("red", "pink")  
		
		t.begin_fill()  
		t.left(140)  
		t.forward(111.65)  
		curve()  
		
		t.left(120)  
		curve()  
		t.forward(111.65)  
		t.end_fill()  
		t.hideturtle()  
		
		turtle.mainloop()  
	
def two():
		t = turtle.Turtle()  
		s = turtle.Screen()  
		s.bgcolor("black")  
		t.pencolor("red")  
		
		a = 0  
		b = 0  
		t.speed(0)  
		t.penup()  
		t.goto(0,200)  
		t.pendown()  
		while(True):  
			t.forward(a)  
			t.right(b)  
			a+=3  
			b+=1  
			if b == 210:  
				break  
			t.hideturtle()  
		
		turtle.done()  
    

def speak(string):
    tts = gTTS(text=string, lang="tr")
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def nc(wake):
    listofwake=["arya","hey arya","beni dinliyomusun"]
    if wake in listofwake:
        playsound("voice/ding.mp3")
        wake = record()
        if wake != '':
           voice = wake.lower()
           print(wake.capitalize())
           response(voice)


#selection = ["voice/ses1.mp3", "voice/kalk.mp3", "voice/sound2.mp3"]
#opening = random.choice(selection)
#playsound(opening)

#speak("selamlar")
#speak("Ben kişisel asistan arya ")

speak("Sana nasıl hitap etmeliyim")
playsound("voice\ding.mp3")
id = ""
id=record()
speak("Hoşgeldin"+id)
playsound("voice/ding.mp3")

voice=record()
print(voice)
voice = voice.lower()

while True:
        print("...")
        wake = record()
 
        if wake != '':
            wake = wake.lower()
            print(wake.capitalize())
            nc(wake)

        
 