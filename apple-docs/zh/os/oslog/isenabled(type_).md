---
title: 'isEnabled(type:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/os/oslog/isenabled(type:)'
source_url: 'https://developer.apple.com/documentation/os/oslog/isenabled(type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/isenabled%28type%3A%29.json'
content_hash: 'sha256:65660d4650534005'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# isEnabled(type:)

<sub>实例方法</sub>

返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEnabled(type: OSLogType) -> Bool
```

## 参数

- `type` — 日志类型常量，例如 [OS_LOG_TYPE_DEFAULT](../os_log_type_t/os_log_type_default.md)、[OS_LOG_TYPE_INFO](../os_log_type_t/os_log_type_info.md)、[OS_LOG_TYPE_DEBUG](../os_log_type_t/os_log_type_debug.md)、[OS_LOG_TYPE_ERROR](../os_log_type_t/os_log_type_error.md) 或 [OS_LOG_TYPE_FAULT](../os_log_type_t/os_log_type_fault.md)，用于指定要检查的日志级别。

## 返回值

若指定级别的日志记录处于启用状态，则为 [true](../../swift/true.md)；否则为 [false](../../swift/false.md)。
