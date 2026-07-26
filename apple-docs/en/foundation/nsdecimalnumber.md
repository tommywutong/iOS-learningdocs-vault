---
title: NSDecimalNumber
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber.json'
content_hash: 'sha256:1d861cbc53668b17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDecimalNumber

<sub>Class</sub>

An object for representing and performing arithmetic on base-10 numbers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDecimalNumber
```

## Overview

In Swift, this object bridges to [Decimal](decimal.md); use [NSDecimalNumber](nsdecimalnumber.md) when you need reference semantics or other Foundation-specific behavior.

`NSDecimalNumber`, an immutable subclass of `NSNumber`, provides an object-oriented wrapper for doing base-10 arithmetic. An instance can represent any number that can be expressed as `mantissa x 10^exponent` where mantissa is a decimal integer up to 38 digits long, and exponent is an integer from –128 through 127.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Decimal](decimal.md) structure, which bridges to the [NSDecimalNumber](nsdecimalnumber.md) class. For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSNumber](nsnumber.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByBooleanLiteral](../swift/expressiblebybooleanliteral.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Decimal Number

- [one](nsdecimalnumber/one.md) — A decimal number equivalent to the number 1.0.
- [zero](nsdecimalnumber/zero.md) — A decimal number equivalent to the number 0.0.
- [notANumber](nsdecimalnumber/notanumber.md) — A decimal number that specifies no number.

### Initializing a Decimal Number

- [- initWithDecimal:](<nsdecimalnumber/init(decimal_).md>) — Initializes a decimal number to represent a given decimal.
- [- initWithMantissa:exponent:isNegative:](<nsdecimalnumber/init(mantissa_exponent_isnegative_).md>) — Initializes a decimal number using the given mantissa, exponent, and sign.
- [- initWithString:](<nsdecimalnumber/init(string_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string.
- [- initWithString:locale:](<nsdecimalnumber/init(string_locale_).md>) — Initializes a decimal number so that its value is equivalent to that in a given numeric string, interpreted using a given locale.

### Performing Arithmetic

- [- decimalNumberByAdding:](<nsdecimalnumber/adding(__).md>) — Adds this number to another given number.
- [- decimalNumberBySubtracting:](<nsdecimalnumber/subtracting(__).md>) — Subtracts another given number from this one.
- [- decimalNumberByMultiplyingBy:](<nsdecimalnumber/multiplying(by_).md>) — Multiplies the number by another given number.
- [- decimalNumberByDividingBy:](<nsdecimalnumber/dividing(by_).md>) — Divides the number by another given number.
- [- decimalNumberByRaisingToPower:](<nsdecimalnumber/raising(topower_).md>) — Raises the number to a given power.
- [- decimalNumberByMultiplyingByPowerOf10:](<nsdecimalnumber/multiplying(bypowerof10_).md>) — Multiplies the number by 10 raised to the given power.
- [- decimalNumberByAdding:withBehavior:](<nsdecimalnumber/adding(__withbehavior_).md>) — Adds this number to another given number using the specified behavior.
- [- decimalNumberBySubtracting:withBehavior:](<nsdecimalnumber/subtracting(__withbehavior_).md>) — Subtracts this a given number from this one using the specified behavior.
- [- decimalNumberByMultiplyingBy:withBehavior:](<nsdecimalnumber/multiplying(by_withbehavior_).md>) — Multiplies this number by another given number using the specified behavior.
- [- decimalNumberByDividingBy:withBehavior:](<nsdecimalnumber/dividing(by_withbehavior_).md>) — Divides this number by another given number using the specified behavior.
- [- decimalNumberByRaisingToPower:withBehavior:](<nsdecimalnumber/raising(topower_withbehavior_).md>) — Raises the number to a given power using the specified behavior.
- [- decimalNumberByMultiplyingByPowerOf10:withBehavior:](<nsdecimalnumber/multiplying(bypowerof10_withbehavior_).md>) — Multiplies the number by 10 raised to the given power using the specified behavior.

### Rounding Off

- [- decimalNumberByRoundingAccordingToBehavior:](<nsdecimalnumber/rounding(accordingtobehavior_).md>) — Returns a rounded version of the decimal number using the specified rounding behavior.

### Managing Behavior

- [defaultBehavior](nsdecimalnumber/defaultbehavior.md) — The way arithmetic methods round off and handle error conditions.
- [NSDecimalNumberBehaviors](nsdecimalnumberbehaviors.md) — A protocol that declares three methods that control the discretionary aspects of working with decimal numbers.
- [NSDecimalNumberHandler](nsdecimalnumberhandler.md) — A class that adopts the decimal number behaviors protocol.

### Accessing the Value

- [decimalValue](nsdecimalnumber/decimalvalue.md) — The decimal number’s value, expressed as an [Decimal](decimal.md) structure.
- [doubleValue](nsdecimalnumber/doublevalue.md) — The decimal number’s closest approximate `double` value.
- [- descriptionWithLocale:](<nsdecimalnumber/description(withlocale_).md>) — Returns a string representation of the decimal number appropriate for the specified locale.
- [objCType](nsdecimalnumber/objctype.md) — A C string containing the Objective-C type for the data contained in the decimal number object.

### Comparing Decimal Numbers

- [- compare:](<nsdecimalnumber/compare(__).md>) — Compares this decimal number and another.

### Getting Maximum and Minimum Possible Values

- [maximumDecimalNumber](nsdecimalnumber/maximum.md) — Returns the largest possible value of a decimal number.
- [minimumDecimalNumber](nsdecimalnumber/minimum.md) — Returns the smallest possible value of a decimal number.

### Recognizing Exceptions

- [NSDecimalNumberExactnessException](nsexceptionname/decimalnumberexactnessexception.md) — The exception raised if there is an exactness error.
- [NSDecimalNumberOverflowException](nsexceptionname/decimalnumberoverflowexception.md) — The exception raised on overflow.
- [NSDecimalNumberUnderflowException](nsexceptionname/decimalnumberunderflowexception.md) — The exception raised on underflow.
- [NSDecimalNumberDivideByZeroException](nsexceptionname/decimalnumberdividebyzeroexception.md) — The exception raised on divide by zero.
