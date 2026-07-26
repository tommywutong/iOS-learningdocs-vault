---
title: indentationLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/indentationlevel
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/indentationlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/indentationlevel.json'
content_hash: 'sha256:90e22306e946d0ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# indentationLevel

<sub>Instance Property</sub>

The level of indentation for the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var indentationLevel: Int { get set }
```

## Discussion

The indentation level sets automatically when you use a hierarchical data source, such as an [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md).

## See Also

### Customizing layout

- [indentationWidth](indentationwidth.md) — The width of an indentation level.
- [indentsAccessories](indentsaccessories.md) — A Boolean value that detemines whether the cell indents accessories on the leading side.
- [separatorLayoutGuide](separatorlayoutguide.md) — A guide for laying out separators in relation to the primary content in the cell.
