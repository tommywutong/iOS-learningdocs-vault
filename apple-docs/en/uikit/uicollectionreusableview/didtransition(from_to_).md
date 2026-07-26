---
title: 'didTransition(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionreusableview/didtransition(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionreusableview/didtransition(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionreusableview/didtransition%28from%3Ato%3A%29.json'
content_hash: 'sha256:4505a4e898d05afa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionReusableView](../uicollectionreusableview.md)

# didTransition(from:to:)

<sub>Instance Method</sub>

Tells your view that the layout object of the collection view changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

## Parameters

- `oldLayout` — The collection view’s previous layout object.

- `newLayout` — The current layout object associated with the collection view.

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to finalize any behaviors associated with the change in layouts.

## See Also

### Managing layout changes

- [- preferredLayoutAttributesFittingAttributes:](<preferredlayoutattributesfitting(__).md>) — Gives the cell a chance to modify the attributes provided by the layout object.
- [- applyLayoutAttributes:](<apply(__).md>) — Applies the specified layout attributes to the view.
- [- willTransitionFromLayout:toLayout:](<willtransition(from_to_).md>) — Tells your view that the layout object of the collection view is about to change.
