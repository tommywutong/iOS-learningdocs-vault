---
title: state
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/state-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwconnection/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/state-swift.property.json'
content_hash: 'sha256:336e7825e03c69ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# state

<sub>Instance Property</sub>

The current state of the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var state: NWConnection.State { get }
```

## See Also

### Handling State Updates

- [State](state-swift.enum.md) — States indicating whether a connection can be used to send and receive data.
- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives connection state updates.
