from django.db import models
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
    name = models.CharField(max_length=64, choices=CHARACTERS)
    tagline = models.CharField(max_length=64, unique=True)
    image = models.BinaryField(blank=True)
    type = models.CharField(max_length=64, choices=TYPES)
    secondary_type = models.CharField(max_length=64, choices=TYPES, null=True)
    weapon_type = models.CharField(max_length=64, choices=WEAPONS)
    base_hp = models.IntegerField()
    base_atk = models.IntegerField()
    base_spd = models.IntegerField()
    base_def = models.IntegerField()
    base_res = models.IntegerField()
    base_atk_name = models.CharField(max_length=64)
    base_def_name = models.CharField(max_length=64)
    base_ult_name = models.CharField(max_length=64)


class Attack(models.Model):
    name = models.CharField(max_length=64, choices=ATTACKS)
    atk = models.IntegerField()
    special = models.CharField(max_length=64)    # any special effects


class Defend(models.Model):
    name = models.CharField(max_length=64, choices=DEFENDS)
    special = models.CharField(max_length=64)    # any special effects


class Ultimate(models.Model):
    name = models.CharField(max_length=64, choices=ULTIMATES)
    special = models.CharField(max_length=64)    # any special effects
