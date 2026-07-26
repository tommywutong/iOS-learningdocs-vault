---
title: FixedWidthInteger Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int128/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/int128/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/fixedwidthinteger-implementations.json'
content_hash: 'sha256:a802ef879c56ef41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [Int128](../int128.md)

# FixedWidthInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&*(_:_:)](<&_(____).md>) — Returns the product of the two given values, wrapping the result in case of any overflow.
- [&*(_:_:)](<&_(____)-ctty.md>) — Returns the product of the two given values, wrapping the result in case of any overflow.
- [&*=(_:_:)](<&_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&+(_:_:)](<&+(____).md>) — Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](<&+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-(_:_:)](<&-(____).md>) — Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&-=(_:_:)](<&-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&\>\>(_:_:)](<&__(____)-227qu.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\>\>(_:_:)](<&__(____)-71ih1.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\<\<(_:_:)](<&__(____)-9gig.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\<\<(_:_:)](<&__(____)-lkqj.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\<\<=(_:_:)](<&__=(____)-1pdlg.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\<\<=(_:_:)](<&__=(____)-2vr5o.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<&__=(____)-5pnjk.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<&__=(____)-69tya.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

### Initializers

- [init(_:)](<init(__)-3gl5w.md>)
- [init(_:)](<init(__)-9xe9j.md>) — Creates a new integer value from the given string.
- [init(_:radix:)](<init(__radix_).md>) — Creates a new integer value from the given string and radix.
- [init(bigEndian:)](<init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init(exactly:)](<init(exactly_)-yans.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.

### Instance Properties

- [bigEndian](bigendian.md) — The big-endian representation of this integer.
- [byteSwapped](byteswapped.md) — A representation of this integer with the byte order swapped.
- [leadingZeroBitCount](leadingzerobitcount.md) — The number of leading zeros in this value’s binary representation.
- [littleEndian](littleendian.md) — The little-endian representation of this integer.
- [nonzeroBitCount](nonzerobitcount.md) — The number of bits equal to 1 in this value’s binary representation.

### Instance Methods

- [addingReportingOverflow(_:)](<addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [multipliedFullWidth(by:)](<multipliedfullwidth(by_).md>) — Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [multipliedReportingOverflow(by:)](<multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [remainderReportingOverflow(dividingBy:)](<remainderreportingoverflow(dividingby_).md>) — Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [subtractingReportingOverflow(_:)](<subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.

### Type Properties

- [bitWidth](bitwidth.md) — The number of bits used for the underlying binary representation of values of this type.
- [max](max.md) — The maximum representable integer in this type.
- [min](min.md) — The minimum representable integer in this type.

### Type Methods

- [random(in:)](<random(in_)-4lf3w.md>) — Returns a random value within the specified range.
- [random(in:)](<random(in_)-55a79.md>) — Returns a random value within the specified range.
- [random(in:using:)](<random(in_using_)-4e4vx.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-7t428.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
