---
title: os_activity_start
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_start
source_url: 'https://developer.apple.com/documentation/os/os_activity_start'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_start.json'
content_hash: 'sha256:3ce7a1548d0e8ca1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_start

<sub>Macro</sub>

> [!warning] Deprecated
> Use [os_activity_create](os_activity_create.md) and [os_activity_apply](os_activity_apply.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_start(description, flags)
```

## See Also

### Deprecated Macros

- [os_activity_set_breadcrumb](os_activity_set_breadcrumb.md) — Flags the current activity as a breadcrumb, to signify an interesting event. _(deprecated)_
- [OS_TRACE_TYPE_DEBUG](os_trace_type_debug.md) — Trace messages that occur when a debugger is attached. _(deprecated)_
- [OS_TRACE_TYPE_INFO](os_trace_type_info.md) — Trace messages that occur when a debugger is attached and additional info is requested. _(deprecated)_
- [OS_TRACE_TYPE_RELEASE](os_trace_type_release.md) — Trace messages to be captured on your app when instealled on a user’s device. _(deprecated)_
