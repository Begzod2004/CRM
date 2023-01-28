from django.db import models


format = [
    ('kg','kilogram'),
    ('dona','dona'),
    ('litr','litr'),
    ('metr','metr'),
]

class Mahsulotlar(models.Model):
    mahsulot_rasm = models.ImageField(upload_to='mahsulotlar/rasm', null=True,blank=True)
    mahsulot_nomi = models.CharField(max_length=200)
    mahsulot_format = models.CharField(choices=format, max_length=10)
    # count = models.IntegerField()


    def __str__(self):
        return f"{self.mahsulot_rasm} | {self.mahsulot_nomi} | {self.mahsulot_format}"

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

class Mahsulot_olchov(models.Model):
    mahsulot_number = models.IntegerField(default=0)
    olchov = models.FloatField(help_text="(kg lik, litrlik ...)")
    narx = models.FloatField(max_length=200)

    def __str__(self):
        return f"{self.olchov} | {self.narx}"

    class Meta:
        verbose_name = "Mahsulot o'lchovi"
        verbose_name_plural = "Mahsulot o'lchovlari"



# class Import(models.Model):
#     mahsulot_nomi = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
#     format = models.CharField(choices=format, max_length=10)
#     miqdor = models.IntegerField()
#     narx = models.IntegerField()
#     import_vaqt = models.DateTimeField()
#     izoh = models.TextField(null=True,blank=True)
#     # count = models.IntegerField()


#     @property
#     def umumiy(self):
#         return self.narx * self.miqdor

#     def __str__(self):
#         return f"{self.mahsulot_nomi} | {self.format} | {self.import_vaqt} | {self.umumiy}"

#     class Meta:
#         verbose_name = 'Import'
#         verbose_name_plural = 'Import'


# class Export(models.Model):
#     mahsulot_nomi = models.ForeignKey(Mahsulotlar, on_delete=models.CASCADE)
#     format = models.CharField(choices=format, max_length=10)
#     miqdor = models.IntegerField()
#     narx = models.IntegerField()
#     export_vaqt = models.DateTimeField()
#     izoh = models.TextField(null=True,blank=True)
#     # count = models.IntegerField()


#     @property
#     def umumiy(self):
#         return self.narx * self.miqdor

#     def __str__(self):
#         return f"{self.mahsulot_nomi} | {self.format} |{self.narx} | {self.export_vaqt} | {self.umumiy}"

#     class Meta:
#         verbose_name = 'Export'
#         verbose_name_plural = 'Export'

STATUS = (
    ('doimiy',"Doimiy"),
    ('bonus',"Bonus")
)

class Bonus(models.Model):
    bonus_nomi = models.CharField(max_length=300, null=True, blank=True)
    bonus_format = models.CharField(choices=format, max_length=10, null=True, blank=True)
    bonus_miqdori = models.FloatField(max_length=1000)
    bonus_summa = models.IntegerField(default=0)
    bonus_muddati = models.DateField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # count = models.IntegerField()



    def __str__(self):
        return f"{self.bonus_nomi} | {self.bonus_format} | {self.bonus_miqdori} | {self.bonus_muddati}"

    class Meta:
        verbose_name = 'Bonus'
        verbose_name_plural = 'Bonuslar'


class Mijoz(models.Model):
    nomi = models.CharField(max_length=200)
    ism_sharif = models.CharField(max_length=200)
    telefon = models.CharField(max_length=19)
    manzil = models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS, null=True, blank=True)
    bonus = models.ForeignKey(Bonus, on_delete=models.CASCADE, null=True, blank=True)
    # count = models.IntegerField()


    def __str__(self):
        return f"{self.nomi} | {self.ism_sharif} | {self.telefon} | {self.manzil}"


    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'




class Buyurtma(models.Model):
    buyurtma_nomi = models.ForeignKey(Mahsulotlar,on_delete=models.CASCADE, related_name='buyurtma')
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    format = models.CharField(choices=format, max_length=10, null=True,blank=True)
    buyurtma_olchov = models.FloatField(default=0)
    narx = models.FloatField(default=0)
    miqdor = models.FloatField(default=0)
    buyurtma_sana = models.DateTimeField(auto_now=True)
    izoh = models.TextField(null=True,blank=True)
    # count = models.IntegerField(null=True,blank=True)


    @property
    def umumiy(self):
        return self.narx * self.miqdor



    def __str__(self):
        return f"{self.mijoz} | {self.buyurtma_nomi} | {self.format} {self.miqdor} | {self.narx} | {self.buyurtma_sana} | {self.umumiy} |"

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'


