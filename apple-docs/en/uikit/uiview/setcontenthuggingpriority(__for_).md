---
title: 'setContentHuggingPriority(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/setcontenthuggingpriority(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/setcontenthuggingpriority(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/setcontenthuggingpriority%28_%3Afor%3A%29.json'
content_hash: 'sha256:f712b9707d2abec1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# setContentHuggingPriority(_:for:)

<sub>Instance Method</sub>

Sets the priority with which a view resists being made larger than its intrinsic size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: NSLayoutConstraint.Axis)
```

## Parameters

- `priority` — The new priority.

- `axis` — The axis for which the content hugging priority should be set.

## Discussion

Custom views should set default values for both orientations on creation, based on their content, typically to `UILayoutPriorityDefaultLow` or `UILayoutPriorityDefaultHigh`. When creating user interfaces, the layout designer can modify these priorities for specific views when the overall layout design requires different tradeoffs than the natural priorities of the views being used in the interface.

Subclasses should not override this method.

## See Also

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:](<systemlayoutsizefitting(__).md>) — Returns the optimal size of the view based on its current constraints.
- [- systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:](<systemlayoutsizefitting(__withhorizontalfittingpriority_verticalfittingpriority_).md>) — Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [intrinsicContentSize](intrinsiccontentsize.md) — The natural size for the receiving view, considering only properties of the view itself.
- [- invalidateIntrinsicContentSize](<invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- contentHuggingPriorityForAxis:](<contenthuggingpriority(for_).md>) — Returns the priority with which a view resists being made larger than its intrinsic size.
