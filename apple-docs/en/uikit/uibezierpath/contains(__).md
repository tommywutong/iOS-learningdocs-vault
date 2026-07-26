---
title: 'contains(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/contains(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/contains%28_%3A%29.json'
content_hash: 'sha256:18fd0133f32c0edd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ point: CGPoint) -> Bool
```

## Parameters

- `point` — The point to test against the path, specified in the path object’s coordinate system.

## Return Value

[true](../../swift/true.md) if the point is considered to be within the path’s enclosed area or [false](../../swift/false.md) if it is not.

## Discussion

The receiver contains the specified point if that point is in a portion of a closed subpath that would normally be painted during a fill operation. This method uses the value of the [usesEvenOddFillRule](usesevenoddfillrule.md) property to determine which parts of the subpath would be filled.

A point is not considered to be enclosed by the path if it is inside an open subpath, regardless of whether that area would be painted during a fill operation. Therefore, to determine mouse hits on open paths, you must create a copy of the path object and explicitly close any subpaths (using the [- closePath](<close().md>) method) before calling this method.

## See Also

### Performing hit-testing

- [empty](isempty.md) — A Boolean value that indicates whether the path has any valid elements.
- [bounds](bounds.md) — The bounding rectangle of the path.
