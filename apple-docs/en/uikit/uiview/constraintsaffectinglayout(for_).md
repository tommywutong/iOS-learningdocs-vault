---
title: 'constraintsAffectingLayout(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/constraintsaffectinglayout(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/constraintsaffectinglayout(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/constraintsaffectinglayout%28for%3A%29.json'
content_hash: 'sha256:37bc38814612c31d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# constraintsAffectingLayout(for:)

<sub>Instance Method</sub>

Returns the constraints impacting the layout of the view for a given axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func constraintsAffectingLayout(for axis: NSLayoutConstraint.Axis) -> [NSLayoutConstraint]
```

## Parameters

- `axis` — The axis for which the constraints should be found.

## Return Value

The constraints impacting the layout of the view for the specified axis.

## Discussion

The returned set of constraints may not all include the view explicitly. Constraints that impact the location of the view implicitly may also be included. While this provides a good starting point for debugging, there is no guarantee that the returned set of constraints will include all of the constraints that have an impact on the view’s layout in the given orientation.

This method should only be used for debugging constraint-based layout. No application should ship with calls to this method as part of its operation.

## See Also

### Debugging Auto Layout

- [hasAmbiguousLayout](hasambiguouslayout.md) — A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.
- [- exerciseAmbiguityInLayout](<exerciseambiguityinlayout().md>) — Randomly changes the frame of a view with an ambiguous layout between the different valid values.
