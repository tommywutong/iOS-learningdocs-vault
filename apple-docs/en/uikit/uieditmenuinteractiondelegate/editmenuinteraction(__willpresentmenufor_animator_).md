---
title: 'editMenuInteraction(_:willPresentMenuFor:animator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:willpresentmenufor:animator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction%28_%3Awillpresentmenufor%3Aanimator%3A%29.json'
content_hash: 'sha256:8a0ad1666588fc45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteractionDelegate](../uieditmenuinteractiondelegate.md)

# editMenuInteraction(_:willPresentMenuFor:animator:)

<sub>Instance Method</sub>

Informs the delegate when the interaction is about to present the menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func editMenuInteraction(_ interaction: UIEditMenuInteraction, willPresentMenuFor configuration: UIEditMenuConfiguration, animator: any UIEditMenuInteractionAnimating)
```

## Parameters

- `interaction` — The interaction object triggering the menu.

- `configuration` — The object containing the configuration details for the menu.

- `animator` — The object you use to add animations that run alongside the appearance transition.

## See Also

### Customizing the Menu

- [- editMenuInteraction:menuForConfiguration:suggestedActions:](<editmenuinteraction(__menufor_suggestedactions_).md>) — Provides the menu to use when the interaction begins or requires an update.
- [- editMenuInteraction:targetRectForConfiguration:](<editmenuinteraction(__targetrectfor_).md>) — Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [- editMenuInteraction:willDismissMenuForConfiguration:animator:](<editmenuinteraction(__willdismissmenufor_animator_).md>) — Informs the delegate when the interaction is about to dismiss the menu.
- [UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with menus.
