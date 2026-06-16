from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        user_id=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.user_id == user_id).first()

def update_task(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        if task.title is not None:
            db_task.title = task.title
        if task.description is not None:
            db_task.description = task.description
        if task.completed is not None:
            db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False
