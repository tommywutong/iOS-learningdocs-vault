---
title: 'apply(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionreusableview/apply(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/apply(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/apply%28_%3A%29.json'
content_hash: 'sha256:0ca57f33199a3d68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# apply(_:)

<sub>Instance Method</sub>

Applies the specified layout attributes to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func apply(_ layoutAttributes: UICollectionViewLayoutAttributes)
```

## Parameters

- `layoutAttributes` — The layout attributes to apply.

## Discussion

The default implementation of this method does nothing.

If the layout object supports custom layout attributes, you can use this method to apply those attributes to the view. In such a case, the `layoutAttributes` parameter should contain an instance of a subclass of [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md). You do not need to override this method to support the standard layout attributes of the [UICollectionViewLayoutAttributes](../uicollectionviewlayoutattributes.md) class. The collection view applies those attributes automatically.

## See Also

### Managing layout changes

- [- preferredLayoutAttributesFittingAttributes:](<preferredlayoutattributesfitting(__).md>) — Gives the cell a chance to modify the attributes provided by the layout object.
- [- willTransitionFromLayout:toLayout:](<willtransition(from_to_).md>) — Tells your view that the layout object of the collection view is about to change.
- [- didTransitionFromLayout:toLayout:](<didtransition(from_to_).md>) — Tells your view that the layout object of the collection view changed.
