# Nethack-dict

一个用于 NetHack 游戏的英汉术语查询工具。本仓库提供了一个命令行脚本 `nhdict.py`，可将常见的 NetHack 英文术语快速翻译为中文。

## 功能简介

* **查询 NetHack 术语**：运行脚本并传入英文词语，即可输出对应的中文翻译，支持大小写不敏感的多单词短语。
* **可配置的词典**：默认词库存放在同目录下的 `nhdict_config.json` 配置文件中，您可以轻松修改或添加词条，无需更改代码。

## 使用方法

1. **安装依赖**：本脚本仅依赖 Python 3 标准库，无需额外安装第三方库。
2. **执行查询**：

    ```sh
    # 进入脚本所在目录后运行
    python nhdict.py goblin
    python nhdict.py "scroll of magic mapping"
    ```

    若未提供参数或未找到对应词条，脚本会输出帮助信息。
3. **修改词库**：默认词库放在脚本目录下的 `nhdict_config.json` 文件，你可以编辑该文件或指定其他配置文件：

    * **编辑默认配置**：直接打开 `nhdict_config.json`，按照 JSON 键值对格式添加或修改条目。例如：

      ```json
      {
        "new term": "新的翻译"
      }
      ```

      键（左侧）为英文原文，值（右侧）为中文翻译。保存后再次运行脚本即可生效。

    * **使用自定义配置文件**：如果你希望将词库放在其他位置，可以通过 `--config` 参数或环境变量 `NHDICT_CONFIG` 指定配置路径：

      ```sh
      python nhdict.py --config /path/to/custom_dict.json goblin
      # 或
      export NHDICT_CONFIG=/path/to/custom_dict.json
      python nhdict.py goblin
      ```

      脚本会优先使用命令行参数指定的词库，其次使用环境变量指定的路径，若两者均不存在则回退到默认文件。

## 项目结构

```
├─ nhdict.py            # 命令行查询脚本
├─ nhdict_config.json   # 词典配置文件（默认内容）
└─ README.md
```

## 贡献

欢迎提交 PR 补充或改进词条、修复问题。若需更复杂的功能，也欢迎提出 Issue 讨论。