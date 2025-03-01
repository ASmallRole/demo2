import pyttsx3

def text_to_speech(text):
    """
    将给定的文本转换为语音输出。

    参数:
    text (str): 需要转换为语音的文本。

    返回:
    无
    """
    # 初始化语音引擎
    engine = pyttsx3.init()
    
    # 获取所有可用的语音
    voices = engine.getProperty('voices')

    # 筛选出中文语音
    zh_voices = [voice for voice in voices if hasattr(voice, 'languages') and len(voice.languages) > 0 
                 and 'zh' in voice.languages[0].decode('utf-8', errors='ignore').lower()]

    # 设置语音为第一个可用的语音
    engine.setProperty('voice', voices[0].id)

    # 设置语音语速为每分钟150个单词
    engine.setProperty('rate', 150)
    
    # 设置语音音量为最大
    engine.setProperty('volume', 1.0)

    # 将给定的文本加入到语音队列中
    engine.say(text)
    
    # 等待所有语音输出完毕
    engine.runAndWait()

# 测试文字转语音功能
text_to_speech("你好，这是一个工作的文字转语音Python程序示例。")
