---
title: indentationWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/indentationwidth
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentationwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/indentationwidth.json'
content_hash: 'sha256:ffc1c2dc137f2948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# indentationWidth

<sub>Instance Property</sub>

The width of an indentation level.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indentationWidth: CGFloat { get set }
```

## Discussion

The overall indentation is the product of [indentationWidth](indentationwidth.md) and [indentationLevel](indentationlevel.md).

## See Also

### Customizing layout

- [indentationLevel](indentationlevel.md) — The level of indentation for the cell.
- [indentsAccessories](indentsaccessories.md) — A Boolean value that detemines whether the cell indents accessories on the leading side.
- [separatorLayoutGuide](separatorlayoutguide.md) — A guide for laying out separators in relation to the primary content in the cell.
