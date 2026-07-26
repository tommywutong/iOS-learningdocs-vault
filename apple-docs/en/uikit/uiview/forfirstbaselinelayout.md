---
title: forFirstBaselineLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/forfirstbaselinelayout
source_url: 'https://developer.apple.com/documentation/uikit/uiview/forfirstbaselinelayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/forfirstbaselinelayout.json'
content_hash: 'sha256:98127a440ca49464'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# forFirstBaselineLayout

<sub>Instance Property</sub>

Returns a view used to satisfy first baseline constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var forFirstBaselineLayout: UIView { get }
```

## Discussion

For views with multiple rows of text, the first baseline is the baseline for the topmost row.

When you make a constraint to a view’s [NSLayoutAttributeFirstBaseline](../nslayoutconstraint/attribute/firstbaseline.md) attribute, Auto Layout uses the baseline of the view returned by this method. If that view does not have a baseline, Auto Layout uses the view’s top edge.

Override this property to return a text-based subview (for example, [UILabel](../uilabel.md) or a nonscrolling [UITextView](../uitextview.md)). The returned view must be a subview of the receiver. The default implementation returns the value contained by [viewForLastBaselineLayout](forlastbaselinelayout.md).

> [!note] Note
> If the same subview is appropriate for both the first and last baseline, you only need to override the [viewForLastBaselineLayout](forlastbaselinelayout.md) getter method.

## See Also

### Aligning views in Auto Layout

- [- alignmentRectForFrame:](<alignmentrect(forframe_).md>) — Returns the view’s alignment rectangle for a given frame.
- [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) — Returns the view’s frame for a given alignment rectangle.
- [alignmentRectInsets](alignmentrectinsets.md) — The insets from the view’s frame that define its alignment rectangle.
- [viewForLastBaselineLayout](forlastbaselinelayout.md) — Returns a view used to satisfy last baseline constraints.
