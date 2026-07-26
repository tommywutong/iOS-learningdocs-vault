---
title: 'layoutAttributesForSupplementaryElement(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/layoutattributesforsupplementaryelement(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/layoutattributesforsupplementaryelement(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/layoutattributesforsupplementaryelement%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:579fb6465d1bc652'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# layoutAttributesForSupplementaryElement(ofKind:at:)

<sub>Instance Method</sub>

Gets the layout information for the specified supplementary view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForSupplementaryElement(ofKind kind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `kind` — A string specifying the kind of supplementary view whose layout attributes you want. Layout classes are responsible for defining the kinds of supplementary views they support.

- `indexPath` — The index path of the supplementary view. The interpretation of this value depends on how the layout implements the view. For example, a view associated with a section might contain just a section value.

## Return Value

The layout attributes of the supplementary view or `nil` if the specified supplementary view does not exist.

## Discussion

Use this method to retrieve the layout information for a particular supplementary view. You should always use this method instead of querying the layout object directly.

## See Also

### Getting layout information

- [- layoutAttributesForItemAtIndexPath:](<layoutattributesforitem(at_).md>) — Gets the layout information for the item at the specified index path.
