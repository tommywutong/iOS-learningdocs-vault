---
title: exerciseAmbiguityInLayout()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/exerciseambiguityinlayout()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/exerciseambiguityinlayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/exerciseambiguityinlayout%28%29.json'
content_hash: 'sha256:36f5573b3c548b58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# exerciseAmbiguityInLayout()

<sub>Instance Method</sub>

Randomly changes the frame of a view with an ambiguous layout between the different valid values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func exerciseAmbiguityInLayout()
```

## Discussion

This method randomly changes the frame of a view with an ambiguous layout between its different valid values, causing the view to move in the interface. This makes it easy to visually identify what the valid frames are and may enable the developer to discern what constraints need to be added to the layout to fully specify a location for the view.

This method should only be used for debugging constraint-based layout. No application should ship with calls to this method as part of its operation.

## See Also

### Debugging Auto Layout

- [- constraintsAffectingLayoutForAxis:](<constraintsaffectinglayout(for_).md>) — Returns the constraints impacting the layout of the view for a given axis.
- [hasAmbiguousLayout](hasambiguouslayout.md) — A Boolean value that determines whether the constraints impacting the layout of the view incompletely specify the location of the view.
