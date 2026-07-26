---
title: FloatingPointSign
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointsign
source_url: 'https://developer.apple.com/documentation/swift/floatingpointsign'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointsign.json'
content_hash: 'sha256:76ddba672ca3e776'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# FloatingPointSign

<sub>Enumeration</sub>

The sign of a floating-point value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum FloatingPointSign
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [RawRepresentable](rawrepresentable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<floatingpointsign/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [FloatingPointSign.minus](floatingpointsign/minus.md) — The sign for a negative value.
- [FloatingPointSign.plus](floatingpointsign/plus.md) — The sign for a positive value.

### Initializers

- [init(rawValue:)](<floatingpointsign/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

### Instance Properties

- [hashValue](floatingpointsign/hashvalue.md) — The hash value.
- [rawValue](floatingpointsign/rawvalue-swift.property.md) — The corresponding value of the raw type.

### Instance Methods

- [hash(into:)](<floatingpointsign/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Aliases

- [RawValue](floatingpointsign/rawvalue-swift.typealias.md) — The raw type that can be used to represent all values of the conforming type.

### Default Implementations

- [Equatable Implementations](floatingpointsign/equatable-implementations.md)

## See Also

### Floating-Point Characteristics

- [FloatingPointClassification](floatingpointclassification.md) — The IEEE 754 floating-point classes.
- [FloatingPointRoundingRule](floatingpointroundingrule.md) — A rule for rounding a floating-point number.
