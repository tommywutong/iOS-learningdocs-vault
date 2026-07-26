---
title: nameType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagscheme/nametype
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagscheme/nametype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagscheme/nametype.json'
content_hash: 'sha256:4d12972c906c1cee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagScheme](../nslinguistictagscheme.md)

# nameType

<sub>Type Property</sub>

Classifies tokens according to whether they are part of a named entity.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let nameType: NSLinguisticTagScheme
```

## Discussion

For possible values, see Name Types.

## See Also

### Schemes

- [NSLinguisticTagSchemeTokenType](tokentype.md) — Classifies tokens according to their broad type:  word, punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeLexicalClass](lexicalclass.md) — Classifies tokens according to class:  part of speech, type of punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeNameTypeOrLexicalClass](nametypeorlexicalclass.md) — Classifies tokens corresponding to names according to [NSLinguisticTagSchemeNameType](nametype.md), and classifies all other tokens according to [NSLinguisticTagSchemeLexicalClass](lexicalclass.md). _(deprecated)_
- [NSLinguisticTagSchemeLemma](lemma.md) — Supplies a stem form of a word token, if known. _(deprecated)_
- [NSLinguisticTagSchemeLanguage](language.md) — Supplies the language for a token, if one can be determined. _(deprecated)_
- [NSLinguisticTagSchemeScript](script.md) — Supplies the script for a token, if one can be determined. _(deprecated)_
