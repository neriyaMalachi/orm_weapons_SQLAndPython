from db import create_db_and_tables, engine
from sqlmodel import Session, select
from models import Weapon
from typing import Optional, List


# -------- פעולות CRUD + שאילתות --------
def add_weapon(session: Session, name: str, type_: str, price: float) -> Weapon:
    w = Weapon(name=name, type=type_, price=price)
    session.add(w)
    session.commit()
    session.refresh(w)
    return w


def get_all_weapons(session: Session) -> List[Weapon]:
    return session.exec(select(Weapon)).all()


def get_weapons_by_type(session: Session, type_: str) -> List[Weapon]:
    stmt = select(Weapon).where(Weapon.type == type_)
    return session.exec(stmt).all()


def get_expensive_weapons(session: Session, min_price: float) -> List[Weapon]:
    stmt = select(Weapon).where(Weapon.price >= min_price).order_by(Weapon.price.desc())
    return session.exec(stmt).all()


def update_weapon_price(session: Session, weapon_id: int, new_price: float) -> Optional[Weapon]:
    w = session.get(Weapon, weapon_id)
    if not w:
        return None
    w.price = new_price
    session.add(w)
    session.commit()
    session.refresh(w)
    return w


def delete_weapon(session: Session, weapon_id: int) -> bool:
    w = session.get(Weapon, weapon_id)
    if not w:
        return False
    session.delete(w)
    session.commit()
    return True


def main():

    create_db_and_tables()
    with Session(engine) as session:
        print("insert valuessss", )
        if not get_all_weapons(session):
            add_weapon(session, "Glock 19", "firearm", 2200)
            add_weapon(session, "AK-47", "firearm", 3500)
            add_weapon(session, "Katana", "cold", 1800)
            add_weapon(session, "Dagger", "cold", 400)
            add_weapon(session, "M4A1", "firearm", 4200)

        print("------------------ select all weapon ------------------")
        for w in get_all_weapons(session):
            print(w)

        print("------------------ select acrose cold ------------------")
        for w in get_weapons_by_type(session, "cold"):
            print(vars(w))

        print("------------------ order_by and < min_price ------------------")
        for w in get_expensive_weapons(session, 2000):
            print(vars(w))

        print("------------------ update where id=1 ------------------", )
        updated = update_weapon_price(session, weapon_id=1, new_price=2500)
        print("update:", vars(updated) if updated else "not found")

        print("------------------ delete where id=4 ------------------" )
        ok = delete_weapon(session, weapon_id=4)
        print("delete" if ok else "not found")


if __name__ == "__main__":
    main()
