---
title: UIContextMenuInteractionAnimating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuinteractionanimating
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractionanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractionanimating.json'
content_hash: 'sha256:1efe1c31eedde63d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuInteractionAnimating

<sub>Protocol</sub>

Methods adopted by system-supplied animator objects when interacting with context menus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIContextMenuInteractionAnimating : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIContextMenuInteractionCommitAnimating](uicontextmenuinteractioncommitanimating.md)

## Topics

### Adding Custom Animations

- [- addAnimations:](<uicontextmenuinteractionanimating/addanimations(__).md>) — Adds the specified animation block to the animator.
- [- addCompletion:](<uicontextmenuinteractionanimating/addcompletion(__).md>) — Adds the specified completion block to the animator.

### Previewing the Content

- [previewViewController](uicontextmenuinteractionanimating/previewviewcontroller.md) — The current preview view controller.

## See Also

### Handling animations

- [- contextMenuInteraction:willDisplayMenuForConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willdisplaymenufor_animator_).md>) — Informs the delegate when a menu display begins.
- [- contextMenuInteraction:willEndForConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willendfor_animator_).md>) — Informs the delegate when a menu display ends.
