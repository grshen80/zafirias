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
    """
        A member that extends the native Django User class.
        TODO: add some form of money and other currency tracking, add friends
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Attack(models.Model):
    """
        An attack and any special effects.
    """

    name = models.CharField(max_length=64, choices=ATTACKS)
    atk = models.IntegerField()
    special = models.CharField(max_length=64)    # any special effects


class Defend(models.Model):
    """
        A defense and any special effects.
    """

    name = models.CharField(max_length=64, choices=DEFENDS)
    special = models.CharField(max_length=64)    # any special effects


class Ultimate(models.Model):
    """
        An ultimate and any special effects.
    """
    name = models.CharField(max_length=64, choices=ULTIMATES)
    special = models.CharField(max_length=64)    # any special effects


class Character(models.Model):
    """
        The characters that make up the champions of Zafirias.
    """

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

    max_hp = models.IntegerField(null=True)
    max_atk = models.IntegerField(null=True)
    max_spd = models.IntegerField(null=True)
    max_def = models.IntegerField(null=True)
    max_res = models.IntegerField(null=True)

    base_atk_name = models.ForeignKey(Attack, null=True, on_delete=models.SET_NULL)
    base_def_name = models.ForeignKey(Defend, null=True, on_delete=models.SET_NULL)
    base_ult_name = models.ForeignKey(Ultimate, null=True, on_delete=models.SET_NULL)


class Unit(models.Model):
    """
        A unit connects a Member to a Character, with specific levels and
        stats.
    """

    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    level = models.IntegerField()

    curr_hp = models.IntegerField()
    curr_atk = models.IntegerField()
    curr_spd = models.IntegerField()
    curr_def = models.IntegerField()
    curr_res = models.IntegerField()
    curr_atk_name = models.CharField(max_length=64)
    curr_def_name = models.CharField(max_length=64)
    curr_ult_name = models.CharField(max_length=64)
