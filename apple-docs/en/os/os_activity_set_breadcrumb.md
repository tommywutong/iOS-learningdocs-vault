---
title: os_activity_set_breadcrumb
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_set_breadcrumb
source_url: 'https://developer.apple.com/documentation/os/os_activity_set_breadcrumb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_set_breadcrumb.json'
content_hash: 'sha256:f7ab7150c9561826'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_set_breadcrumb

<sub>Macro</sub>

Flags the current activity as a breadcrumb, to signify an interesting event.

> [!warning] Deprecated
> Use [os_activity_label_useraction](os_activity_label_useraction.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_set_breadcrumb(name)
```

## Parameters

- `name` — A label that describes the breadcrumb.

## Discussion

Use breadcrumbs to track interactions that span across multiple activities. Keep in mind that not all activities are interesting events.

This function can only be called once per activity;  subsequent calls are ignored.

## See Also

### Deprecated Macros

- [os_activity_start](os_activity_start.md) _(deprecated)_
- [OS_TRACE_TYPE_DEBUG](os_trace_type_debug.md) — Trace messages that occur when a debugger is attached. _(deprecated)_
- [OS_TRACE_TYPE_INFO](os_trace_type_info.md) — Trace messages that occur when a debugger is attached and additional info is requested. _(deprecated)_
- [OS_TRACE_TYPE_RELEASE](os_trace_type_release.md) — Trace messages to be captured on your app when instealled on a user’s device. _(deprecated)_
