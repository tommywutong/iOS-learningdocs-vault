---
title: stateUpdateHandler
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/stateupdatehandler
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/stateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/stateupdatehandler.json'
content_hash: 'sha256:32b11a0c01a24585'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# stateUpdateHandler

<sub>Instance Property</sub>

A handler that receives connection group state updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final var stateUpdateHandler: (@Sendable (NWConnectionGroup.State) -> Void)? { get set }
```

## See Also

### Managing Groups

- [State](state-swift.enum.md) — States that indicate whether you can use a connection group to send and receive messages.
- [state](state-swift.property.md) — The current state of the connection group.
- [cancel()](<cancel().md>) — Cancels the connection group object and leaves the network group.
