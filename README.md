# Matbil Website

https://github.com/servet0/matbil-django-python/assets/123745302/da74f847-5d28-49a6-ab7d-ec2ec81c9d69

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. **Gereksinimleri İndirin:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Veritabanını Migrate Edin:**
    ```bash
    python manage.py migrate
    ```

3. **Yönetici Hesabı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

4. **Sunucuyu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Proje artık `http://localhost:8000` adresinde çalışır durumda olmalıdır. Yönetici paneline `http://localhost:8000/admin` adresinden erişebilirsiniz.


