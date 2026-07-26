---
title: os_workgroup_testcancel
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_testcancel
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_testcancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_testcancel.json'
content_hash: 'sha256:ef1c1d4820d3f484'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_workgroup_testcancel

<sub>Function</sub>

Returns a Boolean value that indicates whether the workgroup is canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_workgroup_testcancel(os_workgroup_t wg);
```

## Parameters

- `wg` — The workgroup you want to cancel.

## Return Value

`true` if the workgroup is canceled, or `false` if it is still active.

## See Also

### Cancellation

- [os_workgroup_cancel](os_workgroup_cancel.md) — Cancels and invalidates the specified workgroup.
