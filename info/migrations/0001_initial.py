# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, max_length=4, verbose_name='year')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=info.models.get_logo_path)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)], default=2017, max_length=4, verbose_name='year')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=info.models.get_speakerpic_path)),
                ('about', models.TextField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=200)),
                ('team_name', models.CharField(max_length=200)),
                ('pic', models.ImageField(blank=True, null=True, upload_to=info.models.get_memberpic_path)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
