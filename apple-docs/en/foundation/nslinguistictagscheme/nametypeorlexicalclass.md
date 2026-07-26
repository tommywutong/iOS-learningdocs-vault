---
title: nameTypeOrLexicalClass
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagscheme/nametypeorlexicalclass
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagscheme/nametypeorlexicalclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagscheme/nametypeorlexicalclass.json'
content_hash: 'sha256:a3d090990c962030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagScheme](../nslinguistictagscheme.md)

# nameTypeOrLexicalClass

<sub>Type Property</sub>

Classifies tokens corresponding to names according to [NSLinguisticTagSchemeNameType](nametype.md), and classifies all other tokens according to [NSLinguisticTagSchemeLexicalClass](lexicalclass.md).

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let nameTypeOrLexicalClass: NSLinguisticTagScheme
```

## Discussion

For possible values, see Name Types and Lexical Classes.

## See Also

### Schemes

- [NSLinguisticTagSchemeTokenType](tokentype.md) — Classifies tokens according to their broad type:  word, punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeLexicalClass](lexicalclass.md) — Classifies tokens according to class:  part of speech, type of punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeNameType](nametype.md) — Classifies tokens according to whether they are part of a named entity. _(deprecated)_
- [NSLinguisticTagSchemeLemma](lemma.md) — Supplies a stem form of a word token, if known. _(deprecated)_
- [NSLinguisticTagSchemeLanguage](language.md) — Supplies the language for a token, if one can be determined. _(deprecated)_
- [NSLinguisticTagSchemeScript](script.md) — Supplies the script for a token, if one can be determined. _(deprecated)_
