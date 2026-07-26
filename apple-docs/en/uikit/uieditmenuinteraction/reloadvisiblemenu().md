---
title: reloadVisibleMenu()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteraction/reloadvisiblemenu()
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/reloadvisiblemenu()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/reloadvisiblemenu%28%29.json'
content_hash: 'sha256:6cecb1b174612171'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# reloadVisibleMenu()

<sub>Instance Method</sub>

Updates the actions an edit menu displays.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func reloadVisibleMenu()
```

## Discussion

You use this method to update the actions the menu displays. The method calls [- editMenuInteraction:menuForConfiguration:suggestedActions:](<../uieditmenuinteractiondelegate/editmenuinteraction(__menufor_suggestedactions_).md>) and updates the UI with the menu the delegate returns. The method has no effect if no menu is present.

## See Also

### Managing edit menu interactions

- [delegate](delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- presentEditMenuWithConfiguration:](<presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- updateVisibleMenuPositionAnimated:](<updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- dismissMenu](<dismissmenu().md>) — Dismiss the edit menu if present.
- [- locationInView:](<location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.
