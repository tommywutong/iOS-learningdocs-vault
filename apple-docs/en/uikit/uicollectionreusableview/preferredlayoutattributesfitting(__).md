---
title: 'preferredLayoutAttributesFitting(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionreusableview/preferredlayoutattributesfitting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/preferredlayoutattributesfitting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/preferredlayoutattributesfitting%28_%3A%29.json'
content_hash: 'sha256:d3d2a89f8b33744a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# preferredLayoutAttributesFitting(_:)

<sub>Instance Method</sub>

Gives the cell a chance to modify the attributes provided by the layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func preferredLayoutAttributesFitting(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes
```

## Parameters

- `layoutAttributes` — The attributes provided by the layout object. These attributes represent the values that the layout intends to apply to the cell.

## Return Value

The final attributes to apply to the cell.

## Discussion

The default implementation of this method adjusts the size values to accommodate changes made by a self-sizing cell. Subclasses can override this method and use it to adjust other layout attributes too. If you override this method and want the cell size adjustments, call `super` first and make your own modifications to the returned attributes.

## See Also

### Managing layout changes

- [- applyLayoutAttributes:](<apply(__).md>) — Applies the specified layout attributes to the view.
- [- willTransitionFromLayout:toLayout:](<willtransition(from_to_).md>) — Tells your view that the layout object of the collection view is about to change.
- [- didTransitionFromLayout:toLayout:](<didtransition(from_to_).md>) — Tells your view that the layout object of the collection view changed.
