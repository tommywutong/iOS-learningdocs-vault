---
title: UICollectionViewFlowLayout.SectionInsetReference
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/sectioninsetreference-swift.enum.json'
content_hash: 'sha256:b871fedb3d605349'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# UICollectionViewFlowLayout.SectionInsetReference

<sub>Enumeration</sub>

Constants that describe the reference point of the section insets.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SectionInsetReference
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UICollectionViewFlowLayoutSectionInsetFromContentInset](sectioninsetreference-swift.enum/fromcontentinset.md) — Section insets are defined in relation to the collection view’s content inset.
- [UICollectionViewFlowLayoutSectionInsetFromLayoutMargins](sectioninsetreference-swift.enum/fromlayoutmargins.md) — Section insets are defined in relation to the margins of the layout.
- [UICollectionViewFlowLayoutSectionInsetFromSafeArea](sectioninsetreference-swift.enum/fromsafearea.md) — Section insets are defined in relation to the safe area of the layout.

### Initializers

- [init(rawValue:)](<sectioninsetreference-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring item spacing

- [minimumLineSpacing](minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](itemsize.md) — The default size to use for cells.
- [estimatedItemSize](estimateditemsize.md) — The estimated size of cells in the collection view.
- [UICollectionViewFlowLayoutAutomaticSize](automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
