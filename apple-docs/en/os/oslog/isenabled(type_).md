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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# isEnabled(type:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the log can write messages with the specified log type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEnabled(type: OSLogType) -> Bool
```

## Parameters

- `type` — A log type constant, such as [OS_LOG_TYPE_DEFAULT](../os_log_type_t/os_log_type_default.md), [OS_LOG_TYPE_INFO](../os_log_type_t/os_log_type_info.md), [OS_LOG_TYPE_DEBUG](../os_log_type_t/os_log_type_debug.md), [OS_LOG_TYPE_ERROR](../os_log_type_t/os_log_type_error.md), or [OS_LOG_TYPE_FAULT](../os_log_type_t/os_log_type_fault.md), that specifies the level of logging to check.

## Return Value

[true](../../swift/true.md) if logging at the specified level is in an enabled state; otherwise, [false](../../swift/false.md).
