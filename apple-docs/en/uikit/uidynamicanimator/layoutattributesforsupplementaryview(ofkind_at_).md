---
title: 'layoutAttributesForSupplementaryView(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/layoutattributesforsupplementaryview(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/layoutattributesforsupplementaryview(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/layoutattributesforsupplementaryview%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:28112f162fae754c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# layoutAttributesForSupplementaryView(ofKind:at:)

<sub>Instance Method</sub>

A convenience method for returning the layout attributes for a collection view supplementary view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func layoutAttributesForSupplementaryView(ofKind kind: String, at indexPath: IndexPath) -> UICollectionViewLayoutAttributes?
```

## Parameters

- `kind` — A string that identifies the type of supplementary view whose layout attributes you want.

- `indexPath` — The index path for the cell whose supplementary view layout attributes you want.

## Return Value

The collection view layout attributes for the specified supplementary view.

## See Also

### Working with collection views

- [- layoutAttributesForCellAtIndexPath:](<layoutattributesforcell(at_).md>) — A convenience method for returning the layout attributes for a collection view cell.
- [- layoutAttributesForDecorationViewOfKind:atIndexPath:](<layoutattributesfordecorationview(ofkind_at_).md>) — A convenience method for returning the layout attributes for a collection view decoration view.
