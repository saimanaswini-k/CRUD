from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import Text,JSON,text,func
from typing import Dict
from sqlalchemy.orm import Mapped,mapped_column



class Dataset(Base):
    __tablename__ = 'datasets'

    id:Mapped[str]=mapped_column(Text,primary_key=True)
    datasets_id:Mapped[str]=mapped_column(Text)
    type:Mapped[str]=mapped_column(Text,nullable=False)
    name :Mapped[str]=mapped_column(Text)
    validation_config:Mapped[Dict]=mapped_column(JSON)
    extraction_config:Mapped[Dict]=mapped_column(JSON)
    dedup_config:Mapped[Dict]=mapped_column(JSON)
    data_schema:Mapped[Dict]=mapped_column(JSON)
    denorm_config:Mapped[Dict]=mapped_column(JSON)
    router_config:Mapped[Dict]=mapped_column(JSON)
    dataset_config:Mapped[Dict]=mapped_column(JSON)
    status:Mapped[str]=mapped_column(Text)
    tags:Mapped[str]=mapped_column(Text)
    data_version:Mapped[str]
    created_by:Mapped[str]=mapped_column(Text)
    updated_by:Mapped[str]=mapped_column(Text)

    
    def __repr__(self):
        return f"<Dataset name={self.name} id={self.id}>"
    


    