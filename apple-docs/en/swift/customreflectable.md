---
title: CustomReflectable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customreflectable
source_url: 'https://developer.apple.com/documentation/swift/customreflectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customreflectable.json'
content_hash: 'sha256:aa8fb222a5c52d37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CustomReflectable

<sub>Protocol</sub>

A type that explicitly supplies its own mirror.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomReflectable
```

## Overview

You can create a mirror for any type using the `Mirror(reflecting:)` initializer, but if you are not satisfied with the mirror supplied for your type by default, you can make it conform to `CustomReflectable` and return a custom `Mirror` instance.

## Relationships

- **Inherited By**: [CustomLeafReflectable](customleafreflectable.md)

- **Conforming Types**: [AnyHashable](anyhashable.md), [Array](array.md), [ArraySlice](arrayslice.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [Character](character.md), [ClosedRange](closedrange.md), [CollectionOfOne](collectionofone.md), [ContiguousArray](contiguousarray.md), [Dictionary](dictionary.md), [Iterator](dictionary/iterator.md), [Double](double.md), [Float](float.md), [Float80](float80.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [Mirror](mirror.md), [Optional](optional.md), [Range](range.md), [Set](set.md), [Iterator](set/iterator.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [StrideThrough](stridethrough.md), [StrideTo](strideto.md), [String](string.md), [UTF16View](string/utf16view.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Substring](substring.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [Scalar](unicode/scalar.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawPointer](unsaferawpointer.md)

## Topics

### Instance Properties

- [customMirror](customreflectable/custommirror.md) — The custom mirror for this instance.

## See Also

### Customizing Your Type’s Reflection

- [CustomLeafReflectable](customleafreflectable.md) — A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md) — A type that supplies a custom description for playground logging.
- [PlaygroundQuickLook](playgroundquicklook.md) — The sum of types that can be used as a Quick Look representation.
- [DebugDescription()](<debugdescription().md>) — Converts description definitions to a debugger Type Summary.
