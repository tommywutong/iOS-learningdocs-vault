---
title: 'collectionView(_:layout:insetForSectionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:insetforsectionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview%28_%3Alayout%3Ainsetforsectionat%3A%29.json'
content_hash: 'sha256:4bd7e07a77535b01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegateFlowLayout](../uicollectionviewdelegateflowlayout.md)

# collectionView(_:layout:insetForSectionAt:)

<sub>Instance Method</sub>

Asks the delegate for the margins to apply to content in the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAt section: Int) -> UIEdgeInsets
```

## Parameters

- `collectionView` — The collection view object displaying the flow layout.

- `collectionViewLayout` — The layout object requesting the information.

- `section` — The index number of the section whose insets are needed.

## Return Value

The margins to apply to items in the section.

## Discussion

If you do not implement this method, the flow layout uses the value in its [sectionInset](../uicollectionviewflowlayout/sectioninset.md) property to set the margins instead. Your implementation of this method can return a fixed set of margin sizes or return different margin sizes for each section.

Section insets are margins applied only to the items in the section. They represent the distance between the header view and the first line of items and between the last line of items and the footer view. They also indicate the spacing on either side of a single line of items. They do not affect the size of the headers or footers themselves.

## See Also

### Getting the section spacing

- [- collectionView:layout:minimumLineSpacingForSectionAtIndex:](<collectionview(__layout_minimumlinespacingforsectionat_).md>) — Asks the delegate for the spacing between successive rows or columns of a section.
- [- collectionView:layout:minimumInteritemSpacingForSectionAtIndex:](<collectionview(__layout_minimuminteritemspacingforsectionat_).md>) — Asks the delegate for the spacing between successive items in the rows or columns of a section.
