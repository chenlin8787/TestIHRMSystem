# 将初始化日志配置的代码放在api模块下的__init__.py中
# 为什么要把初始化日志配置的代码放在这里
# 原因是：后续我们是通过script中的脚本进行测试，而script会先调用封装的api接口
# 也就是script中的测试用例脚本，会先导入api模块中封装的接口
# 由于导入api模块中的接口时，会优先运行__init__.py中的代码
# 所以只要我们导入了api中接口，那么就会运行__init__.py中的代码，从而自动地完成初始化日志配置的操作
# 把整个项目的日志模块都进行一次初始化，后续所有的代码都可以使用logging.info来打印日志
import app, logging

# 初始化日志
app.init_logging()
logging.debug("DEBUG TEST--------")
logging.info("INFO test--------")
