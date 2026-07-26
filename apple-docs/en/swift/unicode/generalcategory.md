---
title: Unicode.GeneralCategory
framework: Swift
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/generalcategory
source_url: 'https://developer.apple.com/documentation/swift/unicode/generalcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/generalcategory.json'
content_hash: 'sha256:40c93407c2994cf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.GeneralCategory

<sub>Enumeration</sub>

The most general classification of a Unicode scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum GeneralCategory
```

## Overview

The general category of a scalar is its “first-order, most usual categorization”. It does not attempt to cover multiple uses of some scalars, such as the use of letters to represent Roman numerals.

## Relationships

- **Conforms To**: [Equatable](../equatable.md), [Hashable](../hashable.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<generalcategory/==(____).md>) — Returns a Boolean value indicating whether two values are equal.

### Enumeration Cases

- [Unicode.GeneralCategory.closePunctuation](generalcategory/closepunctuation.md) — A closing punctuation mark of a pair.
- [Unicode.GeneralCategory.connectorPunctuation](generalcategory/connectorpunctuation.md) — A connecting punctuation mark, like a tie.
- [Unicode.GeneralCategory.control](generalcategory/control.md) — A C0 or C1 control code.
- [Unicode.GeneralCategory.currencySymbol](generalcategory/currencysymbol.md) — A currency sign.
- [Unicode.GeneralCategory.dashPunctuation](generalcategory/dashpunctuation.md) — A dash or hyphen punctuation mark.
- [Unicode.GeneralCategory.decimalNumber](generalcategory/decimalnumber.md) — A decimal digit.
- [Unicode.GeneralCategory.enclosingMark](generalcategory/enclosingmark.md) — An enclosing combining mark.
- [Unicode.GeneralCategory.finalPunctuation](generalcategory/finalpunctuation.md) — A final quotation mark.
- [Unicode.GeneralCategory.format](generalcategory/format.md) — A format control character.
- [Unicode.GeneralCategory.initialPunctuation](generalcategory/initialpunctuation.md) — An initial quotation mark.
- [Unicode.GeneralCategory.letterNumber](generalcategory/letternumber.md) — A letter-like numeric character.
- [Unicode.GeneralCategory.lineSeparator](generalcategory/lineseparator.md) — A line separator, which is specifically (and only) U+2028 LINE SEPARATOR.
- [Unicode.GeneralCategory.lowercaseLetter](generalcategory/lowercaseletter.md) — A lowercase letter.
- [Unicode.GeneralCategory.mathSymbol](generalcategory/mathsymbol.md) — A symbol of mathematical use.
- [Unicode.GeneralCategory.modifierLetter](generalcategory/modifierletter.md) — A modifier letter.
- [Unicode.GeneralCategory.modifierSymbol](generalcategory/modifiersymbol.md) — A non-letterlike modifier symbol.
- [Unicode.GeneralCategory.nonspacingMark](generalcategory/nonspacingmark.md) — A non-spacing combining mark with zero advance width (abbreviated Mn).
- [Unicode.GeneralCategory.openPunctuation](generalcategory/openpunctuation.md) — An opening punctuation mark of a pair.
- [Unicode.GeneralCategory.otherLetter](generalcategory/otherletter.md) — Other letters, including syllables and ideographs.
- [Unicode.GeneralCategory.otherNumber](generalcategory/othernumber.md) — A numeric character of another type.
- [Unicode.GeneralCategory.otherPunctuation](generalcategory/otherpunctuation.md) — A punctuation mark of another type.
- [Unicode.GeneralCategory.otherSymbol](generalcategory/othersymbol.md) — A symbol of another type.
- [Unicode.GeneralCategory.paragraphSeparator](generalcategory/paragraphseparator.md) — A paragraph separator, which is specifically (and only) U+2029 PARAGRAPH SEPARATOR.
- [Unicode.GeneralCategory.privateUse](generalcategory/privateuse.md) — A private-use character.
- [Unicode.GeneralCategory.spaceSeparator](generalcategory/spaceseparator.md) — A space character of non-zero width.
- [Unicode.GeneralCategory.spacingMark](generalcategory/spacingmark.md) — A spacing combining mark with positive advance width.
- [Unicode.GeneralCategory.surrogate](generalcategory/surrogate.md) — A surrogate code point.
- [Unicode.GeneralCategory.titlecaseLetter](generalcategory/titlecaseletter.md) — A digraph character whose first part is uppercase.
- [Unicode.GeneralCategory.unassigned](generalcategory/unassigned.md) — A reserved unassigned code point or a non-character.
- [Unicode.GeneralCategory.uppercaseLetter](generalcategory/uppercaseletter.md) — An uppercase letter.

### Instance Properties

- [hashValue](generalcategory/hashvalue.md) — The hash value.

### Instance Methods

- [hash(into:)](<generalcategory/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Default Implementations

- [Equatable Implementations](generalcategory/equatable-implementations.md)

## See Also

### Unicode Scalar Classifications

- [CanonicalCombiningClass](canonicalcombiningclass.md) — The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.
- [NumericType](numerictype.md) — The numeric type of a scalar.
