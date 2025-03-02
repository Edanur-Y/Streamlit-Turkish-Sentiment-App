## Streamlit Turkish Sentiment App

Bu uygulama Hugging Face'den savasy'nin [bert-base-turkish-sentiment-cased](https://huggingface.co/savasy/bert-base-turkish-sentiment-cased) modelini kullanarak duygu analizi yapar.  

Streamlit'ten canlıya alınmış hali aşağıdaki gibidir.  
![streamlit_gif](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/streamlit-app.gif)  

**Docker Container'ı oluştururken yaşadığım problemler:**
- VSCode, Docker uygulamasına bağlanamıyor.
- Docker uygulamam son sürüm değil ve uygulama içi güncellemede bir sıkıntı var.  

Uygulamayı silip yeniden yüklemek yerine direk AWS üzerinden Image oluşturmayı denedim.
![aws_instance](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/aws_instance.PNG) 

**AWS'de yaşadığım problemler:**  
- Docker Image oluştururken hafıza hatası veriyor.
- Bulut depolamasıyla ilgili bir problem mi diye kontrol ettim fakat oldukça yeterli alan vardı.
![error](https://github.com/Edanur-Y/Streamlit-Turkish-Sentiment-App/blob/main/error.PNG)

**Olası Çözümler**  
- Docker Desktopu yeniden indirip container oluşturmayı denemek  
- Hafıza probleminin kaynağını anlamak

*Container'a koymadan AWS'den direk canlıya alabilirdim fakat zor olan kısmı o değildi zaten:)
