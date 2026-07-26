---
title: concurrent
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/attributes/concurrent
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes/concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/attributes/concurrent.json'
content_hash: 'sha256:518ad3acef5487a0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [Attributes](../attributes.md)

# concurrent

<sub>Type Property</sub>

The queue schedules tasks concurrently.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let concurrent: DispatchQueue.Attributes
```

## Discussion

If this attribute is not present, the queue schedules tasks serially in first-in, first-out (FIFO) order.

## See Also

### Attributes

- [initiallyInactive](initiallyinactive.md) — The newly created queue is inactive.
