---
title: language
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagscheme/language
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagscheme/language'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagscheme/language.json'
content_hash: 'sha256:bdabdbe9ef66ad00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagScheme](../nslinguistictagscheme.md)

# language

<sub>Type Property</sub>

Supplies the language for a token, if one can be determined.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let language: NSLinguisticTagScheme
```

## Discussion

Each value for this tag scheme is a BCP-47 language identifier. For example, the language identifier for English is “en” and the identifier for Chinese written using the Simplified Chinese script is “zh-Hans”. The identifier “und” is used if a specific language cannot be determined.

The tagger generally attempts to determine the language of text at the level of an entire sentence, paragraph, or document, rather than word by word.

## See Also

### Schemes

- [NSLinguisticTagSchemeTokenType](tokentype.md) — Classifies tokens according to their broad type:  word, punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeLexicalClass](lexicalclass.md) — Classifies tokens according to class:  part of speech, type of punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeNameType](nametype.md) — Classifies tokens according to whether they are part of a named entity. _(deprecated)_
- [NSLinguisticTagSchemeNameTypeOrLexicalClass](nametypeorlexicalclass.md) — Classifies tokens corresponding to names according to [NSLinguisticTagSchemeNameType](nametype.md), and classifies all other tokens according to [NSLinguisticTagSchemeLexicalClass](lexicalclass.md). _(deprecated)_
- [NSLinguisticTagSchemeLemma](lemma.md) — Supplies a stem form of a word token, if known. _(deprecated)_
- [NSLinguisticTagSchemeScript](script.md) — Supplies the script for a token, if one can be determined. _(deprecated)_
