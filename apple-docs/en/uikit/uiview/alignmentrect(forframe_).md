---
title: 'alignmentRect(forFrame:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/alignmentrect(forframe:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/alignmentrect(forframe:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/alignmentrect%28forframe%3A%29.json'
content_hash: 'sha256:353c2d2c25b8c317'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# alignmentRect(forFrame:)

<sub>Instance Method</sub>

Returns the view’s alignment rectangle for a given frame.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func alignmentRect(forFrame frame: CGRect) -> CGRect
```

## Parameters

- `frame` — The frame whose corresponding alignment rectangle is desired.

## Return Value

The alignment rectangle for the specified frame.

## Discussion

The constraint-based layout system uses alignment rectangles to align views, rather than their frame. This allows custom views to be aligned based on the location of their content while still having a frame that encompasses any ornamentation they need to draw around their content, such as shadows or reflections.

The default implementation returns the view’s frame modified by the view’s [alignmentRectInsets](alignmentrectinsets.md). Most custom views can use  [alignmentRectInsets](alignmentrectinsets.md) to specify the location of their content within their frame. Custom views that require arbitrary transformations can override [- alignmentRectForFrame:](<alignmentrect(forframe_).md>) and [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) to describe the location of their content. These two methods must always be inverses of each other.

## See Also

### Aligning views in Auto Layout

- [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) — Returns the view’s frame for a given alignment rectangle.
- [alignmentRectInsets](alignmentrectinsets.md) — The insets from the view’s frame that define its alignment rectangle.
- [viewForFirstBaselineLayout](forfirstbaselinelayout.md) — Returns a view used to satisfy first baseline constraints.
- [viewForLastBaselineLayout](forlastbaselinelayout.md) — Returns a view used to satisfy last baseline constraints.
