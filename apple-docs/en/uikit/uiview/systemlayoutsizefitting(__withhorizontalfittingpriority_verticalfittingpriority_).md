---
title: 'systemLayoutSizeFitting(_:withHorizontalFittingPriority:verticalFittingPriority:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/systemlayoutsizefitting(_:withhorizontalfittingpriority:verticalfittingpriority:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/systemlayoutsizefitting%28_%3Awithhorizontalfittingpriority%3Averticalfittingpriority%3A%29.json'
content_hash: 'sha256:b4dd54f031943f38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# systemLayoutSizeFitting(_:withHorizontalFittingPriority:verticalFittingPriority:)

<sub>Instance Method</sub>

Returns the optimal size of the view based on its constraints and the specified fitting priorities.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority: UILayoutPriority) -> CGSize
```

## Parameters

- `targetSize` — The size that you prefer for the view. To obtain a view that is as small as possible, specify the constant [UILayoutFittingCompressedSize](layoutfittingcompressedsize.md). To obtain a view that is as large as possible, specify the constant [UILayoutFittingExpandedSize](layoutfittingexpandedsize.md).

- `horizontalFittingPriority` — The priority for horizontal constraints. Specify [UILayoutPriorityFittingSizeLevel](../uilayoutpriority/fittingsizelevel.md) to get a width that is as close as possible to the width value of `targetSize`.

- `verticalFittingPriority` — The priority for vertical constraints. Specify [UILayoutPriorityFittingSizeLevel](../uilayoutpriority/fittingsizelevel.md) to get a height that is as close as possible to the height value of `targetSize`.

## Return Value

The optimal size for the view based on the provided constraint priorities.

## Discussion

Use this method when you want to prioritize the view’s constraints when determining the best possible size of the view.  This method does not actually change the size of the view.

## See Also

### Measuring in Auto Layout

- [- systemLayoutSizeFittingSize:](<systemlayoutsizefitting(__).md>) — Returns the optimal size of the view based on its current constraints.
- [intrinsicContentSize](intrinsiccontentsize.md) — The natural size for the receiving view, considering only properties of the view itself.
- [- invalidateIntrinsicContentSize](<invalidateintrinsiccontentsize().md>) — Invalidates the view’s intrinsic content size.
- [- contentCompressionResistancePriorityForAxis:](<contentcompressionresistancepriority(for_).md>) — Returns the priority with which a view resists being made smaller than its intrinsic size.
- [- setContentCompressionResistancePriority:forAxis:](<setcontentcompressionresistancepriority(__for_).md>) — Sets the priority with which a view resists being made smaller than its intrinsic size.
- [- contentHuggingPriorityForAxis:](<contenthuggingpriority(for_).md>) — Returns the priority with which a view resists being made larger than its intrinsic size.
- [- setContentHuggingPriority:forAxis:](<setcontenthuggingpriority(__for_).md>) — Sets the priority with which a view resists being made larger than its intrinsic size.
