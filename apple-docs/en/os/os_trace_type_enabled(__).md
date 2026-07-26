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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_trace_type_enabled(_:)

<sub>Function</sub>

Returns whether the specified info level trace information is enabled.

> [!warning] Deprecated
> Use [os_log_type_enabled](<oslog/isenabled(type_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_trace_type_enabled(_ type: UInt8) -> Bool
```

## Parameters

- `type` — The type of trace to check. Possible values are [OS_TRACE_TYPE_DEBUG](os_trace_type_debug.md) and [OS_TRACE_TYPE_INFO](os_trace_type_info.md).

## Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when a given level of trace messages are enabled.

## See Also

### Deprecated Functions

- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — Returns whether debug level trace information is enabled. _(deprecated)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — Returns whether info level trace information is enabled. _(deprecated)_
