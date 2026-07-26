---
title: lexicalClass
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagscheme/lexicalclass
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagscheme/lexicalclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagscheme/lexicalclass.json'
content_hash: 'sha256:c58242eaa9c64bf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagScheme](../nslinguistictagscheme.md)

# lexicalClass

<sub>Type Property</sub>

Classifies tokens according to class:  part of speech, type of punctuation, or whitespace.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let lexicalClass: NSLinguisticTagScheme
```

## Discussion

For possible values, see Lexical Classes.

The lexical class of a tag is a further distinction of its token type. Token types and lexical classes have the following correspondence:

| Token type | Lexical classes |
|---|---|
| [NSLinguisticTagWord](../nslinguistictag/word.md) | [NSLinguisticTagNoun](../nslinguistictag/noun.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagVerb](../nslinguistictag/verb.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagAdjective](../nslinguistictag/adjective.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagAdverb](../nslinguistictag/adverb.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagPronoun](../nslinguistictag/pronoun.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagDeterminer](../nslinguistictag/determiner.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagParticle](../nslinguistictag/particle.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagPreposition](../nslinguistictag/preposition.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagNumber](../nslinguistictag/number.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagConjunction](../nslinguistictag/conjunction.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagInterjection](../nslinguistictag/interjection.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagClassifier](../nslinguistictag/classifier.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagIdiom](../nslinguistictag/idiom.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagOtherWord](../nslinguistictag/otherword.md) |
| [NSLinguisticTagPunctuation](../nslinguistictag/punctuation.md) | [NSLinguisticTagSentenceTerminator](../nslinguistictag/sentenceterminator.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagOpenQuote](../nslinguistictag/openquote.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagCloseQuote](../nslinguistictag/closequote.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagOpenParenthesis](../nslinguistictag/openparenthesis.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagCloseParenthesis](../nslinguistictag/closeparenthesis.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagWordJoiner](../nslinguistictag/wordjoiner.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagDash](../nslinguistictag/dash.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagOtherPunctuation](../nslinguistictag/otherpunctuation.md) |
| [NSLinguisticTagWhitespace](../nslinguistictag/whitespace.md) | [NSLinguisticTagParagraphBreak](../nslinguistictag/paragraphbreak.md) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [NSLinguisticTagOtherWhitespace](../nslinguistictag/otherwhitespace.md) |
| [NSLinguisticTagOther](../nslinguistictag/other.md) | _None_ |

## See Also

### Schemes

- [NSLinguisticTagSchemeTokenType](tokentype.md) — Classifies tokens according to their broad type:  word, punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeNameType](nametype.md) — Classifies tokens according to whether they are part of a named entity. _(deprecated)_
- [NSLinguisticTagSchemeNameTypeOrLexicalClass](nametypeorlexicalclass.md) — Classifies tokens corresponding to names according to [NSLinguisticTagSchemeNameType](nametype.md), and classifies all other tokens according to [NSLinguisticTagSchemeLexicalClass](lexicalclass.md). _(deprecated)_
- [NSLinguisticTagSchemeLemma](lemma.md) — Supplies a stem form of a word token, if known. _(deprecated)_
- [NSLinguisticTagSchemeLanguage](language.md) — Supplies the language for a token, if one can be determined. _(deprecated)_
- [NSLinguisticTagSchemeScript](script.md) — Supplies the script for a token, if one can be determined. _(deprecated)_
