---
title: kCFStringTokenizerUnitParagraph
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstringtokenizerunitparagraph
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitparagraph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstringtokenizerunitparagraph.json'
content_hash: 'sha256:99031a3d8be3edd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStringTokenizerUnitParagraph

<sub>Global Variable</sub>

Specifies that a string should be tokenized by paragraph. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFStringTokenizerUnitParagraph: CFOptionFlags { get }
```

## See Also

### Constants

- [kCFStringTokenizerUnitWord](kcfstringtokenizerunitword.md) — Specifies that a string should be tokenized by word. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — Specifies that a string should be tokenized by sentence. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — Specifies that a string should be tokenized by line break. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitWordBoundary](kcfstringtokenizerunitwordboundary.md) — Specifies that a string should be tokenized by locale-sensitive word boundary.
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [kCFStringTokenizerAttributeLanguage](kcfstringtokenizerattributelanguage.md) — Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.
