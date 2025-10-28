from pydantic import BaseModel
from typing import List, Optional

# ---USER---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        orm_mode = True

# ---CAMPAIGN---
class CampaignBase(BaseModel):
    name: str

class CampaignCreate(CampaignBase):
    pass

class CampaignResponse(CampaignBase):
    id: int
    gm_id: int
    class Config:
        orm_mode = True

# ---BATTLE---
class BattleBase(BaseModel):
    name: str

class BattleCreate(BattleBase):
    campaign_id: int

class BattleResponse(BattleBase):
    id: int
    campaign_id: int
    is_active: bool
    class Config:
        orm_mode = True

# ---COMBATANT---
class CombatantBase(BaseModel):
    name: str
    type: str
    initiative: int
    ac: int
    hp: int

class CombatantCreate(CombatantBase):
    battle_id: int

class CombatantResponse(CombatantBase):
    id: int
    battle_id: int
    class Config:
        orm_mode: True