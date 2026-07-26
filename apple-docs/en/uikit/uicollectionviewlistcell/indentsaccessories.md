---
title: indentsAccessories
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/indentsaccessories
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentsaccessories'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/indentsaccessories.json'
content_hash: 'sha256:c319cea0e6621acf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# indentsAccessories

<sub>Instance Property</sub>

A Boolean value that detemines whether the cell indents accessories on the leading side.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indentsAccessories: Bool { get set }
```

## Discussion

If the value is [false](../../swift/false.md), the cell indents the content view only.

The default value of this property is [true](../../swift/true.md).

## See Also

### Customizing layout

- [indentationLevel](indentationlevel.md) — The level of indentation for the cell.
- [indentationWidth](indentationwidth.md) — The width of an indentation level.
- [separatorLayoutGuide](separatorlayoutguide.md) — A guide for laying out separators in relation to the primary content in the cell.
