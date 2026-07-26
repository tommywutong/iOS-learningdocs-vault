---
title: NSPoint
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspoint
source_url: 'https://developer.apple.com/documentation/foundation/nspoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspoint.json'
content_hash: 'sha256:f159193650e8c2de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPoint

<sub>Type Alias</sub>

A point in a Cartesian coordinate system.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias NSPoint = CGPoint
```

## Discussion

Prior to OS X v10.5 the coordinates were represented by `float` values rather than `CGFloat` values.

When building for 64 bit systems, or building 32 bit like 64 bit, `NSPoint` is typedef’d to `CGPoint`.

## Topics

### Managing Points

- [NSEqualPoints](<nsequalpoints(____).md>) — Returns a Boolean value that indicates whether two points are equal.
- [NSMakePoint](<nsmakepoint(____).md>) — Creates a new `NSPoint` from the specified values.
- [NSPointFromString](<nspointfromstring(__).md>) — Returns a point from a text-based representation.
- [NSStringFromPoint](<nsstringfrompoint(__).md>) — Returns a string representation of a point.
- [NSPointFromCGPoint](<nspointfromcgpoint(__).md>) — Returns an `NSPoint` typecast from a `CGPoint`.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.

### Zero Constant

- [NSZeroPoint](nszeropoint.md) — An `NSPoint` structure with both x and y coordinates set to `0`.

### Related Types

- [NSPointArray](nspointarray.md) — Type indicating a parameter is array of `NSPoint` structures.
- [NSPointPointer](nspointpointer.md) — Type indicating a parameter is a pointer to an `NSPoint` structure.

## See Also

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSSize](nssize.md) — A two-dimensional size.
- [NSRect](nsrect.md) — A rectangle.
- [AffineTransform](affinetransform.md) — A graphics coordinate transformation.
- [NSEdgeInsets](nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
