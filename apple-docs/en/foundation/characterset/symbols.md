---
title: symbols
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/characterset/symbols
source_url: 'https://developer.apple.com/documentation/foundation/characterset/symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/symbols.json'
content_hash: 'sha256:c66401209e8d7c94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# symbols

<sub>Type Property</sub>

Returns a character set containing the characters in Unicode General Category S*.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var symbols: CharacterSet { get }
```

## See Also

### Getting Standard Character Sets

- [alphanumerics](alphanumerics.md) — Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [capitalizedLetters](capitalizedletters.md) — Returns a character set containing the characters in Unicode General Category Lt.
- [controlCharacters](controlcharacters.md) — Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [decimalDigits](decimaldigits.md) — Returns a character set containing the characters in the category of Decimal Numbers.
- [decomposables](decomposables.md) — Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [illegalCharacters](illegalcharacters.md) — Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [letters](letters.md) — Returns a character set containing the characters in Unicode General Category L* & M*.
- [lowercaseLetters](lowercaseletters.md) — Returns a character set containing the characters in Unicode General Category Ll.
- [newlines](newlines.md) — Returns a character set containing the newline characters (`U+000A ~ U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [nonBaseCharacters](nonbasecharacters.md) — Returns a character set containing the characters in Unicode General Category M*.
- [punctuationCharacters](punctuationcharacters.md) — Returns a character set containing the characters in Unicode General Category P*.
- [uppercaseLetters](uppercaseletters.md) — Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [whitespaces](whitespaces.md) — Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION (U+0009)`.
- [whitespacesAndNewlines](whitespacesandnewlines.md) — Returns a character set containing characters in Unicode General Category Z*, `U+000A ~ U+000D`, and `U+0085`.
