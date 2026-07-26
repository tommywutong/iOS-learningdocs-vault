---
title: 'contentHuggingPriority(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/contenthuggingpriority(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/contenthuggingpriority(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/contenthuggingpriority%28for%3A%29.json'
content_hash: 'sha256:502dfcfe7ef5fa30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# contentHuggingPriority(for:)

<sub>Instance Method</sub>

Returns the priority with which a view resists being made larger than its intrinsic size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func contentHuggingPriority(for axis: NSLayoutConstraint.Axis) -> UILayoutPriority
```

## Parameters

- `axis` — The axis of the view that might be enlarged.

## Return Value

The priority with which the view should resist being enlarged from its intrinsic size on the specified axis.

## Discussion

The constraint-based layout system uses these priorities when determining the best layout for views that are encountering constraints that would require them to be larger than their intrinsic size.

## See Also

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:](<systemlayoutsizefitting(__).md>) — Returns the optimal size of the view based on its current constraints.
- [- systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:](<systemlayoutsizefitting(__withhorizontalfittingpriority_verticalfittingpriority_).md>) — Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [intrinsicContentSize](intrinsiccontentsize.md) — The natural size for the receiving view, considering only properties of the view itself.
- [- invalidateIntrinsicContentSize](<invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentHuggingPriority:forAxis:](<setcontenthuggingpriority(__for_).md>) — Sets the priority with which a view resists being made larger than its intrinsic size.
