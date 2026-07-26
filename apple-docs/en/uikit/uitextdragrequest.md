---
title: UITextDragRequest
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragrequest
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragrequest.json'
content_hash: 'sha256:2aa6b26f5f55e8b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDragRequest

<sub>Protocol</sub>

The interface for describing the attributes of a drag activity originating in a text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UITextDragRequest : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the drag items

- [existingItems](uitextdragrequest/existingitems.md) — The array of drag items present in a drag session.
- [suggestedItems](uitextdragrequest/suggesteditems.md) — An array of drag items that the system provides when the text drag delegate doesn’t provide custom drag items.

### Getting information about the text

- [dragRange](uitextdragrequest/dragrange.md) — A range of text associated with a drag item in an active drag session that originated in a text view.
- [selected](uitextdragrequest/isselected.md) — A Boolean value indicating whether text is selected for dragging.

### Getting the drag session

- [dragSession](uitextdragrequest/dragsession.md) — The active drag session.

## See Also

### Drag content

- [UITextDragPreviewRenderer](uitextdragpreviewrenderer.md) — Renders previews of text dragged by the user.
