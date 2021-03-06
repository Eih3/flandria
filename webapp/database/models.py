from webapp import db
from webapp.utils import get_current_time

class ItemList(db.Model):
    __tablename__ = "item_list"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    table = db.Column(db.String)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    rare_grade = db.Column(db.Integer, default=None)

# Monsters

class Monster(db.Model):
    __tablename__ = "monster"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    level = db.Column(db.Integer)
    range = db.Column(db.String)
    location = db.Column(db.Integer)
    rating_type = db.Column(db.Integer)
    required_hitrate = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    min_dmg = db.Column(db.Integer)
    max_dmg = db.Column(db.Integer)
    physical_defense = db.Column(db.Integer)
    magical_defense = db.Column(db.Integer)

# Equipment stuff

class Accessory(db.Model):
    __tablename__ = "accessory"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    gender = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

class Dress(db.Model):
    __tablename__ = "dress"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    gender = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    duration = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

    included_in_filtered_view = db.Column(db.Boolean, default=False)

class Hat(db.Model):
    __tablename__ = "hat"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    gender = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    duration = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

    included_in_filtered_view = db.Column(db.Boolean, default=False)

# Weapons

class Cariad(db.Model):
    __tablename__ = "cariad"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

class Dagger(db.Model):
    __tablename__ = "dagger"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)  

class Duals(db.Model):
    __tablename__ = "duals"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float) 

class Rifle(db.Model):
    __tablename__ = "rifle"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float) 

class OneHandedSword(db.Model):
    __tablename__ = "one_handed_sword"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

class TwoHandedSword(db.Model):
    __tablename__ = "two_handed_sword"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

class Rapier(db.Model):
    __tablename__ = "rapier"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    itemtype = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    physical_attack_min = db.Column(db.Integer)
    magical_attack_min = db.Column(db.Integer)
    physical_attack_max = db.Column(db.Integer)
    magical_attack_max = db.Column(db.Integer)
    range = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    attack_speed = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

class Shield(db.Model):
    __tablename__ = "shield"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    itemtype = db.Column(db.String)
    physical_defense = db.Column(db.Integer)
    class_land = db.Column(db.String)
    magic_defense = db.Column(db.Integer)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

# Armor

class Gauntlet(db.Model):
    __tablename__ = "gauntlet"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    upgrade_code = db.Column(db.Integer)
    physical_defense = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

class Coat(db.Model):
    __tablename__ = "coat"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    upgrade_code = db.Column(db.Integer)
    physical_defense = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

class Pants(db.Model):
    __tablename__ = "pants"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    upgrade_code = db.Column(db.Integer)
    physical_defense = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

class Shoes(db.Model):
    __tablename__ = "shoes"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    upgrade_code = db.Column(db.String)
    physical_defense = db.Column(db.Integer)
    magic_defense = db.Column(db.Integer)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)   

# Fishing stuff

class FishingBait(db.Model):
    __tablename__ = "fishing_bait"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)

class FishingMaterial(db.Model):
    __tablename__ = "fishing_material"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)

class FishingRod(db.Model):
    __tablename__ = "fishing_rod"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    class_land = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    itemtype = db.Column(db.String)
    tradable = db.Column(db.Boolean)
    bonus_code_1 = db.Column(db.Integer)
    bonus_operator_1 = db.Column(db.String)
    bonus_1 = db.Column(db.Float)
    bonus_code_2 = db.Column(db.Integer)
    bonus_operator_2 = db.Column(db.String)
    bonus_2 = db.Column(db.Float)
    bonus_code_3 = db.Column(db.Integer)
    bonus_operator_3 = db.Column(db.String)
    bonus_3 = db.Column(db.Float)
    bonus_code_4 = db.Column(db.Integer)
    bonus_operator_4 = db.Column(db.String)
    bonus_4 = db.Column(db.Float)
    bonus_code_5 = db.Column(db.Integer)
    bonus_operator_5 = db.Column(db.String)
    bonus_5 = db.Column(db.Float)

