---
title: stateUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwconnection/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/stateupdatehandler.json'
content_hash: 'sha256:88d55563bbc81933'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# stateUpdateHandler

<sub>Instance Property</sub>

A handler that receives connection state updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var stateUpdateHandler: (@Sendable (NWConnection.State) -> Void)? { get set }
```

## See Also

### Handling State Updates

- [state](state-swift.property.md) — The current state of the connection.
- [State](state-swift.enum.md) — States indicating whether a connection can be used to send and receive data.
