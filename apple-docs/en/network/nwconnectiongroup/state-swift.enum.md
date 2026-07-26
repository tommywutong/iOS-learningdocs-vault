---
title: NWConnectionGroup.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnectiongroup/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwconnectiongroup/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnectiongroup/state-swift.enum.json'
content_hash: 'sha256:7887b24b9d5942d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnectionGroup](../nwconnectiongroup.md)

# NWConnectionGroup.State

<sub>Enumeration</sub>

States that indicate whether you can use a connection group to send and receive messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### States

- [NWConnectionGroup.State.setup](state-swift.enum/setup.md) — You have not yet started the connection group.
- [NWConnectionGroup.State.waiting(_:)](<state-swift.enum/waiting(__).md>) — The connection group is waiting for a network path change.
- [NWConnectionGroup.State.ready](state-swift.enum/ready.md) — The connection group is joined, and ready to send and receive data.
- [NWConnectionGroup.State.failed(_:)](<state-swift.enum/failed(__).md>) — The connection group encountered a fatal error.
- [NWConnectionGroup.State.cancelled](state-swift.enum/cancelled.md) — The connection group has been canceled.

## See Also

### Managing Groups

- [stateUpdateHandler](stateupdatehandler.md) — A handler that receives connection group state updates.
- [state](state-swift.property.md) — The current state of the connection group.
- [cancel()](<cancel().md>) — Cancels the connection group object and leaves the network group.
