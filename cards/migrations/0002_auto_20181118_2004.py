# Generated by Django 2.1.3 on 2018-11-18 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.SmallIntegerField(verbose_name=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='card',
            old_name='names',
            new_name='name',
        ),
        migrations.AddField(
            model_name='quantity',
            name='Card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.Card'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.User'),
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(related_name='Deck', to='cards.Card'),
        ),
        migrations.AddField(
            model_name='deck',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Deck', to='cards.User'),
        ),
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ManyToManyField(related_name='Card', to='cards.User'),
        ),
    ]
