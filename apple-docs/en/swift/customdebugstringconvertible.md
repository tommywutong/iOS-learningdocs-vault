---
title: CustomDebugStringConvertible
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customdebugstringconvertible
source_url: 'https://developer.apple.com/documentation/swift/customdebugstringconvertible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customdebugstringconvertible.json'
content_hash: 'sha256:3f4e4888f28193d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CustomDebugStringConvertible

<sub>Protocol</sub>

A type with a customized textual representation suitable for debugging purposes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomDebugStringConvertible
```

## Overview

Swift provides a default debugging textual representation for any type. That default representation is used by the `String(reflecting:)` initializer and the `debugPrint(_:)` function for types that don’t provide their own. To customize that representation, make your type conform to the `CustomDebugStringConvertible` protocol.

Because the `String(reflecting:)` initializer works for instances of _any_ type, returning an instance’s `debugDescription` if the value passed conforms to `CustomDebugStringConvertible`, accessing a type’s `debugDescription` property directly or using `CustomDebugStringConvertible` as a generic constraint is discouraged.

> [!note] Note
> Calling the `dump(_:_:_:_:)` function and printing in the debugger uses both `String(reflecting:)` and `Mirror(reflecting:)` to collect information about an instance. If you implement `CustomDebugStringConvertible` conformance for your custom type, you may want to consider providing a custom mirror by implementing `CustomReflectable` conformance, as well.

## Conforming to the CustomDebugStringConvertible Protocol

Add `CustomDebugStringConvertible` conformance to your custom types by defining a `debugDescription` property.

For example, this custom `Point` struct uses the default representation supplied by the standard library:

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21, y: 30)
print(String(reflecting: p))
// Prints "Point(x: 21, y: 30)"
```

After adding `CustomDebugStringConvertible` conformance by implementing the `debugDescription` property, `Point` provides its own custom debugging representation.

```swift
extension Point: CustomDebugStringConvertible {
    var debugDescription: String {
        return "(\(x), \(y))"
    }
}

print(String(reflecting: p))
// Prints "(21, 30)"
```

## Relationships

- **Inherited By**: [CodingKey](codingkey.md)

- **Conforming Types**: [AnyHashable](anyhashable.md), [AnyKeyPath](anykeypath.md), [Array](array.md), [ArraySlice](arrayslice.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [CVaListPointer](cvalistpointer.md), [Character](character.md), [ClosedRange](closedrange.md), [CollectionOfOne](collectionofone.md), [ContiguousArray](contiguousarray.md), [DecodingError](decodingerror.md), [Dictionary](dictionary.md), [Keys](dictionary/keys-swift.struct.md), [Values](dictionary/values-swift.struct.md), [Double](double.md), [EncodingError](encodingerror.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [KeyPath](keypath.md), [KeyValuePairs](keyvaluepairs.md), [ObjectIdentifier](objectidentifier.md), [OpaquePointer](opaquepointer.md), [Optional](optional.md), [PartialKeyPath](partialkeypath.md), [Range](range.md), [ReferenceWritableKeyPath](referencewritablekeypath.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [Set](set.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [String](string.md), [Index](string/index.md), [UTF16View](string/utf16view.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Substring](substring.md), [Scalar](unicode/scalar.md), [UnsafeBufferPointer](unsafebufferpointer.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md), [WritableKeyPath](writablekeypath.md)

## Topics

### Instance Properties

- [debugDescription](customdebugstringconvertible/debugdescription.md) — A textual representation of this instance, suitable for debugging.

## See Also

### String Representation

- [CustomStringConvertible](customstringconvertible.md) — A type with a customized textual representation.
- [LosslessStringConvertible](losslessstringconvertible.md) — A type that can be represented as a string in a lossless, unambiguous way.
