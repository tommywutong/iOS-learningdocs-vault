---
title: Comparable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/comparable
source_url: 'https://developer.apple.com/documentation/swift/comparable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/comparable.json'
content_hash: 'sha256:cd4ad324dac4cb5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Comparable

<sub>Protocol</sub>

A type that can be compared using the relational operators `<`, `<=`, `>=`, and `>`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Comparable : Equatable, ~Copyable, ~Escapable
```

## Overview

The `Comparable` protocol is used for types that have an inherent order, such as numbers and strings. Many types in the standard library already conform to the `Comparable` protocol. Add `Comparable` conformance to your own custom types when you want to be able to compare instances using relational operators or use standard library methods that are designed for `Comparable` types.

The most familiar use of relational operators is to compare numbers, as in the following example:

```swift
let currentTemp = 73

if currentTemp >= 90 {
    print("It's a scorcher!")
} else if currentTemp < 65 {
    print("Might need a sweater today.")
} else {
    print("Seems like picnic weather!")
}
// Prints "Seems like picnic weather!"
```

You can use special versions of some sequence and collection operations when working with a `Comparable` type. For example, if your array’s elements conform to `Comparable`, you can call the `sort()` method without using arguments to sort the elements of your array in ascending order.

```swift
var measurements = [1.1, 1.5, 2.9, 1.2, 1.5, 1.3, 1.2]
measurements.sort()
print(measurements)
// Prints "[1.1, 1.2, 1.2, 1.3, 1.5, 1.5, 2.9]"
```

## Conforming to the Comparable Protocol

Types with Comparable conformance implement the less-than operator (`<`) and the equal-to operator (`==`). These two operations impose a strict total order on the values of a type, in which exactly one of the following must be true for any two values `a` and `b`:

- `a == b`
- `a < b`
- `b < a`

In addition, the following conditions must hold:

- `a < a` is always `false` (Irreflexivity)
- `a < b` implies `!(b < a)` (Asymmetry)
- `a < b` and `b < c` implies `a < c` (Transitivity)

To add `Comparable` conformance to your custom types, define the `<` and `==` operators as static methods of your types. The `==` operator is a requirement of the `Equatable` protocol, which `Comparable` extends—see that protocol’s documentation for more information about equality in Swift. Because default implementations of the remainder of the relational operators are provided by the standard library, you’ll be able to use `!=`, `>`, `<=`, and `>=` with instances of your type without any further code.

As an example, here’s an implementation of a `Date` structure that stores the year, month, and day of a date:

```swift
struct Date {
    let year: Int
    let month: Int
    let day: Int
}
```

To add `Comparable` conformance to `Date`, first declare conformance to `Comparable` and implement the `<` operator function.

```swift
extension Date: Comparable {
    static func < (lhs: Date, rhs: Date) -> Bool {
        if lhs.year != rhs.year {
            return lhs.year < rhs.year
        } else if lhs.month != rhs.month {
            return lhs.month < rhs.month
        } else {
            return lhs.day < rhs.day
        }
    }
```

This function uses the least specific nonmatching property of the date to determine the result of the comparison. For example, if the two `year` properties are equal but the two `month` properties are not, the date with the lesser value for `month` is the lesser of the two dates.

Next, implement the `==` operator function, the requirement inherited from the `Equatable` protocol.

```swift
    static func == (lhs: Date, rhs: Date) -> Bool {
        return lhs.year == rhs.year && lhs.month == rhs.month
            && lhs.day == rhs.day
    }
}
```

Two `Date` instances are equal if each of their corresponding properties is equal.

Now that `Date` conforms to `Comparable`, you can compare instances of the type with any of the relational operators. The following example compares the date of the first moon landing with the release of David Bowie’s song “Space Oddity”:

```swift
let spaceOddity = Date(year: 1969, month: 7, day: 11)   // July 11, 1969
let moonLanding = Date(year: 1969, month: 7, day: 20)   // July 20, 1969
if moonLanding > spaceOddity {
    print("Major Tom stepped through the door first.")
} else {
    print("David Bowie was following in Neil Armstrong's footsteps.")
}
// Prints "Major Tom stepped through the door first."
```

Note that the `>` operator provided by the standard library is used in this example, not the `<` operator implemented above.

> [!note] Note
> A conforming type may contain a subset of values which are treated as exceptional—that is, values that are outside the domain of meaningful arguments for the purposes of the `Comparable` protocol. For example, the special “not a number” value for floating-point types (`FloatingPoint.nan`) compares as neither less than, greater than, nor equal to any normal floating-point value. Exceptional values need not take part in the strict total order.

## Relationships

- **Inherits From**: [Equatable](equatable.md)

- **Inherited By**: [BinaryFloatingPoint](binaryfloatingpoint.md), [BinaryInteger](binaryinteger.md), [DurationProtocol](durationprotocol.md), [FixedWidthInteger](fixedwidthinteger.md), [FloatingPoint](floatingpoint.md), [InstantProtocol](instantprotocol.md), [SignedInteger](signedinteger.md), [Strideable](strideable.md), [StringProtocol](stringprotocol.md), [UnsignedInteger](unsignedinteger.md)

- **Conforming Types**: [AnyIndex](anyindex.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Character](character.md), [Index](closedrange/index.md), [Index](collectiondifference/index.md), [Instant](continuousclock/instant.md), [Index](dictionary/index.md), [Index](discontiguousslice/index.md), [Double](double.md), [Duration](duration.md), [Index](enumeratedsequence/index.md), [Index](flattensequence/index.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [JobPriority](jobpriority.md), [Index](lazyprefixwhilesequence/index.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [Index](reversedcollection/index.md), [Index](set/index.md), [String](string.md), [Index](string/index.md), [Substring](substring.md), [Instant](suspendingclock/instant.md), [TaskPriority](taskpriority.md), [UInt](uint.md), [UInt128](uint128.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [CanonicalCombiningClass](unicode/canonicalcombiningclass.md), [Scalar](unicode/scalar.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md)

## Topics

### Range Expressions

- [...(_:_:)](<comparable/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [...(_:)](<comparable/'...(__)-6mvrh.md>) — Returns a partial range extending upward from a lower bound.
- [...(_:)](<comparable/'...(__)-1quco.md>) — Returns a partial range up to, and including, its upper bound.

### Tuple Comparison

- [\<(_:_:)](<_(____)-1b1cu.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-4ck5h.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-23151.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-6p1tf.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-3hhjy.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<(_:_:)](<_(____)-8mgtp.md>) — Returns a Boolean value indicating whether the first tuple is ordered before the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-16p1e.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-3jpod.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-8u5uu.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-6kea2.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-1hzxz.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\<=(_:_:)](<_=(____)-7n746.md>) — Returns a Boolean value indicating whether the first tuple is ordered before or the same as the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-yktb.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-4xg09.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-7p512.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-5gb41.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-3ewuy.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>(_:_:)](<_(____)-kqsy.md>) — Returns a Boolean value indicating whether the first tuple is ordered after the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-1ak1k.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-6kwvw.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-7p28b.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-43xgn.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-6i1ov.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.
- [\>=(_:_:)](<_=(____)-1n7oc.md>) — Returns a Boolean value indicating whether the first tuple is ordered after or the same as the second in a lexicographical ordering.

### Operators

- [..\<(_:)](<comparable/'.._(__).md>) — Returns a partial range up to, but not including, its upper bound.
- [..\<(_:_:)](<comparable/'.._(____).md>) — Returns a half-open range that contains its lower bound but not its upper bound.
- [\>(_:_:)](<comparable/_(____)-8j02g.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [\<(_:_:)](<comparable/_(____)-9jp4d.md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [\>=(_:_:)](<comparable/_=(____)-4hu01.md>) — Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [\<=(_:_:)](<comparable/_=(____)-buc5.md>) — Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.

## See Also

### Equality and Ordering

- [Equatable](equatable.md) — A type that can be compared for value equality.
- [Identifiable](identifiable.md) — A class of types whose instances hold the value of an entity with stable identity.
