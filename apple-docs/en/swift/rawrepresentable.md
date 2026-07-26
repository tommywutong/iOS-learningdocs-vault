---
title: RawRepresentable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rawrepresentable
source_url: 'https://developer.apple.com/documentation/swift/rawrepresentable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawrepresentable.json'
content_hash: 'sha256:8f59f2263a59618f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RawRepresentable

<sub>Protocol</sub>

A type that can be converted to and from an associated raw value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RawRepresentable<RawValue>
```

## Overview

With a `RawRepresentable` type, you can switch back and forth between a custom type and an associated `RawValue` type without losing the value of the original `RawRepresentable` type. Using the raw value of a conforming type streamlines interoperation with Objective-C and legacy APIs and simplifies conformance to other protocols, such as `Equatable`, `Comparable`, and `Hashable`.

The `RawRepresentable` protocol is seen mainly in two categories of types: enumerations with raw value types and option sets.

## Enumerations with Raw Values

For any enumeration with a string, integer, or floating-point raw type, the Swift compiler automatically adds `RawRepresentable` conformance. When defining your own custom enumeration, you give it a raw type by specifying the raw type as the first item in the enumeration’s type inheritance list. You can also use literals to specify values for one or more cases.

For example, the `Counter` enumeration defined here has an `Int` raw value type and gives the first case a raw value of `1`:

```swift
enum Counter: Int {
    case one = 1, two, three, four, five
}
```

You can create a `Counter` instance from an integer value between 1 and 5 by using the `init?(rawValue:)` initializer declared in the `RawRepresentable` protocol. This initializer is failable because although every case of the `Counter` type has a corresponding `Int` value, there are many `Int` values that _don’t_ correspond to a case of `Counter`.

```swift
for i in 3...6 {
    print(Counter(rawValue: i))
}
// Prints "Optional(Counter.three)"
// Prints "Optional(Counter.four)"
// Prints "Optional(Counter.five)"
// Prints "nil"
```

## Option Sets

Option sets all conform to `RawRepresentable` by inheritance using the `OptionSet` protocol. Whether using an option set or creating your own, you use the raw value of an option set instance to store the instance’s bitfield. The raw value must therefore be of a type that conforms to the `FixedWidthInteger` protocol, such as `UInt8` or `Int`. For example, the `Direction` type defines an option set for the four directions you can move in a game.

```swift
struct Directions: OptionSet {
    let rawValue: UInt8

