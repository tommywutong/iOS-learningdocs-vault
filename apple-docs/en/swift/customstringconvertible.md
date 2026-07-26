---
title: CustomStringConvertible
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customstringconvertible
source_url: 'https://developer.apple.com/documentation/swift/customstringconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customstringconvertible.json'
content_hash: 'sha256:3fbf77525604919d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CustomStringConvertible

<sub>Protocol</sub>

A type with a customized textual representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomStringConvertible
```

## Overview

Types that conform to the `CustomStringConvertible` protocol can provide their own representation to be used when converting an instance to a string. The `String(describing:)` initializer is the preferred way to convert an instance of _any_ type to a string. If the passed instance conforms to `CustomStringConvertible`, the `String(describing:)` initializer and the `print(_:)` function use the instance’s custom `description` property.

Accessing a type’s `description` property directly or using `CustomStringConvertible` as a generic constraint is discouraged.

## Conforming to the CustomStringConvertible Protocol

Add `CustomStringConvertible` conformance to your custom types by defining a `description` property.

For example, this custom `Point` struct uses the default representation supplied by the standard library:

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(p)
// Prints "Point(x: 21, y: 30)"
```

After implementing the `description` property and declaring `CustomStringConvertible` conformance, the `Point` type provides its own custom representation.

```swift
extension Point: CustomStringConvertible {
    var description: String {
        return "(\(x), \(y))"
    }
}

print(p)
// Prints "(21, 30)"
```

## Relationships

- **Inherited By**: [BinaryInteger](binaryinteger.md), [CodingKey](codingkey.md), [FixedWidthInteger](fixedwidthinteger.md), [LosslessStringConvertible](losslessstringconvertible.md), [SIMD](simd.md), [SignedInteger](signedinteger.md), [StringProtocol](stringprotocol.md), [UnsignedInteger](unsignedinteger.md)

- **Conforming Types**: [AnyHashable](anyhashable.md), [Array](array.md), [ArraySlice](arrayslice.md), [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [Bool](bool.md), [Character](character.md), [ClosedRange](closedrange.md), [ContiguousArray](contiguousarray.md), [DefaultStringInterpolation](defaultstringinterpolation.md), [Dictionary](dictionary.md), [Keys](dictionary/keys-swift.struct.md), [Values](dictionary/values-swift.struct.md), [DiscontiguousSlice](discontiguousslice.md), [Index](discontiguousslice/index.md), [Double](double.md), [Duration](duration.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [KeyValuePairs](keyvaluepairs.md), [Mirror](mirror.md), [Range](range.md), [RangeSet](rangeset.md), [Ranges](rangeset/ranges-swift.struct.md), [RemoteCallTarget](../distributed/remotecalltarget.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md), [Set](set.md), [StaticString](staticstring.md), [String](string.md), [Encoding](string/encoding.md), [UTF16View](string/utf16view.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Substring](substring.md), [TaskLocal](tasklocal.md), [TaskPriority](taskpriority.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [Scalar](unicode/scalar.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [UnownedJob](unownedjob.md), [WordPair](../synchronization/wordpair.md)

## Topics

### Instance Properties

- [description](customstringconvertible/description.md) — A textual representation of this instance.

## See Also

### String Representation

- [LosslessStringConvertible](losslessstringconvertible.md) — A type that can be represented as a string in a lossless, unambiguous way.
- [CustomDebugStringConvertible](customdebugstringconvertible.md) — A type with a customized textual representation suitable for debugging purposes.
