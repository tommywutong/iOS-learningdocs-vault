---
title: 'layoutAttributesForItem(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/layoutattributesforitem(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/layoutattributesforitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/layoutattributesforitem%28at%3A%29.json'
content_hash: 'sha256:be9f428894df7960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# layoutAttributesForItem(at:)

<sub>Instance Method</sub>

Gets the layout information for the item at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForItem(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `indexPath` — The index path of the item.

## Return Value

The layout attributes for the item or `nil` if no item exists at the specified path.

## Discussion

Use this method to retrieve the layout information for a particular item. You should always use this method instead of querying the layout object directly.

## See Also

### Getting layout information

- [- layoutAttributesForSupplementaryElementOfKind:atIndexPath:](<layoutattributesforsupplementaryelement(ofkind_at_).md>) — Gets the layout information for the specified supplementary view.
