---
title: os_signpost_enabled
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_enabled
source_url: 'https://developer.apple.com/documentation/os/os_signpost_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_enabled.json'
content_hash: 'sha256:a51a8657e6a0d466'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_signpost_enabled

<sub>Function</sub>

Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_signpost_enabled(os_log_t log);
```

## Parameters

- `log` — The [OS_LOG_DEFAULT](os_log_default.md) constant or a custom log object that you create with the [os_log_create](os_log_create.md) function.

## See Also

### Getting Log Configuration

- [os_log_info_enabled](os_log_info_enabled.md) — Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.
- [os_log_debug_enabled](os_log_debug_enabled.md) — Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.
- [os_log_type_enabled](<oslog/isenabled(type_).md>) — Returns a Boolean value that indicates whether the log can write messages with the specified log type.
