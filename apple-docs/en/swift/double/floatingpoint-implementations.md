---
title: FloatingPoint Implementations
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/floatingpoint-implementations
source_url: 'https://developer.apple.com/documentation/swift/double/floatingpoint-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/floatingpoint-implementations.json'
content_hash: 'sha256:23f2387f4474bddf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# FloatingPoint Implementations

<sub>API Collection</sub>

## Topics

### Operators

- [*(_:_:)](<_(____).md>) — Multiplies two values and produces their product, rounding to a representable value.
- [*=(_:_:)](<_=(____).md>) — Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [+(_:_:)](<+(____).md>) — Adds two values and produces their sum, rounded to a representable value.
- [+=(_:_:)](<+=(____).md>) — Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [-(_:)](<-(__).md>) — Calculates the additive inverse of a value.
- [-(_:_:)](<-(____).md>) — Subtracts one value from another and produces their difference, rounded to a representable value.
- [-=(_:_:)](<-=(____).md>) — Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [/(_:_:)](<_(____).md>) — Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [\>(_:_:)](<_(____)-552jp.md>)
- [/=(_:_:)](<_=(____).md>) — Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [\<=(_:_:)](<_=(____)-5yoz7.md>)
- [\>=(_:_:)](<_=(____)-9o6h8.md>)

### Initializers

- [init(_:)](<init(__)-5blrp.md>) — Creates a new value, rounded to the closest possible representation.
- [init(_:)](<init(__)-84ohu.md>) — Creates a new value, rounded to the closest possible representation.
- [init(exactly:)](<init(exactly_)-2uexo.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(sign:exponent:significand:)](<init(sign_exponent_significand_).md>) — Creates a new value from the given sign, exponent, and significand.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_).md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf:magnitudeOf:)](<init(signof_magnitudeof_)-6i9uy.md>) — Creates a new floating-point value using the sign of one value and the magnitude of another.

### Instance Properties

- [exponent](exponent-swift.property.md) — The exponent of the floating-point value.
- [floatingPointClass](floatingpointclass.md) — The classification of this value.
- [isCanonical](iscanonical.md) — A Boolean value indicating whether the instance’s representation is in its canonical form.
- [isFinite](isfinite.md) — A Boolean value indicating whether this instance is finite.
- [isInfinite](isinfinite.md) — A Boolean value indicating whether the instance is infinite.
- [isNaN](isnan.md) — A Boolean value indicating whether the instance is NaN (“not a number”).
- [isNormal](isnormal.md) — A Boolean value indicating whether this instance is normal.
- [isSignalingNaN](issignalingnan.md) — A Boolean value indicating whether the instance is a signaling NaN.
- [isSubnormal](issubnormal.md) — A Boolean value indicating whether the instance is subnormal.
- [isZero](iszero.md) — A Boolean value indicating whether the instance is equal to zero.
- [nextDown](nextdown.md) — The greatest representable value that compares less than this value.
- [nextUp](nextup.md) — The least representable value that compares greater than this value.
- [sign](sign.md) — The sign of the floating-point value.
- [significand](significand.md) — The significand of the floating-point value.
- [ulp](ulp.md) — The unit in the last place of this value.

### Instance Methods

- [addProduct(_:_:)](<addproduct(____).md>) — Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [addingProduct(_:_:)](<addingproduct(____).md>) — Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [formRemainder(dividingBy:)](<formremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value.
- [formSquareRoot()](<formsquareroot().md>) — Replaces this value with its square root, rounded to a representable value.
- [formTruncatingRemainder(dividingBy:)](<formtruncatingremainder(dividingby_).md>) — Replaces this value with the remainder of itself divided by the given value using truncating division.
- [isEqual(to:)](<isequal(to_).md>) — Returns a Boolean value indicating whether this instance is equal to the given value.
- [isLess(than:)](<isless(than_).md>) — Returns a Boolean value indicating whether this instance is less than the given value.
- [isLessThanOrEqualTo(_:)](<islessthanorequalto(__).md>) — Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [isTotallyOrdered(belowOrEqualTo:)](<istotallyordered(beloworequalto_).md>) — Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [negate()](<negate().md>) — Replaces this value with its additive inverse.
- [remainder(dividingBy:)](<remainder(dividingby_).md>) — Returns the remainder of this value divided by the given value.
- [round()](<round().md>)
- [round(_:)](<round(__).md>) — Rounds the value to an integral value using the specified rounding rule.
- [rounded()](<rounded().md>)
- [rounded(_:)](<rounded(__).md>) — Returns this value rounded to an integral value using the specified rounding rule.
- [squareRoot()](<squareroot().md>) — Returns the square root of the value, rounded to a representable value.
- [truncatingRemainder(dividingBy:)](<truncatingremainder(dividingby_).md>) — Returns the remainder of this value divided by the given value using truncating division.

### Type Aliases

- [Exponent](exponent-swift.typealias.md) — A type that can represent any written exponent.

### Type Properties

- [greatestFiniteMagnitude](greatestfinitemagnitude.md) — The greatest finite number representable by this type.
- [infinity](infinity.md) — Positive infinity.
- [leastNonzeroMagnitude](leastnonzeromagnitude.md) — The least positive number.
- [leastNormalMagnitude](leastnormalmagnitude.md) — The least positive normal number.
- [nan](nan.md) — A quiet NaN (“not a number”).
- [pi](pi.md) — The mathematical constant pi (π), approximately equal to 3.14159.
- [radix](radix.md) — The radix, or base of exponentiation, for a floating-point type.
- [signalingNaN](signalingnan.md) — A signaling NaN (“not a number”).
- [ulpOfOne](ulpofone.md) — The unit in the last place of 1.0.
- [ulpOfOne](ulpofone-1s81x.md) — The unit in the last place of 1.0.

### Type Methods

- [maximum(_:_:)](<maximum(____).md>) — Returns the greater of the two given values.
- [maximumMagnitude(_:_:)](<maximummagnitude(____).md>) — Returns the value with greater magnitude.
- [minimum(_:_:)](<minimum(____).md>) — Returns the lesser of the two given values.
- [minimumMagnitude(_:_:)](<minimummagnitude(____).md>) — Returns the value with lesser magnitude.
