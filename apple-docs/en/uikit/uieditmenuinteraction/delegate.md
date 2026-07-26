---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/delegate.json'
content_hash: 'sha256:73dc701cdab72fcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# delegate

<sub>Instance Property</sub>

An object that customizes presentation of the menu and actions to display for an edit menu interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIEditMenuInteractionDelegate)? { get }
```

## See Also

### Managing edit menu interactions

- [- presentEditMenuWithConfiguration:](<presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- reloadVisibleMenu](<reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- updateVisibleMenuPositionAnimated:](<updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- dismissMenu](<dismissmenu().md>) — Dismiss the edit menu if present.
- [- locationInView:](<location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.
