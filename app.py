import logging
from logging import handlers
import os

HEADERS = {"Content-type": "application/json"}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMP_ID = ""


# 编写初始化日志的函数
def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 创建日志等级
    logger.setLevel(logging.INFO)
    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    filename = os.path.dirname(os.path.abspath(__file__)) + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when='M',
                                                   interval=1,
                                                   backupCount=3,
                                                   encoding='utf-8')
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中(2个)
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器当中(2个)
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_logging()  # 调用初始化日志的函数
    logging.info("Test 测试日志打印")  # 初始化日之后，能利用logging来打印日志
