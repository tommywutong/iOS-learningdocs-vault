---
title: 'trace(_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/logger/trace(_:)'
source_url: 'https://developer.apple.com/documentation/os/logger/trace(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger/trace%28_%3A%29.json'
content_hash: 'sha256:180da2680d2018dd'
translated: true
---

> 导航：[Technologies](../../technologies.md) · [os](../../os.md) · [Logger](../logger.md)

# trace(_:)

<sub>实例方法</sub>

向日志写入一条跟踪消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trace(_ message: OSLogMessage)
```

## 参数

- `message` — logger 写入日志的插值字符串。消息中的每一处插值都可以指定各自的格式化与隐私选项。更多信息参见 [消息参数格式化器](../message-argument-formatters.md)。

## 讨论

> [!important] 重要
> 不要创建 [OSLogMessage](../oslogmessage.md) 的实例。相反，请以插值字符串作为 `message` 参数提供，系统会自动进行转换。

此方法在功能上等效于 [debug(_:)](<debug(__).md>) 方法。

## 另请参阅

### 记录作用域消息

- [notice(_:)](<notice(__).md>) — 使用默认日志类型向日志写入一条消息。
- [debug(_:)](<debug(__).md>) — 向日志写入一条调试消息。
- [info(_:)](<info(__).md>) — 向日志写入一条信息性消息。
- [error(_:)](<error(__).md>) — 向日志写入有关错误的信息。
- [warning(_:)](<warning(__).md>) — 向日志写入有关警告的信息。
- [fault(_:)](<fault(__).md>) — 向日志写入一条关于你的 App 执行时出现的 bug 的消息。
- [critical(_:)](<critical(__).md>) — 向日志写入一条关于你的 App 执行中关键事件的消息。
