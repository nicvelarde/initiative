from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

# User Table (Game Master)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password_hash = Column(String)

    # GM can have multiple campaigns
    campaigns = relationship("Campaign", back_populates="gm")

# Campaign Table
class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gm_id = Column(Integer, ForeignKey("users.id"))

    gm = relationship("User", back_populates="campaigns")
    battles = relationship("Battle", back_populates="campaign")

# Battle Table
class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    active = Column(Boolean, default=False)

    campaign = relationship("Campaign", back_populates="battles")
    combatants = relationship("Combatant", back_populates="battle")

# Combatant Table (Players + Monsters)
class Combatant(Base):
    __tablename__ = "combatants"

    id = Column(Integer, primary_key=True, index=True)
    battle_id = Column(Integer, ForeignKey("battles.id"))
    name = Column(String)
    type = Column(String) # player or monster
    initiative = Column(Integer)
    ac = Column(Integer, nullable=True)
    hp = Column(Integer, nullable=True)

    battle = relationship("Battle", back_populates="combatants")