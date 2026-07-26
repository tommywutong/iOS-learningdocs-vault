---
title: accessories
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlistcell/accessories-8nui4
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/accessories-8nui4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlistcell/accessories-8nui4.json'
content_hash: 'sha256:5c8c78baf7ebbbc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewListCell](../uicollectionviewlistcell.md)

# accessories

<sub>Instance Property</sub>

An array of the accessories that decorate the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var accessories: [UICellAccessory] { get set }
```

## Discussion

System accessories have system-defined placement within the cell. The system automatically determines their rendering order and which side of the cell they appear on. The order of system accessories in the array doesn’t affect their placement.

For custom accessories, you determine their placement. The order of custom accessories in the array affects the order in which the system evaluates their [Position](../uicellaccessory-swift.struct/placement/position.md).

> [!important] Important
> The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

## See Also

### Managing cell accessories

- [UICellAccessory](../uicellaccessory-swift.struct.md) — An accessory in a collection view list cell.
