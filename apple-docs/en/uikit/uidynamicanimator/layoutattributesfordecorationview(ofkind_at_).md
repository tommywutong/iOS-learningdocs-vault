---
title: 'layoutAttributesForDecorationView(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/layoutattributesfordecorationview(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesfordecorationview(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/layoutattributesfordecorationview%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:c8cba0765a086e58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# layoutAttributesForDecorationView(ofKind:at:)

<sub>Instance Method</sub>

A convenience method for returning the layout attributes for a collection view decoration view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForDecorationView(ofKind decorationViewKind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `decorationViewKind` — The kind identifier for the specified decoration view.

- `indexPath` — The index path for the cell whose decoration view layout attributes you want.

## Return Value

The collection view layout attributes for the specified decoration view.

## See Also

### Working with collection views

- [- layoutAttributesForCellAtIndexPath:](<layoutattributesforcell(at_).md>) — A convenience method for returning the layout attributes for a collection view cell.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — A convenience method for returning the layout attributes for a collection view supplementary view.