# Materials and Recipes

class Material(db.Model):
    __tablename__ = "material"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)
    produced_by_code = db.Column(db.String, db.ForeignKey('recipe.code'))
    produced_by = db.relationship("Recipe")

class Recipe(db.Model):
    __tablename__ = "recipe"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    rare_grade = db.Column(db.Integer)

    result_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    result_item = db.relationship("ItemList", foreign_keys=[result_code])

    material_1_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_1_quantity = db.Column(db.Integer)
    material_1 = db.relationship("ItemList", foreign_keys=[material_1_code])

    material_2_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_2_quantity = db.Column(db.Integer)
    material_2 = db.relationship("ItemList", foreign_keys=[material_2_code])

    material_3_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_3_quantity = db.Column(db.Integer)
    material_3 = db.relationship("ItemList", foreign_keys=[material_3_code])

    material_4_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_4_quantity = db.Column(db.Integer)
    material_4 = db.relationship("ItemList", foreign_keys=[material_4_code])

    material_5_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_5_quantity = db.Column(db.Integer)
    material_5 = db.relationship("ItemList", foreign_keys=[material_5_code])

    material_6_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_6_quantity = db.Column(db.Integer)
    material_6 = db.relationship("ItemList", foreign_keys=[material_6_code])

class ProductBook(db.Model):
    __tablename__ = "product_book"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)

    target_code = db.Column(db.String, db.ForeignKey("production.code"))
    target = db.relationship("Production", foreign_keys=[target_code], lazy="joined")

class Production(db.Model):
    __tablename__ = "production"
    __bind_key__ = "static_florensia_data"

    code = db.Column(db.String, primary_key=True)
    type = db.Column(db.Integer)
    points_needed = db.Column(db.Integer)
    division = db.Column(db.Integer)
    
    result_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    result_quantity = db.Column(db.Integer)
    result_item = db.relationship("ItemList", foreign_keys=[result_code], lazy="joined")

    material_1_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_1_quantity = db.Column(db.Integer)
    material_1 = db.relationship("ItemList", foreign_keys=[material_1_code])

    material_2_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_2_quantity = db.Column(db.Integer)
    material_2 = db.relationship("ItemList", foreign_keys=[material_2_code])

    material_3_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_3_quantity = db.Column(db.Integer)
    material_3 = db.relationship("ItemList", foreign_keys=[material_3_code])

    material_4_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_4_quantity = db.Column(db.Integer)
    material_4 = db.relationship("ItemList", foreign_keys=[material_4_code])

    material_5_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_5_quantity = db.Column(db.Integer)
    material_5 = db.relationship("ItemList", foreign_keys=[material_5_code])

    material_6_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    material_6_quantity = db.Column(db.Integer)
    material_6 = db.relationship("ItemList", foreign_keys=[material_6_code])

# Pet stuff

class PetCombineHelp(db.Model):
    __tablename__ = "pet_combine_help"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    efficiency = db.Column(db.Integer)

class PetCombineStone(db.Model):
    __tablename__ = "pet_combine_stone"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    increment_min = db.Column(db.Integer)
    increment_max = db.Column(db.Integer)

class PetSkillStone(db.Model):
    __tablename__ = "pet_skill_stone"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    cooldown = db.Column(db.Integer)
    casttime = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)
    level = db.Column(db.Integer)
    description = db.Column(db.String)

class Pet(db.Model): # TODO: Stats
    __tablename__ = "pet"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    duration = db.Column(db.Integer)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)

class RidingPet(db.Model):
    __tablename__ = "riding_pet"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    duration = db.Column(db.Integer)
    description = db.Column(db.String)
    tradable = db.Column(db.Boolean)

# Ship stuff

class Shell(db.Model):
    __tablename__ = "shell"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    damage = db.Column(db.Integer)

class ShipAnchor(db.Model):
    __tablename__ = "ship_anchor"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    rare_grade = db.Column(db.Integer)

    ship_deceleration = db.Column(db.Integer)
    ship_turnpower = db.Column(db.Integer)
    balance = db.Column(db.Integer)

