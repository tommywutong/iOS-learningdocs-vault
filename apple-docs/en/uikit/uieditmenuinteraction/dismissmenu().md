---
title: dismissMenu()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteraction/dismissmenu()
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/dismissmenu()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/dismissmenu%28%29.json'
content_hash: 'sha256:66dbe537f2d69749'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# dismissMenu()

<sub>Instance Method</sub>

Dismiss the edit menu if present.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismissMenu()
```

## Discussion

You use this method to dismiss the menu, for example, from an observer callback in your app.

## See Also

### Managing edit menu interactions

- [delegate](delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- presentEditMenuWithConfiguration:](<presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- reloadVisibleMenu](<reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- updateVisibleMenuPositionAnimated:](<updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- locationInView:](<location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.
