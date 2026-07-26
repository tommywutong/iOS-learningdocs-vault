---
title: Locale.Script
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/script
source_url: 'https://developer.apple.com/documentation/foundation/locale/script'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/script.json'
content_hash: 'sha256:b39c957950a7470e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Script

<sub>Structure</sub>

The written script used with a given language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Script
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a script

- [init(_:)](<script/init(__).md>) — Creates a script from a BCP 47 identifier.
- [init(stringLiteral:)](<script/init(stringliteral_).md>) — Creates a script from a BCP 47 identifier as a string literal.

### Examining script properties

- [identifier](script/identifier.md)

### Using defined scripts

- [unknown](script/unknown.md) — Represents an uncoded script

### Instance Properties

- [isISOScript](script/isisoscript.md) — Returns if the script is an ISO 15924 script

### Type Properties

- [adlam](script/adlam.md)
- [arabic](script/arabic.md)
- [arabicNastaliq](script/arabicnastaliq.md)
- [armenian](script/armenian.md)
- [bangla](script/bangla.md)
- [cherokee](script/cherokee.md)
- [cyrillic](script/cyrillic.md)
- [devanagari](script/devanagari.md)
- [ethiopic](script/ethiopic.md)
- [georgian](script/georgian.md)
- [greek](script/greek.md)
- [gujarati](script/gujarati.md)
- [gurmukhi](script/gurmukhi.md)
- [hanSimplified](script/hansimplified.md)
- [hanTraditional](script/hantraditional.md)
- [hanifiRohingya](script/hanifirohingya.md)
- [hebrew](script/hebrew.md)
- [hiragana](script/hiragana.md)
- [japanese](script/japanese.md)
- [kannada](script/kannada.md)
- [katakana](script/katakana.md)
- [khmer](script/khmer.md)
- [korean](script/korean.md)
- [lao](script/lao.md)
- [latin](script/latin.md)
- [malayalam](script/malayalam.md)
- [meiteiMayek](script/meiteimayek.md)
- [myanmar](script/myanmar.md)
- [odia](script/odia.md)
- [olChiki](script/olchiki.md)
- [sinhala](script/sinhala.md)
- [syriac](script/syriac.md)
- [tamil](script/tamil.md)
- [telugu](script/telugu.md)
- [thaana](script/thaana.md)
- [thai](script/thai.md)
- [tibetan](script/tibetan.md)

## See Also

### Examining language properties

- [languageCode](language-swift.struct/languagecode.md) — The language code that identifies the language.
- [LanguageCode](languagecode-swift.struct.md) — An alphabetical code associated with a language.
- [region](language-swift.struct/region.md) — The region used with the language.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [script](language-swift.struct/script.md) — The written script of the language.
- [characterDirection](language-swift.struct/characterdirection.md) — The ordering of characters within a line.
- [LanguageDirection](languagedirection.md) — An alias for the standard set of language directions.
