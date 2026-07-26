---
title: UICollectionViewDelegateFlowLayout
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdelegateflowlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegateflowlayout.json'
content_hash: 'sha256:4b57d696cbbb3d2e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDelegateFlowLayout

<sub>Protocol</sub>

The methods that let you coordinate with a flow layout object to implement a grid-based layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UICollectionViewDelegateFlowLayout : UICollectionViewDelegate
```

## Overview

The methods of this protocol define the size of items and the spacing between items in the grid. All of the methods in this protocol are optional. If you don’t implement a particular method, the flow layout delegate uses values in its own properties for the appropriate spacing information.

The [UICollectionViewFlowLayout](uicollectionviewflowlayout.md) object expects the collection view’s delegate object to adopt this protocol. Therefore, implement this protocol on the object assigned to your collection view’s [delegate](uicollectionview/delegate.md) property.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UICollectionViewDelegate](uicollectionviewdelegate.md), [UIScrollViewDelegate](uiscrollviewdelegate.md)

## Topics

### Getting the size of items

- [- collectionView:layout:sizeForItemAtIndexPath:](<uicollectionviewdelegateflowlayout/collectionview(__layout_sizeforitemat_).md>) — Asks the delegate for the size of the specified item’s cell.

### Getting the section spacing

- [- collectionView:layout:insetForSectionAtIndex:](<uicollectionviewdelegateflowlayout/collectionview(__layout_insetforsectionat_).md>) — Asks the delegate for the margins to apply to content in the specified section.
- [- collectionView:layout:minimumLineSpacingForSectionAtIndex:](<uicollectionviewdelegateflowlayout/collectionview(__layout_minimumlinespacingforsectionat_).md>) — Asks the delegate for the spacing between successive rows or columns of a section.
- [- collectionView:layout:minimumInteritemSpacingForSectionAtIndex:](<uicollectionviewdelegateflowlayout/collectionview(__layout_minimuminteritemspacingforsectionat_).md>) — Asks the delegate for the spacing between successive items in the rows or columns of a section.

### Getting the header and footer sizes

- [- collectionView:layout:referenceSizeForHeaderInSection:](<uicollectionviewdelegateflowlayout/collectionview(__layout_referencesizeforheaderinsection_).md>) — Asks the delegate for the size of the header view in the specified section.
- [- collectionView:layout:referenceSizeForFooterInSection:](<uicollectionviewdelegateflowlayout/collectionview(__layout_referencesizeforfooterinsection_).md>) — Asks the delegate for the size of the footer view in the specified section.
