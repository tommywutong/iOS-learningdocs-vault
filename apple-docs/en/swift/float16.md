---
title: Float16
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16
source_url: 'https://developer.apple.com/documentation/swift/float16'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16.json'
content_hash: 'sha256:60d315c7c83fa820'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Float16

<sub>Structure</sub>

A half-precision (16-bit), floating-point value type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Float16
```

## Overview

On macOS, `Float16` is only available when targeting Apple silicon. On other supported platforms, `Float16` is available for all architectures. If the specified target supports 16-bit floating point arithmetic directly, those instructions will be used; otherwise Float16 arithmetic will be emulated by the swift compiler and runtime.

## Relationships

- **Conforms To**: [AdditiveArithmetic](additivearithmetic.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSGraph.Builder.OperationParameter](../accelerate/bnnsgraph/builder/operationparameter.md), [BNNSScalar](../accelerate/bnnsscalar.md), [BinaryFloatingPoint](binaryfloatingpoint.md), [BitwiseCopyable](bitwisecopyable.md), [Comparable](comparable.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [FloatingPoint](floatingpoint.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [MLShapedArrayScalar](../coreml/mlshapedarrayscalar.md), [MLTensorScalar](../coreml/mltensorscalar.md), [Numeric](numeric.md), [Plottable](../charts/plottable.md), [PrimitivePlottableProtocol](../charts/primitiveplottableprotocol.md), [SIMDScalar](simdscalar.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [SignedNumeric](signednumeric.md), [Strideable](strideable.md), [TextOutputStreamable](textoutputstreamable.md), [USDPrim.Attribute.MetadataValue](../usdkit/usdprim/attribute/metadatavalue.md), [USDPrim.Attribute.Value](../usdkit/usdprim/attribute/value.md), [USDValueProtocol](../usdkit/usdvalueprotocol.md)

## Topics

### Initializers

- [init()](<float16/init().md>)
- [init(_:)](<float16/init(__)-5x2si.md>)
- [init(_:)](<float16/init(__)-77b3g.md>) — Creates a new instance initialized to the given value.
- [init(bitPattern:)](<float16/init(bitpattern_).md>) — Creates a new value with the given bit pattern.
- [init(exactly:)](<float16/init(exactly_)-27ijx.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<float16/init(exactly_)-4hyr3.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<float16/init(exactly_)-8rmd7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(nan:signaling:)](<float16/init(nan_signaling_).md>) — Creates a NaN (“not a number”) value with the specified payload.

### Instance Properties

- [bitPattern](float16/bitpattern.md) — The bit pattern of the value’s encoding.

### Default Implementations

- [AdditiveArithmetic Implementations](float16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](float16/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](float16/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](float16/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](float16/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](float16/customstringconvertible-implementations.md)
- [Decodable Implementations](float16/decodable-implementations.md)
- [Encodable Implementations](float16/encodable-implementations.md)
- [Equatable Implementations](float16/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](float16/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](float16/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](float16/floatingpoint-implementations.md)
- [Hashable Implementations](float16/hashable-implementations.md)
- [LosslessStringConvertible Implementations](float16/losslessstringconvertible-implementations.md)
- [Numeric Implementations](float16/numeric-implementations.md)
- [OperationParameter Implementations](float16/operationparameter-implementations.md)
- [SIMDScalar Implementations](float16/simdscalar-implementations.md)
- [SignedNumeric Implementations](float16/signednumeric-implementations.md)
- [Strideable Implementations](float16/strideable-implementations.md)
- [TextOutputStreamable Implementations](float16/textoutputstreamable-implementations.md)

## See Also

### Floating-Point Values

- [Float80](float80.md) — An extended-precision, floating-point value type.
