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
doc_path: /documentation/swift/uint/fixedwidthinteger-implementations
source_url: 'https://developer.apple.com/documentation/swift/uint/fixedwidthinteger-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/fixedwidthinteger-implementations.json'
content_hash: 'sha256:01de636cdf19d2ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Swift Standard Library](../swift-standard-library.md) · [Numbers and Basic Values](../numbers-and-basic-values.md) · [Special-Use Numeric Types](../special-use-numeric-types.md) · [UInt](../uint.md)

# FixedWidthInteger Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [&*(_:_:)](<&_(____).md>) — Returns the product of the two given values, wrapping the result in case of any overflow.
- [&*=(_:_:)](<&_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&+(_:_:)](<&+(____).md>) — Returns the sum of the two given values, wrapping the result in case of any overflow.
- [&+=(_:_:)](<&+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [&-(_:_:)](<&-(____).md>) — Returns the difference of the two given values, wrapping the result in case of any overflow.
- [&-=(_:_:)](<&-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [&\<\<(_:_:)](<&__(____)-2kxq1.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\<\<(_:_:)](<&__(____)-4xvpf.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\>\>(_:_:)](<&__(____)-5zh57.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\>\>(_:_:)](<&__(____)-76nen.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\>\>(_:_:)](<&__(____)-83cmc.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [&\<\<(_:_:)](<&__(____)-vou2.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [&\<\<=(_:_:)](<&__=(____)-13mjf.md>) — Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [&\>\>=(_:_:)](<&__=(____)-704vn.md>) — Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.

### Initializers

- [init(_:)](<init(__)-2hmhy.md>) — Creates a new integer value from the given string.
- [init(_:)](<init(__)-6gt9n.md>)
- [init(_:radix:)](<init(__radix_).md>) — Creates a new integer value from the given string and radix.
- [init(bigEndian:)](<init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init(exactly:)](<init(exactly_)-7yhn2.md>)
- [init(littleEndian:)](<init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.

### Instance Properties

- [bigEndian](bigendian.md) — The big-endian representation of this integer.
- [littleEndian](littleendian.md) — The little-endian representation of this integer.

### Type Methods

- [random(in:)](<random(in_)-8zzqt.md>) — Returns a random value within the specified range.
- [random(in:)](<random(in_)-9mjpk.md>) — Returns a random value within the specified range.
- [random(in:using:)](<random(in_using_)-3dwvw.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-4lsb1.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
