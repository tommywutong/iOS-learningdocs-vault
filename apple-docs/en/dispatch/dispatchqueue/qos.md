---
title: qos
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/qos
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/qos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/qos.json'
content_hash: 'sha256:e751eb22b0a0cbc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# qos

<sub>Instance Property</sub>

The quality-of-service level assgined to the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var qos: DispatchQoS { get }
```

## See Also

### Managing Queue Attributes

- [label](label.md) — The label you assigned to the dispatch queue at creation time.
- [dispatch_set_target_queue](<../dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.
