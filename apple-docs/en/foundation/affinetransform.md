---
title: AffineTransform
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/affinetransform
source_url: 'https://developer.apple.com/documentation/foundation/affinetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/affinetransform.json'
content_hash: 'sha256:309f9fc9deb4fdd0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AffineTransform

<sub>Structure</sub>

A graphics coordinate transformation.

<sub>macOS</sub>

```swift
struct AffineTransform
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Transforms

- [init()](<affinetransform/init().md>) — Creates an affine transformation matrix with identity values.
- [init(rotationByDegrees:)](<affinetransform/init(rotationbydegrees_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(rotationByRadians:)](<affinetransform/init(rotationbyradians_).md>) — Creates an affine transformation matrix from a rotation angle.
- [init(scale:)](<affinetransform/init(scale_).md>) — Creates an affine transformation matrix from scaling a single value.
- [init(scaleByX:byY:)](<affinetransform/init(scalebyx_byy_).md>) — Creates an affine transformation matrix from scaling values.
- [init(translationByX:byY:)](<affinetransform/init(translationbyx_byy_).md>) — Creates an affine transformation matrix from translation values.
- [init(m11:m12:m21:m22:tX:tY:)](<affinetransform/init(m11_m12_m21_m22_tx_ty_).md>) — Creates an affine transformation.

### Getting the Identity Transform

- [identity](affinetransform/identity.md) — An identity affine transformation matrix.

### Accumulating Tranformations

- [rotate(byDegrees:)](<affinetransform/rotate(bydegrees_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [rotate(byRadians:)](<affinetransform/rotate(byradians_).md>) — Mutates an affine transformation matrix to apply a rotation.
- [scale(_:)](<affinetransform/scale(__).md>) — Mutates an affine transformation matrix to apply scaling in both x and y dimensions.
- [scale(x:y:)](<affinetransform/scale(x_y_).md>) — Mutates an affine transformation matrix to apply scaling in each of the x and y dimensions.
- [translate(x:y:)](<affinetransform/translate(x_y_).md>) — Mutates an affine transformation matrix to perform the specified translation.
- [append(_:)](<affinetransform/append(__).md>) — Mutates an affine transformation by appending another affine transform.
- [prepend(_:)](<affinetransform/prepend(__).md>) — Mutates an affine transformation by prepending another affine transform.
- [invert()](<affinetransform/invert().md>) — Inverts the transformation matrix, if possible.
- [inverted()](<affinetransform/inverted().md>) — Returns an inverted version of the matrix, if possible, or nil if not.

### Transforming Data and Objects

- [transform(_:)](<affinetransform/transform(__)-1ozpp.md>) — Applies the affine transform to the specified point.
- [transform(_:)](<affinetransform/transform(__)-6fze6.md>) — Applies the affine transform to the specified size.

### Accessing the Transformation Matrix

- [m11](affinetransform/m11.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m12](affinetransform/m12.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m21](affinetransform/m21.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [m22](affinetransform/m22.md) — An element of the transform matrix that contributes scaling, rotation, and shear.
- [tX](affinetransform/tx.md) — An element of the transform matrix that contributes translation.
- [tY](affinetransform/ty.md) — An element of the transform matrix that contributes translation.

### Using Reference Types

- [NSAffineTransform](nsaffinetransform.md) — A graphics coordinate transformation.

## See Also

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSPoint](nspoint.md) — A point in a Cartesian coordinate system.
- [NSSize](nssize.md) — A two-dimensional size.
- [NSRect](nsrect.md) — A rectangle.
- [NSEdgeInsets](nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
