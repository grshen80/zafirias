from django.db import models
from django import forms
from django.contrib.auth.models import User

CHARACTERS = (
    ('INGRACIA', 'Ingracia'),
    ('RAELENE', 'Raelene'),
    ('RIOCARD', 'Riocard'),
    ('RION', 'Rion'),
)

TYPES = (
    ('COPSE', 'Copse'),
    ('PYRE', 'Pyre'),
    ('TERRA', 'Terra'),
    ('STEEL', 'Steel'),
    ('STORM', 'Storm'),
)

WEAPONS = (
    ('HAMMER', 'Hammer'),      # Terra melee
    ('DAGGER', 'Dagger'),      # Pyre melee
    ('AXE', 'Axe'),            # Copse melee
    ('SWORD', 'Sword'),        # Steel melee
    ('WHIP', 'Whip'),          # Storm melee
    ('BRACELET', 'Bracelet'),  # Pyre ranged magic
    ('RING', 'Ring'),          # Storm ranged magic
    ('EARRINGS', 'Earrings'),  # Terra ranged magic
    ('BOW', 'Bow'),            # Copse ranged weapon
    ('GUN', 'Gun'),            # Steel ranged weapon
    ('STAFF', 'Staff'),        # Terra healer
    ('TORCH', 'Torch'),        # Pyre healer
    ('WAND', 'Wand'),          # Copse healer
    ('SCEPTER', 'Scepter'),    # Steel healer
    ('FLUTE', 'Flute'),        # Storm healer
)

ATTACKS = (

)

DEFENDS = (

)

ULTIMATES = (

)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Character(models.Model):
    name = forms.CharField(max_length=64, choices=CHARACTERS)
    tagline = forms.CharField(max_length=64, unique=True)
    image = models.BinaryField(blank=True)
    type = forms.CharField(max_length=64, choices=TYPES)
    secondary_type = forms.CharField(max_length=64, choices=TYPES, null=True)
    weapon_type = forms.CharField(max_length=64, choices=WEAPONS)
    base_hp = forms.IntegerField()
    base_atk = forms.IntegerField()
    base_spd = forms.IntegerField()
    base_def = forms.IntegerField()
    base_res = forms.IntegerField()
    base_atk_name = forms.CharField(max_length=64)
    base_def_name = forms.CharField(max_length=64)
    base_ult_name = forms.CharField(max_length=64)


class Attack(models.Model):
    name = forms.CharField(max_length=64, choices=ATTACKS)
    atk = forms.IntegerField()
    special = forms.CharField(max_length=64)    # any special effects


class Defend(models.Model):
    name = forms.CharField(max_length=64, choices=DEFENDS)
    special = forms.CharField(max_length=64)    # any special effects


class Ultimate(models.Model):
    name = forms.CharField(max_length=64, choices=ULTIMATES)
    special = forms.CharField(max_length=64)    # any special effects
