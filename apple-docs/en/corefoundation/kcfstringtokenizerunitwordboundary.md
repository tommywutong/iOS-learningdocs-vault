---
title: kCFStringTokenizerUnitWordBoundary
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstringtokenizerunitwordboundary
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstringtokenizerunitwordboundary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstringtokenizerunitwordboundary.json'
content_hash: 'sha256:b983cb08e389fc49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStringTokenizerUnitWordBoundary

<sub>Global Variable</sub>

Specifies that a string should be tokenized by locale-sensitive word boundary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFStringTokenizerUnitWordBoundary: CFOptionFlags { get }
```

## Discussion

You can use this constant in double-click range detection and whole word search. It is locale-sensitive. If the locale is `en_US_POSIX`, a colon (U+003A) is treated as a word separator. If the `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is `NULL`, the locale from the global `AppleTextBreakLocale` preference is used if it is available; otherwise the locale defaults to the first locale in `AppleLanguages`.

`kCFStringTokenizerUnitWordBoundary` also returns space between words as a token.

## See Also

### Constants

- [kCFStringTokenizerUnitWord](kcfstringtokenizerunitword.md) — Specifies that a string should be tokenized by word. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — Specifies that a string should be tokenized by sentence. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md) — Specifies that a string should be tokenized by paragraph. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — Specifies that a string should be tokenized by line break. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [kCFStringTokenizerAttributeLanguage](kcfstringtokenizerattributelanguage.md) — Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.
