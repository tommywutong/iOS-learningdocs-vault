---
title: Range
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/range
source_url: 'https://developer.apple.com/documentation/swift/range'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/range.json'
content_hash: 'sha256:dfdadbb5c15d0ef9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Range

<sub>Structure</sub>

A half-open interval from a lower bound up to, but not including, an upper bound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Range<Bound> where Bound : Comparable
```

## Overview

You create a `Range` instance by using the half-open range operator (`..<`).

```swift
let underFive = 0.0..<5.0
```

You can use a `Range` instance to quickly check if a value is contained in a particular range of values. For example:

```swift
underFive.contains(3.14)
// true
underFive.contains(6.28)
// false
underFive.contains(5.0)
// false
```

`Range` instances can represent an empty interval, unlike `ClosedRange`.

```swift
let empty = 0.0..<0.0
empty.contains(0.0)
// false
empty.isEmpty
// true
```

## Using a Range as a Collection of Consecutive Values

When a range uses integers as its lower and upper bounds, or any other type that conforms to the `Strideable` protocol with an integer stride, you can use that range in a `for`-`in` loop or with any sequence or collection method. The elements of the range are the consecutive values from its lower bound up to, but not including, its upper bound.

```swift
for n in 3..<5 {
    print(n)
}
// Prints "3"
// Prints "4"
```

Because floating-point types such as `Float` and `Double` are their own `Stride` types, they cannot be used as the bounds of a countable range. If you need to iterate over consecutive floating-point values, see the `stride(from:to:by:)` function.

## Relationships

- **Conforms To**: [BNNSGraph.Builder.SliceIndex](../accelerate/bnnsgraph/builder/sliceindex.md), [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [CustomTestStringConvertible](../testing/customteststringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [MLShapedArrayRangeExpression](../coreml/mlshapedarrayrangeexpression.md), [MLTensorRangeExpression](../coreml/mltensorrangeexpression.md), [NDArray.RangeExpression](../coreai/ndarray/rangeexpression.md), [RandomAccessCollection](randomaccesscollection.md), [RangeExpression](rangeexpression.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Creating a Range

- [..\<(_:_:)](<comparable/'.._(____).md>) — Returns a half-open range that contains its lower bound but not its upper bound.

### Converting Ranges

- [relative(to:)](<range/relative(to_).md>) — Returns the range of indices described by this range expression within the given collection.
- [init(_:in:)](<range/init(__in_)-5cclx.md>)
- [init(_:in:)](<range/init(__in_)-5qfor.md>)

### Inspecting a Range

- [isEmpty](range/isempty.md) — A Boolean value indicating whether the range contains no elements.
- [lowerBound](range/lowerbound.md) — The range’s lower bound.
- [upperBound](range/upperbound.md) — The range’s upper bound.

### Checking for Containment

- [~=(_:_:)](<range/~=(____).md>) — Returns a Boolean value indicating whether a value is included in a range.

### Clamping a Range

- [clamped(to:)](<range/clamped(to_).md>) — Returns a copy of this range clamped to the given limiting range.

### Working with Foundation Ranges

- [init(_:)](<range/init(__)-15u6b.md>)
- [init(_:)](<range/init(__)-1q7lu.md>)

### Comparing Ranges

- [==(_:_:)](<range/==(____).md>) — Returns a Boolean value indicating whether two ranges are equal.
- [!=(_:_:)](<range/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [overlaps(_:)](<range/overlaps(__)-7osha.md>) — Returns a Boolean value indicating whether this range and the given range contain an element in common.
- [overlaps(_:)](<range/overlaps(__)-9fkb2.md>) — Returns a Boolean value indicating whether this range and the given closed range contain an element in common.

### Manipulating Indices

- [hash(into:)](<range/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Describing a Range

- [description](range/description.md) — A textual representation of the range.
- [debugDescription](range/debugdescription.md) — A textual representation of the range, suitable for debugging.
- [customMirror](range/custommirror.md) — The custom mirror for this instance.

### Encoding and Decoding a Range

- [encode(to:)](<range/encode(to_).md>) — Encodes this value into the given encoder.
- [init(from:)](<range/init(from_).md>) — Creates a new instance by decoding from the given decoder.

### Infrequently Used Functionality

- [init(uncheckedBounds:)](<range/init(uncheckedbounds_).md>) — Creates an instance with the given bounds.
- [hashValue](range/hashvalue.md) — The hash value.

### Initializers

- [init(_:)](<range/init(__)-35b1j.md>) — Now that Range is conditionally a collection when Bound: Strideable, CountableRange is no longer needed. This is a deprecated initializer for any remaining uses of Range(countableRange).
- [init(_:)](<range/init(__)-79g1a.md>) — Creates an instance equivalent to the given `ClosedRange`.
- [init(_:in:)](<range/init(__in_)-24465.md>)
- [init(_:in:)](<range/init(__in_)-612lr.md>)
- [init(_:in:)](<range/init(__in_)-75xo3.md>)
- [init(_:in:)](<range/init(__in_)-9vre5.md>)

### Instance Methods

- [contains(_:)](<range/contains(__)-4xxju.md>) — Returns a Boolean value indicating whether the given range is contained within this range.
- [contains(_:)](<range/contains(__)-680jp.md>) — Returns a Boolean value indicating whether the given closed range is contained within this range.
- [contains(_:)](<range/contains(__)-76nb4.md>) — Returns a Boolean value indicating whether the given element is contained within the range.
- [formatted()](<range/formatted().md>) — Formats the date range as an interval.
- [formatted(_:)](<range/formatted(__).md>) — Formats the date range using the specified style.
- [formatted(date:time:)](<range/formatted(date_time_).md>) — Formats the date range using the specified date and time format styles.
- [isValid(within:)](<range/isvalid(within_)-2fba2.md>) — Indicates whether the range is valid for use with the provided attributed string.
- [isValid(within:)](<range/isvalid(within_)-8h4h8.md>) — Indicates whether the range is valid for use with the provided discontiguous attributed string.

### Type Methods

- [upToNextMajor(from:)](<range/uptonextmajor(from_).md>) — Returns a requirement for a version range, starting at the given minimum version and going up to the next major version. This is the recommended version requirement.
- [upToNextMinor(from:)](<range/uptonextminor(from_).md>) — Returns a requirement for a version range, starting at the given minimum version and going up to the next minor version.

### Default Implementations

- [BidirectionalCollection Implementations](range/bidirectionalcollection-implementations.md)
- [Collection Implementations](range/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](range/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](range/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](range/customstringconvertible-implementations.md)
- [Decodable Implementations](range/decodable-implementations.md)
- [Encodable Implementations](range/encodable-implementations.md)
- [Equatable Implementations](range/equatable-implementations.md)
- [Hashable Implementations](range/hashable-implementations.md)
- [RangeExpression Implementations](range/rangeexpression-implementations.md)
- [Sequence Implementations](range/sequence-implementations.md)

## See Also

### Ranges

- [..\<(_:_:)](<comparable/'.._(____).md>) — Returns a half-open range that contains its lower bound but not its upper bound.
- [RangeSet](rangeset.md) — A set of values of any comparable type, represented by ranges.
- [...(_:_:)](<comparable/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [ClosedRange](closedrange.md) — An interval from a lower bound up to, and including, an upper bound.
