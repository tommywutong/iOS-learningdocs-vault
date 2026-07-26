---
title: CGFloat
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cgfloat-swift.struct
source_url: 'https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgfloat-swift.struct.json'
content_hash: 'sha256:7fcf6010a1cc7bca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CGFloat

<sub>Structure</sub>

The basic type for floating-point scalar values in Core Graphics and related frameworks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct CGFloat
```

## Overview

The size and precision of this type depend on the CPU architecture. When you build for a 64-bit CPU, the [CGFloat](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 64-bit, IEEE double-precision floating point type, equivalent to the [Double](../swift/double.md) type. When you build for a 32-bit CPU, the [CGFloat](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 32-bit, IEEE single-precision floating point type, equivalent to the [Float](../swift/float.md) type.

## Relationships

- **Conforms To**: [AdditiveArithmetic](../swift/additivearithmetic.md), [Animatable](../swiftui/animatable.md), [BinaryFloatingPoint](../swift/binaryfloatingpoint.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [CVarArg](../swift/cvararg.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [FloatingPoint](../swift/floatingpoint.md), [Hashable](../swift/hashable.md), [Numeric](../swift/numeric.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SignedNumeric](../swift/signednumeric.md), [Strideable](../swift/strideable.md), [VectorArithmetic](../swiftui/vectorarithmetic.md)

## Topics

### Initializers

- [init()](<cgfloat-swift.struct/init().md>) — Create an instance initialized to zero.
- [init(_:)](<cgfloat-swift.struct/init(__)-7dkuk.md>) — Create an instance initialized to `value`.
- [init(_:)](<cgfloat-swift.struct/init(__)-99gmf.md>) — Creates a new value, rounded to the closest possible representation.
- [init(bitPattern:)](<cgfloat-swift.struct/init(bitpattern_).md>)
- [init(exactly:)](<cgfloat-swift.struct/init(exactly_).md>)
- [init(nan:signaling:)](<cgfloat-swift.struct/init(nan_signaling_).md>)
- [init(truncating:)](<cgfloat-swift.struct/init(truncating_).md>)

### Instance Properties

- [bitPattern](cgfloat-swift.struct/bitpattern.md)
- [native](cgfloat-swift.struct/native.md) — The native value.

### Type Aliases

- [NativeType](cgfloat-swift.struct/nativetype.md) — The native type used to store the `CGFloat`.

### Default Implementations

- [CustomReflectable Implementations](cgfloat-swift.struct/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](cgfloat-swift.struct/customstringconvertible-implementations.md)
- [ExpressibleByFloatLiteral Implementations](cgfloat-swift.struct/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](cgfloat-swift.struct/expressiblebyintegerliteral-implementations.md)
- [Hashable Implementations](cgfloat-swift.struct/hashable-implementations.md)
- [Strideable Implementations](cgfloat-swift.struct/strideable-implementations.md)

## See Also

### Structures

- [CGAffineTransform](cgaffinetransform.md)
- [CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [CGPoint](cgpoint.md)
- [CGRect](cgrect.md)
- [CGSize](cgsize.md) — A structure that contains width and height values.
- [CGVector](cgvector.md) — A structure that contains a two-dimensional vector.
