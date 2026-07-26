---
title: Unicode.NumericType
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/numerictype
source_url: 'https://developer.apple.com/documentation/swift/unicode/numerictype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/numerictype.json'
content_hash: 'sha256:9c7e670131a3645f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.NumericType

<sub>Enumeration</sub>

The numeric type of a scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NumericType
```

## Overview

Scalars with a non-nil numeric type include numbers, fractions, numeric superscripts and subscripts, and circled or otherwise decorated number glyphs.

Some letterlike scalars used in numeric systems, such as Greek or Latin letters, do not have a non-nil numeric type, in order to prevent programs from incorrectly interpreting them as numbers in non-numeric contexts.

## Relationships

- **Conforms To**: [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<numerictype/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [Unicode.NumericType.decimal](numerictype/decimal.md) — A digit that is commonly understood to form base-10 numbers.
- [Unicode.NumericType.digit](numerictype/digit.md) — A digit that does not meet the requirements of the `decimal` numeric type.
- [Unicode.NumericType.numeric](numerictype/numeric.md) — A digit that does not meet the requirements of the `decimal` numeric type or a non-digit numeric value.

### Instance Properties

- [hashValue](numerictype/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<numerictype/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Default Implementations

- [Equatable Implementations](numerictype/equatable-implementations.md)

## See Also

### Unicode Scalar Classifications

- [GeneralCategory](generalcategory.md) — The most general classification of a Unicode scalar.
- [CanonicalCombiningClass](canonicalcombiningclass.md) — The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.
