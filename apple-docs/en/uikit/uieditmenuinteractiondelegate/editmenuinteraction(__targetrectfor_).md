---
title: 'editMenuInteraction(_:targetRectFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:targetrectfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction%28_%3Atargetrectfor%3A%29.json'
content_hash: 'sha256:485fb257100fe6a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteractionDelegate](../uieditmenuinteractiondelegate.md)

# editMenuInteraction(_:targetRectFor:)

<sub>Instance Method</sub>

Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func editMenuInteraction(_ interaction: UIEditMenuInteraction, targetRectFor configuration: UIEditMenuConfiguration) -> CGRect
```

## Parameters

- `interaction` — The interaction object triggering the menu.

- `configuration` — The object containing the configuration details for the menu.

## Return Value

Returns a rectangle relative to the edit menu interaction’s view. Return [CGRectNull](../../coregraphics/cgrectnull.md) to use the default rectangle.

## Discussion

UIKit calls this method when the interaction begins or requires an update for the position of the menu when calling [- updateVisibleMenuPositionAnimated:](<../uieditmenuinteraction/updatevisiblemenuposition(animated_).md>). The menu displays around the target rectangle you provide, space permitting, with the menu pointing in the direction the configuration specifies. When not implemented, the default is an empty rectangle centered at configuration.sourcePoint. Return [CGRectNull](../../coregraphics/cgrectnull.md) to use the default rect.

The following example provides the frame of the subview as the target rectangle for the interaction.

```swift
func editMenuInteraction(_ interaction: UIEditMenuInteraction, targetRectFor configuration: UIEditMenuConfiguration) -> CGRect {
    guard let selectedShapeView = shapeView(at: configuration.sourcePoint) else {
        return .null // Uses the default implementation.
    }

    return selectedShapeView.frame
}
```

## See Also

### Customizing the Menu

- [- editMenuInteraction:menuForConfiguration:suggestedActions:](<editmenuinteraction(__menufor_suggestedactions_).md>) — Provides the menu to use when the interaction begins or requires an update.
- [- editMenuInteraction:willPresentMenuForConfiguration:animator:](<editmenuinteraction(__willpresentmenufor_animator_).md>) — Informs the delegate when the interaction is about to present the menu.
- [- editMenuInteraction:willDismissMenuForConfiguration:animator:](<editmenuinteraction(__willdismissmenufor_animator_).md>) — Informs the delegate when the interaction is about to dismiss the menu.
- [UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with menus.