class ShipBody(db.Model):
    __tablename__ = "ship_body"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    rare_grade = db.Column(db.Integer)

    ship_defense = db.Column(db.Integer)
    ship_guns_front = db.Column(db.Integer)
    ship_guns_side = db.Column(db.Integer)
    ship_guns_speed = db.Column(db.Integer)
    ship_hitrange = db.Column(db.Integer)
    physical_defense = db.Column(db.Integer)
    protection = db.Column(db.Integer)
    ability_hp = db.Column(db.Integer)

class ShipFigure(db.Model):
    __tablename__ = "ship_figure"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    rare_grade = db.Column(db.Integer)

    balance = db.Column(db.Integer)
    protection = db.Column(db.Integer)

class ShipFlag(db.Model):
    __tablename__ = "ship_flag"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)

class ShipFront(db.Model):
    __tablename__ = "ship_front"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    rare_grade = db.Column(db.Integer)

    physical_defense = db.Column(db.Integer)
    protection = db.Column(db.Integer)
    ability_hp = db.Column(db.Integer)
    balance = db.Column(db.Integer)

class ShipHeadMast(db.Model):
    __tablename__ = "ship_head_mast"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)

    ship_wind_favorable = db.Column(db.Integer)
    ship_wind_adverse = db.Column(db.Integer)
    ship_acceleration = db.Column(db.Integer)
    ship_turnpower = db.Column(db.Integer)
    balance = db.Column(db.Integer)

class ShipMagicStone(db.Model):
    __tablename__ = "ship_magic_stone"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)

    ability_en = db.Column(db.Integer)
    ability_en_recovery = db.Column(db.Integer)

class ShipMainMast(db.Model):
    __tablename__ = "ship_main_mast"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)

    ship_wind_favorable = db.Column(db.Integer)
    ship_wind_adverse = db.Column(db.Integer)
    ship_acceleration = db.Column(db.Integer)
    ship_deceleration = db.Column(db.Integer)
    ship_turnpower = db.Column(db.Integer)
    balance = db.Column(db.Integer)

class ShipNormalWeapon(db.Model):
    __tablename__ = "ship_normal_weapon"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)

    ship_defense = db.Column(db.Integer)
    ship_range = db.Column(db.Integer)
    critical = db.Column(db.Integer)
    ship_reloadspeed = db.Column(db.Integer)
    ship_guns_front = db.Column(db.Integer)
    ship_guns_side = db.Column(db.Integer)
    ship_guns_speed = db.Column(db.Integer)
    ship_hitrange = db.Column(db.Integer)
    balance = db.Column(db.Integer)

    bonus_code_1 = db.Column(db.Integer)
    bonus_1 = db.Column(db.Integer)
    bonus_code_2 = db.Column(db.Integer)
    bonus_2 = db.Column(db.Integer)
    bonus_code_3 = db.Column(db.Integer)
    bonus_3 = db.Column(db.Integer)
    bonus_code_4 = db.Column(db.Integer)
    bonus_4 = db.Column(db.Integer)
    bonus_code_5 = db.Column(db.Integer)
    bonus_5 = db.Column(db.Integer)

class ShipSpecialWeapon(db.Model):
    __tablename__ = "ship_special_weapon"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    npc_price_tuning = db.Column(db.Integer)
    class_sea = db.Column(db.String)
    level_land = db.Column(db.Integer)
    level_sea = db.Column(db.Integer)
    rare_grade = db.Column(db.Integer)

    ship_defense = db.Column(db.Integer)
    ship_range = db.Column(db.Integer)
    critical = db.Column(db.Integer)
    ship_reloadspeed = db.Column(db.Integer)
    ship_guns_speed = db.Column(db.Integer)
    ship_hitrange = db.Column(db.Integer)
    ability_en_usage = db.Column(db.Integer)

    bonus_code_1 = db.Column(db.Integer)
    bonus_1 = db.Column(db.Integer)
    bonus_code_2 = db.Column(db.Integer)
    bonus_2 = db.Column(db.Integer)
    bonus_code_3 = db.Column(db.Integer)
    bonus_3 = db.Column(db.Integer)
    bonus_code_4 = db.Column(db.Integer)
    bonus_4 = db.Column(db.Integer)
    bonus_code_5 = db.Column(db.Integer)
    bonus_5 = db.Column(db.Integer)

