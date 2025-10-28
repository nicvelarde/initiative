from sqlalchemy.orm import Session
from models import User, Campaign, Battle, Combatant
from schemas import UserCreate, CampaignCreate, BattleCreate, CombatantCreate

#---USER---
def create_user(db: Session, user: UserCreate):
    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

#---CAMPAIGN---
def create_campaign(db: Session, campaign: CampaignCreate, gm_id: int):
    new_campaign = Campaign(name=campaign.name, gm_id=gm_id)
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    return new_campaign

def get_campaigns_by_gm(db: Session, gm_id: int):
    return db.query(Campaign).filter(Campaign.gm_id == gm_id).all()

# ---BATTLE---
def create_battle(db: Session, battle: BattleCreate):
    new_battle = Battle(
        name=battle.name,
        campaign_id=battle.campaign_id,
        is_active=False
    )
    db.add(new_battle)
    db.commit()
    db.refresh(new_battle)
    return new_battle

def set_battle_active(db: Session, battle_id: int, active: bool):
    battle = db.query(Battle).filter(Battle.id == battle.id).first()
    if battle:
        battle.is_active = active
        db.commit()
        db.refresh(battle)
    return battle

# ---COMBATANT---
def add_combatant(db: Session, combatant: CombatantCreate):
    new_combatant = Combatant(
        name=combatant.name,
        type=combatant.type,
        initiative=combatant.initiative,
        ac=combatant.ac,
        hp=combatant.hp,
        battle_id=combatant.battle_id
    )
    db.add(new_combatant)
    db.commit()
    db.refresh(new_combatant)
    return new_combatant

def get_combatants_by_battle(db: Session, battle_id: int):
    return (
        db.query(Combatant)
        .filter(Combatant.battle_id == battle_id)
        .order_by(Combatant.initiative.desc())
        .all()
    )