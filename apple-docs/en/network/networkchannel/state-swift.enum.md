---
title: NetworkChannel.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/state-swift.enum
source_url: 'https://developer.apple.com/documentation/network/networkchannel/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/state-swift.enum.json'
content_hash: 'sha256:5667c1479dde6b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# NetworkChannel.State

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NetworkChannel.State.cancelled](state-swift.enum/cancelled.md) — Cancelled connections have been invalidated by the client and will send no more events
- [NetworkChannel.State.failed(_:)](<state-swift.enum/failed(__).md>)
- [NetworkChannel.State.preparing](state-swift.enum/preparing.md) — Preparing connections are actively establishing the connection
- [NetworkChannel.State.ready](state-swift.enum/ready.md) — Ready connections can send and receive data
- [NetworkChannel.State.setup](state-swift.enum/setup.md) — The initial state prior to start
- [NetworkChannel.State.waiting(_:)](<state-swift.enum/waiting(__).md>)
