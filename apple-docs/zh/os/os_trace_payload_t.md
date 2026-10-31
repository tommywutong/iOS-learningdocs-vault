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
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_trace_payload_t

<sub>类型别名</sub>

指向 trace 负载的指针。

> [!warning] 已废弃
> 请改用日志（logging）。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(NSObject<OS_xpc_object> *) os_trace_payload_t;
```

## 另请参阅

### 已废弃的类型别名

- [os_breadcrumb_t](os_breadcrumb_t.md) _(已废弃)_
- [os_trace_payload_object_t](os_trace_payload_object_t.md) — 指向 trace 负载对象的指针。 _(已废弃)_
