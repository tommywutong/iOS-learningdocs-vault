---
title: CGGeometry
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggeometry
source_url: 'https://developer.apple.com/documentation/coregraphics/cggeometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggeometry.json'
content_hash: 'sha256:d25a1e042056d0e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGeometry

<sub>API Collection</sub>

Various structures and associated functions for 2D geometric primitives.

## Overview

The data structure [CGPoint](../corefoundation/cgpoint.md) represents a point in a two-dimensional coordinate system. The data structure [CGRect](../corefoundation/cgrect.md) represents the location and dimensions of a rectangle. The data structure [CGSize](../corefoundation/cgsize.md) represents the dimensions of width and height.

A [CGPoint](../corefoundation/cgpoint.md), [CGRect](../corefoundation/cgrect.md), or [CGSize](../corefoundation/cgsize.md) structure does not explicitly define the unit of measure for its member quantities. A point’s x- and y-coordinates or a size’s width and height are unitless quantities—whether such measurements are treated as pixels, scale-factor-independent points, texture elements (texels), or some other unit depends on the API using the measurement, and on the context in which that API is used. For example, a [CGRect](../corefoundation/cgrect.md) structure specifying the frame of an [NSView](../appkit/nsview.md) or [UIView](../uikit/uiview.md) object defines the view’s dimensions in points, not pixels. However, the effects of using a [CGPoint](../corefoundation/cgpoint.md) structure in a [CGContext](cgcontext.md) drawing operation depend on the scale factor associated with that context. Where not otherwise specified, you can assume that a [CGPoint](../corefoundation/cgpoint.md), [CGRect](../corefoundation/cgrect.md), or [CGSize](../corefoundation/cgsize.md) structure is defined in points, not pixels. (For details, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156) or [High Resolution Guidelines for OS X](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40012302).)

The height and width stored in a [CGRect](../corefoundation/cgrect.md) data structure can be negative. For example, a rectangle with an origin of `[0.0, 0.0]` and a size of `[10.0,10.0]`  is exactly equivalent to a rectangle with an origin of `[10.0, 10.0]` and a size of `[-10.0,-10.0]`. Your application can standardize a rectangle—that is, ensure that the height and width are stored as positive values—by calling the `CGRectStandardize` function. All functions described in this reference that take [CGRect](../corefoundation/cgrect.md) data structures as inputs implicitly standardize those rectangles before calculating their results. For this reason, your applications should avoid directly reading and writing the data stored in the [CGRect](../corefoundation/cgrect.md) data structure. Instead, use the functions described here to manipulate rectangles and to retrieve their characteristics.

## Topics

### Creating a Dictionary Representation from a Geometric Primitive

- [CGPointCreateDictionaryRepresentation](<cgpointcreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the specified point.
- [CGSizeCreateDictionaryRepresentation](<cgsizecreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the specified size.
- [CGRectCreateDictionaryRepresentation](<cgrectcreatedictionaryrepresentation(__).md>) — Returns a dictionary representation of the provided rectangle.

### Creating a Geometric Primitive from a Dictionary Representation

- [CGPointMakeWithDictionaryRepresentation](<cgpointmakewithdictionaryrepresentation(____).md>) — Fills in a point using the contents of the specified dictionary.
- [CGSizeMakeWithDictionaryRepresentation](<cgsizemakewithdictionaryrepresentation(____).md>) — Fills in a size using the contents of the specified dictionary.
- [CGRectMakeWithDictionaryRepresentation](<cgrectmakewithdictionaryrepresentation(____).md>) — Fills in a rectangle using the contents of the specified dictionary.

### Creating a Geometric Primitive from Values

- [CGPointMake](<cgpointmake(____).md>) — Returns a point with the specified coordinates.
- [CGRectMake](<cgrectmake(________).md>) — Returns a rectangle with the specified coordinate and size values.
- [CGSizeMake](<cgsizemake(____).md>) — Returns a size with the specified dimension values.
- [CGVectorMake](<cgvectormake(____).md>) — Returns a vector with the specified dimension values.

### Modifying Rectangles

- [CGRectInset](<cgrectinset(______).md>) — Returns a rectangle that is smaller or larger than the source rectangle, with the same center point.
- [CGRectIntegral](<cgrectintegral(__).md>) — Returns the smallest rectangle that results from converting the source rectangle values to integers.
- [CGRectIntersection](<cgrectintersection(____).md>) — Returns the intersection of two rectangles.
- [CGRectOffset](<cgrectoffset(______).md>) — Returns a rectangle with an origin that is offset from that of the source rectangle.
- [CGRectStandardize](<cgrectstandardize(__).md>) — Returns a rectangle with a positive width and height.
- [CGRectUnion](<cgrectunion(____).md>) — Returns the smallest rectangle that contains the two source rectangles.

### Comparing Values

- [CGRectEqualToRect](<cgrectequaltorect(____).md>) — Returns whether two rectangles are equal in size and position. _(deprecated)_
- [CGRectIntersectsRect](<cgrectintersectsrect(____).md>) — Returns whether two rectangles intersect.

### Checking for Membership

- [CGRectContainsPoint](<cgrectcontainspoint(____).md>) — Returns whether a rectangle contains a specified point.
- [CGRectContainsRect](<cgrectcontainsrect(____).md>) — Returns whether the first rectangle contains the second rectangle.

### Getting Min, Mid, and Max Values

- [CGRectGetMinX](<cgrectgetminx(__).md>) — Returns the smallest value for the x-coordinate of the rectangle.
- [CGRectGetMinY](<cgrectgetminy(__).md>) — Returns the smallest value for the y-coordinate of the rectangle.
- [CGRectGetMidX](<cgrectgetmidx(__).md>) — Returns the x- coordinate that establishes the center of a rectangle.
- [CGRectGetMidY](<cgrectgetmidy(__).md>) — Returns the y-coordinate that establishes the center of the rectangle.
- [CGRectGetMaxX](<cgrectgetmaxx(__).md>) — Returns the largest value of the x-coordinate for the rectangle.
- [CGRectGetMaxY](<cgrectgetmaxy(__).md>) — Returns the largest value for the y-coordinate of the rectangle.

### Getting Height and Width

- [CGRectGetHeight](<cgrectgetheight(__).md>) — Returns the height of a rectangle.
- [CGRectGetWidth](<cgrectgetwidth(__).md>) — Returns the width of a rectangle.

### Checking Rectangle Characteristics

- [CGRectIsEmpty](<cgrectisempty(__).md>) — Returns whether a rectangle has zero width or height, or is a null rectangle.
- [CGRectIsNull](<cgrectisnull(__).md>) — Returns whether the rectangle is equal to the null rectangle.
- [CGRectIsInfinite](<cgrectisinfinite(__).md>) — Returns whether a rectangle is infinite.

### Data Types

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [CGPoint](../corefoundation/cgpoint.md)
- [CGRect](../corefoundation/cgrect.md)
- [CGSize](../corefoundation/cgsize.md) — A structure that contains width and height values.
- [CGVector](../corefoundation/cgvector.md) — A structure that contains a two-dimensional vector.

### Constants

- [CGRectInfinite](cgrectinfinite.md) — A rectangle that has infinite extent.
- [Geometric Zeros](geometric-zeros.md) — A zero point, zero rectangle, or zero size.
- [CGRectNull](cgrectnull.md) — The null rectangle, representing an invalid value.
- [CGRectEdge](../corefoundation/cgrectedge.md)
- [CGFloat Informational Macros](cgfloat-informational-macros.md) — Informational macros for the `CGFloat` type.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
