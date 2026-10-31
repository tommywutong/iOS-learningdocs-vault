---
title: Logger
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/logger
source_url: 'https://developer.apple.com/documentation/os/logger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/logger.json'
content_hash: 'sha256:c3627fff833037ca'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# Logger

<sub>结构体</sub>

用于向统一日志系统写入插值字符串消息的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Logger
```

## 概述

创建 [Logger](logger.md) 结构体，并用它来记录有关你的 App 行为的消息。记录消息时，你需要指定消息本身，以及任何有助于评估 App 状态的程序变量或自定义数据。你还要选择一个日志级别来表明该消息的严重程度。系统会在内存中记录日志消息，并且在某些情况下也会把这些消息写入磁盘上的数据存储。日志级别决定哪些消息保留在内存中，哪些会写入磁盘。

创建 [Logger](logger.md) 结构体时，可指定可选的子系统和分类字符串，以便为你记录的所有消息添加上下文。子系统对应你的 App 的某个较大功能区域，分类对应该子系统内的某个具体领域。诊断问题时，可以用这些字符串过滤掉无关消息。

要记录一条消息，请调用与该消息相应日志级别对应的方法。创建消息时，使用 Swift 字符串。字符串可以包含插值，例如有符号和无符号整数、浮点数与双精度值、布尔值、其他字符串、Objective-C 对象，以及遵循 [CustomStringConvertible](../swift/customstringconvertible.md) 协议的类型。你也可以包含元类型，例如 `Int.self`。

```swift
let logger = Logger()
let x = 42
logger.info("The answer is \(x)")
```

当你在消息中包含插值字符串或自定义对象时，系统默认会隐去该字符串或对象的值。此行为可防止系统在日志文件中泄露可能对用户敏感的信息，例如用户的账户信息。如果数据不包含敏感信息，请在记录该信息时更改该值的隐私选项。在下面的代码示例中，系统会隐去第一条日志消息中的账户信息，但会显示第二条日志消息中的用户选择：

```swift
logger.log("Paid with bank account \(accountNumber)")   // Redacted!
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // Visible
```

## 关系

- **遵循**： [Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 创建 Logger

- [init()](<logger/init().md>) — 创建一个写入默认子系统的 logger。
- [init(subsystem:category:)](<logger/init(subsystem_category_).md>) — 使用指定的子系统和分类创建一个 logger。
- [init(_:)](<logger/init(__).md>) — 创建一个写入指定日志的 logger。
- [OSLog](oslog.md) — 相关日志消息的容器。

### 记录消息

- [log(_:)](<logger/log(__).md>) — 使用默认日志类型向日志写入一条消息。
- [log(level:_:)](<logger/log(level___).md>) — 使用指定的日志类型向日志写入一条消息。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
- [OSLogMessage](oslogmessage.md) — 表示日志消息的对象。

### 记录作用域消息

- [notice(_:)](<logger/notice(__).md>) — 使用默认日志类型向日志写入一条消息。
- [debug(_:)](<logger/debug(__).md>) — 向日志写入一条调试消息。
- [trace(_:)](<logger/trace(__).md>) — 向日志写入一条跟踪消息。
- [info(_:)](<logger/info(__).md>) — 向日志写入一条信息性消息。
- [error(_:)](<logger/error(__).md>) — 向日志写入有关错误的信息。
- [warning(_:)](<logger/warning(__).md>) — 向日志写入有关警告的信息。
- [fault(_:)](<logger/fault(__).md>) — 向日志写入一条关于你的 App 执行时出现的 bug 的消息。
- [critical(_:)](<logger/critical(__).md>) — 向日志写入一条关于你的 App 执行中关键事件的消息。

### 实例方法

- [isEnabled(type:)](<logger/isenabled(type_).md>) — 检查 Logger 是否可以为给定的日志类型发出日志消息。这允许你根据日志级别对日志记录进行更精细的控制。

### 类型属性

- [disabled](logger/disabled.md) — 一个已禁用的 Logger，运行时不会发出日志消息。可用于关闭通过某个特定 logger 变量发出的所有日志记录。

## 另请参阅

### 日志消息

- [Message Argument Formatters](message-argument-formatters.md) — 使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
