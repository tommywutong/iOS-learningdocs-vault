---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/bounds.json'
content_hash: 'sha256:59d5d8f470579c47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# bounds

<sub>Instance Property</sub>

The bounding rectangle of the path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

The value in this property represents the smallest rectangle that completely encloses all points in the path, including any control points for Bézier and quadratic curves.

## See Also

### Performing hit-testing

- [- containsPoint:](<contains(__).md>) — Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [empty](isempty.md) — A Boolean value that indicates whether the path has any valid elements.
