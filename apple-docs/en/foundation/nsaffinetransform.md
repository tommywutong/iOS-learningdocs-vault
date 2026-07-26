---
title: NSAffineTransform
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsaffinetransform
source_url: 'https://developer.apple.com/documentation/foundation/nsaffinetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsaffinetransform.json'
content_hash: 'sha256:dda96df2198b914d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAffineTransform

<sub>Class</sub>

A graphics coordinate transformation.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSAffineTransform
```

## Overview

In Swift, this object bridges to [AffineTransform](affinetransform.md); use [NSAffineTransform](nsaffinetransform.md) when you need reference semantics or other Foundation-specific behavior.

A transformation specifies how points in one coordinate system are transformed to points in another coordinate system. An affine transformation is a special type of transformation that preserves parallel lines in a path but does not necessarily preserve lengths or angles. Scaling, rotation, and translation are the most commonly used manipulations supported by affine transforms, but shearing is also possible.

> [!note] Note
> In OS X 10.3 and earlier the [NSAffineTransform](nsaffinetransform.md) class was declared and implemented entirely in the Application Kit framework. As of macOS 10.4 the [NSAffineTransform](nsaffinetransform.md) class has been split across the Foundation and Application Kit frameworks.

Methods for applying affine transformations to the current graphics context and a method for applying an affine transformation to an [NSBezierPath](../appkit/nsbezierpath.md) object are described in NSAffineTransform Additions Reference in the Application Kit.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [AffineTransform](affinetransform.md) structure, which bridges to the [NSAffineTransform](nsaffinetransform.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating an Affine Transform

- [- init](<nsaffinetransform/init().md>) — Initializes an affine transform matrix to the identity matrix.
- [- initWithTransform:](<nsaffinetransform/init(transform_).md>) — Initializes the receiver’s matrix using another transform object.

### Accumulating Transformations

- [- rotateByDegrees:](<nsaffinetransform/rotate(bydegrees_).md>) — Applies a rotation factor (measured in degrees) to the receiver’s transformation matrix.
- [- rotateByRadians:](<nsaffinetransform/rotate(byradians_).md>) — Applies a rotation factor (measured in radians) to the receiver’s transformation matrix.
- [- scaleBy:](<nsaffinetransform/scale(by_).md>) — Applies the specified scaling factor along both x and y axes to the receiver’s transformation matrix.
- [- scaleXBy:yBy:](<nsaffinetransform/scalex(by_yby_).md>) — Applies scaling factors to each axis of the receiver’s transformation matrix.
- [- translateXBy:yBy:](<nsaffinetransform/translatex(by_yby_).md>) — Applies the specified translation factors to the receiver’s transformation matrix.
- [- appendTransform:](<nsaffinetransform/append(__).md>) — Appends the specified matrix to the receiver’s matrix.
- [- prependTransform:](<nsaffinetransform/prepend(__).md>) — Prepends the specified matrix to the receiver’s matrix.
- [- invert](<nsaffinetransform/invert().md>) — Replaces the receiver’s matrix with its inverse matrix.

### Transforming Data and Objects

- [- transformPoint:](<nsaffinetransform/transform(__)-41p16.md>) — Applies the receiver’s transform to the specified point and returns the result.
- [- transformSize:](<nsaffinetransform/transform(__)-5r6ol.md>) — Applies the receiver’s transform to the specified size and returns the results.
- [- transformBezierPath:](<nsaffinetransform/transform(__)-6z1xo.md>) — Creates and returns a new Bézier path object with each point in the given path transformed by the receiver.

### Accessing the Transformation Matrix

- [transformStruct](nsaffinetransform/transformstruct.md) — The matrix coefficients stored as the transformation matrix.
- [NSAffineTransformStruct](nsaffinetransformstruct.md) — A structure that defines the three-by-three matrix that performs an affine transform between two coordinate systems.

### Setting and Building the Current Transformation Matrix

- [- set](<nsaffinetransform/set().md>) — Sets the current transformation matrix to the receiver’s transformation matrix.
- [- concat](<nsaffinetransform/concat().md>) — Appends the receiver’s matrix to the current transformation matrix stored in the current graphics context, replacing the current transformation matrix with the result.

### Initializers

- [init(coder:)](<nsaffinetransform/init(coder_).md>)
