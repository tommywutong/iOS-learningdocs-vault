---
title: 'os_trace_type_enabled(_:)'
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.13 起废弃）, tvOS 8.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/os/os_trace_type_enabled(_:)'
source_url: 'https://developer.apple.com/documentation/os/os_trace_type_enabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_trace_type_enabled%28_%3A%29.json'
content_hash: 'sha256:21c860bf5eea87ce'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_trace_type_enabled(_:)

<sub>函数</sub>

返回是否已启用指定的 info 级别 trace 信息。

> [!warning] 已废弃
> 请改用 [os_log_type_enabled](<oslog/isenabled(type_).md>)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_trace_type_enabled(_ type: UInt8) -> Bool
```

## 参数

- `type` — 要检查的 trace 类型。可能的值为 [OS_TRACE_TYPE_DEBUG](os_trace_type_debug.md) 和 [OS_TRACE_TYPE_INFO](os_trace_type_info.md)。

## 讨论

一般而言，trace 点不应涉及昂贵操作，但某些情况有必要。使用此函数，仅在给定级别的 trace 消息已启用时再做昂贵工作。

## 另请参阅

### 已废弃的函数

- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — 返回是否已启用 debug 级别的 trace 信息。 _(已废弃)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — 返回是否已启用 info 级别的 trace 信息。 _(已废弃)_
