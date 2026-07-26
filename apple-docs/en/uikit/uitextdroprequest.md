---
title: UITextDropRequest
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdroprequest
source_url: 'https://developer.apple.com/documentation/uikit/uitextdroprequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdroprequest.json'
content_hash: 'sha256:a6d21bd679013c9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDropRequest

<sub>Protocol</sub>

The interface for specifying the attributes of a drop request for a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDropRequest : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting information about the text drop request

- [dropPosition](uitextdroprequest/dropposition.md) — The text position corresponding to the location of a drop session.
- [sameView](uitextdroprequest/issameview.md) — A Boolean value indicating whether the drag and the drop are within the same text view.
- [suggestedProposal](uitextdroprequest/suggestedproposal.md) — The text drop proposal offered by the text view.

### Getting the drop session

- [dropSession](uitextdroprequest/dropsession.md) — The drop session for the text view.

## See Also

### Drop management

- [UITextDropProposal](uitextdropproposal.md) — A proposed configuration for the behavior of a text drop interaction.
- [Action](uitextdropproposal/action.md) — The text drop action styles for text views.
- [Performer](uitextdropproposal/performer.md) — The performers that are responsible for handling the drop operation.
- [ProgressMode](uitextdropproposal/progressmode.md) — The text drop progress styles for user-visible progress indication.
