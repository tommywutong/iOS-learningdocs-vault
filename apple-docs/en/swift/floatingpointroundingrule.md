---
title: FloatingPointRoundingRule
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpointroundingrule
source_url: 'https://developer.apple.com/documentation/swift/floatingpointroundingrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpointroundingrule.json'
content_hash: 'sha256:acdd200bcbe04266'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# FloatingPointRoundingRule

<sub>Enumeration</sub>

A rule for rounding a floating-point number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum FloatingPointRoundingRule
```

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<floatingpointroundingrule/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [FloatingPointRoundingRule.awayFromZero](floatingpointroundingrule/awayfromzero.md) — Round to the closest allowed value whose magnitude is greater than or equal to that of the source.
- [FloatingPointRoundingRule.down](floatingpointroundingrule/down.md) — Round to the closest allowed value that is less than or equal to the source.
- [FloatingPointRoundingRule.toNearestOrAwayFromZero](floatingpointroundingrule/tonearestorawayfromzero.md) — Round to the closest allowed value; if two values are equally close, the one with greater magnitude is chosen.
- [FloatingPointRoundingRule.toNearestOrEven](floatingpointroundingrule/tonearestoreven.md) — Round to the closest allowed value; if two values are equally close, the even one is chosen.
- [FloatingPointRoundingRule.towardZero](floatingpointroundingrule/towardzero.md) — Round to the closest allowed value whose magnitude is less than or equal to that of the source.
- [FloatingPointRoundingRule.up](floatingpointroundingrule/up.md) — Round to the closest allowed value that is greater than or equal to the source.

### Instance Properties

- [hashValue](floatingpointroundingrule/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<floatingpointroundingrule/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Default Implementations

- [Equatable Implementations](floatingpointroundingrule/equatable-implementations.md)

## See Also

### Floating-Point Characteristics

- [FloatingPointClassification](floatingpointclassification.md) — The IEEE 754 floating-point classes.
- [FloatingPointSign](floatingpointsign.md) — The sign of a floating-point value.