    static let up    = Directions(rawValue: 1 << 0)
    static let down  = Directions(rawValue: 1 << 1)
    static let left  = Directions(rawValue: 1 << 2)
    static let right = Directions(rawValue: 1 << 3)
}
```

Unlike enumerations, option sets provide a nonfailable `init(rawValue:)` initializer to convert from a raw value, because option sets don’t have an enumerated list of all possible cases. Option set values have a one-to-one correspondence with their associated raw values.

In the case of the `Directions` option set, an instance can contain zero, one, or more of the four defined directions. This example declares a constant with three currently allowed moves. The raw value of the `allowedMoves` instance is the result of the bitwise OR of its three members’ raw values:

```swift
let allowedMoves: Directions = [.up, .down, .left]
print(allowedMoves.rawValue)
// Prints "7"
```

Option sets use bitwise operations on their associated raw values to implement their mathematical set operations. For example, the `contains()` method on `allowedMoves` performs a bitwise AND operation to check whether the option set contains an element.

```swift
print(allowedMoves.contains(.right))
// Prints "false"
print(allowedMoves.rawValue & Directions.right.rawValue)
// Prints "0"
```

## Relationships

- **Inherited By**: [OptionSet](optionset.md)

- **Conforming Types**: [CodingUserInfoKey](codinguserinfokey.md), [FloatingPointSign](floatingpointsign.md), [Encoding](string/encoding.md), [TaskPriority](taskpriority.md), [CanonicalCombiningClass](unicode/canonicalcombiningclass.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md)

## Topics

### Creating a Value

- [init(rawValue:)](<rawrepresentable/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

### Accessing the Raw Value

- [rawValue](rawrepresentable/rawvalue-swift.property.md) — The corresponding value of the raw type.
- [RawValue](rawrepresentable/rawvalue-swift.associatedtype.md) — The raw type that can be used to represent all values of the conforming type.

### Comparing Values

- [==(_:_:)](<==(____)-9hu5c.md>) — Returns a Boolean value indicating whether the two arguments are equal.
- [!=(_:_:)](<!=(____)-9wy5n.md>) — Returns a Boolean value indicating whether the two arguments are not equal.
- [!=(_:_:)](<!=(____)-8pggn.md>) — Returns a Boolean value indicating whether the two arguments are not equal.

### Decoding a Value

- [init(from:)](<rawrepresentable/init(from_)-5auil.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
- [init(from:)](<rawrepresentable/init(from_)-5ar5m.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Bool`.
- [init(from:)](<rawrepresentable/init(from_)-417i8.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Double`.
- [init(from:)](<rawrepresentable/init(from_)-9u9tp.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Float`.
- [init(from:)](<rawrepresentable/init(from_)-4ibll.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.
- [init(from:)](<rawrepresentable/init(from_)-3hvw1.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt`.
- [init(from:)](<rawrepresentable/init(from_)-5ktev.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int8`.
- [init(from:)](<rawrepresentable/init(from_)-2hvc0.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int16`.
- [init(from:)](<rawrepresentable/init(from_)-114vz.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [init(from:)](<rawrepresentable/init(from_)-29lhi.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int64`.
- [init(from:)](<rawrepresentable/init(from_)-94955.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt8`.
- [init(from:)](<rawrepresentable/init(from_)-6z4x4.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt16`.
- [init(from:)](<rawrepresentable/init(from_)-3arr3.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt32`.
- [init(from:)](<rawrepresentable/init(from_)-812cy.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt64`.

### Encoding a Value

- [encode(to:)](<rawrepresentable/encode(to_)-4evma.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [encode(to:)](<rawrepresentable/encode(to_)-5igsi.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Bool`.
- [encode(to:)](<rawrepresentable/encode(to_)-4tbh4.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Double`.
- [encode(to:)](<rawrepresentable/encode(to_)-21ma8.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Float`.
- [encode(to:)](<rawrepresentable/encode(to_)-8horh.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [encode(to:)](<rawrepresentable/encode(to_)-78oqu.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt`.
- [encode(to:)](<rawrepresentable/encode(to_)-4pavm.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int8`.
- [encode(to:)](<rawrepresentable/encode(to_)-86dqn.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int16`.
- [encode(to:)](<rawrepresentable/encode(to_)-7dyeb.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [encode(to:)](<rawrepresentable/encode(to_)-4gohs.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.
- [encode(to:)](<rawrepresentable/encode(to_)-9u5rt.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.
- [encode(to:)](<rawrepresentable/encode(to_)-cla3.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.
- [encode(to:)](<rawrepresentable/encode(to_)-27waz.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt32`.
- [encode(to:)](<rawrepresentable/encode(to_)-16ame.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt64`.

### Initializers

- [init(codingKey:)](<rawrepresentable/init(codingkey_)-3mxjn.md>)
- [init(codingKey:)](<rawrepresentable/init(codingkey_)-9gih0.md>)
- [init(from:)](<rawrepresentable/init(from_)-6yajb.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt128`.
- [init(from:)](<rawrepresentable/init(from_)-8fm8i.md>) — Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int128`.

### Instance Properties

- [codingKey](rawrepresentable/codingkey-2f0gm.md)
- [codingKey](rawrepresentable/codingkey-xnw1.md)
- [hashValue](rawrepresentable/hashvalue.md)
- [rawAttachmentValueRepresentation](rawrepresentable/rawattachmentvaluerepresentation.md) _(beta)_

### Instance Methods

- [encode(to:)](<rawrepresentable/encode(to_)-172ut.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `Int128`.
- [encode(to:)](<rawrepresentable/encode(to_)-3ahar.md>) — Encodes this value into the given encoder, when the type’s `RawValue` is `UInt128`.
- [hash(into:)](<rawrepresentable/hash(into_).md>)

### Type Aliases

- [AtomicOptionalRepresentation](rawrepresentable/atomicoptionalrepresentation.md) — The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
- [AtomicRepresentation](rawrepresentable/atomicrepresentation.md) — The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.

### Type Methods

- [decodeAtomicOptionalRepresentation(_:)](<rawrepresentable/decodeatomicoptionalrepresentation(__).md>) — Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [decodeAtomicRepresentation(_:)](<rawrepresentable/decodeatomicrepresentation(__).md>) — Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [encodeAtomicOptionalRepresentation(_:)](<rawrepresentable/encodeatomicoptionalrepresentation(__).md>) — Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.
- [encodeAtomicRepresentation(_:)](<rawrepresentable/encodeatomicrepresentation(__).md>) — Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.
- [makeFromRawAttachmentValue(_:)](<rawrepresentable/makefromrawattachmentvalue(__).md>) _(beta)_

## See Also

### Raw Representation

- [CaseIterable](caseiterable.md) — A type that provides a collection of all of its values.
