---
title: kCFStringTokenizerAttributeLanguage
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstringtokenizerattributelanguage
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerattributelanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstringtokenizerattributelanguage.json'
content_hash: 'sha256:af8a3a036533eda5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStringTokenizerAttributeLanguage

<sub>Global Variable</sub>

Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFStringTokenizerAttributeLanguage: CFOptionFlags { get }
```

## Discussion

Used with [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) or [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md).

## See Also

### Constants

- [kCFStringTokenizerUnitWord](kcfstringtokenizerunitword.md) — Specifies that a string should be tokenized by word. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — Specifies that a string should be tokenized by sentence. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md) — Specifies that a string should be tokenized by paragraph. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — Specifies that a string should be tokenized by line break. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitWordBoundary](kcfstringtokenizerunitwordboundary.md) — Specifies that a string should be tokenized by locale-sensitive word boundary.
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
