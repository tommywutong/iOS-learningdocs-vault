---
title: 调试时自定义日志记录行为
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/customizing-logging-behavior-while-debugging
source_url: 'https://developer.apple.com/documentation/os/customizing-logging-behavior-while-debugging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/customizing-logging-behavior-while-debugging.json'
content_hash: 'sha256:1755d736b2f161bf'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 调试时自定义日志记录行为

<sub>文章</sub>

控制记录哪些日志事件。

## 概述

日志记录行为通常由系统统一管理。不过，在 macOS 上调试时，你可以以 root 身份登录，使用 `log` 命令行工具的 `config` 参数为某个子系统启用不同的日志记录级别。下面的示例展示了如何为某个子系统启用 debug 级别的日志记录：

```bash
$ sudo log config --mode "level:debug" --subsystem com.your_company.your_subsystem_name
```

使用 `log` 工具的 `status` 参数查看某个子系统当前的日志记录级别：

```bash
$ sudo log config --status --subsystem com.your_company.your_subsystem_name
Mode for 'com.your_company.your_subsystem_name'  DEBUG
```

你也可以在 `/Library/Preferences/Logging/Subsystems/` 目录下创建并安装一个日志记录配置描述文件属性列表文件，从而覆盖特定子系统的日志记录行为。用一个反向 DNS 表示法的标识符字符串给该文件命名，例如 `com.your_company.your_subsystem_name.plist`。接下来，在文件的顶层添加一个或多个设置字典。`DEFAULT-OPTIONS` 设置字典为整个子系统定义全局行为设置。分类设置字典则为该子系统内特定分类的消息定义行为。下面的示例展示了日志记录配置描述文件的顶层结构：

```plist
<dict>
    <key>DEFAULT-OPTIONS</key>
    <dict>
       <!-- GLOBAL SUBSYSTEM OR PROCESS SETTINGS -->
    </dict>
    <key>CategoryName</key>
    <dict>
       <!-- CATEGORY SETTINGS -->
    </dict>
</dict>
```

日志记录描述文件里的每个设置字典都包含一个 `Level` 子字典，其中包含以下设置键：

| 键 | 说明 |
|---|---|
| `Enable` | 启用特定的日志级别。 |
| `Persist` | 控制消息是先存储在内存中再保存到数据存储区，还是仅存储在内存中。 |

`Enable` 键和 `Persist` 键都接受以下字符串值：

| 值 | 说明 |
|---|---|
| `Inherit` | 明确指定该子系统或分类继承其父级的行为。对分类而言，父级是子系统；对子系统而言，父级是系统。 |
| `Default` | 只捕获 default 级别的消息。 |
| `Info` | 捕获 default 级别和 info 级别的消息。 |
| `Debug` | 捕获 default 级别、info 级别和 debug 级别的消息。 |

下面的示例展示了一个 `Level` 子字典，它启用了 info 级别的日志记录，并继承子系统或系统的持久化行为：

```plist
<key>Level</key>
<dict>
    <key>Enable</key>
    <string>Info</string>
    <key>Persist</key>
    <string>Inherit</string>
</dict>
```

下面的示例展示了一份完整的日志记录描述文件，它把某个子系统配置为执行 info 级别的日志记录，并把该子系统内的 `server-connections` 分类配置为执行 debug 级别的日志记录：

```plist
<dict>
    <key>DEFAULT-OPTIONS</key>
    <dict>
        <key>Level</key>
        <dict>
            <key>Enable</key>
            <string>Info</string>
            <key>Persist</key>
            <string>Inherit</string>
        </dict>
    </dict>
    <key>server-connections</key>
    <dict>
        <key>Level</key>
        <dict>
            <key>Enable</key>
            <string>Debug</string>
            <key>Persist</key>
            <string>Inherit</string>
        </dict>
    </dict>
</dict>
```

> [!note] 注意
> 子系统继承系统的日志记录行为，分类继承其所属子系统的行为。因此，只有在设置与继承的行为不同时，才需要显式指定。

## 另请参阅

### 基础

- [Generating Log Messages from Your Code](generating-log-messages-from-your-code.md) — 记录有用的调试与分析信息，并在消息中包含动态内容。
- [Viewing Log Messages](viewing-log-messages.md) — 使用各种工具获取日志信息。
