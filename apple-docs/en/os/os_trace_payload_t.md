---
title: os_trace_payload_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_trace_payload_t
source_url: 'https://developer.apple.com/documentation/os/os_trace_payload_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_trace_payload_t.json'
content_hash: 'sha256:455ead4034edc13e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_trace_payload_t

<sub>Type Alias</sub>

A pointer to a trace payload.

> [!warning] Deprecated
> Use logging instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(NSObject<OS_xpc_object> *) os_trace_payload_t;
```

## See Also

### Deprecated Type Aliases

- [os_breadcrumb_t](os_breadcrumb_t.md) _(deprecated)_
- [os_trace_payload_object_t](os_trace_payload_object_t.md) — A pointer to a trace payload object. _(deprecated)_
