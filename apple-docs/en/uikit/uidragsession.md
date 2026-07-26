---
title: UIDragSession
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragsession
source_url: 'https://developer.apple.com/documentation/uikit/uidragsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragsession.json'
content_hash: 'sha256:fca8928a91859b11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDragSession

<sub>Protocol</sub>

The interface for configuring a drag session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIDragSession : UIDragDropSession
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIDragDropSession](uidragdropsession.md)

## Topics

### Accessing local information

- [localContext](uidragsession/localcontext.md) — The optional custom data that you attach to a drag session, visible only to the app in which the drag activity begins.

## See Also

### Drag sources

- [UIDragItem](uidragitem.md) — A representation of an underlying data item as a person drags it from one location to another.
- [UIDragDropSession](uidragdropsession.md) — The common interface for querying the state of both drag sessions and drop sessions.
- [UIDragAnimating](uidraganimating.md) — The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.
