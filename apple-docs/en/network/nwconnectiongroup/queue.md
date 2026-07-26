---
title: queue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/queue
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/queue.json'
content_hash: 'sha256:324da7583067d55d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# queue

<sub>Instance Property</sub>

The queue on which you handle group events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var queue: DispatchQueue? { get }
```

## See Also

### Inspecting Groups

- [descriptor](descriptor.md) — The descriptor of the group you use to initialize the connection group.
- [parameters](parameters.md) — The parameters with which you initialize the connection group.
