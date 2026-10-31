---
title: os_trace_debug_enabled()
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.13 起废弃）, tvOS 8.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_trace_debug_enabled()
source_url: 'https://developer.apple.com/documentation/os/os_trace_debug_enabled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_trace_debug_enabled%28%29.json'
content_hash: 'sha256:5e86624c8e8a9ea9'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_trace_debug_enabled()

<sub>函数</sub>

返回 debug 级别的 trace 信息是否处于启用状态。

> [!warning] 已废弃
> 请改用 [os_log_debug_enabled](os_log_debug_enabled.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_trace_debug_enabled() -> Bool
```

## 讨论

一般而言，trace 点不应涉及昂贵操作，但在某些情况下有必要这样做。使用此函数，仅在启用了 debug 级别的 trace 消息时才执行昂贵工作。

## 另请参阅

### 已废弃函数

- [os_trace_info_enabled](<os_trace_info_enabled().md>) — 返回 info 级别的 trace 信息是否处于启用状态。 _(已废弃)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — 返回指定 info 级别的 trace 信息是否处于启用状态。 _(已废弃)_
