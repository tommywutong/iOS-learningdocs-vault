---
title: CIVector
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/civector
source_url: 'https://developer.apple.com/documentation/coreimage/civector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/civector.json'
content_hash: 'sha256:166cd5c693dfd9e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIVector

<sub>Class</sub>

The Core Image class that defines a vector object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIVector
```

## Overview

A `CIVector` can store one or more `CGFloat` in one object. They can store a group of float values for a variety of different uses such as coordinate points, direction vectors, geometric rectangles, transform matrices, convolution weights, or just a list a parameter values.

You use `CIVector` objects in conjunction with other Core Image classes, such as [CIFilter](cifilter-swift.class.md) and [CIKernel](cikernel.md).  Many of the built-in Core Image filters have one or more `CIVector` inputs that you can set to affect the filter’s behavior.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Vector

- [+ vectorWithCGAffineTransform:](<civector/init(cgaffinetransform_)-59e4k.md>) — Create a Core Image vector object that is initialized with six values provided by a `CGAffineTransform` structure.
- [+ vectorWithCGPoint:](<civector/init(cgpoint_)-3mobm.md>) — Create a Core Image vector object that is initialized with two values provided by a `CGPoint` structure.
- [+ vectorWithCGRect:](<civector/init(cgrect_)-3undj.md>) — Create a Core Image vector object that is initialized with four values provided by a `CGRect` structure.

### Initializing a Vector

- [- initWithValues:count:](<civector/init(values_count_).md>) — Initialize a Core Image vector object with the specified the values.
- [- initWithX:](<civector/init(x_).md>) — Initialize a Core Image vector object with one value.
- [- initWithX:Y:](<civector/init(x_y_)-4grr.md>) — Initialize a Core Image vector object with two values.
- [- initWithX:Y:Z:](<civector/init(x_y_z_)-zais.md>) — Initialize a Core Image vector object with three values.
- [- initWithX:Y:Z:W:](<civector/init(x_y_z_w_)-75emo.md>) — Initialize a Core Image vector object with four values.
- [- initWithString:](<civector/init(string_).md>) — Initialize a Core Image vector object with values provided in a string representation.
- [- initWithCGAffineTransform:](<civector/init(cgaffinetransform_)-6o8gl.md>) — Initialize a Core Image vector object with six values provided by a `CGAffineTransform` structure.
- [- initWithCGPoint:](<civector/init(cgpoint_)-8cf9j.md>) — Initialize a Core Image vector object with two values provided by a `CGPoint` structure.
- [- initWithCGRect:](<civector/init(cgrect_)-6bolw.md>) — Initialize a Core Image vector object with four values provided by a `CGRect` structure.

### Getting Values From a Vector

- [- valueAtIndex:](<civector/value(at_).md>) — Returns a value from a specific position in the vector.
- [count](civector/count.md) — The number of items in the vector.
- [X](civector/x.md) — The value located in the first position in the vector.
- [Y](civector/y.md) — The value located in the second position in the vector.
- [Z](civector/z.md) — The value located in the third position in the vector.
- [W](civector/w.md) — The value located in the forth position in the vector.
- [stringRepresentation](civector/stringrepresentation.md) — Returns a formatted string with all the values of a `CIVector`.
- [CGAffineTransformValue](civector/cgaffinetransformvalue.md) — Returns the values in the vector as a `CGAffineTransformValue` structure.
- [CGPointValue](civector/cgpointvalue.md) — Returns the values in the vector as a `CGPoint` structure.
- [CGRectValue](civector/cgrectvalue.md) — Returns the values in the vector as a `CGRect` structure.

### Initializers

- [init(CGAffineTransform:)](<civector/init(cgaffinetransform_)-61k8d.md>)
- [init(CGAffineTransform:)](<civector/init(cgaffinetransform_)-gf61.md>)
- [init(CGPoint:)](<civector/init(cgpoint_)-2q3w0.md>)
- [init(CGPoint:)](<civector/init(cgpoint_)-339fj.md>)
- [init(CGRect:)](<civector/init(cgrect_)-60mr0.md>)
- [init(CGRect:)](<civector/init(cgrect_)-9l6dq.md>)
- [init(coder:)](<civector/init(coder_).md>)
- [init(x:Y:)](<civector/init(x_y_)-2ia98.md>)
- [init(x:Y:)](<civector/init(x_y_)-8ln4z.md>)
- [init(x:Y:Z:)](<civector/init(x_y_z_)-6pett.md>)
- [init(x:Y:Z:)](<civector/init(x_y_z_)-94o0c.md>)
- [init(x:Y:Z:W:)](<civector/init(x_y_z_w_)-3lp39.md>)
- [init(x:Y:Z:W:)](<civector/init(x_y_z_w_)-9obnr.md>)

## See Also

### Filters

- [CIFilter](cifilter-swift.class.md) — An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [CIRAWFilter](cirawfilter.md) — A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [CIColor](cicolor.md) — The Core Image class that defines a color object.
