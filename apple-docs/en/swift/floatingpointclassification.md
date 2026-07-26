---
title: FloatingPointClassification
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointclassification
source_url: 'https://developer.apple.com/documentation/swift/floatingpointclassification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointclassification.json'
content_hash: 'sha256:1bca2cad46cafdb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# FloatingPointClassification

<sub>Enumeration</sub>

The IEEE 754 floating-point classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum FloatingPointClassification
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<floatingpointclassification/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [FloatingPointClassification.negativeInfinity](floatingpointclassification/negativeinfinity.md) — A value equal to `-infinity`.
- [FloatingPointClassification.negativeNormal](floatingpointclassification/negativenormal.md) — A negative value that uses the full precision of the floating-point type.
- [FloatingPointClassification.negativeSubnormal](floatingpointclassification/negativesubnormal.md) — A negative, nonzero number that does not use the full precision of the floating-point type.
- [FloatingPointClassification.negativeZero](floatingpointclassification/negativezero.md) — A value equal to zero with a negative sign.
- [FloatingPointClassification.positiveInfinity](floatingpointclassification/positiveinfinity.md) — A value equal to `+infinity`.
- [FloatingPointClassification.positiveNormal](floatingpointclassification/positivenormal.md) — A positive value that uses the full precision of the floating-point type.
- [FloatingPointClassification.positiveSubnormal](floatingpointclassification/positivesubnormal.md) — A positive, nonzero number that does not use the full precision of the floating-point type.
- [FloatingPointClassification.positiveZero](floatingpointclassification/positivezero.md) — A value equal to zero with a positive sign.
- [FloatingPointClassification.quietNaN](floatingpointclassification/quietnan.md) — A silent NaN (“not a number”) value.
- [FloatingPointClassification.signalingNaN](floatingpointclassification/signalingnan.md) — A signaling NaN (“not a number”).

### Instance Properties

- [hashValue](floatingpointclassification/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<floatingpointclassification/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Default Implementations

- [Equatable Implementations](floatingpointclassification/equatable-implementations.md)

## See Also

### Floating-Point Characteristics

- [FloatingPointRoundingRule](floatingpointroundingrule.md) — A rule for rounding a floating-point number.
- [FloatingPointSign](floatingpointsign.md) — The sign of a floating-point value.
