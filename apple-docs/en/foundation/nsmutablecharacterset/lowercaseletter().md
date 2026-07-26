---
title: lowercaseLetter()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablecharacterset/lowercaseletter()
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset/lowercaseletter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset/lowercaseletter%28%29.json'
content_hash: 'sha256:a5c86d32c45d8830'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableCharacterSet](../nsmutablecharacterset.md)

# lowercaseLetter()

<sub>Type Method</sub>

Returns a character set containing the characters in Unicode General Category Ll.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func lowercaseLetter() -> NSMutableCharacterSet
```

## See Also

### Getting Standard Character Sets

- [+ alphanumericCharacterSet](<alphanumeric().md>) — Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [+ capitalizedLetterCharacterSet](<capitalizedletter().md>) — Returns a character set containing the characters in Unicode General Category Lt.
- [+ controlCharacterSet](<control().md>) — Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [+ decimalDigitCharacterSet](<decimaldigit().md>) — Returns a character set containing the characters in the category of decimal numbers.
- [+ decomposableCharacterSet](<decomposable().md>) — Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [+ illegalCharacterSet](<illegal().md>) — Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [+ letterCharacterSet](<letter().md>) — Returns a character set containing the characters in Unicode General Category L* & M*.
- [+ newlineCharacterSet](<newline().md>) — Returns a character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [+ nonBaseCharacterSet](<nonbase().md>) — Returns a character set containing the characters in Unicode General Category M*.
- [+ punctuationCharacterSet](<punctuation().md>) — Returns a character set containing the characters in Unicode General Category P*.
- [+ symbolCharacterSet](<symbol().md>) — Returns a character set containing the characters in Unicode General Category S*.
- [+ uppercaseLetterCharacterSet](<uppercaseletter().md>) — Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [+ whitespaceAndNewlineCharacterSet](<whitespaceandnewline().md>) — Returns a character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [+ whitespaceCharacterSet](<whitespace().md>) — Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).
