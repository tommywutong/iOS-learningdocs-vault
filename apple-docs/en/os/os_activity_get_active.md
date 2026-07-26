---
title: os_activity_get_active
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_get_active
source_url: 'https://developer.apple.com/documentation/os/os_activity_get_active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_get_active.json'
content_hash: 'sha256:43ad463112235cbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_get_active

<sub>Function</sub>

Returns the stack of nested activities associated with the current thread.

> [!warning] Deprecated
> This function is no longer supported, and there is no replacement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern unsigned int os_activity_get_active(os_activity_id_t *entries, unsigned int *count);
```

## Parameters

- `entries` — A buffer sized to hold the the number of activities being requested.

- `count` — The number of activities requested.

## Return Value

The number of activities written to `entries`.

## Discussion

Because activities can be nested, there can be more than one activity involved on the current thread.

This function should be used only by diagnostic tools for making additional determinations about a situation.

## See Also

### Deprecated Functions

- [os_log_is_enabled](os_log_is_enabled.md) _(deprecated)_
- [os_log_is_debug_enabled](os_log_is_debug_enabled.md) _(deprecated)_
- [os_activity_end](os_activity_end.md) — Ends the specified activity on the current thread. _(deprecated)_
- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — Returns whether debug level trace information is enabled. _(deprecated)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — Returns whether info level trace information is enabled. _(deprecated)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — Returns whether the specified info level trace information is enabled. _(deprecated)_
