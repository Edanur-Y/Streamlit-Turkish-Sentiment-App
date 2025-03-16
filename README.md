## Streamlit Turkish Sentiment App

Bu uygulama Hugging Face'den savasy'nin [bert-base-turkish-sentiment-cased](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased) modelini kullanarak duygu analizi yapar.  

Streamlit'ten canlıya alınmış hali aşağıdaki gibidir.  
![streamlit_gif](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/streamlit-app.gif)  

**Docker Container'ı oluştururken yaşadığım problemler:**   
- Image export edilirken Docker engine duruyor. Yeniden başlatmaya çalıştığımda WSL'le ilgili bir hata veriyor. (Kapatıp yeniden açtığımda engine çalışıyor.) 
  Image tam oluşmadığı için devam edemedim.  
  
(Image'a ad vermeyi unutmuşum, -t flagi ile verilebilir.)
![docker_problem](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/docker_problem.PNG)

Direk AWS üzerinden Image oluşturmayı denedim.
![aws_instance](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/aws_instance.PNG) 

**AWS'de yaşadığım problemler:**  
- Docker Image oluştururken hafıza hatası veriyor.
- Bulut depolamasıyla ilgili bir problem mi diye kontrol ettim fakat oldukça yeterli alan vardı.
![error](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/error.PNG)

**Olası Çözümler**  
- Docker sorunu için: WSL yeniden indirilebilir.
- AWS sorunu için: Bilgisayarda ve Docker'da da yeterli alan vardı fakat daha basit ve küçük boyutlu bir proje ile deneme yapılıp aynı sorun devam ediyor mu diye bakılabilir.
