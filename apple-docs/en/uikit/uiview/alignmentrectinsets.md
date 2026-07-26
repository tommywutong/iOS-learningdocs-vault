---
title: alignmentRectInsets
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/alignmentrectinsets
source_url: 'https://developer.apple.com/documentation/uikit/uiview/alignmentrectinsets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/alignmentrectinsets.json'
content_hash: 'sha256:23e7884b627f7cd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# alignmentRectInsets

<sub>Instance Property</sub>

The insets from the view’s frame that define its alignment rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alignmentRectInsets: UIEdgeInsets { get }
```

## Discussion

The default value of this property is an [UIEdgeInsets](../uiedgeinsets.md) structure with zero values. Custom views that draw ornamentation around their content should use this property to return insets that align with the edges of the content, excluding the ornamentation. This allows the constraint-based layout system to align views based on their content, rather than just their frame.

Custom views whose content location can’t be expressed by a simple set of insets should override [- alignmentRectForFrame:](<alignmentrect(forframe_).md>) and [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) to describe their custom transform between alignment rectangle and frame.

## See Also

### Aligning views in Auto Layout

- [- alignmentRectForFrame:](<alignmentrect(forframe_).md>) — Returns the view’s alignment rectangle for a given frame.
- [- frameForAlignmentRect:](<frame(foralignmentrect_).md>) — Returns the view’s frame for a given alignment rectangle.
- [viewForFirstBaselineLayout](forfirstbaselinelayout.md) — Returns a view used to satisfy first baseline constraints.
- [viewForLastBaselineLayout](forlastbaselinelayout.md) — Returns a view used to satisfy last baseline constraints.
