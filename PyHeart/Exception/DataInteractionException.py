import enum

class DataInteractionException(Exception):
    pass




class DataInteractionExceptionType(enum):

    UNSUPPORTED_OPERATION = "Unsupported operation 不受支持的操作"

    DATA_FILE_NOT_FOUND = "Data file not found 数据文件未找到"

    DATA_SOURCE_ERROR = "Data source error 数据源配置或读取出错"

    UNKNOWN_ERROR = "Unknown error 恭喜你,这是个人类高质量bug"
