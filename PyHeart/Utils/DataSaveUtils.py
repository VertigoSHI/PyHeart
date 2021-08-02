import pandas as pd
import numpy as np
import enum


# 数据存取源 暂时只支持CSV(笑)
class DataSourceType(enum):
    MYSQL = "Mysql"
    REDIS = "Redis"
    JSON = "Json"
    CSV = "CSV"
    MONGODB = "MongoDB"

class DataInteractType(enum):
    WRITE = "Write 写操作"
    READ = "Read 读操作"


class DataSaveUtils:
    def SaveData(self, data_save_type,data_interact_type):
        if data_save_type == DataSourceType.CSV:
           if data_interact_type == DataInteractType.WRITE:
               pass
           elif data_interact_type == DataInteractType.READ:
               pass
        else: pass