class Ombor(models.Model):
    mahsulot = models.CharField(max_length=300)
    format = models.CharField(choices=format, max_length=10)
    olchov = models.FloatField(null=True, blank=True, help_text='Necha kg lik yoki metr lik ekani haqida ...')
    narx = models.FloatField(default=0)
    miqdor = models.FloatField()
    date_created = models.DateTimeField(auto_now=True)
    izoh = models.TextField(null=True,blank=True)
    # count = models.FloatField(null=True,blank=True)


    @property
    def umumiy(self):
        return self.narx * self.miqdor

    def __str__(self):
        return f"{self.mahsulot} | {self.format} | {self.olchov} | {self.narx} | {self.miqdor} | {self.umumiy} | "

    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborxona'


STAFKA = (
    ('0.25',"0.25"),
    ('0.50',"0.50"),
    ('0.75',"0.75"),
    ('1',"1"),
    ('1.5',"1.5"),
)


class Hodim(models.Model):
    ism_sharif = models.CharField(max_length=200)
    lavozim = models.CharField(max_length=100)
    oylik = models.CharField(max_length=1000000, null=True, blank=True)
    stavka = models.CharField(max_length=123,choices=STAFKA)
    # count = models.IntegerField(null=True,blank=True)



    def __str__(self):
        return f"{self.ism_sharif} | {self.lavozim} |  {self.oylik} | {self.stavka}"

    class Meta:
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'





TYPE_STATUS = (
    ('kirim',"kirim"),
    ('chiqim',"chiqim"),
)
STATUS = (
    ('mijoz',"Mijoz"),
    ('mahsulot',"Mahsulot"),
    ('hodim',"Hodim"),
)

class TranzaksiyaCategory(models.Model):
    title = models.CharField(max_length=20)
    turi = models.CharField(max_length=200,choices=TYPE_STATUS)
    status = models.CharField(max_length=200,choices=TYPE_STATUS)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name = 'Tranzaksiya tur'
        verbose_name_plural = 'Tranzaksiya turlari'

PAY_STATUS = (
    ('naqt',"Naqt"),
    ('plastik',"Plastik"),
    ('kochirma',"Ko'chirma")
)

# Tranzaksiya turida majburiy 4 ta bo'lim - Mijozdan tushum, Hodimga oylik, Omborga mahsulot, Pulni qaytarish 

class Moliya_kirim(models.Model):
    tranzaksiya_turi = models.ForeignKey(TranzaksiyaCategory, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    tolov_turi = models.CharField(max_length=200,choices=PAY_STATUS)
    summa = models.FloatField()
    vaqt = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.tranzaksiya_turi.turi} | {self.mijoz.nomi} | {self.tolov_turi}"

    class Meta:
        verbose_name = 'Moliya kirim'
        verbose_name_plural = 'Moliya kirim'


# Moliya chiqim - Hodimga oylik, Mijoz pulini qaytarish, Omborga 

class Moliya_chiqim(models.Model):
    tranzaksiya_turi = models.ForeignKey(TranzaksiyaCategory, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    hodim = models.ForeignKey(Hodim, on_delete=models.CASCADE, null=True, blank=True) # Istasa hodimga ham oylik bera oladi
    tolov_turi = models.CharField(max_length=200,choices=PAY_STATUS)
    summa = models.FloatField()
    vaqt = models.DateTimeField(auto_now=True)
    mahsulot_nomi = models.ForeignKey(Ombor,on_delete=models.CASCADE, related_name='mahsulot_nomi')
    format = models.CharField(choices=format, max_length=10, null=True,blank=True)
    mahsulot_olchov = models.FloatField(default=0)
    narx = models.FloatField(default=0)
    miqdor = models.FloatField(default=0)
    description = models.TextField(null=True, blank=True)
    # count = models.IntegerField(null=True, blank=True)
    @property
    def umumiy(self):
        return self.narx * self.miqdor

    def __str__(self):
        return f"{self.tranzaksiya_turi.turi} | {self.mijoz.nomi} | {self.hodim.ism_sharif} | {self.tolov_turi} | "

    class Meta:
        verbose_name = 'Moliya chiqim'
        verbose_name_plural = 'Moliya chiqim'

########################################## OXIRIDA ANALITIKA QILINADI ###############################################


# class Analitika(models.Model):
#     client_count = models.CharField(max_length=200)
#     product_count = models.CharField(max_length=200)
#     bonus_count = models.CharField(max_length=19)
#     hodim_count = models.CharField(max_length=200)
#     ombor_count = models.SmallIntegerField(choices=STATUS, default=0)
#     def __str__(self):
#         return f"{self.client_count} | {self.product_count} | {self.bonus_count} | {self.hodim_count} | {self.ombor_count}"
#     class Meta:
#         verbose_name = 'Analitika'
#         verbose_name_plural = 'Analitikalar'

