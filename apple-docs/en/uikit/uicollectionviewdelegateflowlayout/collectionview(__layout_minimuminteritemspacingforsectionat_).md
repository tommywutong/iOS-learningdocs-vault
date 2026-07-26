---
title: 'collectionView(_:layout:minimumInteritemSpacingForSectionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimuminteritemspacingforsectionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview%28_%3Alayout%3Aminimuminteritemspacingforsectionat%3A%29.json'
content_hash: 'sha256:81ddeb1164be156c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegateFlowLayout](../uicollectionviewdelegateflowlayout.md)

# collectionView(_:layout:minimumInteritemSpacingForSectionAt:)

<sub>Instance Method</sub>

Asks the delegate for the spacing between successive items in the rows or columns of a section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat
```

## Parameters

- `collectionView` — The collection view object displaying the flow layout.

- `collectionViewLayout` — The layout object requesting the information.

- `section` — The index number of the section whose inter-item spacing is needed.

## Return Value

The minimum space (measured in points) to apply between successive items in the lines of a section.

## Discussion

If you do not implement this method, the flow layout uses the value in its [minimumInteritemSpacing](../uicollectionviewflowlayout/minimuminteritemspacing.md) property to set the space between items instead. Your implementation of this method can return a fixed value or return different spacing values for each section.

For a vertically scrolling grid, this value represents the minimum spacing between items in the same row. For a horizontally scrolling grid, this value represents the minimum spacing between items in the same column. This spacing is used to compute how many items can fit in a single line, but after the number of items is determined, the actual spacing may possibly be adjusted upward.

## See Also

### Getting the section spacing

- [- collectionView:layout:insetForSectionAtIndex:](<collectionview(__layout_insetforsectionat_).md>) — Asks the delegate for the margins to apply to content in the specified section.
- [- collectionView:layout:minimumLineSpacingForSectionAtIndex:](<collectionview(__layout_minimumlinespacingforsectionat_).md>) — Asks the delegate for the spacing between successive rows or columns of a section.
