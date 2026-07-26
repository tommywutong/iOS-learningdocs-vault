---
title: 'layoutAttributesForCell(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/layoutattributesforcell(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesforcell(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/layoutattributesforcell%28at%3A%29.json'
content_hash: 'sha256:9bb637c87dfd3870'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# layoutAttributesForCell(at:)

<sub>Instance Method</sub>

A convenience method for returning the layout attributes for a collection view cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForCell(at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `indexPath` — The index path for the cell whose layout attributes you want.

## Return Value

The collection view layout attributes for the specified collection view cell.

## See Also

### Working with collection views

- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — A convenience method for returning the layout attributes for a collection view decoration view.
- [- layoutAttributesForSupplementaryViewOfKind:atIndexPath:](<layoutattributesforsupplementaryview(ofkind_at_).md>) — A convenience method for returning the layout attributes for a collection view supplementary view.