# Maps and NPC

class Map(db.Model):
    __tablename__ = "map"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

class NPC(db.Model):
    __tablename__ = "npc"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)

# Quest stuff

class QuestMission(db.Model):
    __tablename__ = "quest_mission"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quest_code = db.Column(db.String, db.ForeignKey('quest.code'))

    work_type = db.Column(db.Integer)
    work_value = db.Column(db.String)
    count = db.Column(db.Integer)

    # 0
    item_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item = db.relationship("ItemList", foreign_keys=[item_code])

    # 1, 4, 17
    npc_code = db.Column(db.String, db.ForeignKey("npc.code"))
    npc = db.relationship("NPC", foreign_keys=[npc_code])

    # 2
    monster_code = db.Column(db.String, db.ForeignKey("monster.code"))
    monster = db.relationship("Monster", foreign_keys=[monster_code])

    # 3
    quest_item_code = db.Column(db.String, db.ForeignKey("quest_item.code"))
    quest_item = db.relationship("QuestItem", foreign_keys=[quest_item_code])

class QuestGiveDescription(db.Model):
    __tablename__ = "quest_give_description"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quest_code = db.Column(db.String, db.ForeignKey('quest.code'))

    item_code = db.Column(db.String, db.ForeignKey("quest_item.code"))
    item = db.relationship("QuestItem", foreign_keys=[item_code])

    amount = db.Column(db.Integer)

class QuestLootDescription(db.Model):
    __tablename__ = "quest_loot_description"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quest_code = db.Column(db.String, db.ForeignKey('quest.code'))

    monster_code = db.Column(db.String, db.ForeignKey("monster.code"))
    monster = db.relationship("Monster", foreign_keys=[monster_code])

    item_code = db.Column(db.String, db.ForeignKey("quest_item.code"))
    item = db.relationship("QuestItem", foreign_keys=[item_code])

    rate = db.Column(db.Integer)

class QuestSelectableItem(db.Model):
    __tablename__ = "quest_selectable_item"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quest_code = db.Column(db.String, db.ForeignKey('quest.code'))

    item_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item = db.relationship("ItemList", foreign_keys=[item_code])

    amount = db.Column(db.Integer)

class QuestDescription(db.Model):
    __tablename__ = "quest_description"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    quest_code = db.Column(db.String, db.ForeignKey("quest.code"))
    language_code = db.Column(db.String)

    title = db.Column(db.String)
    mission_1 = db.Column(db.Text)
    mission_2 = db.Column(db.Text)
    mission_3 = db.Column(db.Text)
    desc = db.Column(db.Text)
    pre_dialog = db.Column(db.Text)
    start_dialog = db.Column(db.Text)
    run_dialog = db.Column(db.Text)
    finish_dialog = db.Column(db.Text)

class Quest(db.Model):
    __tablename__ = "quest"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    level = db.Column(db.Integer)
    must_party = db.Column(db.Boolean)
    player_class = db.Column(db.String)
    exp_reward = db.Column(db.String)
    money_reward = db.Column(db.String)
    location = db.Column(db.Integer)

    before_quest_code = db.Column(db.String, db.ForeignKey("quest.code"))
    before_quest = db.relation("Quest", remote_side=[code])

    source_object_code = db.Column(db.String, db.ForeignKey("npc.code"))
    source_object = db.relationship("NPC", foreign_keys=[source_object_code])

    source_area_code = db.Column(db.String, db.ForeignKey("map.code"))
    source_area = db.relationship("Map", foreign_keys=[source_area_code])

    supplier_code = db.Column(db.String, db.ForeignKey("npc.code"))
    supplier = db.relationship("NPC", foreign_keys=[supplier_code])

    give_descriptions = db.relationship("QuestGiveDescription")
    loot_descriptions = db.relationship("QuestLootDescription")
    selectable_items = db.relationship("QuestSelectableItem")
    missions = db.relationship("QuestMission")
    descriptions = db.relationship("QuestDescription")

