---
title: automaticSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/automaticsize
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/automaticsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/automaticsize.json'
content_hash: 'sha256:7059ae75eef7a99b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# automaticSize

<sub>Type Property</sub>

A placeholder size for self-sizing cells.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class let automaticSize: CGSize
```

## Discussion

Set this constant as the value for the [estimatedItemSize](estimateditemsize.md) property to enable self-sizing cells for your collection view. This is a non-zero, placeholder value that tells the collection view to query each cell for its actual size using the cell’s [- preferredLayoutAttributesFittingAttributes:](<../uicollectionreusableview/preferredlayoutattributesfitting(__).md>) method.

## See Also

### Configuring item spacing

- [minimumLineSpacing](minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](itemsize.md) — The default size to use for cells.
- [estimatedItemSize](estimateditemsize.md) — The estimated size of cells in the collection view.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
- [SectionInsetReference](sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.
