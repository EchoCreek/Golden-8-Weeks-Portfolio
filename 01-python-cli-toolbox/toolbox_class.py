# 导入所需的库
import os.path

import requests  # 用于发送HTTP网络请求
from googletrans import Translator  # 用于将文本翻译成不同语言
import configparser

# 从requests库的异常模块中，特别导入RequestException和JSONDecodeError
# 这样做可以让我们捕获更具体的异常类型，而不是宽泛的Exception
from requests.exceptions import RequestException, JSONDecodeError


# 定义一个名为Toolbox的类，它集合了多个工具函数
class Toolbox:

    # 类的构造方法（初始化方法）
    # 当创建Toolbox类的实例（对象）时，这个方法会被自动调用
    def __init__(self):
        """
        构造方法不再接收api_key。
        我们将api_key的加载和管理封装在类内部。
        """
        self.api_url = "https://api.seniverse.com/v3/weather/now.json"
        self.cat_api_url = "https://catfact.ninja/fact"
        self.timeout = 10
        # 将api_key作为一个实例属性，其值在需要时才加载
        self.api_key = None

    def _get_api_key(self):
        """
        一个内部方法，用于加载或请求API Key。
        这是整个机制的核心。
        """
        # 如果已经加载过，直接返回
        if self.api_key:
            return self.api_key

        config = configparser.ConfigParser()
        config_file = 'config.ini'

        # 检查配置文件是否存在
        if os.path.exists(config_file):
            config.read(config_file)
            # 尝试从配置文件中读取API Key
            if 'API' in config and 'key' in config['API']:
                self.api_key = config['API']['key']
                return self.api_key

        # 如果文件不存在或文件中没有Key，则提示用户输入
        print("🔑 首次使用或未找到配置，请输入您的心知天气API Key：")
        user_key = input("> ").strip()

        # 保存用户输入的Key到配置文件
        config['API'] = {'key': user_key}
        with open(config_file, 'w') as f:
            config.write(f)

        print("✔ API Key已保存至 config.ini，下次将自动读取。")
        self.api_key = user_key
        return self.api_key

    # 定义一个静态方法 get_ip
    # @staticmethod 装饰器表示这个方法不依赖于类的实例（即不需要self参数）
    # 它可以被类直接调用，例如 Toolbox.get_ip()
    @staticmethod
    def get_ip():
        """
        获取并打印本机的公网IP地址。
        """
        # 开始一个try块，用于捕获可能发生的网络和数据处理异常
        try:
            # 发送GET请求到httpbin.org/ip，并设置超时时间
            response = requests.get("https://httpbin.org/ip", timeout=10)
            # 检查HTTP响应状态码。如果状态码是4xx（客户端错误）或5xx（服务器错误），
            # 这行代码会自动抛出一个HTTPError异常，然后被下面的except块捕获。
            response.raise_for_status()

            # 如果请求成功，将返回的JSON格式内容解析成Python字典
            ip_data = response.json()
            # 从字典中提取'origin'键对应的值（即IP地址）并打印
            print(f"IP: {ip_data['origin']}")

        # 如果在try块中发生了任何与requests相关的网络错误（如连接超时、DNS错误等）
        except RequestException as e:
            print(f"获取IP失败，网络请求错误: {e}")
        # 如果服务器返回的内容不是有效的JSON格式，response.json()会抛出此异常
        except JSONDecodeError:
            print("获取IP失败，无法解析返回的JSON数据。")
        # 如果返回的JSON中没有'origin'这个键，会抛出此异常
        except KeyError:
            print("获取IP失败，返回的JSON数据格式不符合预期。")

    # 定义获取天气的方法，它需要一个实例（self）和一个城市名（city）
    def get_weather(self, city):
        """
        根据城市名称，获取并打印实时天气信息。
        :param city: 需要查询天气的城市名，字符串类型。
        """

        api_key = self._get_api_key()

        # 准备请求所需的参数，这是一个字典
        params = {
            "key": self.api_key,  # API密钥
            "location": city,  # 城市
            "language": "zh-Hans",  # 返回语言为简体中文
            "unit": "c"  # 温度单位为摄氏度
        }

        # 开始异常捕获块
        try:
            # 发送GET请求，传入URL、参数和超时时间
            response = requests.get(self.api_url, params=params, timeout=self.timeout)
            # 同样，检查HTTP响应状态码，确保请求成功
            response.raise_for_status()

            # 解析JSON响应
            data = response.json()

            # 从返回的数据中获取'results'列表
            result_list = data['results']

            # 关键检查：如果API返回的'results'列表为空（例如，找不到该城市）
            if not result_list:
                # 打印提示信息并使用return提前结束该方法
                print(f"找不到城市'{city}'的天气信息。")
                return

            # 如果列表不为空，获取第一个元素（通常只有一个）
            weather_data = result_list[0]

            # 从数据中提取地点、天气现象和温度
            location_name = weather_data['location']['name']
            weather_text = weather_data['now']['text']
            temperature = weather_data['now']['temperature']

            # 格式化并打印天气信息
            print('----------------')
            print(f"地点：{location_name}")
            print(f"天气：{weather_text}")
            print(f"温度：{temperature} ℃")
            print('----------------')

        # 捕获网络请求相关的异常
        except RequestException as e:
            print(f"获取天气失败，网络请求错误: {e}")
        # 捕获JSON解析异常
        except JSONDecodeError:
            print("获取天气失败，无法解析返回的数据。")
        # 将KeyError和IndexError合并捕获，因为它们都代表数据结构不符合预期
        # 例如，JSON中缺少某个键（KeyError），或列表为空却尝试访问元素（IndexError）
        except (KeyError, IndexError) as e:
            print(f"获取天气失败，返回的数据格式不符合预期: {e}")

    # 定义获取猫咪趣闻的方法
    def get_cat_fact(self):
        """
        获取一条随机的猫咪趣闻（英文），打印原文，然后尝试将其翻译成中文。
        """
        # 外层try块，负责获取猫咪趣闻API的数据
        try:
            # 发送GET请求并设置超时
            response = requests.get(self.cat_api_url, timeout=self.timeout)
            # 检查HTTP响应状态码
            response.raise_for_status()

            # 解析JSON数据
            data = response.json()
            # 提取趣闻内容
            cat_fact_english = data['fact']

            # 打印英文原文
            print("---------------")
            print("英文原文：")
            print(cat_fact_english)
            print("---------------")

            # 内层try块，专门处理翻译过程的异常。
            # 这样设计可以确保即使翻译失败，程序也不会崩溃，用户至少能看到英文原文。
            try:
                # 创建一个翻译器实例
                translator = Translator()
                # 调用translate方法进行翻译，目标语言为简体中文('zh-cn')
                translator_result = translator.translate(cat_fact_english, dest='zh-cn')
                # 从翻译结果中获取翻译后的文本
                cat_fact_chinese = translator_result.text

                # 打印中文翻译
                print("中文翻译：")
                print(cat_fact_chinese)
                print("---------------")
            # 捕获翻译过程中可能发生的任何异常（网络、服务限制等）
            except Exception as e:
                # 打印一个友好的错误提示
                print(f"翻译失败，错误: {e}")
                print("---------------")

        # 以下是外层try块对应的异常捕获
        # 捕获网络请求异常
        except RequestException as e:
            print(f"获取猫咪趣闻失败，网络请求错误: {e}")
        # 捕获JSON解析异常
        except JSONDecodeError:
            print("获取猫咪趣闻失败，无法解析返回的数据。")
        # 捕获因数据结构问题导致的KeyError
        except KeyError:
            print("获取猫咪趣闻失败，返回的JSON数据格式不符合预期。")