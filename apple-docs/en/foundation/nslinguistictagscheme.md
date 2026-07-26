---
title: NSLinguisticTagScheme
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslinguistictagscheme
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagscheme.json'
content_hash: 'sha256:3c9ddf8f5e85376d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLinguisticTagScheme

<sub>Structure</sub>

Constants for the tag schemes specified when initializing a linguistic tagger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSLinguisticTagScheme
```

## Discussion

When initializing a linguistic tagger with [- initWithTagSchemes:options:](<nslinguistictagger/init(tagschemes_options_).md>), you specify one or more tag schemes that correspond to the kind of information you’re interested in for a selection of natural language text. To ensure optimal performance, avoid specifying tag schemes that you won’t use.

Some tag schemes are only available for certain units and languages. Use the [+ availableTagSchemesForUnit:language:](<nslinguistictagger/availabletagschemes(for_language_).md>) or [+ availableTagSchemesForLanguage:](<nslinguistictagger/availabletagschemes(forlanguage_).md>) methods to determine the possible values for a specified language and linguistic unit.

When working with linguistic tags using the methods described in Getting Linguistic Tags and Enumerating Linguistic Tags, the returned tag value depends on the specified scheme. For example, given the token “Überraschung”, the returned tag is [NSLinguisticTagNoun](nslinguistictag/noun.md) when using the [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) tag scheme, “de” (German language) when using the [NSLinguisticTagSchemeLanguage](nslinguistictagscheme/language.md) tag scheme, and “Latn” (Latin script) when using the [NSLinguisticTagSchemeScript](nslinguistictagscheme/script.md) tag scheme, as shown in the following code.

```swift
let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass, .language, .script], options: 0)
tagger.string = "Überraschung"

tagger.tag(at: 0, unit: .word, scheme: .lexicalClass, tokenRange: nil) // Noun
tagger.tag(at: 0, unit: .word, scheme: .language, tokenRange: nil) // de
tagger.tag(at: 0, unit: .word, scheme: .script, tokenRange: nil) // Latn
```

The following table lists the available tag schemes, their applicable linguistic units, and possible tag values.

| Linguistic tag scheme | Applicable linguistic units | Possible tag values |
|---|---|---|
| [NSLinguisticTagSchemeTokenType](nslinguistictagscheme/tokentype.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) | See Token Types |
| [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) | See Lexical Classes |
| [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) | See Name Types |
| [NSLinguisticTagSchemeNameTypeOrLexicalClass](nslinguistictagscheme/nametypeorlexicalclass.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) | See Name Types and Lexical Classes |
| [NSLinguisticTagSchemeLemma](nslinguistictagscheme/lemma.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) | A stem of the word |
| [NSLinguisticTagSchemeLanguage](nslinguistictagscheme/language.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md), [NSLinguisticTaggerUnitSentence](nslinguistictaggerunit/sentence.md), [NSLinguisticTaggerUnitParagraph](nslinguistictaggerunit/paragraph.md), [NSLinguisticTaggerUnitDocument](nslinguistictaggerunit/document.md) | A BCP-47 language tag |
| [NSLinguisticTagSchemeScript](nslinguistictagscheme/script.md) | [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md), [NSLinguisticTaggerUnitSentence](nslinguistictaggerunit/sentence.md), [NSLinguisticTaggerUnitParagraph](nslinguistictaggerunit/paragraph.md), [NSLinguisticTaggerUnitDocument](nslinguistictaggerunit/document.md) | An ISO 15924 script code |

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Schemes

- [NSLinguisticTagSchemeTokenType](nslinguistictagscheme/tokentype.md) — Classifies tokens according to their broad type:  word, punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) — Classifies tokens according to class:  part of speech, type of punctuation, or whitespace. _(deprecated)_
- [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) — Classifies tokens according to whether they are part of a named entity. _(deprecated)_
- [NSLinguisticTagSchemeNameTypeOrLexicalClass](nslinguistictagscheme/nametypeorlexicalclass.md) — Classifies tokens corresponding to names according to [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md), and classifies all other tokens according to [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md). _(deprecated)_
- [NSLinguisticTagSchemeLemma](nslinguistictagscheme/lemma.md) — Supplies a stem form of a word token, if known. _(deprecated)_
- [NSLinguisticTagSchemeLanguage](nslinguistictagscheme/language.md) — Supplies the language for a token, if one can be determined. _(deprecated)_
- [NSLinguisticTagSchemeScript](nslinguistictagscheme/script.md) — Supplies the script for a token, if one can be determined. _(deprecated)_

### Initializers

- [init(_:)](<nslinguistictagscheme/init(__).md>)
- [init(rawValue:)](<nslinguistictagscheme/init(rawvalue_).md>)

## See Also

### Supporting Types

- [NSLinguisticTaggerUnit](nslinguistictaggerunit.md) — Constants representing linguistic units.
- [NSLinguisticTag](nslinguistictag.md) — A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.
