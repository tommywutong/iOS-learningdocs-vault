---
title: 'init(qosClass:relativePriority:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqos/init(qosclass:relativepriority:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/init(qosclass:relativepriority:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/init%28qosclass%3Arelativepriority%3A%29.json'
content_hash: 'sha256:76b378fedf363bab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# init(qosClass:relativePriority:)

<sub>Initializer</sub>

Creates a new `DispatchQoS` object with the specified QoS class and relative priority.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(qosClass: DispatchQoS.QoSClass, relativePriority: Int)
```

## Parameters

- `qosClass` — The QoS class. For possible values, see [QoSClass](qosclass-swift.enum.md).

- `relativePriority` — The relative priority.

## See Also

### Creating a QoS Structure

- [QoSClass](qosclass-swift.enum.md) — Quality-of-service classes that specify the priorities for executing tasks.
