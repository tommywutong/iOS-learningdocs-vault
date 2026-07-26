---
title: intrinsicContentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/intrinsiccontentsize
source_url: 'https://developer.apple.com/documentation/uikit/uiview/intrinsiccontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/intrinsiccontentsize.json'
content_hash: 'sha256:60bf1fd622f1a89c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# intrinsicContentSize

<sub>Instance Property</sub>

The natural size for the receiving view, considering only properties of the view itself.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var intrinsicContentSize: CGSize { get }
```

## Discussion

Custom views typically have content that they display of which the layout system is unaware. Setting this property allows a custom view to communicate to the layout system what size it would like to be based on its content. This intrinsic size must be independent of the content frame, because there’s no way to dynamically communicate a changed width to the layout system based on a changed height, for example.

If a custom view has no intrinsic size for a given dimension, it can use [UIViewNoIntrinsicMetric](nointrinsicmetric.md) for that dimension.

## See Also

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:](<systemlayoutsizefitting(__).md>) — Returns the optimal size of the view based on its current constraints.
- [- systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:](<systemlayoutsizefitting(__withhorizontalfittingpriority_verticalfittingpriority_).md>) — Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [- invalidateIntrinsicContentSize](<invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- contentHuggingPriorityForAxis:](<contenthuggingpriority(for_).md>) — Returns the priority with which a view resists being made larger than its intrinsic size.
- [- setContentHuggingPriority:forAxis:](<setcontenthuggingpriority(__for_).md>) — Sets the priority with which a view resists being made larger than its intrinsic size.
