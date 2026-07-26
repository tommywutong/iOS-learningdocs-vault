---
title: illegalCharacters
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/illegalcharacters
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/illegalcharacters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/illegalcharacters.json'
content_hash: 'sha256:077a009f4d96584c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# illegalCharacters

<sub>Type Property</sub>

A character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var illegalCharacters: CharacterSet { get }
```

## Return Value

A character set containing all the illegal characters.

## See Also

### Getting Standard Character Sets

- [alphanumericCharacterSet](alphanumerics.md) — A character set containing the characters in Unicode General Categories L*, M*, and N*.
- [capitalizedLetterCharacterSet](capitalizedletters.md) — A character set containing the characters in Unicode General Category Lt.
- [controlCharacterSet](controlcharacters.md) — A character set containing the characters in Unicode General Category Cc and Cf.
- [decimalDigitCharacterSet](decimaldigits.md) — A character set containing the characters in the category of Decimal Numbers.
- [decomposableCharacterSet](decomposables.md) — A character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [letterCharacterSet](letters.md) — A character set containing the characters in Unicode General Category L* & M*.
- [lowercaseLetterCharacterSet](lowercaseletters.md) — A character set containing the characters in Unicode General Category Ll.
- [newlineCharacterSet](newlines.md) — A character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [nonBaseCharacterSet](nonbasecharacters.md) — A character set containing the characters in Unicode General Category M*.
- [punctuationCharacterSet](punctuationcharacters.md) — A character set containing the characters in Unicode General Category P*.
- [symbolCharacterSet](symbols.md) — A character set containing the characters in Unicode General Category S*.
- [uppercaseLetterCharacterSet](uppercaseletters.md) — A character set containing the characters in Unicode General Category Lu and Lt.
- [whitespaceAndNewlineCharacterSet](whitespacesandnewlines.md) — A character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [whitespaceCharacterSet](whitespaces.md) — A character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).
