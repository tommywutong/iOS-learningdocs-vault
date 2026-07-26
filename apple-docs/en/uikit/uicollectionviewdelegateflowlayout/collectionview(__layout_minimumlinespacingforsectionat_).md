---
title: 'collectionView(_:layout:minimumLineSpacingForSectionAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:minimumlinespacingforsectionat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview%28_%3Alayout%3Aminimumlinespacingforsectionat%3A%29.json'
content_hash: 'sha256:3a463932cad74747'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegateFlowLayout](../uicollectionviewdelegateflowlayout.md)

# collectionView(_:layout:minimumLineSpacingForSectionAt:)

<sub>Instance Method</sub>

Asks the delegate for the spacing between successive rows or columns of a section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat
```

## Parameters

- `collectionView` — The collection view object displaying the flow layout.

- `collectionViewLayout` — The layout object requesting the information.

- `section` — The index number of the section whose line spacing is needed.

## Return Value

The minimum space (measured in points) to apply between successive lines in a section.

## Discussion

If you do not implement this method, the flow layout uses the value in its [minimumLineSpacing](../uicollectionviewflowlayout/minimumlinespacing.md) property to set the space between lines instead. Your implementation of this method can return a fixed value or return different spacing values for each section.

For a vertically scrolling grid, this value represents the minimum spacing between successive rows. For a horizontally scrolling grid, this value represents the minimum spacing between successive columns. This spacing is not applied to the space between the header and the first line or between the last line and the footer.

## See Also

### Getting the section spacing

- [- collectionView:layout:insetForSectionAtIndex:](<collectionview(__layout_insetforsectionat_).md>) — Asks the delegate for the margins to apply to content in the specified section.
- [- collectionView:layout:minimumInteritemSpacingForSectionAtIndex:](<collectionview(__layout_minimuminteritemspacingforsectionat_).md>) — Asks the delegate for the spacing between successive items in the rows or columns of a section.
