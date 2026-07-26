---
title: UITextInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteractiondelegate.json'
content_hash: 'sha256:1a4c937aa0e31b8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextInteractionDelegate

<sub>Protocol</sub>

An interface that an object implements to receive information about text interaction events.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling text interaction events

- [- interactionShouldBegin:atPoint:](<uitextinteractiondelegate/interactionshouldbegin(__at_).md>) — Asks the delegate whether the text interaction should begin.
- [- interactionWillBegin:](<uitextinteractiondelegate/interactionwillbegin(__).md>) — Tells the delegate that the text interaction will begin.
- [- interactionDidEnd:](<uitextinteractiondelegate/interactiondidend(__).md>) — Tells the delegate that the text interaction ended.

## See Also

### Text interactions

- [UITextInteraction](uitextinteraction.md) — An interaction that provides text selection gestures and UI to custom text views.
- [UITextInteractionMode](uitextinteractionmode.md) — Modes that determine the selection behaviors that a text interaction provides.
