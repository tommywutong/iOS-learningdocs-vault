---
title: NSNumber
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnumber
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber.json'
content_hash: 'sha256:8710d6f97df6a286'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNumber

<sub>Class</sub>

An object wrapper for primitive scalar numeric values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSNumber
```

## Overview

`NSNumber` is a subclass of `NSValue` that offers a value as any C scalar (numeric) type. It defines a set of methods specifically for setting and accessing the value as a signed or unsigned `char`, `short int`, `int`, `long int`, `long long int`, `float`, or `double` or as a `BOOL`. (Note that number objects do not necessarily preserve the type they are created with.) It also defines a [- compare:](<nsnumber/compare(__).md>) method to determine the ordering of two `NSNumber` objects.

`NSNumber` is “toll-free bridged” with its Core Foundation counterparts: [CFNumber](../corefoundation/cfnumber.md) for integer and floating point values, and [CFBoolean](../corefoundation/cfboolean.md) for Boolean values. See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

### Value Conversions

`NSNumber` provides readonly properties that return the object’s stored value converted to a particular Boolean, integer, unsigned integer, or floating point C scalar type. Because numeric types have different storage capabilities, attempting to initialize with a value of one type and access the value of another type may produce an erroneous result—for example, initializing with a `double` value exceeding `FLT_MAX` and accessing its [floatValue](nsnumber/floatvalue.md), or initializing with an negative integer value and accessing its [unsignedIntegerValue](nsnumber/uintvalue.md). In some cases, attempting to initialize with a value of a type and access the value of another type may result in loss of precision—for example, initializing with a `double` value with many significant digits and accessing its [floatValue](nsnumber/floatvalue.md), or initializing with a large integer value and accessing its [charValue](nsnumber/int8value.md).

An `NSNumber` object initialized with a value of a particular type accessing the converted value of a different _kind_ of type, such as `unsigned int` and `float`, will convert its stored value to that converted type in the following ways:

| `Value` | [boolValue](nsnumber/boolvalue.md) | [integerValue](nsnumber/intvalue-95zzp.md) | [unsignedIntegerValue](nsnumber/uintvalue.md) | [floatValue](nsnumber/floatvalue.md) |
|---|---|---|---|---|
| [false](../swift/false.md) | [false](../swift/false.md) | `0` | `0` | `0.0` |
| [true](../swift/true.md) | [true](../swift/true.md) | `1` | `1` | `1.0` |

| `Value` | [boolValue](nsnumber/boolvalue.md) | [integerValue](nsnumber/intvalue-95zzp.md) | [unsignedIntegerValue](nsnumber/uintvalue.md) | [floatValue](nsnumber/floatvalue.md) |
|---|---|---|---|---|
| `0` | [false](../swift/false.md) | `0` | `0` | `0.0` |
| `1` | [true](../swift/true.md) | `1` | `1` | `1.0` |
| `-1` | [true](../swift/true.md) | `-1` | _invalid, erroneous result_ | `-1.0` |

| `Value` | [boolValue](nsnumber/boolvalue.md) | [integerValue](nsnumber/intvalue-95zzp.md) | [unsignedIntegerValue](nsnumber/uintvalue.md) | [floatValue](nsnumber/floatvalue.md) |
|---|---|---|---|---|
| `0` | [false](../swift/false.md) | `0` | `0` | `0.0` |
| `1` | [true](../swift/true.md) | `1` | `1` | `1.0` |

| `Value` | [boolValue](nsnumber/boolvalue.md) | [integerValue](nsnumber/intvalue-95zzp.md) | [unsignedIntegerValue](nsnumber/uintvalue.md) | [floatValue](nsnumber/floatvalue.md) |
|---|---|---|---|---|
| `0.0` | [false](../swift/false.md) | `0` | `0` | `0.0` |
| `1.0` | [true](../swift/true.md) | `1` | `1` | `1.0` |
| `-1.0` | [true](../swift/true.md) | `-1` | _invalid, erroneous result_ | `-1.0` |

### Subclassing Notes

As with any class cluster, subclasses of `NSNumber` must override the primitive methods of its superclass, `NSValue`. In addition, there are two requirements around the data type your subclass represents:

1. Your implementation of [objCType](nsvalue/objctype.md) must return one of “`c`”, “`C`”, “`s`”, “`S`”, “`i`”, “`I`”, “`l`”, “`L`”, “`q`”, “`Q`”, “`f`”, and “`d`”. This is required for the other methods of [NSNumber](nsnumber.md) to behave correctly.
2. Your subclass must override the accessor method that corresponds to the declared type—for example, if your implementation of [objCType](nsvalue/objctype.md) returns  “`i`”, you must override [intValue](nsnumber/int32value.md).

## Relationships

- **Inherits From**: [NSValue](nsvalue.md)

- **Inherited By**: [NSDecimalNumber](nsdecimalnumber.md)

- **Conforms To**: [CKRecordValue](../cloudkit/ckrecordvalue-c.protocol.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByBooleanLiteral](../swift/expressiblebybooleanliteral.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFetchRequestResult](../coredata/nsfetchrequestresult.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSNumber Object

- [- initWithBool:](<nsnumber/init(value_)-1ojz2.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as a `BOOL`.
- [- initWithChar:](<nsnumber/init(value_)-8krjs.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as a signed `char`.
- [- initWithDouble:](<nsnumber/init(value_)-15chk.md>) — Returns an `NSNumber` object initialized to contain `value`, treated as a `double`.
- [- initWithFloat:](<nsnumber/init(value_)-2vlwk.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as a `float`.
- [- initWithInt:](<nsnumber/init(value_)-7jvmg.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as a signed `int`.
- [- initWithInteger:](<nsnumber/init(value_)-5jcjl.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `NSInteger`.
- [- initWithLongLong:](<nsnumber/init(value_)-40ad0.md>) — Returns an `NSNumber` object initialized to contain `value`, treated as a signed `long long`.
- [- initWithShort:](<nsnumber/init(value_)-16drx.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as a signed `short`.
- [- initWithUnsignedChar:](<nsnumber/init(value_)-8se67.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned char`.
- [- initWithUnsignedInt:](<nsnumber/init(value_)-47coa.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned int`.
- [- initWithUnsignedInteger:](<nsnumber/init(value_)-3l4ek.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `NSUInteger`.
- [- initWithUnsignedLongLong:](<nsnumber/init(value_)-43lc7.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned long long`.
- [- initWithUnsignedShort:](<nsnumber/init(value_)-87y9m.md>) — Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned short`.

### Accessing Numeric Values

- [boolValue](nsnumber/boolvalue.md) — The number object’s value expressed as a Boolean value.
- [charValue](nsnumber/int8value.md) — The number object’s value expressed as a `char`.
- [decimalValue](nsnumber/decimalvalue.md) — The number object’s value expressed as an [Decimal](decimal.md) structure.
- [doubleValue](nsnumber/doublevalue.md) — The number object’s value expressed as a `double`, converted as necessary.
- [floatValue](nsnumber/floatvalue.md) — The number object’s value expressed as a `float`, converted as necessary.
- [intValue](nsnumber/int32value.md) — The number object’s value expressed as an `int`, converted as necessary.
- [integerValue](nsnumber/intvalue-95zzp.md) — The number object’s value expressed as an `NSInteger` object, converted as necessary.
- [longLongValue](nsnumber/int64value.md) — The number object’s value expressed as a `long long`, converted as necessary.
- [shortValue](nsnumber/int16value.md) — The number object’s value expressed as a `short`, converted as necessary.
- [unsignedCharValue](nsnumber/uint8value.md) — The number object’s value expressed as an unsigned `char`, converted as necessary.
- [unsignedIntegerValue](nsnumber/uintvalue.md) — The number object’s value expressed as an `NSUInteger` object, converted as necessary.
- [unsignedIntValue](nsnumber/uint32value.md) — The number object’s value expressed as an unsigned `int`, converted as necessary.
- [unsignedLongLongValue](nsnumber/uint64value.md) — The number object’s value expressed as an unsigned `long long`, converted as necessary.
- [unsignedShortValue](nsnumber/uint16value.md) — The number object’s value expressed as an unsigned `short`, converted as necessary.

### Retrieving String Representations

- [- descriptionWithLocale:](<nsnumber/description(withlocale_).md>) — Returns a string that represents the contents of the number object for a given locale.
- [stringValue](nsnumber/stringvalue.md) — The number object’s value expressed as a human-readable string.

### Comparing NSNumber Objects

- [- compare:](<nsnumber/compare(__).md>) — Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.
- [- isEqualToNumber:](<nsnumber/isequal(to_).md>) — Returns a Boolean value that indicates whether the number object’s value and a given number are equal.

### Number Validation

- [NSDecimalIsNotANumber](<nsdecimalisnotanumber(__).md>) — Returns a Boolean that indicates whether a given decimal contains a valid number.

### Initializers

- [init(bool:)](<nsnumber/init(bool_).md>)
- [init(char:)](<nsnumber/init(char_).md>)
- [- initWithCoder:](<nsnumber/init(coder_).md>)
- [init(double:)](<nsnumber/init(double_).md>)
- [init(float:)](<nsnumber/init(float_).md>)
- [init(int:)](<nsnumber/init(int_).md>)
- [init(integer:)](<nsnumber/init(integer_).md>)
- [init(longLong:)](<nsnumber/init(longlong_).md>)
- [init(short:)](<nsnumber/init(short_).md>)
- [init(unsignedChar:)](<nsnumber/init(unsignedchar_).md>)
- [init(unsignedInt:)](<nsnumber/init(unsignedint_).md>)
- [init(unsignedInteger:)](<nsnumber/init(unsignedinteger_).md>)
- [init(unsignedLongLong:)](<nsnumber/init(unsignedlonglong_).md>)
- [init(unsignedShort:)](<nsnumber/init(unsignedshort_).md>)

### Default Implementations

- [ExpressibleByBooleanLiteral Implementations](nsnumber/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](nsnumber/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](nsnumber/expressiblebyintegerliteral-implementations.md)
