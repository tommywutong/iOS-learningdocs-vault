---
title: 'contains(_:using:transform:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpath/contains(_:using:transform:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpath/contains(_:using:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpath/contains%28_%3Ausing%3Atransform%3A%29.json'
content_hash: 'sha256:e23f206f54186496'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPath](../cgpath.md)

# contains(_:using:transform:)

<sub>Instance Method</sub>

Returns whether the specified point is interior to the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ point: CGPoint, using rule: CGPathFillRule = .winding, transform: CGAffineTransform = .identity) -> Bool
```

## Parameters

- `point` — The point to check.

- `rule` — The rule for determining which areas to treat as the interior of the path. Defaults to the [CGPathFillRule.winding](../cgpathfillrule/winding.md) rule if not specified.

- `transform` — An affine transform to apply to the point before checking for containment in the path. Defaults to the [CGAffineTransformIdentity](../cgaffinetransformidentity.md) transform if not specified.

## Return Value

[true](../../swift/true.md) if the point is interior to the path; otherwise, [false](../../swift/false.md).

## Discussion

A point is contained in a path if it would be inside the painted region when the path is filled.

## See Also

### Related Documentation

- [CGPathFillRule](../cgpathfillrule.md) — Rules for determining which regions are interior to a path, used by the [fillPath(using:)](<../cgcontext/fillpath(using_).md>) and [clip(using:)](<../cgcontext/clip(using_).md>) methods.

### Examining a Graphics Path

- [CGPathGetBoundingBox](boundingbox.md) — Returns the bounding box containing all points in a graphics path.
- [CGPathGetPathBoundingBox](boundingboxofpath.md) — Returns the bounding box of a graphics path.
- [CGPathGetCurrentPoint](currentpoint.md) — Returns the current point in a graphics path.
- [CGPathIsEmpty](isempty.md) — Indicates whether or not a graphics path is empty.
- [CGPathIsRect](<isrect(__).md>) — Indicates whether or not a graphics path represents a rectangle.
