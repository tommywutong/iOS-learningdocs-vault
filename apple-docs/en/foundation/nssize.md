---
title: NSSize
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssize
source_url: 'https://developer.apple.com/documentation/foundation/nssize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssize.json'
content_hash: 'sha256:a787e47e6f382881'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSize

<sub>Type Alias</sub>

A two-dimensional size.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias NSSize = CGSize
```

## Discussion

Normally, the values of `width` and `height` are non-negative. The functions that create an `NSSize` structure do not prevent you from setting a negative value for these attributes. If the value of `width` or `height` is negative, however, the behavior of some methods may be undefined.

### Special Considerations

Prior to OS X v10.5 the width and height were represented by `float` values rather than `CGFloat` values.

When building for 64 bit systems, or building 32 bit like 64 bit, `NSSize` is typedef’d to `CGSize`.

## Topics

### Managing Sizes

- [NSEqualSizes](<nsequalsizes(____).md>) — Returns a Boolean that indicates whether two size values are equal.
- [NSMakeSize](<nsmakesize(____).md>) — Returns a new `NSSize` from the specified values.
- [NSSizeFromString](<nssizefromstring(__).md>) — Returns an `NSSize` from a text-based representation.
- [NSStringFromSize](<nsstringfromsize(__).md>) — Returns a string representation of a size.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
- [NSSizeToCGSize](<nssizetocgsize(__).md>) — Returns a `CGSize` typecast from an `NSSize`.

### Zero Constant

- [NSZeroSize](nszerosize.md) — An `NSSize` structure set to `0` in both dimensions.

### Related Types

- [NSSizeArray](nssizearray.md) — Type indicating a parameter is an array of `NSSize` structures.
- [NSSizePointer](nssizepointer.md) — Type indicating parameter is a pointer to an `NSSize` structure.

## See Also

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSPoint](nspoint.md) — A point in a Cartesian coordinate system.
- [NSRect](nsrect.md) — A rectangle.
- [AffineTransform](affinetransform.md) — A graphics coordinate transformation.
- [NSEdgeInsets](nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
