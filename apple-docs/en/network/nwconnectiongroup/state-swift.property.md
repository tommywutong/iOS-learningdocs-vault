---
title: state
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/state-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/state-swift.property.json'
content_hash: 'sha256:9e5dac9f8526541d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# state

<sub>Instance Property</sub>

The current state of the connection group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var state: NWConnectionGroup.State { get }
```

## See Also

### Managing Groups

- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives connection group state updates.
- [State](state-swift.enum.md) — States that indicate whether you can use a connection group to send and receive messages.
- [cancel()](<cancel().md>) — Cancels the connection group object and leaves the network group.
