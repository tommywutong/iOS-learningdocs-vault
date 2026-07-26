---
title: 'collectionView(_:layout:referenceSizeForFooterInSection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview(_:layout:referencesizeforfooterinsection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout/collectionview%28_%3Alayout%3Areferencesizeforfooterinsection%3A%29.json'
content_hash: 'sha256:39793cc296a2fb61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegateFlowLayout](../uicollectionviewdelegateflowlayout.md)

# collectionView(_:layout:referenceSizeForFooterInSection:)

<sub>Instance Method</sub>

Asks the delegate for the size of the footer view in the specified section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, referenceSizeForFooterInSection section: Int) -> CGSize
```

## Parameters

- `collectionView` — The collection view object displaying the flow layout.

- `collectionViewLayout` — The layout object requesting the information.

- `section` — The index of the section whose footer size is being requested.

## Return Value

The size of the footer. If you return a value of size (0, 0), no footer is added.

## Discussion

If you do not implement this method, the flow layout uses the value in its [footerReferenceSize](../uicollectionviewflowlayout/footerreferencesize.md) property to set the size of the footer.

During layout, only the size that corresponds to the appropriate scrolling direction is used. For example, for the vertical scrolling direction, the layout object uses the height value specified by this property. (In that instance, the width of the footer would be set to the width of the collection view.) If the size in the appropriate scrolling dimension is 0, no footer is added.

## See Also

### Getting the header and footer sizes

- [- collectionView:layout:referenceSizeForHeaderInSection:](<collectionview(__layout_referencesizeforheaderinsection_).md>) — Asks the delegate for the size of the header view in the specified section.
