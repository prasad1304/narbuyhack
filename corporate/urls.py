from django.urls import path
from .views import (CorporateViewHome, CorporateContact, CorporateSubmission, CorporateView,
                    CorporateLargeScale, CorporateFarmers)


app_name = "corporate"
urlpatterns = [
    path('', CorporateView, name="corporate_home"),
    path('home/', CorporateViewHome, name="corporate_login"),
    path('contact/', CorporateContact, name="contact_form"),
    path('submission/', CorporateSubmission, name="submission"),
    path('form-large/', CorporateLargeScale, name="largescale"),
    path('farmers/', CorporateFarmers, name="corporate_farmers"),
    
   
    

]
