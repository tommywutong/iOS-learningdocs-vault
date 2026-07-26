---
title: sectionInsetReference
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.property.json'
content_hash: 'sha256:1c0718e13cd3089d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# sectionInsetReference

<sub>Instance Property</sub>

The boundary that section insets are defined in relation to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionInsetReference: UICollectionViewFlowLayout.SectionInsetReference { get set }
```

## Discussion

The default value of this property is [UICollectionViewFlowLayoutSectionInsetFromContentInset](sectioninsetreference-swift.enum/fromcontentinset.md).

The minimum value of this property is always the collection view’s [contentInset](../uiscrollview/contentinset.md). For example, if the value of this property is [UICollectionViewFlowLayoutSectionInsetFromSafeArea](sectioninsetreference-swift.enum/fromsafearea.md), but the adjusted content inset is greater than the combination of the safe area and section insets, then the section’s content is aligned with the content inset instead.

## See Also

### Configuring item spacing

- [minimumLineSpacing](minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](itemsize.md) — The default size to use for cells.
- [estimatedItemSize](estimateditemsize.md) — The estimated size of cells in the collection view.
- [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [SectionInsetReference](sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.
