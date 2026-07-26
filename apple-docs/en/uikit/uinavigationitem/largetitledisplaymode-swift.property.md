---
title: largeTitleDisplayMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/largetitledisplaymode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.property.json'
content_hash: 'sha256:529a1c421d504507'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# largeTitleDisplayMode

<sub>Instance Property</sub>

The mode for displaying the title of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode { get set }
```

## Discussion

When large titles are available, this property controls how the navigation bar displays the navigation item’s title. The default value of this property is [UINavigationItemLargeTitleDisplayModeAutomatic](largetitledisplaymode-swift.enum/automatic.md), which causes the title to use the same styling as the previously displayed navigation item. You can change the value of this property to force the navigation bar to display a large title ([UINavigationItemLargeTitleDisplayModeAlways](largetitledisplaymode-swift.enum/always.md)) or a small title ([UINavigationItemLargeTitleDisplayModeNever](largetitledisplaymode-swift.enum/never.md)) for this item.

If the [prefersLargeTitles](../uinavigationbar/preferslargetitles.md) property of the navigation bar is [false](../../swift/false.md), this property has no effect and the navigation item’s title is always displayed as a small title.

## See Also

### Configuring the title

- [title](title.md) — The navigation item’s title that displays in the navigation bar.
- [attributedTitle](attributedtitle-25fxb.md)
- [largeTitle](largetitle.md) — String to be used as the large title.
- [LargeTitleDisplayMode](largetitledisplaymode-swift.enum.md) — Constants that indicate how to size the title of this item.
