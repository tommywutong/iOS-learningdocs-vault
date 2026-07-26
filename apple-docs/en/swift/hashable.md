---
title: Hashable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/hashable
source_url: 'https://developer.apple.com/documentation/swift/hashable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/hashable.json'
content_hash: 'sha256:129e0d7ed8be6608'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Hashable

<sub>Protocol</sub>

A type that can be hashed into a `Hasher` to produce an integer hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Hashable : Equatable, ~Copyable, ~Escapable
```

## Overview

You can use any type that conforms to the `Hashable` protocol in a set or as a dictionary key. Many types in the standard library conform to `Hashable`: Strings, integers, floating-point and Boolean values, and even sets are hashable by default. Some other types, such as optionals, arrays and ranges automatically become hashable when their type arguments implement the same.

Your own custom types can be hashable as well. When you define an enumeration without associated values, it gains `Hashable` conformance automatically, and you can add `Hashable` conformance to your other custom types by implementing the `hash(into:)` method. For structs whose stored properties are all `Hashable`, and for enum types that have all-`Hashable` associated values, the compiler is able to provide an implementation of `hash(into:)` automatically.

Hashing a value means feeding its essential components into a hash function, represented by the `Hasher` type. Essential components are those that contribute to the type’s implementation of `Equatable`. Two instances that are equal must feed the same values to `Hasher` in `hash(into:)`, in the same order.

## Conforming to the Hashable Protocol

To use your own custom type in a set or as the key type of a dictionary, add `Hashable` conformance to your type. The `Hashable` protocol inherits from the `Equatable` protocol, so you must also satisfy that protocol’s requirements.

The compiler automatically synthesizes your custom type’s `Hashable` and requirements when you declare `Hashable` conformance in the type’s original declaration and your type meets these criteria:

- For a `struct`, all its stored properties must conform to `Hashable`.
- For an `enum`, all its associated values must conform to `Hashable`. (An `enum` without associated values has `Hashable` conformance even without the declaration.)

To customize your type’s `Hashable` conformance, to adopt `Hashable` in a type that doesn’t meet the criteria listed above, or to extend an existing type to conform to `Hashable`, implement the `hash(into:)` method in your custom type.

In your `hash(into:)` implementation, call `combine(_:)` on the provided `Hasher` instance with the essential components of your type. To ensure that your type meets the semantic requirements of the `Hashable` and `Equatable` protocols, it’s a good idea to also customize your type’s `Equatable` conformance to match.

As an example, consider a `GridPoint` type that describes a location in a grid of buttons. Here’s the initial declaration of the `GridPoint` type:

```swift
/// A point in an x-y coordinate system.
struct GridPoint {
    var x: Int
    var y: Int
}
```

You’d like to create a set of the grid points where a user has already tapped. Because the `GridPoint` type is not hashable yet, it can’t be used in a set. To add `Hashable` conformance, provide an `==` operator function and implement the `hash(into:)` method.

```swift
extension GridPoint: Hashable {
    static func == (lhs: GridPoint, rhs: GridPoint) -> Bool {
        return lhs.x == rhs.x && lhs.y == rhs.y
    }

