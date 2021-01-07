## 使用说明

1. 使用了[SpacyNLP](https://rasa.com/docs/rasa/components#spacynlp)作为pipeline
2. 安装依赖 `pip install -U spacy`
3. `python -m spacy download zh_core_web_sm`下载中文model
4. `python -m spacy link zh_core_web_sm zh`
5. `rasa train`
6. `rasa run action`

### 注意:
  - 在`rasa train`之前要删除掉默认生成的英文model, 即清空models文件夹下原有的文件

### 参考:
  - https://rasa.com/docs/rasa/components
  - https://spacy.io/usage/models#download
  
