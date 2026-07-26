---
title: separatorLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/separatorlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/separatorlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/separatorlayoutguide.json'
content_hash: 'sha256:3ca65d901ead7456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# separatorLayoutGuide

<sub>Instance Property</sub>

A guide for laying out separators in relation to the primary content in the cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var separatorLayoutGuide: UILayoutGuide { get }
```

## Discussion

This property only takes effect in a layout section that supports separators, like a section that you create using [list(using:layoutEnvironment:)](<../nscollectionlayoutsection/list(using_layoutenvironment_).md>).

The separator layout guide represents the frame of the separator, which the system uses to determine where to draw the separator at the bottom of the cell.

By default, when you apply a system-provided content configuration to a list cell, the separator automatically aligns to the primary text in the content view. For custom subviews in the cell, you need to add a constraint to this layout guide that connects it to the leading edge of the cell’s primary content.

![](../../../../attachments/8604949838a7f6bcc3cba5d4bc284a2f/media-3680734@2x.png)

<sub>Diagram of a Favorites menu item with a separator below the cell, indicating another cell below. The separator layout guide appears around the frame of the separator. The leading edge of the separator layout guide is constrained to the leading edge of the primary content, the beginning of the word “Favorites.”</sub>

To align the separators to your content, add constraints to the leading or trailing anchors of this layout guide.

## See Also

### Customizing layout

- [indentationLevel](indentationlevel.md) — The level of indentation for the cell.
- [indentationWidth](indentationwidth.md) — The width of an indentation level.
- [indentsAccessories](indentsaccessories.md) — A Boolean value that detemines whether the cell indents accessories on the leading side.
