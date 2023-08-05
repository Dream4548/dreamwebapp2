# Dreamweb-app

## คำสั่ง runs
    python manage.py runserver

## คำสั่งสร้างแอพ
    python manage.py startapp <ชื่อแอพ>

## คำสั่งสร้างแอดมิน
    python manage.py createsuperuser



# สร้างโมเดล
```python
 from django.db import models


class Student(models.Model):
    std_id = models.IntegerField()
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    phone = models.CharField(max_length=10)

```
## สัมพันธ์ของ Model แบบ Many-to-One
### Model แบบ Many-to-One เป็นโมเดลที่รับข้อมูลหลายชุดเข้าและสรุปผลลัพธ์เป็นเพียงชุดเดียว โดยที่สามารถใช้ในงานที่ต้องการจำแนกหมวดหมู่หรือทำนายผลลัพธ์ที่เป็นตัวแปรเดียว เช่น ในงานการจำแนกความรู้สึกในข้อความ แปลภาษา การระบุชื่อสิ่งของในข้อความ (NER) หรือสร้างเนื้อหาใหม่จากข้อมูลที่มีอยู่ ความสำคัญคือการเตรียมข้อมูลให้เหมาะสมและปรับแต่งโมเดลให้เหมาะสมกับงานที่ต้องการใช้งาน เพื่อให้ได้ผลลัพธ์ที่แม่นยำและมีประสิทธิภาพเช่นเดียวกัน