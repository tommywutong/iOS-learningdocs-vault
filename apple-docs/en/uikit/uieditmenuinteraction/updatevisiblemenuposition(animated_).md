---
title: 'updateVisibleMenuPosition(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteraction/updatevisiblemenuposition(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/updatevisiblemenuposition(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/updatevisiblemenuposition%28animated%3A%29.json'
content_hash: 'sha256:365e63438a6a24e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# updateVisibleMenuPosition(animated:)

<sub>Instance Method</sub>

Updates the position of the currently visible menu with an option to animate the action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func updateVisibleMenuPosition(animated: Bool)
```

## Parameters

- `animated` — `YES` to animate the transition to the new position; `NO` to make the transition immediate.

## Discussion

You use this method to update the location of the menu. This method calls [- editMenuInteraction:targetRectForConfiguration:](<../uieditmenuinteractiondelegate/editmenuinteraction(__targetrectfor_).md>) and updates the position of the menu using the position the delegate returns. The method has no effect if no menu is present.

## See Also

### Managing edit menu interactions

- [delegate](delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- presentEditMenuWithConfiguration:](<presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- reloadVisibleMenu](<reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- dismissMenu](<dismissmenu().md>) — Dismiss the edit menu if present.
- [- locationInView:](<location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.
