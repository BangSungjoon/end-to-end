from django import forms
<<<<<<< HEAD
from .models import Camping

class CampingForm(forms.ModelForm):
    class Meta:
        model = Camping
        fields = (
            'cam_name',
            'cam_address',
            'cam_tel',
            'cam_env',
            'cam_type',
            'cam_period',
            'cam_day',
            )

        labels = {
            'cam_name': '캠핑장 이름',

            'cam_address':'주소',
            'cam_tel':"전화번호",
            'cam_env':"캠핑장 환경",
            'cam_type':"캠핑장 유형",
            'cam_period':"운영기간",
            'cam_day':"운영일"
=======
from .models import CampInfo

class CampingForm(forms.ModelForm):
    class Meta:
        model = CampInfo
        fields = (
            'camp_name',
            'camp_address',
            'camp_call',
            'camp_environment',
            'camp_type',
            'camp_ope_period',
            'camp_ope_day',
            )

        labels = {
            'camp_name': '캠핑장 이름',

            'camp_address':'주소',
            'camp_call':"전화번호",
            'camp_environment':"캠핑장 환경",
            'camp_type':"캠핑장 유형",
            'camp_ope_period':"운영기간",
            'camp_ope_day':"운영일"
>>>>>>> kmy
        }
        