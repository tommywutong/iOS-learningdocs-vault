---
title: os_trace_info_enabled()
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+（11.0 起废弃）, iPadOS 10.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.13 起废弃）, tvOS 10.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（4.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_trace_info_enabled()
source_url: 'https://developer.apple.com/documentation/os/os_trace_info_enabled()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_trace_info_enabled%28%29.json'
content_hash: 'sha256:ef5113443af8466b'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_trace_info_enabled()

<sub>函数</sub>

返回是否已启用 info 级别的 trace 信息。

> [!warning] 已废弃
> 请改用 [os_log_info_enabled](os_log_info_enabled.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_trace_info_enabled() -> Bool
```

## 讨论

一般来说，trace 点不应涉及开销较大的操作，但有些情况需要这样做。仅在已启用 info 级别的 trace 消息时，才使用此函数执行开销较大的工作。

## 另请参阅

### 已废弃的函数

- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — 返回是否已启用 debug 级别的 trace 信息。 _(已废弃)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — 返回是否已启用指定的 info 级别 trace 信息。 _(已废弃)_
