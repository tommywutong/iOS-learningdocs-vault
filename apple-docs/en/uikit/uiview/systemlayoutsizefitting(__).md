---
title: 'systemLayoutSizeFitting(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/systemlayoutsizefitting(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/systemlayoutsizefitting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/systemlayoutsizefitting%28_%3A%29.json'
content_hash: 'sha256:f2d01cc5974854b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# systemLayoutSizeFitting(_:)

<sub>Instance Method</sub>

Returns the optimal size of the view based on its current constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize
```

## Parameters

- `targetSize` — The size that you prefer for the view. To obtain a view that is as small as possible, specify the constant [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md). To obtain a view that is as large as possible, specify the constant [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md).

## Return Value

The optimal size for the view.

## Discussion

This method returns a size value for the view that optimally satisfies the view’s current constraints and is as close to the value in the `targetSize` parameter as possible. This method does not actually change the size of the view.

## See Also

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:](<systemlayoutsizefitting(__withhorizontalfittingpriority_verticalfittingpriority_).md>) — Returns the optimal size of the view based on its constraints and the specified fitting priorities.
- [intrinsicContentSize](intrinsiccontentsize.md) — The natural size for the receiving view, considering only properties of the view itself.
- [- invalidateIntrinsicContentSize](<invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- contentHuggingPriorityForAxis:](<contenthuggingpriority(for_).md>) — Returns the priority with which a view resists being made larger than its intrinsic size.
- [- setContentHuggingPriority:forAxis:](<setcontenthuggingpriority(__for_).md>) — Sets the priority with which a view resists being made larger than its intrinsic size.
