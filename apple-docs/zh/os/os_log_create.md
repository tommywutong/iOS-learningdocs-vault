---
title: os_log_create
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_create
source_url: 'https://developer.apple.com/documentation/os/os_log_create'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_create.json'
content_hash: 'sha256:c1aa28515862ca30'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_log_create

<sub>函数</sub>

创建一个自定义日志对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_log_tos_log_create(const char *subsystem, const char *category);
```

## 参数

- `subsystem` — 一个采用反向 DNS 表示法的标识符字符串，表示正在执行日志记录的子系统，例如 `com.your_company.your_subsystem_name`。该子系统用于对相关日志消息进行分类和过滤，以及对相关日志记录设置进行分组。

- `category` — 指定子系统内的一个分类。系统使用该分类对相关日志消息进行分类和过滤，并在子系统设置内对相关日志记录设置进行分组。分类的日志记录设置会覆盖其父子系统的设置。

## 返回值

一个 `os_log_t` 类型的值，可将其传给其他日志记录函数以执行日志记录，并判断特定日志级别是否已启用。该函数始终会返回一个值；不再需要时应将其释放。

## 讨论

通常情况下，使用 [OS_LOG_DEFAULT](os_log_default.md) 常量，按系统的默认行为执行日志记录。仅当你想用特定的子系统和分类标记消息以便过滤，或想通过描述文件自定义子系统的日志记录行为以供调试时，才需要创建自定义日志对象。你只需调用一次此函数来初始化自定义日志对象。更改日志记录设置时无需再次调用。系统会自动检测日志记录设置的更改。

## 另请参阅

### 相关文档

- [os_log_type_enabled](<oslog/isenabled(type_).md>) — 返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。
