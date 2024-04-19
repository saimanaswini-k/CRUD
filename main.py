from fastapi import FastAPI,status,HTTPException,Depends
from pydantic import BaseModel
from typing import List,Dict
from database import SessionLocal
from models import Dataset
import models
from models import Dataset


app=FastAPI(
    title="Rest API",
    description="CRUD using FastAPI & Postgresql",
    docs_url="/"
)

class Dataset(BaseModel):
    id:str
    datasets_id:str
    type:str
    name:str
    validation_config:Dict
    extraction_config:Dict
    dedup_config:Dict
    data_schema:Dict
    denorm_config:Dict
    router_config:Dict
    dataset_config:Dict
    status:str
    tags:str
    data_version:int
    created_by:str
    updated_by:str
    


class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/v1/dataset',response_model=List[Dataset],status_code=200)
def get_all_datasets():
    
 datasets=db.query(models.Dataset).all()
 return datasets

@app.get('/v1/dataset/{dataset_id}',response_model=Dataset,status_code=status.HTTP_200_OK)
def get_a_dataset(dataset_id:str):
    dataset=db.query(models.Dataset).filter(models.Dataset.id==dataset_id).first()
    return dataset

    
@app.post('/v1/dataset',response_model=Dataset,status_code=status.HTTP_201_CREATED)
def create_a_dataset(dataset:Dataset):
    db_dataset=db.query(models.Dataset).filter(models.Dataset.name==dataset.name).first()

    if db_dataset is not None:
        raise HTTPException(status_code=400,detail="Dataset already exists")


    new_dataset=models.Dataset(
        id=dataset.id,
        datasets_id=dataset.datasets_id,
        type=dataset.type,
        name=dataset.name,
        validation_config=dataset.validation_config,
        extraction_config=dataset.extraction_config,
        dedup_config=dataset.dedup_config,
        data_schema=dataset.data_schema,
        denorm_config=dataset.denorm_config,
        router_config=dataset.router_config,
        dataset_config=dataset.dataset_config,
        status=dataset.status,
        tags=dataset.tags,
        data_version=dataset.data_version,
        created_by=dataset.created_by,
        updated_by=dataset.updated_by
        
    )

    db.add(new_dataset)
    db.commit()
    

    return new_dataset

@app.put('/v1/dataset/{dataset_id}',response_model=Dataset,status_code=status.HTTP_200_OK)
def update_a_dataset(dataset_id:str,dataset:Dataset):
    dataset_to_update=db.query(models.Dataset).filter(models.Dataset.id==dataset_id).first()

    dataset_to_update.datasets_id=dataset.datasets_id
    dataset_to_update.type=dataset.type
    dataset_to_update.name=dataset.name
    dataset_to_update.validation_config=dataset.validation_config
    dataset_to_update.extraction_config=dataset.extraction_config
    dataset_to_update.dedup_config=dataset.dedup_config
    dataset_to_update.data_schema=dataset.data_schema
    dataset_to_update.denorm_config=dataset.denorm_config
    dataset_to_update.router_config=dataset.router_config
    dataset_to_update.dataset_config=dataset.dataset_config
    dataset_to_update.status=dataset.status
    dataset_to_update.tags=dataset.tags
    dataset_to_update.data_version=dataset.data_version
    


    db.commit()
    return dataset_to_update
    
@app.patch('/v1/dataset/{dataset_id}', response_model=Dataset, status_code=status.HTTP_200_OK)
def update_a_dataset_partial(dataset_id: str, update_data: dict):
  dataset_partial_update = db.query(models.Dataset).filter(models.Dataset.id == dataset_id).first()

  # Update only specified attributes
  for key, value in update_data.items():
    if hasattr(dataset_partial_update, key):  
      setattr(dataset_partial_update, key, value)

  db.commit()
  return dataset_partial_update


@app.delete('/v1/dataset/{dataset_id}')
def delete_dataset(dataset_id:str):
    dataset_to_delete=db.query(models.Dataset).filter(models.Dataset.id==dataset_id).first()

    if dataset_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(dataset_to_delete)
    db.commit()

    return {"Message":"Dataset deleted"}

