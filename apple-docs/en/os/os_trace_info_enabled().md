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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_trace_info_enabled()

<sub>Function</sub>

Returns whether info level trace information is enabled.

> [!warning] Deprecated
> Use [os_log_info_enabled](os_log_info_enabled.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_trace_info_enabled() -> Bool
```

## Discussion

Generally, trace points should not involve expensive operations, however some circumstances warrant it. Use this function to do expensive work only when info level trace messages are enabled.

## See Also

### Deprecated Functions

- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — Returns whether debug level trace information is enabled. _(deprecated)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — Returns whether the specified info level trace information is enabled. _(deprecated)_
