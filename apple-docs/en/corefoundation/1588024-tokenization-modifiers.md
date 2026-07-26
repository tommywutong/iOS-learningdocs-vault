---
title: Tokenization Modifiers
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1588024-tokenization-modifiers
source_url: 'https://developer.apple.com/documentation/corefoundation/1588024-tokenization-modifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1588024-tokenization-modifiers.json'
content_hash: 'sha256:bcb53bf3c5662853'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStringTokenizer](cfstringtokenizer.md)

# Tokenization Modifiers

<sub>API Collection</sub>

Tokenization options are used with [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) to specify how the string should be tokenized

## Overview

You use the tokenization unit options with [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) to specify how a string should be tokenized.

You use the modifiers together with a tokenization unit to modify the way the string is tokenized.

You use the attribute specifiers to tell the tokenizer to prepare the specified attribute when it tokenizes the given string. You can retrieve the attribute value by calling [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) with one of the attribute options.

The locale sensitivity of the tokenization unit options may change in a future release.

## Topics

### Constants

- [kCFStringTokenizerUnitWord](kcfstringtokenizerunitword.md) — Specifies that a string should be tokenized by word. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — Specifies that a string should be tokenized by sentence. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md) — Specifies that a string should be tokenized by paragraph. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — Specifies that a string should be tokenized by line break. The `locale` parameter of [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) is ignored.
- [kCFStringTokenizerUnitWordBoundary](kcfstringtokenizerunitwordboundary.md) — Specifies that a string should be tokenized by locale-sensitive word boundary.
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — Used with `kCFStringTokenizerUnitWord`, tells the tokenizer to prepare the Latin transcription when it tokenizes the string.
- [kCFStringTokenizerAttributeLanguage](kcfstringtokenizerattributelanguage.md) — Tells the tokenizer to prepare the language (specified as an RFC 3066bis string) when it tokenizes the string.

## See Also

### Constants

- [CFStringTokenizerTokenType](cfstringtokenizertokentype.md) — Token types returned by [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) and [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>).
