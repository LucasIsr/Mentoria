from app_resendsrefac.models import Adress
from app_resendsrefac.models import Resident

class AdressServices:

    @staticmethod
    def get(id_adress):
        try:
            adress=Adress.objects.get(id_adress=id_adress)
            return adress
        except:
            return None
        
    @staticmethod
    def query_all():
        adress=Adress.objects.all()
        return adress
     
        

class ResidentServices:

    @staticmethod
    def get(id_resident):
        try:
            resident=Resident.objects.get(id_resident=id_resident)
            return resident
        except:
            return None
        
    @staticmethod
    def query_all():
        resident=Resident.objects.all()
        return resident
    
    