class QuestItem(db.Model):
    __tablename__ = "quest_item"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)

class QuestScroll(db.Model): 
    __tablename__ = "quest_scroll"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    quest_code = db.Column(db.String, db.ForeignKey("quest.code"))
    quest = db.relationship("Quest", foreign_keys=[quest_code])

# Enhancing stuff

class UpgradeCrystal(db.Model): # TODO Description languages
    __tablename__ = "upgrade_crystal"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    description = db.Column(db.String)
    tradable = db.Column(db.Boolean)

class UpgradeHelp(db.Model):
    __tablename__ = "upgrade_help"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    description = db.Column(db.String)
    tradable = db.Column(db.Boolean)

class UpgradeRule(db.Model):
    __tablename__ = "upgrade_rule"
    __bind_key__ = "static_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    upgrade_code = db.Column(db.String)
    upgrade_level = db.Column(db.Integer)
    code_0 = db.Column(db.Integer)
    operator_0 = db.Column(db.String)
    value_0 = db.Column(db.Integer)
    code_1 = db.Column(db.Integer)
    operator_1 = db.Column(db.String)
    value_1 = db.Column(db.Integer)
    code_2 = db.Column(db.Integer)
    operator_2 = db.Column(db.String)
    value_2 = db.Column(db.Integer)
    code_3 = db.Column(db.Integer)
    operator_3 = db.Column(db.String)
    value_3 = db.Column(db.Integer)
    gelt = db.Column(db.Integer)

class UpgradeStone(db.Model): # TODO Description languages
    __tablename__ = "upgrade_stone"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    description = db.Column(db.String)
    tradable = db.Column(db.Boolean)

class SealBreakHelp(db.Model):
    __tablename__ = "seal_break_help"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    description = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)

# other stuff

