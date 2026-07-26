---
title: 'willTransition(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionreusableview/willtransition(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/willtransition(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/willtransition%28from%3Ato%3A%29.json'
content_hash: 'sha256:b5c137444a90c628'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# willTransition(from:to:)

<sub>Instance Method</sub>

Tells your view that the layout object of the collection view is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

## Parameters

- `oldLayout` — The current layout object associated with the collection view.

- `newLayout` — The new layout object that is about to be applied to the collection view.

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to prepare for the change in layouts.

## See Also

### Managing layout changes

- [- preferredLayoutAttributesFittingAttributes:](<preferredlayoutattributesfitting(__).md>) — Gives the cell a chance to modify the attributes provided by the layout object.
- [- applyLayoutAttributes:](<apply(__).md>) — Applies the specified layout attributes to the view.
- [- didTransitionFromLayout:toLayout:](<didtransition(from_to_).md>) — Tells your view that the layout object of the collection view changed.
