---
title: UIEditMenuInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractiondelegate.json'
content_hash: 'sha256:99772de789b14a4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEditMenuInteractionDelegate

<sub>Protocol</sub>

The methods for customizing the menu the interaction displays.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol UIEditMenuInteractionDelegate : NSObjectProtocol
```

## Overview

You use this protocol to customize the actions or presentation of the menu an [UIEditMenuInteraction](uieditmenuinteraction.md) object displays.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Customizing the Menu

- [- editMenuInteraction:menuForConfiguration:suggestedActions:](<uieditmenuinteractiondelegate/editmenuinteraction(__menufor_suggestedactions_).md>) — Provides the menu to use when the interaction begins or requires an update.
- [- editMenuInteraction:targetRectForConfiguration:](<uieditmenuinteractiondelegate/editmenuinteraction(__targetrectfor_).md>) — Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [- editMenuInteraction:willPresentMenuForConfiguration:animator:](<uieditmenuinteractiondelegate/editmenuinteraction(__willpresentmenufor_animator_).md>) — Informs the delegate when the interaction is about to present the menu.
- [- editMenuInteraction:willDismissMenuForConfiguration:animator:](<uieditmenuinteractiondelegate/editmenuinteraction(__willdismissmenufor_animator_).md>) — Informs the delegate when the interaction is about to dismiss the menu.
- [UIEditMenuInteractionAnimating](uieditmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with menus.

## See Also

### Edit menus

- [UIEditMenuInteraction](uieditmenuinteraction.md) — An interaction that provides edit operations using a menu.
- [UIEditMenuConfiguration](uieditmenuconfiguration.md) — An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — A set of standard methods that apps can adopt to support editing.
