---
title: forLastBaselineLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/forlastbaselinelayout
source_url: 'https://developer.apple.com/documentation/uikit/uiview/forlastbaselinelayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/forlastbaselinelayout.json'
content_hash: 'sha256:280c02130e459ac7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# forLastBaselineLayout

<sub>Instance Property</sub>

Returns a view used to satisfy last baseline constraints.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var forLastBaselineLayout: UIView { get }
```

## Discussion

For views with multiple rows of text, the last baseline is the baseline for the bottommost row.

When you make a constraint to a view’s [NSLayoutAttributeLastBaseline](../nslayoutconstraint/attribute/lastbaseline.md) attribute, Auto Layout uses the baseline of the view returned by this method. If that view does not have a baseline, Auto Layout uses the view’s bottom edge.

Override this property to return a text-based subview (for example, [UILabel](../uilabel.md) or a nonscrolling [UITextView](../uitextview.md)). The returned view must be a subview of the receiver. The default implementation returns the receiving view.

## See Also

### Aligning views in Auto Layout

- [- alignmentRectForFrame:](<alignmentrect(forframe_).md>) — Returns the view’s alignment rectangle for a given frame.
- [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) — Returns the view’s frame for a given alignment rectangle.
- [alignmentRectInsets](alignmentrectinsets.md) — The insets from the view’s frame that define its alignment rectangle.
- [viewForFirstBaselineLayout](forfirstbaselinelayout.md) — Returns a view used to satisfy first baseline constraints.
