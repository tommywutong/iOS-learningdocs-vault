---
title: UIEditMenuInteractionAnimating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteractionanimating
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractionanimating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractionanimating.json'
content_hash: 'sha256:aa08e7914bd8537a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEditMenuInteractionAnimating

<sub>Protocol</sub>

Methods adopted by system-supplied animator objects when interacting with menus.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIEditMenuInteractionAnimating : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Adding Animations

- [- addAnimations:](<uieditmenuinteractionanimating/addanimations(__).md>) — Adds a closure that performs animations to run alongside the edit menu interaction presentation.
- [- addCompletion:](<uieditmenuinteractionanimating/addcompletion(__).md>) — Adds a closure to perform operations when the edit menu interaction presentation animations are complete.

## See Also

### Customizing the Menu

- [- editMenuInteraction:menuForConfiguration:suggestedActions:](<uieditmenuinteractiondelegate/editmenuinteraction(__menufor_suggestedactions_).md>) — Provides the menu to use when the interaction begins or requires an update.
- [- editMenuInteraction:targetRectForConfiguration:](<uieditmenuinteractiondelegate/editmenuinteraction(__targetrectfor_).md>) — Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [- editMenuInteraction:willPresentMenuForConfiguration:animator:](<uieditmenuinteractiondelegate/editmenuinteraction(__willpresentmenufor_animator_).md>) — Informs the delegate when the interaction is about to present the menu.
- [- editMenuInteraction:willDismissMenuForConfiguration:animator:](<uieditmenuinteractiondelegate/editmenuinteraction(__willdismissmenufor_animator_).md>) — Informs the delegate when the interaction is about to dismiss the menu.
