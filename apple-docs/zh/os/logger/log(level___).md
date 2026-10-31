---
title: 'log(level:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/log(level:_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/log(level:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/log%28level%3A_%3A%29.json'
content_hash: 'sha256:ffb80a420f25b135'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# log(level:_:)

<sub>实例方法</sub>

使用指定的日志类型向日志写入一条消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func log(level: OSLogType, _ message: OSLogMessage)
```

## 参数

- `level` — 消息的日志级别，决定消息的严重程度以及系统是否将其持久化到磁盘。可能的取值参见 [OSLogType](../oslogtype.md)。

- `message` — logger 写入日志的插值字符串。消息中的每一处插值都可以指定各自的格式化与隐私选项。更多信息参见 [消息参数格式化器](../message-argument-formatters.md)。

## 讨论

> [!important] 重要
> 不要创建 [OSLogMessage](../oslogmessage.md) 的实例。相反，请以插值字符串作为 `message` 参数提供，系统会自动进行转换。

## 另请参阅

### 记录消息

- [log(_:)](<log(__).md>) — 使用默认日志类型向日志写入一条消息。
- [OSLogType](../oslogtype.md) — 统一日志系统提供的各种日志级别。
- [OSLogMessage](../oslogmessage.md) — 表示日志消息的对象。
