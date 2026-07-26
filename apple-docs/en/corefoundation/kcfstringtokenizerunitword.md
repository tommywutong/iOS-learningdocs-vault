---
title: kCFStringTokenizerUnitWord
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstringtokenizerunitword
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstringtokenizerunitword.json'
content_hash: 'sha256:45a83ad80bea7493'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStringTokenizerUnitWord

<sub>Global Variable</sub>

Specifies that a string should be tokenized by word. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFStringTokenizerUnitWord: CFOptionFlags { get }
```

## See Also

### Constants

- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — Specifies that a string should be tokenized by sentence. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md) — Specifies that a string should be tokenized by paragraph. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — Specifies that a string should be tokenized by line break. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitWordBoundary](kcfstringtokenizerunitwordboundary.md) — Specifies that a string should be tokenized by locale-sensitive word boundary.
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [kCFStringTokenizerAttributeLanguage](kcfstringtokenizerattributelanguage.md) — Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.
