---
title: os_log_debug_enabled
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_log_debug_enabled
source_url: 'https://developer.apple.com/documentation/os/os_log_debug_enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_log_debug_enabled.json'
content_hash: 'sha256:8404d10dac90ac37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_log_debug_enabled

<sub>Macro</sub>

Returns a Boolean value that indicates whether debug-level logging is in an enabled state for a specified log object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_log_debug_enabled(log)
```

## Parameters

- `log` — The [OS_LOG_DEFAULT](os_log_default.md) constant or a custom log object that you create with the [os_log_create](os_log_create.md) function.

## Return Value

[true](../swift/true.md) if debug-level logging is in an enabled state; otherwise, [false](../swift/false.md).

## See Also

### Related Documentation

- [OS_LOG_TYPE_DEBUG](../kernel/os_log_type_t/os_log_type_debug.md) — Debug-level messages are only captured in memory when debug logging is enabled through a configuration change. They’re purged in accordance with the configuration’s persistence setting. Messages logged at this level contain information that may be useful during development or while troubleshooting a specific problem. Debug logging is intended for use in a development environment and not in shipping software. Logging a message of this type is equivalent to calling the  function.

### Getting Log Configuration

- [os_log_info_enabled](os_log_info_enabled.md) — Returns a Boolean value that indicates whether info-level logging is in an enabled state for a specified log object.
- [os_log_type_enabled](<oslog/isenabled(type_).md>) — Returns a Boolean value that indicates whether the log can write messages with the specified log type.
- [os_signpost_enabled](os_signpost_enabled.md) — Returns a Boolean value that indicates whether signposts are in an enabled state for the specified log.