    func hash(into hasher: inout Hasher) {
        hasher.combine(x)
        hasher.combine(y)
    }
}
```

The `hash(into:)` method in this example feeds the grid point’s `x` and `y` properties into the provided hasher. These properties are the same ones used to test for equality in the `==` operator function.

Now that `GridPoint` conforms to the `Hashable` protocol, you can create a set of previously tapped grid points.

```swift
var tappedPoints: Set = [GridPoint(x: 2, y: 3), GridPoint(x: 4, y: 1)]
let nextTap = GridPoint(x: 0, y: 1)
if tappedPoints.contains(nextTap) {
    print("Already tapped at (\(nextTap.x), \(nextTap.y)).")
} else {
    tappedPoints.insert(nextTap)
    print("New tap detected at (\(nextTap.x), \(nextTap.y)).")
}
// Prints "New tap detected at (0, 1).")
```

## Relationships

- **Inherits From**: [Equatable](equatable.md)

- **Inherited By**: [BinaryFloatingPoint](binaryfloatingpoint.md), [BinaryInteger](binaryinteger.md), [DistributedActor](../distributed/distributedactor.md), [FixedWidthInteger](fixedwidthinteger.md), [FloatingPoint](floatingpoint.md), [InstantProtocol](instantprotocol.md), [SIMD](simd.md), [SignedInteger](signedinteger.md), [StringProtocol](stringprotocol.md), [UnsignedInteger](unsignedinteger.md)

- **Conforming Types**: [AnyHashable](anyhashable.md), [AnyKeyPath](anykeypath.md), [Array](array.md), [ArraySlice](arrayslice.md), [Continuation](asyncstream/continuation.md), [Termination](asyncstream/continuation/termination.md), [Continuation](asyncthrowingstream/continuation.md), [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [ByteOrder](byteorder.md), [Character](character.md), [ClosedRange](closedrange.md), [Index](closedrange/index.md), [CodingUserInfoKey](codinguserinfokey.md), [CollectionDifference](collectiondifference.md), [Change](collectiondifference/change.md), [Index](collectiondifference/index.md), [CollectionOfOne](collectionofone.md), [ContiguousArray](contiguousarray.md), [Instant](continuousclock/instant.md), [Dictionary](dictionary.md), [Index](dictionary/index.md), [Keys](dictionary/keys-swift.struct.md), [DiscontiguousSlice](discontiguousslice.md), [Index](discontiguousslice/index.md), [Double](double.md), [Duration](duration.md), [TimeFormatStyle](duration/timeformatstyle.md), [Attributed](duration/timeformatstyle/attributed-swift.struct.md), [Pattern](duration/timeformatstyle/pattern-swift.struct.md), [UnitsFormatStyle](duration/unitsformatstyle.md), [Attributed](duration/unitsformatstyle/attributed-swift.struct.md), [FractionalPartDisplayStrategy](duration/unitsformatstyle/fractionalpartdisplaystrategy.md), [Unit](duration/unitsformatstyle/unit.md), [UnitWidth](duration/unitsformatstyle/unitwidth-swift.struct.md), [ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy.md), [EmptyCollection](emptycollection.md), [ErrorCode](../distributed/executedistributedtargeterror/errorcode-swift.enum.md), [Index](flattensequence/index.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [FloatingPointClassification](floatingpointclassification.md), [FloatingPointRoundingRule](floatingpointroundingrule.md), [FloatingPointSign](floatingpointsign.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [KeyPath](keypath.md), [Index](lazyprefixwhilesequence/index.md), [LocalTestingActorID](../distributed/localtestingactorid.md), [DisplayStyle](mirror/displaystyle-swift.enum.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [ObservationRegistrar](../observation/observationregistrar.md), [OpaquePointer](opaquepointer.md), [Optional](optional.md), [PartialKeyPath](partialkeypath.md), [Range](range.md), [RangeSet](rangeset.md), [Ranges](rangeset/ranges-swift.struct.md), [ReferenceWritableKeyPath](referencewritablekeypath.md), [RegexRepetitionBehavior](regexrepetitionbehavior.md), [RegexSemanticLevel](regexsemanticlevel.md), [RegexWordBoundaryKind](regexwordboundarykind.md), [RemoteCallTarget](../distributed/remotecalltarget.md), [Result](result.md), [Index](reversedcollection/index.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md), [Set](set.md), [Index](set/index.md), [String](string.md), [Comparator](string/comparator.md), [Encoding](string/encoding.md), [Index](string/index.md), [CapitalizationType](string/intentinputoptions/capitalizationtype-swift.enum.md), [KeyboardType](string/intentinputoptions/keyboardtype-swift.enum.md), [Placeholder](string/localizationvalue/placeholder.md), [StandardComparator](string/standardcomparator.md), [Substring](substring.md), [Instant](suspendingclock/instant.md), [Task](task.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [CanonicalCombiningClass](unicode/canonicalcombiningclass.md), [GeneralCategory](unicode/generalcategory.md), [NumericType](unicode/numerictype.md), [Scalar](unicode/scalar.md), [UTF32](unicode/utf32.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [UniqueArray](uniquearray.md), [UnownedTaskExecutor](unownedtaskexecutor.md), [UnsafeCurrentTask](unsafecurrenttask.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md), [WritableKeyPath](writablekeypath.md)

## Topics

### Providing a Hash Value

- [hash(into:)](<hashable/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Deprecated

- [hashValue](hashable/hashvalue.md) — The hash value.

## See Also

### Sets and Dictionaries

- [Hasher](hasher.md) — The universal hash function used by `Set` and `Dictionary`.
