---
title: hasAmbiguousLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/hasambiguouslayout
source_url: 'https://developer.apple.com/documentation/uikit/uiview/hasambiguouslayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/hasambiguouslayout.json'
content_hash: 'sha256:37b4ca6ac4b20c4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# hasAmbiguousLayout

<sub>Instance Property</sub>

A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hasAmbiguousLayout: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the view’s location is incompletely specified, [false](../../swift/false.md) otherwise.

If there aren’t enough constraints in the system to uniquely determine layout, the layout is considered ambiguous. For example, if the only constraint in the system is `x = y + 100`, the layout is ambiguous because there are many possible values for `x` and `y`. UIKit does not automatically detect every ambiguous layout, so you may need to look for symptoms of ambiguity, such as views that jump from place to place, or that are in the wrong place.

This property should only be used for debugging constraint-based layout. No app should ship with usage of this property as part of its operation.

## See Also

### Debugging Auto Layout

- [- constraintsAffectingLayoutForAxis:](<constraintsaffectinglayout(for_).md>) — Returns the constraints impacting the layout of the view for a given axis.
- [- exerciseAmbiguityInLayout](<exerciseambiguityinlayout().md>) — Randomly changes the frame of a view with an ambiguous layout between the different valid values.
