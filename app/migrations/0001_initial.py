# Generated by Django 4.1.5 on 2023-01-27 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bonus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bonus_nomi", models.CharField(blank=True, max_length=300, null=True)),
                (
                    "bonus_format",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("kg", "kilogram"),
                            ("dona", "dona"),
                            ("litr", "litr"),
                            ("metr", "metr"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("bonus_miqdori", models.FloatField(max_length=1000)),
                ("bonus_summa", models.IntegerField(default=0)),
                ("bonus_muddati", models.DateField(blank=True, null=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
            ],
            options={
                "verbose_name": "Bonus",
                "verbose_name_plural": "Bonuslar",
            },
        ),
        migrations.CreateModel(
            name="Hodim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ism_sharif", models.CharField(max_length=200)),
                ("lavozim", models.CharField(max_length=100)),
                ("oylik", models.CharField(blank=True, max_length=1000000, null=True)),
                (
                    "stavka",
                    models.FloatField(
                        choices=[
                            ("0.25", "0.25"),
                            ("0.50", "0.50"),
                            ("0.75", "0.75"),
                            ("1", "1"),
                            ("1.5", "1.5"),
                        ],
                        max_length=200,
                    ),
                ),
            ],
            options={
                "verbose_name": "Hodim",
                "verbose_name_plural": "Hodimlar",
            },
        ),
        migrations.CreateModel(
            name="Mahsulot_olchov",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mahsulot_number", models.IntegerField(default=0)),
                ("olchov", models.FloatField(help_text="(kg lik, litrlik ...)")),
                ("narx", models.FloatField(max_length=200)),
            ],
            options={
                "verbose_name": "Mahsulot o'lchovi",
                "verbose_name_plural": "Mahsulot o'lchovlari",
            },
        ),
        migrations.CreateModel(
            name="Mahsulotlar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "mahsulot_rasm",
                    models.ImageField(
                        blank=True, null=True, upload_to="mahsulotlar/rasm"
                    ),
                ),
                ("mahsulot_nomi", models.CharField(max_length=200)),
                (
                    "mahsulot_format",
                    models.CharField(
                        choices=[
                            ("kg", "kilogram"),
                            ("dona", "dona"),
                            ("litr", "litr"),
                            ("metr", "metr"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
            options={
                "verbose_name": "Mahsulot",
                "verbose_name_plural": "Mahsulotlar",
            },
        ),
        migrations.CreateModel(
            name="Mijoz",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nomi", models.CharField(max_length=200)),
                ("ism_sharif", models.CharField(max_length=200)),
                ("telefon", models.CharField(max_length=19)),
                ("manzil", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("doimiy", "Doimiy"), ("bonus", "Bonus")],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "bonus",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.bonus",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mijoz",
                "verbose_name_plural": "Mijozlar",
            },
        ),
        migrations.CreateModel(
            name="Ombor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mahsulot", models.CharField(max_length=300)),
                (
                    "format",
                    models.CharField(
                        choices=[
                            ("kg", "kilogram"),
                            ("dona", "dona"),
                            ("litr", "litr"),
                            ("metr", "metr"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "olchov",
                    models.FloatField(
                        help_text="Necha kg lik yoki metr lik ekani haqida ..."
                    ),
                ),
                ("narx", models.FloatField(default=0)),
                ("miqdor", models.FloatField()),
                ("izoh", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Ombor",
                "verbose_name_plural": "Omborxona",
            },
        ),
        migrations.CreateModel(
            name="TranzaksiyaCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                (
                    "turi",
                    models.CharField(
                        choices=[("kirim", "kirim"), ("chiqim", "chiqim")],
                        max_length=200,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tranzaksiya tur",
                "verbose_name_plural": "Tranzaksiya turlari",
            },
        ),
        migrations.CreateModel(
            name="Moliya_kirim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tolov_turi",
                    models.CharField(
                        choices=[
                            ("naqt", "Naqt"),
                            ("plastik", "Plastik"),
                            ("kochirma", "Ko'chirma"),
                        ],
                        max_length=200,
                    ),
                ),
                ("summa", models.FloatField()),
                ("vaqt", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "mijoz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.mijoz"
                    ),
                ),
                (
                    "tranzaksiya_turi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.tranzaksiyacategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Moliya kirim",
                "verbose_name_plural": "Moliya kirim",
            },
        ),
        migrations.CreateModel(
            name="Moliya_chiqim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tolov_turi",
                    models.CharField(
                        choices=[
                            ("naqt", "Naqt"),
                            ("plastik", "Plastik"),
                            ("kochirma", "Ko'chirma"),
                        ],
                        max_length=200,
                    ),
                ),
                ("summa", models.FloatField()),
                ("vaqt", models.DateTimeField(auto_now=True)),
                (
                    "format",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("kg", "kilogram"),
                            ("dona", "dona"),
                            ("litr", "litr"),
                            ("metr", "metr"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("mahsulot_olchov", models.FloatField(default=0)),
                ("narx", models.FloatField(default=0)),
                ("miqdor", models.FloatField(default=0)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "hodim",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.hodim",
                    ),
                ),
                (
                    "mahsulot_nomi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mahsulot_nomi",
                        to="app.ombor",
                    ),
                ),
                (
                    "mijoz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.mijoz"
                    ),
                ),
                (
                    "tranzaksiya_turi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.tranzaksiyacategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Moliya chiqim",
                "verbose_name_plural": "Moliya chiqim",
            },
        ),
        migrations.CreateModel(
            name="Buyurtma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "format",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("kg", "kilogram"),
                            ("dona", "dona"),
                            ("litr", "litr"),
                            ("metr", "metr"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("buyurtma_olchov", models.FloatField(default=0)),
                ("narx", models.FloatField(default=0)),
                ("miqdor", models.FloatField(default=0)),
                ("buyurtma_sana", models.DateTimeField(auto_now=True)),
                ("izoh", models.TextField(blank=True, null=True)),
                (
                    "buyurtma_nomi",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buyurtma",
                        to="app.mahsulotlar",
                    ),
                ),
                (
                    "mijoz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.mijoz"
                    ),
                ),
            ],
            options={
                "verbose_name": "Buyurtma",
                "verbose_name_plural": "Buyurtmalar",
            },
        ),
    ]
