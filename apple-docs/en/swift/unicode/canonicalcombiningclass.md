---
title: Unicode.CanonicalCombiningClass
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/canonicalcombiningclass
source_url: 'https://developer.apple.com/documentation/swift/unicode/canonicalcombiningclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/canonicalcombiningclass.json'
content_hash: 'sha256:ae00d7b9a78a8055'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.CanonicalCombiningClass

<sub>Structure</sub>

The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CanonicalCombiningClass
```

## Overview

Canonical combining classes are used by the ordering algorithm to determine if two sequences of combining marks should be considered canonically equivalent (that is, identical in interpretation). Two sequences are canonically equivalent if they are equal when sorting the scalars in ascending order by their combining class.

For example, consider the sequence `"\u{0041}\u{0301}\u{0316}"` (LATIN CAPITAL LETTER A, COMBINING ACUTE ACCENT, COMBINING GRAVE ACCENT BELOW). The combining classes of these scalars have the numeric values 0, 230, and 220, respectively. Sorting these scalars by their combining classes yields `"\u{0041}\u{0316}\u{0301}"`, so two strings that differ only by the ordering of those scalars would compare as equal:

```swift
let aboveBeforeBelow = "\u{0041}\u{0301}\u{0316}"
let belowBeforeAbove = "\u{0041}\u{0316}\u{0301}"
print(aboveBeforeBelow == belowBeforeAbove)
// Prints "true"
```

## Named and Unnamed Combining Classes

Canonical combining classes are defined in the Unicode Standard as integers in the range `0...254`. For convenience, the standard assigns symbolic names to a subset of these combining classes.

The `CanonicalCombiningClass` type conforms to `RawRepresentable` with a raw value of type `UInt8`. You can create instances of the type by using the static members named after the symbolic names, or by using the `init(rawValue:)` initializer.

```swift
let overlayClass = Unicode.CanonicalCombiningClass(rawValue: 1)
let overlayClassIsOverlay = overlayClass == .overlay
// overlayClassIsOverlay == true
```

## Relationships

- **Conforms To**: [Comparable](../comparable.md), [Equatable](../equatable.md), [Hashable](../hashable.md), [RawRepresentable](../rawrepresentable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<canonicalcombiningclass/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [\<(_:_:)](<canonicalcombiningclass/_(____).md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

### Initializers

- [init(rawValue:)](<canonicalcombiningclass/init(rawvalue_).md>) — Creates a new canonical combining class with the given raw integer value.

### Instance Properties

- [hashValue](canonicalcombiningclass/hashvalue.md) — The hash value.
- [rawValue](canonicalcombiningclass/rawvalue-swift.property.md) — The raw integer value of the canonical combining class.

### Instance Methods

- [hash(into:)](<canonicalcombiningclass/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Type Aliases

- [RawValue](canonicalcombiningclass/rawvalue-swift.typealias.md) — The raw type that can be used to represent all values of the conforming type.

### Type Properties

- [above](canonicalcombiningclass/above.md) — Distinct marks directly above.
- [aboveLeft](canonicalcombiningclass/aboveleft.md) — Distinct marks at the top left.
- [aboveRight](canonicalcombiningclass/aboveright.md) — Distinct marks at the top right.
- [attachedAbove](canonicalcombiningclass/attachedabove.md) — Marks attached directly above.
- [attachedAboveRight](canonicalcombiningclass/attachedaboveright.md) — Marks attached at the top right.
- [attachedBelow](canonicalcombiningclass/attachedbelow.md) — Marks attached directly below.
- [attachedBelowLeft](canonicalcombiningclass/attachedbelowleft.md) — Marks attached at the bottom left.
- [below](canonicalcombiningclass/below.md) — Distinct marks directly below.
- [belowLeft](canonicalcombiningclass/belowleft.md) — Distinct marks at the bottom left.
- [belowRight](canonicalcombiningclass/belowright.md) — Distinct marks at the bottom right.
- [doubleAbove](canonicalcombiningclass/doubleabove.md) — Distinct marks extending above two bases.
- [doubleBelow](canonicalcombiningclass/doublebelow.md) — Distinct marks subtending two bases.
- [iotaSubscript](canonicalcombiningclass/iotasubscript.md) — Greek iota subscript only (U+0345 COMBINING GREEK YPOGEGRAMMENI).
- [kanaVoicing](canonicalcombiningclass/kanavoicing.md) — Combining marks that are attached to hiragana and katakana to indicate voicing changes.
- [left](canonicalcombiningclass/left.md) — Distinct marks to the left.
- [notReordered](canonicalcombiningclass/notreordered.md) — Base glyphs that occupy their own space and do not combine with others.
- [nukta](canonicalcombiningclass/nukta.md) — Diacritic nukta marks in Brahmi-derived scripts.
- [overlay](canonicalcombiningclass/overlay.md) — Marks that overlay a base letter or symbol.
- [right](canonicalcombiningclass/right.md) — Distinct marks to the right.
- [virama](canonicalcombiningclass/virama.md) — Diacritic virama marks in Brahmi-derived scripts.

### Default Implementations

- [Comparable Implementations](canonicalcombiningclass/comparable-implementations.md)
- [Equatable Implementations](canonicalcombiningclass/equatable-implementations.md)

## See Also

### Unicode Scalar Classifications

- [GeneralCategory](generalcategory.md) — The most general classification of a Unicode scalar.
- [NumericType](numerictype.md) — The numeric type of a scalar.
