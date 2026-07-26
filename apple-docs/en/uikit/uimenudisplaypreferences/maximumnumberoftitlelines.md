---
title: maximumNumberOfTitleLines
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenudisplaypreferences/maximumnumberoftitlelines
source_url: 'https://developer.apple.com/documentation/uikit/uimenudisplaypreferences/maximumnumberoftitlelines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenudisplaypreferences/maximumnumberoftitlelines.json'
content_hash: 'sha256:1dda2a2340ea5ff7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuDisplayPreferences](../uimenudisplaypreferences.md)

# maximumNumberOfTitleLines

<sub>Instance Property</sub>

The number of lines the menu displays for an item’s title or subtitle before it truncates the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumNumberOfTitleLines: Int { get set }
```

## Discussion

By default, [UIMenu](../uimenu.md) restricts the number of lines in a menu item’s title or subtitle to create a balance between a compact and expressive display. If you dynamically prepare menu items that might contain more text, set this value to a higher number and use this object as the menu’s [displayPreferences](../uimenu/displaypreferences.md).

> [!note] Note
> Setting this property has no effect on menus in Mac Catalyst apps.
