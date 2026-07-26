---
title: UIContextMenuInteractionCommitAnimating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuinteractioncommitanimating
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractioncommitanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractioncommitanimating.json'
content_hash: 'sha256:3e6b67a5c34b873c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuInteractionCommitAnimating

<sub>Protocol</sub>

Methods adopted by system-supplied animator objects when committing preview-related animations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIContextMenuInteractionCommitAnimating : UIContextMenuInteractionAnimating
```

## Overview

When the user taps in a preview interface to dismiss it, UIKit creates an object that adopts this protocol and passes it to your [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) method. Use the object to add any custom animations that you want to run alongside the dismissal animations.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md)

## Topics

### Specifying the Commit Style

- [preferredCommitStyle](uicontextmenuinteractioncommitanimating/preferredcommitstyle.md) — The preferred animation style triggered when the user taps the preview.
- [UIContextMenuInteractionCommitStyle](uicontextmenuinteractioncommitstyle.md) — Constants that control the interaction commit style.

## See Also

### Responding to the menu’s appearance

- [- contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a preview action begins.
