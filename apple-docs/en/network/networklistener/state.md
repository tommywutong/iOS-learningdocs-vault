---
title: NetworkListener.State
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/state
source_url: 'https://developer.apple.com/documentation/network/networklistener/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/state.json'
content_hash: 'sha256:4f09f1cb81c28ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# NetworkListener.State

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum State
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NetworkListener.State.cancelled](state/cancelled.md) — Cancelled listeners have been invalidated by the client and will send no more events
- [NetworkListener.State.failed(_:)](<state/failed(__).md>) — Failed listeners are no longer able to receive incoming connections
- [NetworkListener.State.ready](state/ready.md) — Ready listeners are able to receive incoming connections Bonjour service may not yet be registered
- [NetworkListener.State.setup](state/setup.md) — Prior to start, the listener will be in the setup state
- [NetworkListener.State.waiting(_:)](<state/waiting(__).md>) — Waiting listeners do not have a viable network
