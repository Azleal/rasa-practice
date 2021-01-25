# week2 笔记

## Rasa介绍:
	- Rasa是一个开源的基于机器学习的chatbot开发框架。其主要分成两大模块：Rasa NLU和Rasa Core。使用Rasa NLU + Rasa Core，开发者可以迅速构建自己的chatbot.

### Rasa NLU:
	- Rasa NLU负责提供自然语言理解的工具，包括意图分类和实体抽取。
	- Intent代表用户意图。Entities即实体，代表用户输入语句的细节信息。

### Rasa Core基本概念总结
	- action: 对系统响应的抽象。Rasa将对话管理视作一个分类问题，每轮都会在预先设定好的action集合中选出一个类别
		- Rasa Core定义了3种action：
		- default action：系统预先定义好的动作，如action_listen、action_restart、action_default_fallback
		- utter action：一般以utter_开头，这种action就只会单纯地给用户返回文本消息。这类的action无需具体实现代码，只需在配置文件中指定其对应的相应文本模板即可
		- custom action：用户可以任意编写此类action的代码。用户一般需要自己架设一个额外服务，然后在实现action时，让代码请求这个服务
	- Tracker：用于追踪对话状态的模块。当用户输入被解析后，会传入Tracker进行更新，然后系统会读取Tracker里的信息，作为策略判断的输入。
		- InMemoryTrackerStore (默认)
		- RedisTrackerStore
		- MongoTrackerStore
		- Custom Tracker Store
	- Events： 用于描述一个对话过程中可能发生的事情。
	- Dispatcher：作用是将消息以各种形式发送给用户。
	- Policy：其输入是tracker记录的当前对话状态，输出是一个系统响应action。
	- Story：描述可能出现的对话场景。实际上story就是一个个用户输入intent(entities)和系统设定的输出action用于policy的训练。

### 实践
	对于本地python环境版本及下载过慢等问题，构建docker镜像。基于https://github.com/BSlience/rasa-conversational-ai。
```
FROM python:3.8-slim

RUN apt-get update && apt install -y curl libzbar-dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /rasa

COPY ./ /rasa/

RUN ls -alh

RUN python -m pip install -U pip

RUN /bin/bash -c "source $HOME/.poetry/env && cd /rasa &&  poetry install && \
    pip3 install  jieba rasa-x --extra-index-url https://pypi.rasa.com/simple "

RUN rasa train --num-threads 4

```
	以上代码构建出训练之后的环境。





	