class RandomBox(db.Model):
    __tablename__ = "random_box"
    __bind_key__ = "static_florensia_data"

    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)

    item_0_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_0_quantity = db.Column(db.Integer)
    item_0_probability = db.Column(db.Float)
    item_0 = db.relationship("ItemList", foreign_keys=[item_0_code])
    item_1_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_1_quantity = db.Column(db.Integer)
    item_1_probability = db.Column(db.Float)
    item_1 = db.relationship("ItemList", foreign_keys=[item_1_code])
    item_2_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_2_quantity = db.Column(db.Integer)
    item_2_probability = db.Column(db.Float)
    item_2 = db.relationship("ItemList", foreign_keys=[item_2_code])
    item_3_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_3_quantity = db.Column(db.Integer)
    item_3_probability = db.Column(db.Float)
    item_3 = db.relationship("ItemList", foreign_keys=[item_3_code])
    item_4_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_4_quantity = db.Column(db.Integer)
    item_4_probability = db.Column(db.Float)
    item_4 = db.relationship("ItemList", foreign_keys=[item_4_code])
    item_5_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_5_quantity = db.Column(db.Integer)
    item_5_probability = db.Column(db.Float)
    item_5 = db.relationship("ItemList", foreign_keys=[item_5_code])
    item_6_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_6_quantity = db.Column(db.Integer)
    item_6_probability = db.Column(db.Float)
    item_6 = db.relationship("ItemList", foreign_keys=[item_6_code])
    item_7_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_7_quantity = db.Column(db.Integer)
    item_7_probability = db.Column(db.Float)
    item_7 = db.relationship("ItemList", foreign_keys=[item_7_code])
    item_8_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_8_quantity = db.Column(db.Integer)
    item_8_probability = db.Column(db.Float)
    item_8 = db.relationship("ItemList", foreign_keys=[item_8_code])
    item_9_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_9_quantity = db.Column(db.Integer)
    item_9_probability = db.Column(db.Float)
    item_9 = db.relationship("ItemList", foreign_keys=[item_9_code])
    item_10_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_10_quantity = db.Column(db.Integer)
    item_10_probability = db.Column(db.Float)
    item_10 = db.relationship("ItemList", foreign_keys=[item_10_code])
    item_11_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_11_quantity = db.Column(db.Integer)
    item_11_probability = db.Column(db.Float)
    item_11 = db.relationship("ItemList", foreign_keys=[item_11_code])
    item_12_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_12_quantity = db.Column(db.Float)
    item_12_probability = db.Column(db.Integer)
    item_12 = db.relationship("ItemList", foreign_keys=[item_12_code])
    item_13_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_13_quantity = db.Column(db.Integer)
    item_13_probability = db.Column(db.Float)
    item_13 = db.relationship("ItemList", foreign_keys=[item_13_code])
    item_14_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_14_quantity = db.Column(db.Integer)
    item_14_probability = db.Column(db.Float)
    item_14 = db.relationship("ItemList", foreign_keys=[item_14_code])
    item_15_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_15_quantity = db.Column(db.Integer)
    item_15_probability = db.Column(db.Float)
    item_15 = db.relationship("ItemList", foreign_keys=[item_15_code])
    item_16_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_16_quantity = db.Column(db.Integer)
    item_16_probability = db.Column(db.Float)
    item_16 = db.relationship("ItemList", foreign_keys=[item_16_code])
    item_17_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_17_quantity = db.Column(db.Integer)
    item_17_probability = db.Column(db.Float)
    item_17 = db.relationship("ItemList", foreign_keys=[item_17_code])
    item_18_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_18_quantity = db.Column(db.Integer)
    item_18_probability = db.Column(db.Float)
    item_18 = db.relationship("ItemList", foreign_keys=[item_18_code])
    item_19_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_19_quantity = db.Column(db.Integer)
    item_19_probability = db.Column(db.Float)
    item_19 = db.relationship("ItemList", foreign_keys=[item_19_code])
    item_20_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_20_quantity = db.Column(db.Integer)
    item_20_probability = db.Column(db.Float)
    item_20 = db.relationship("ItemList", foreign_keys=[item_20_code])
    item_21_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_21_quantity = db.Column(db.Integer)
    item_21_probability = db.Column(db.Float)
    item_21 = db.relationship("ItemList", foreign_keys=[item_21_code])
    item_22_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_22_quantity = db.Column(db.Integer)
    item_22_probability = db.Column(db.Float)
    item_22 = db.relationship("ItemList", foreign_keys=[item_22_code])
    item_23_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_23_quantity = db.Column(db.Integer)
    item_23_probability = db.Column(db.Float)
    item_23 = db.relationship("ItemList", foreign_keys=[item_23_code])
    item_24_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_24_quantity = db.Column(db.Integer)
    item_24_probability = db.Column(db.Float)
    item_24 = db.relationship("ItemList", foreign_keys=[item_24_code])
    item_25_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_25_quantity = db.Column(db.Integer)
    item_25_probability = db.Column(db.Float)
    item_25 = db.relationship("ItemList", foreign_keys=[item_25_code])
    item_26_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_26_quantity = db.Column(db.Integer)
    item_26_probability = db.Column(db.Float)
    item_26 = db.relationship("ItemList", foreign_keys=[item_26_code])
    item_27_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_27_quantity = db.Column(db.Integer)
    item_27_probability = db.Column(db.Float)
    item_27 = db.relationship("ItemList", foreign_keys=[item_27_code])
    item_28_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_28_quantity = db.Column(db.Integer)
    item_28_probability = db.Column(db.Float)
    item_28 = db.relationship("ItemList", foreign_keys=[item_28_code])
    item_29_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_29_quantity = db.Column(db.Integer)
    item_29_probability = db.Column(db.Float)
    item_29 = db.relationship("ItemList", foreign_keys=[item_29_code])
    item_30_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_30_quantity = db.Column(db.Integer)
    item_30_probability = db.Column(db.Float)
    item_30 = db.relationship("ItemList", foreign_keys=[item_30_code])
    item_31_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_31_quantity = db.Column(db.Integer)
    item_31_probability = db.Column(db.Float)
    item_31 = db.relationship("ItemList", foreign_keys=[item_31_code])
    item_32_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_32_quantity = db.Column(db.Integer)
    item_32_probability = db.Column(db.Float)
    item_32 = db.relationship("ItemList", foreign_keys=[item_32_code])
    item_33_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_33_quantity = db.Column(db.Integer)
    item_33_probability = db.Column(db.Float)
    item_33 = db.relationship("ItemList", foreign_keys=[item_33_code])
    item_34_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_34_quantity = db.Column(db.Integer)
    item_34_probability = db.Column(db.Float)
    item_34 = db.relationship("ItemList", foreign_keys=[item_34_code])
    item_35_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_35_quantity = db.Column(db.Integer)
    item_35_probability = db.Column(db.Float)
    item_35 = db.relationship("ItemList", foreign_keys=[item_35_code])
    item_36_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_36_quantity = db.Column(db.Integer)
    item_36_probability = db.Column(db.Float)
    item_36 = db.relationship("ItemList", foreign_keys=[item_36_code])
    item_37_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_37_quantity = db.Column(db.Integer)
    item_37_probability = db.Column(db.Float)
    item_37 = db.relationship("ItemList", foreign_keys=[item_37_code])
    item_38_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_38_quantity = db.Column(db.Integer)
    item_38_probability = db.Column(db.Float)
    item_38 = db.relationship("ItemList", foreign_keys=[item_38_code])
    item_39_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_39_quantity = db.Column(db.Integer)
    item_39_probability = db.Column(db.Float)
    item_39 = db.relationship("ItemList", foreign_keys=[item_39_code])
    item_40_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_40_quantity = db.Column(db.Integer)
    item_40_probability = db.Column(db.Float)
    item_40 = db.relationship("ItemList", foreign_keys=[item_40_code])
    item_41_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_41_quantity = db.Column(db.Integer)
    item_41_probability = db.Column(db.Float)
    item_41 = db.relationship("ItemList", foreign_keys=[item_41_code])
    item_42_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_42_quantity = db.Column(db.Integer)
    item_42_probability = db.Column(db.Float)
    item_42 = db.relationship("ItemList", foreign_keys=[item_42_code])
    item_43_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_43_quantity = db.Column(db.Integer)
    item_43_probability = db.Column(db.Float)
    item_43 = db.relationship("ItemList", foreign_keys=[item_43_code])
    item_44_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_44_quantity = db.Column(db.Integer)
    item_44_probability = db.Column(db.Float)
    item_44 = db.relationship("ItemList", foreign_keys=[item_44_code])
    item_45_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_45_quantity = db.Column(db.Integer)
    item_45_probability = db.Column(db.Float)
    item_45 = db.relationship("ItemList", foreign_keys=[item_45_code])
    item_46_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_46_quantity = db.Column(db.Integer)
    item_46_probability = db.Column(db.Float)
    item_46 = db.relationship("ItemList", foreign_keys=[item_46_code])
    item_47_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_47_quantity = db.Column(db.Integer)
    item_47_probability = db.Column(db.Float)
    item_47 = db.relationship("ItemList", foreign_keys=[item_47_code])
    item_48_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_48_quantity = db.Column(db.Integer)
    item_48_probability = db.Column(db.Float)
    item_48 = db.relationship("ItemList", foreign_keys=[item_48_code])
    item_49_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_49_quantity = db.Column(db.Integer)
    item_49_probability = db.Column(db.Float)
    item_49 = db.relationship("ItemList", foreign_keys=[item_49_code])
    item_50_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_50_quantity = db.Column(db.Integer)
    item_50_probability = db.Column(db.Float)
    item_50 = db.relationship("ItemList", foreign_keys=[item_50_code])
    item_51_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_51_quantity = db.Column(db.Integer)
    item_51_probability = db.Column(db.Float)
    item_51 = db.relationship("ItemList", foreign_keys=[item_51_code])
    item_52_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_52_quantity = db.Column(db.Integer)
    item_52_probability = db.Column(db.Float)
    item_52 = db.relationship("ItemList", foreign_keys=[item_52_code])
    item_53_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_53_quantity = db.Column(db.Integer)
    item_53_probability = db.Column(db.Float)
    item_53 = db.relationship("ItemList", foreign_keys=[item_53_code])
    item_54_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_54_quantity = db.Column(db.Integer)
    item_54_probability = db.Column(db.Float)
    item_54 = db.relationship("ItemList", foreign_keys=[item_54_code])
    item_55_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_55_quantity = db.Column(db.Integer)
    item_55_probability = db.Column(db.Float)
    item_55 = db.relationship("ItemList", foreign_keys=[item_55_code])
    item_56_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_56_quantity = db.Column(db.Integer)
    item_56_probability = db.Column(db.Float)
    item_56 = db.relationship("ItemList", foreign_keys=[item_56_code])
    item_57_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_57_quantity = db.Column(db.Integer)
    item_57_probability = db.Column(db.Float)
    item_57 = db.relationship("ItemList", foreign_keys=[item_57_code])
    item_58_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_58_quantity = db.Column(db.Integer)
    item_58_probability = db.Column(db.Float)
    item_58 = db.relationship("ItemList", foreign_keys=[item_58_code])
    item_59_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_59_quantity = db.Column(db.Integer)
    item_59_probability = db.Column(db.Float)
    item_59 = db.relationship("ItemList", foreign_keys=[item_59_code])
    item_60_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item_60_quantity = db.Column(db.Integer)
    item_60_probability = db.Column(db.Float)
    item_60 = db.relationship("ItemList", foreign_keys=[item_60_code])

