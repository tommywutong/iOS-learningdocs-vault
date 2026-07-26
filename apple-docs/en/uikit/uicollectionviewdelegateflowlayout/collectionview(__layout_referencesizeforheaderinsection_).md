---
title: 'collectionView(_:layout:referenceSizeForHeaderInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforheaderinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview%28_%3Alayout%3Areferencesizeforheaderinsection%3A%29.json'
content_hash: 'sha256:6ccae527978b182f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegateFlowLayout](../uicollectionviewdelegateflowlayout.md)

# collectionView(_:layout:referenceSizeForHeaderInSection:)

<sub>Instance Method</sub>

Asks the delegate for the size of the header view in the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForHeaderInSection section: Int) -> CGSize
```

## Parameters

- `collectionView` — The collection view object displaying the flow layout.

- `collectionViewLayout` — The layout object requesting the information.

- `section` — The index of the section whose header size is being requested.

## Return Value

The size of the header. If you return a value of size (0, 0), no header is added.

## Discussion

If you do not implement this method, the flow layout uses the value in its [headerReferenceSize](../uicollectionviewflowlayout/headerreferencesize.md) property to set the size of the header.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value returned by your method. (In that instance, the width of the header would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no header is added.

## See Also

### Getting the header and footer sizes

- [- collectionView:layout:referenceSizeForFooterInSection:](<collectionview(__layout_referencesizeforfooterinsection_).md>) — Asks the delegate for the size of the footer view in the specified section.
