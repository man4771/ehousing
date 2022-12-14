# Generated by Django 4.1.1 on 2022-10-03 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("Content", models.TextField(max_length=5000)),
                ("PublishDate", models.DateTimeField(auto_now_add=True)),
                ("UpdatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "book",},
        ),
        migrations.CreateModel(
            name="Master",
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
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=12)),
                ("IsActive", models.BooleanField(default=False)),
                ("RegDate", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "master",},
        ),
        migrations.CreateModel(
            name="UserRole",
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
                ("Role", models.CharField(max_length=10)),
            ],
            options={"db_table": "userrole",},
        ),
        migrations.CreateModel(
            name="Teacher",
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
                    "Date_of_joining",
                    models.DateField(auto_created=True, default="1991-01-01"),
                ),
                (
                    "Date_of_birth",
                    models.DateField(auto_created=True, default="1991-01-01"),
                ),
                (
                    "ProfileImage",
                    models.FileField(default="avatar.png", upload_to="profiles/"),
                ),
                ("FullName", models.CharField(blank=True, default="", max_length=25)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("m", "male"), ("f", "female")], max_length=5
                    ),
                ),
                ("Roll_no", models.IntegerField()),
                ("Address", models.TextField(blank=True, default="", max_length=150)),
                (
                    "Master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ehousingapp.master",
                    ),
                ),
            ],
            options={"db_table": "teacher",},
        ),
        migrations.CreateModel(
            name="Student",
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
                    "Date_of_joining",
                    models.DateField(auto_created=True, default="1991-01-01"),
                ),
                (
                    "Date_of_birth",
                    models.DateField(auto_created=True, default="1991-01-01"),
                ),
                (
                    "ProfileImage",
                    models.FileField(default="news-5.jpg", upload_to="profiles/"),
                ),
                ("FullName", models.CharField(blank=True, default="", max_length=25)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("m", "male"), ("f", "female")], max_length=5
                    ),
                ),
                ("Roll_no", models.IntegerField(blank=True, default="1")),
                ("Address", models.TextField(blank=True, default="", max_length=150)),
                (
                    "Master",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ehousingapp.master",
                    ),
                ),
            ],
            options={"db_table": "student",},
        ),
        migrations.AddField(
            model_name="master",
            name="UserRole",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ehousingapp.userrole"
            ),
        ),
    ]
