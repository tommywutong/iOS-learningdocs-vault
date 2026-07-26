---
title: os_activity_end
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_end
source_url: 'https://developer.apple.com/documentation/os/os_activity_end'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_end.json'
content_hash: 'sha256:68cb6ab8fbc09de7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_end

<sub>Function</sub>

Ends the specified activity on the current thread.

> [!warning] Deprecated
> Use [os_activity_create](os_activity_create.md) and [os_activity_apply](os_activity_apply.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_end(os_activity_t activity);
```

## Parameters

- `activity` — The activity to end.

## Discussion

Calling this function signifies only that the originator has received control back from the activity.  Work related to the activity may still be in flight at the time this function is called.

## See Also

### Deprecated Functions

- [os_log_is_enabled](os_log_is_enabled.md) _(deprecated)_
- [os_log_is_debug_enabled](os_log_is_debug_enabled.md) _(deprecated)_
- [os_activity_get_active](os_activity_get_active.md) — Returns the stack of nested activities associated with the current thread. _(deprecated)_
- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — Returns whether debug level trace information is enabled. _(deprecated)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — Returns whether info level trace information is enabled. _(deprecated)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — Returns whether the specified info level trace information is enabled. _(deprecated)_
