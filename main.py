from ses_alma import sesi_dinle
from cevap_verme import sesli_cevap
from model import cevap_olustur
import asyncio

if __name__ == "__main__":

    while True:
        ses_input = sesi_dinle()        
        if ses_input == ("Anlayamadım, lütfen tekrar edin." or ses_input == "Ses algılanamadı, lütfen tekrar deneyin." 
                        or ses_input == "Bağlantı hatası!!! Google API'ye erişim sağlanamadı."):
            print("Görüşürüz.")
            break  
        else:
            print("Kullanıcı: ", ses_input)
            ses_output = cevap_olustur(ses_input)
            print("Asistan: ", ses_output)
            asyncio.run(sesli_cevap(ses_output))
            