class Consumable(db.Model):
    __tablename__ = "consumable"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    class_land = db.Column(db.Integer)
    cooltime = db.Column(db.Integer)
    efficiency = db.Column(db.Integer)
    description = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)
    tradable = db.Column(db.Boolean)

class Bullet(db.Model):
    __tablename__ = "bullet"
    __bind_key__ = "static_florensia_data"
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    icon = db.Column(db.String)
    npc_price = db.Column(db.Integer)
    npc_price_disposal = db.Column(db.Integer)

# Other stuff

class ExcludeFromView(db.Model):
    __tablename__ = "exclude_from_view"
    __bind_key__ = "unstatic_florensia_data"
    item_code = db.Column(db.String, db.ForeignKey("item_list.code"), primary_key=True)
    item = db.relationship("ItemList", foreign_keys=[item_code])

class Drop(db.Model):
    __tablename__ = "drop"
    __bind_key__ = "unstatic_florensia_data"
    index = db.Column(db.Integer, primary_key=True, autoincrement=True)

    monster_code = db.Column(db.String, db.ForeignKey("monster.code"))
    monster = db.relationship("Monster", foreign_keys=[monster_code])

    item_code = db.Column(db.String, db.ForeignKey("item_list.code"))
    item = db.relationship("ItemList", foreign_keys=[item_code])

class DropMessage(db.Model):
    __tablename__ = "drop_message"
    __bind_key__ = "unstatic_florensia_data"

    index = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_time = db.Column(db.DateTime, default=get_current_time)

    declined = db.Column(db.Boolean, default=False)
    accepted = db.Column(db.Boolean, default=False)

    monster_code = db.Column(db.String, db.ForeignKey("monster.code"), nullable=False)
    monster = db.relationship("Monster", foreign_keys=[monster_code])

    message = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", foreign_keys=[user_id])
