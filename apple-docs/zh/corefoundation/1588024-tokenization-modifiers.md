---
title: 分词修饰符
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
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFStringTokenizer](cfstringtokenizer.md)

# 分词修饰符

<sub>API 集合</sub>

分词选项与 [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 一起使用，以指定应对字符串如何分词

## 概述

你将分词单位选项与 [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 一起使用，以指定应对字符串如何分词。

你将修饰符与分词单位一起使用，以修改字符串的分词方式。

你使用属性说明符告诉分词器在对给定字符串分词时准备指定的属性。你可以通过调用 [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) 并传入某个属性选项来检索属性值。

分词单位选项对区域设置（locale）的敏感性可能在未来版本中发生变化。

## 主题

### 常量

- [kCFStringTokenizerUnitWord](kcfstringtokenizerunitword.md) — 指定应按词对字符串分词。[CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 的 `locale` 参数会被忽略。
- [kCFStringTokenizerUnitSentence](kcfstringtokenizerunitsentence.md) — 指定应按句对字符串分词。[CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 的 `locale` 参数会被忽略。
- [kCFStringTokenizerUnitParagraph](kcfstringtokenizerunitparagraph.md) — 指定应按段落对字符串分词。[CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 的 `locale` 参数会被忽略。
- [kCFStringTokenizerUnitLineBreak](kcfstringtokenizerunitlinebreak.md) — 指定应按换行对字符串分词。[CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) 的 `locale` 参数会被忽略。
- [kCFStringTokenizerUnitWordBoundary](kcfstringtokenizerunitwordboundary.md) — 指定应按与区域设置相关的词边界对字符串分词。
- [kCFStringTokenizerAttributeLatinTranscription](kcfstringtokenizerattributelatintranscription.md) — 与 `kCFStringTokenizerUnitWord` 一起使用，告诉分词器在对字符串分词时准备拉丁转写。
- [kCFStringTokenizerAttributeLanguage](kcfstringtokenizerattributelanguage.md) — 告诉分词器在对字符串分词时准备语言（以 RFC 3066bis 字符串形式指定）。

## 另请参阅

### 常量

- [CFStringTokenizerTokenType](cfstringtokenizertokentype.md) — 由 [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) 和 [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>) 返回的词元类型。
