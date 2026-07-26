---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteraction/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/location%28in%3A%29.json'
content_hash: 'sha256:19b0fcd09c4f7781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# location(in:)

<sub>Instance Method</sub>

Returns the location of the user interaction in the specified view’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func location(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view containing the target coordinate system. To return a point in the window’s coordinate system, specify `nil`.

## Return Value

The location of the interaction in the coordinate system of view.

## See Also

### Managing edit menu interactions

- [delegate](delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- presentEditMenuWithConfiguration:](<presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- reloadVisibleMenu](<reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- updateVisibleMenuPositionAnimated:](<updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- dismissMenu](<dismissmenu().md>) — Dismiss the edit menu if present.
