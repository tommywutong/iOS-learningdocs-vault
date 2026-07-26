---
title: badgeCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration/badgecount
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/badgecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/badgecount.json'
content_hash: 'sha256:0c747a128daaaf14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# badgeCount

<sub>Instance Property</sub>

The number of items in a multiple-item interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var badgeCount: Int { get set }
```

## Discussion

The system uses this value to generate a badge for the stack of selected items to indicate how many items the menu is acting on. A value below `2` hides the badge. If you don’t set this value, the system determines it automatically.

## See Also

### Handling multiple-item interactions

- [secondaryItemIdentifiers](secondaryitemidentifiers.md) — A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.
