---
title: os_log_is_enabled
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.11+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_log_is_enabled
source_url: 'https://developer.apple.com/documentation/os/os_log_is_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_is_enabled.json'
content_hash: 'sha256:c85c53218e1492b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_log_is_enabled

<sub>Function</sub>

> [!warning] Deprecated
> This function always returns [true](../swift/true.md). Use [os_log_type_enabled](<oslog/isenabled(type_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_log_is_enabled(os_log_t log);
```

## See Also

### Deprecated Functions

- [os_log_is_debug_enabled](os_log_is_debug_enabled.md) _(deprecated)_
- [os_activity_get_active](os_activity_get_active.md) — Returns the stack of nested activities associated with the current thread. _(deprecated)_
- [os_activity_end](os_activity_end.md) — Ends the specified activity on the current thread. _(deprecated)_
- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — Returns whether debug level trace information is enabled. _(deprecated)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — Returns whether info level trace information is enabled. _(deprecated)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — Returns whether the specified info level trace information is enabled. _(deprecated)_
