---
title: Locale.LanguageCode
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/languagecode-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/languagecode-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/languagecode-swift.struct.json'
content_hash: 'sha256:23c36c91c7922099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.LanguageCode

<sub>Structure</sub>

An alphabetical code associated with a language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LanguageCode
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a language code

- [init(_:)](<languagecode-swift.struct/init(__).md>) — Creates a language code from an identifier.
- [init(stringLiteral:)](<languagecode-swift.struct/init(stringliteral_).md>) — Creates a language code from an identifier as a string literal.

### Examining language code properties

- [identifier](languagecode-swift.struct/identifier.md) — The identifier used to create the language code.
- [isISOLanguage](languagecode-swift.struct/isisolanguage.md) — A Boolean value that indicates whether this language code is in the list of ISO-defined languages.

### Using ISO-defined language codes

- [isoLanguageCodes](languagecode-swift.struct/isolanguagecodes.md) — Returns an array of ISO-defined language codes.

### Instance Methods

- [identifier(_:)](<languagecode-swift.struct/identifier(__).md>) — Returns the ISO code of the given identifier type. Returns nil if the language isn’t a valid ISO language, or if the specified identifier type isn’t available to the language.

### Type Properties

- [ainu](languagecode-swift.struct/ainu.md)
- [albanian](languagecode-swift.struct/albanian.md)
- [amharic](languagecode-swift.struct/amharic.md)
- [apacheWestern](languagecode-swift.struct/apachewestern.md)
- [arabic](languagecode-swift.struct/arabic.md)
- [armenian](languagecode-swift.struct/armenian.md)
- [assamese](languagecode-swift.struct/assamese.md)
- [assyrian](languagecode-swift.struct/assyrian.md)
- [azerbaijani](languagecode-swift.struct/azerbaijani.md)
- [bangla](languagecode-swift.struct/bangla.md)
- [belarusian](languagecode-swift.struct/belarusian.md)
- [bodo](languagecode-swift.struct/bodo.md)
- [bulgarian](languagecode-swift.struct/bulgarian.md)
- [burmese](languagecode-swift.struct/burmese.md)
- [cantonese](languagecode-swift.struct/cantonese.md)
- [catalan](languagecode-swift.struct/catalan.md)
- [cherokee](languagecode-swift.struct/cherokee.md)
- [chinese](languagecode-swift.struct/chinese.md)
- [croatian](languagecode-swift.struct/croatian.md)
- [czech](languagecode-swift.struct/czech.md)
- [danish](languagecode-swift.struct/danish.md)
- [dhivehi](languagecode-swift.struct/dhivehi.md)
- [dogri](languagecode-swift.struct/dogri.md)
- [dutch](languagecode-swift.struct/dutch.md)
- [dzongkha](languagecode-swift.struct/dzongkha.md)
- [english](languagecode-swift.struct/english.md)
- [estonian](languagecode-swift.struct/estonian.md)
- [faroese](languagecode-swift.struct/faroese.md)
- [finnish](languagecode-swift.struct/finnish.md)
- [french](languagecode-swift.struct/french.md)
- [fula](languagecode-swift.struct/fula.md)
- [georgian](languagecode-swift.struct/georgian.md)
- [german](languagecode-swift.struct/german.md)
- [greek](languagecode-swift.struct/greek.md)
- [gujarati](languagecode-swift.struct/gujarati.md)
- [hawaiian](languagecode-swift.struct/hawaiian.md)
- [hebrew](languagecode-swift.struct/hebrew.md)
- [hindi](languagecode-swift.struct/hindi.md)
- [hungarian](languagecode-swift.struct/hungarian.md)
- [icelandic](languagecode-swift.struct/icelandic.md)
- [igbo](languagecode-swift.struct/igbo.md)
- [indonesian](languagecode-swift.struct/indonesian.md)
- [irish](languagecode-swift.struct/irish.md)
- [italian](languagecode-swift.struct/italian.md)
- [japanese](languagecode-swift.struct/japanese.md)
- [kannada](languagecode-swift.struct/kannada.md)
- [kashmiri](languagecode-swift.struct/kashmiri.md)
- [kazakh](languagecode-swift.struct/kazakh.md)
- [khmer](languagecode-swift.struct/khmer.md)
- [konkani](languagecode-swift.struct/konkani.md)
- [korean](languagecode-swift.struct/korean.md)
- [kurdish](languagecode-swift.struct/kurdish.md)
- [kurdishSorani](languagecode-swift.struct/kurdishsorani.md)
- [kyrgyz](languagecode-swift.struct/kyrgyz.md)
- [lao](languagecode-swift.struct/lao.md)
- [latvian](languagecode-swift.struct/latvian.md)
- [lithuanian](languagecode-swift.struct/lithuanian.md)
- [māori](languagecode-swift.struct/m_ori.md)
- [macedonian](languagecode-swift.struct/macedonian.md)
- [maithili](languagecode-swift.struct/maithili.md)
- [malay](languagecode-swift.struct/malay.md)
- [malayalam](languagecode-swift.struct/malayalam.md)
- [maltese](languagecode-swift.struct/maltese.md)
- [manipuri](languagecode-swift.struct/manipuri.md)
- [marathi](languagecode-swift.struct/marathi.md)
- [mongolian](languagecode-swift.struct/mongolian.md)
- [multiple](languagecode-swift.struct/multiple.md) — The `mul` code: represents the language of some content when there are more than one languages
- [navajo](languagecode-swift.struct/navajo.md)
- [nepali](languagecode-swift.struct/nepali.md)
- [norwegian](languagecode-swift.struct/norwegian.md)
- [norwegianBokmål](languagecode-swift.struct/norwegianbokm_l.md)
- [norwegianNynorsk](languagecode-swift.struct/norwegiannynorsk.md)
- [odia](languagecode-swift.struct/odia.md)
- [pashto](languagecode-swift.struct/pashto.md)
- [persian](languagecode-swift.struct/persian.md)
- [polish](languagecode-swift.struct/polish.md)
- [portuguese](languagecode-swift.struct/portuguese.md)
- [punjabi](languagecode-swift.struct/punjabi.md)
- [rohingya](languagecode-swift.struct/rohingya.md)
- [romanian](languagecode-swift.struct/romanian.md)
- [russian](languagecode-swift.struct/russian.md)
- [samoan](languagecode-swift.struct/samoan.md)
- [sanskrit](languagecode-swift.struct/sanskrit.md)
- [santali](languagecode-swift.struct/santali.md)
- [serbian](languagecode-swift.struct/serbian.md)
- [sindhi](languagecode-swift.struct/sindhi.md)
- [sinhala](languagecode-swift.struct/sinhala.md)
- [slovak](languagecode-swift.struct/slovak.md)
- [slovenian](languagecode-swift.struct/slovenian.md)
- [spanish](languagecode-swift.struct/spanish.md)
- [swahili](languagecode-swift.struct/swahili.md)
- [swedish](languagecode-swift.struct/swedish.md)
- [tagalog](languagecode-swift.struct/tagalog.md)
- [tajik](languagecode-swift.struct/tajik.md)
- [tamil](languagecode-swift.struct/tamil.md)
- [telugu](languagecode-swift.struct/telugu.md)
- [thai](languagecode-swift.struct/thai.md)
- [tibetan](languagecode-swift.struct/tibetan.md)
- [tongan](languagecode-swift.struct/tongan.md)
- [turkish](languagecode-swift.struct/turkish.md)
- [turkmen](languagecode-swift.struct/turkmen.md)
- [ukrainian](languagecode-swift.struct/ukrainian.md)
- [unavailable](languagecode-swift.struct/unavailable.md) — The `zxx` code: used in cases when the content is not in any particular languages, such as images, symbols, etc.
- [uncoded](languagecode-swift.struct/uncoded.md) — The `mis` code: represents languages that have not been included in the ISO standard yet
- [unidentified](languagecode-swift.struct/unidentified.md) — The `und` code: used in cases where the language has not been identified
- [urdu](languagecode-swift.struct/urdu.md)
- [uyghur](languagecode-swift.struct/uyghur.md)
- [uzbek](languagecode-swift.struct/uzbek.md)
- [vietnamese](languagecode-swift.struct/vietnamese.md)
- [welsh](languagecode-swift.struct/welsh.md)
- [yiddish](languagecode-swift.struct/yiddish.md)

### Enumerations

- [IdentifierType](languagecode-swift.struct/identifiertype.md) — Types of ISO 639 language code.

## See Also

### Examining language properties

- [languageCode](language-swift.struct/languagecode.md) — The language code that identifies the language.
- [region](language-swift.struct/region.md) — The region used with the language.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [script](language-swift.struct/script.md) — The written script of the language.
- [Script](script.md) — The written script used with a given language.
- [characterDirection](language-swift.struct/characterdirection.md) — The ordering of characters within a line.
- [LanguageDirection](languagedirection.md) — An alias for the standard set of language directions.
