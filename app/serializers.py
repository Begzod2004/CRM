from rest_framework import serializers
from .models import *

# class ImportSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Import
#         fields = "__all__"
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['count'] = Import.objects.count()
#         return representation

# class ExportSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Export
#         fields = "__all__"

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['count'] = Export.objects.count()
#         return representation   


class MijozSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = [
            'id',
            'nomi',
            'ism_sharif',
            'telefon',
            'manzil',
            'status',
            'bonus',
                    ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Mijoz.objects.count()
        return representation

class OmborSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = [
            'id',
            'mahsulot',
            'format',
            'olchov',
            'narx',
            'miqdor',
            'date_created',
            'izoh',
                    ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Ombor.objects.count()
        return representation


class HodimSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hodim
        fields = [
            'id',
            'ism_sharif',
            'lavozim',
            'oylik',
            'stavka',
            ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Hodim.objects.count()
        return representation



class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

    def to_representation(self, instance):
        data = super(BuyurtmaSerializers, self).to_representation(instance)
        data['mijoz'] = MijozSerializers(instance=instance.mijoz).data
        data['buyurtma_nomi'] = MahsulotlarSerializers(instance=instance.buyurtma_nomi).data
        data['count'] = Buyurtma.objects.count()
        return data


class BonusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bonus
        fields = "__all__"
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Bonus.objects.count()
        return representation


class MahsulotlarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulotlar
        fields = ('id','mahsulot_rasm','mahsulot_nomi','mahsulot_format')


class Mahsulot_olchovSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot_olchov
        fields = ('id','mahsulot_number','olchov','narx',)


class Buyurtma1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields =  ('id', 'buyurtma_nomi', 'mijoz', 'format', 'buyurtma_olchov', 'narx', 'miqdor', 'buyurtma_sana', 'izoh')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Buyurtma.objects.count()
        return representation


class TranzaksiyaCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = TranzaksiyaCategory
        fields =  ('id', 'title', 'turi')


class Moliya_kirimSerializers(serializers.ModelSerializer):
    mijoz = MijozSerializers()
    tranzaksiya_turi = TranzaksiyaCategorySerializers()
    class Meta:
        model = Moliya_kirim
        fields =  ('id', 'tranzaksiya_turi', 'mijoz', 'tolov_turi', 'summa', 'vaqt', 'description')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Moliya_kirim.objects.count()
        return representation


class Moliya_chiqimSerializers(serializers.ModelSerializer):
    mijoz = MijozSerializers()
    tranzaksiya_turi = TranzaksiyaCategorySerializers()
    class Meta:
        model = Moliya_chiqim
        fields =  ('id', 'tranzaksiya_turi', 'mijoz','hodim', 'tolov_turi', 'summa','mahsulot_nomi', 'format', 'mahsulot_olchov','narx','miqdor', 'vaqt', 'description')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['count'] = Moliya_chiqim.objects.count()
        return representation