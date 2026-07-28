---
title: 语法分析详细信息
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/grammatical-analysis-details
source_url: 'https://developer.apple.com/documentation/foundation/grammatical-analysis-details'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/grammatical-analysis-details.json'
content_hash: 'sha256:820aa312edee8d68'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSSpellServer](nsspellserver.md)

# 语法分析详细信息

<sub>API 集合</sub>

这些常量用作 [NSSpellServer](nsspellserver.md) 和 [checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)](<../appkit/nsspellchecker/checkgrammar(of_startingat_language_wrap_inspelldocumentwithtag_details_).md>)（[NSSpellChecker](../appkit/nsspellchecker.md)）返回的 outDetails 字典中的键。

## 主题

### 常量

- [NSGrammarRange](nsgrammarrange.md) — `NSGrammarRange` 字典键的值应是一个包含 `NSRange` 的 `NSValue`。该范围是用作返回值的句子范围的子范围，其位置应为相对于句子开头的偏移量。例如，表示整个句子范围中前四个字符的 `NSGrammarRange` 应为 `{0, 4}`。如果字典中不存在 `NSGrammarRange` 键，则系统假定它等于整个句子范围。
- [NSGrammarUserDescription](nsgrammaruserdescription.md) — `NSGrammarUserDescription` 字典键的值应是一个 `NSString`，其中包含有关该范围的描述性文本，以直接呈现给用户；用户描述应提供足够的信息，让用户能够纠正问题。建议始终提供 `NSGrammarUserDescription`，但若要向用户呈现纠正指导，必须提供 `NSGrammarUserDescription` 或 `NSGrammarCorrections`。
- [NSGrammarCorrections](nsgrammarcorrections.md) — `NSGrammarCorrections` 键的值应是一个由多个 `NSString` 组成的 `NSArray`，表示可用于纠正问题的替代内容，但并非所有情况下都能提供这些内容。若要向用户呈现纠正指导，必须提供 `NSGrammarUserDescription` 或 `NSGrammarCorrections`。
