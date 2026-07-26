---
title: initiallyInactive
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqueue/attributes/initiallyinactive
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes/initiallyinactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/attributes/initiallyinactive.json'
content_hash: 'sha256:3e5a84d634eb6495'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQueue](../../dispatchqueue.md) · [Attributes](../attributes.md)

# initiallyInactive

<sub>Type Property</sub>

The newly created queue is inactive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let initiallyInactive: DispatchQueue.Attributes
```

## Discussion

Normally, a newly created queue schedules submitted blocks for execution immediately. Use this attribute to prevent the queue from scheduling blocks until you call its [dispatch_activate](<../../dispatchobject/activate().md>) method.

## See Also

### Attributes

- [concurrent](concurrent.md) — The queue schedules tasks concurrently.
