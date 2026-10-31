---
title: 对自然语言文本进行分词
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/tokenizing-natural-language-text
source_url: 'https://developer.apple.com/documentation/foundation/tokenizing-natural-language-text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/tokenizing-natural-language-text.json'
content_hash: 'sha256:373b3611f20a5861'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSLinguisticTagger](nslinguistictagger.md)

# 对自然语言文本进行分词

<sub>文章</sub>

枚举字符串中的单词。

## 概述

处理自然语言文本时，将文本分词成单个单词通常很有用。使用 [NSLinguisticTagger](nslinguistictagger.md) 枚举单词，而不是简单地按空白拆分组成部分，可以确保在多种文字和语言中行为正确。例如，中文和日语都不使用空格来分隔单词。

下面的示例和配套步骤展示如何使用 [NSLinguisticTagger](nslinguistictagger.md) 枚举自然语言文本中的单词。

```swift
let text = """
All human beings are born free and equal in dignity and rights.
They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood.
"""

let tagger = NSLinguisticTagger(tagSchemes: [.tokenType], options: 0)
tagger.string = text

let range = NSRange(location: 0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: range, unit: .word, scheme: .tokenType, options: options) { _, tokenRange, _ in
    let word = (text as NSString).substring(with: tokenRange)
    print(word)
}
```

1. 创建一个 [NSLinguisticTagger](nslinguistictagger.md) 实例，并将 [NSLinguisticTagSchemeTokenType](nslinguistictagscheme/tokentype.md) 指定为要使用的标签方案。
2. 将语言标记器的 [string](nslinguistictagger/string.md) 属性设置为自然语言文本。
3. 通过调用 [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) 方法枚举字符串的整个范围，将 [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) 指定为标签单元、[NSLinguisticTagSchemeTokenType](nslinguistictagscheme/tokentype.md) 指定为要枚举的标签方案，并省略任何标点或空白。
4. 在枚举块中，获取原始文本在 `tokenRange` 处的子字符串，以获得每个单词。
5. 运行这段代码，将 `text` 中的每个单词打印在新的一行上。

## 另请参阅

### 相关文档

- [Identifying Parts of Speech](identifying-parts-of-speech.md) — 对字符串中的名词、动词、形容词及其他词性进行分类。
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md) — 使用语言标注器对字符串执行命名实体识别。

### 第一步

- [- initWithTagSchemes:options:](<nslinguistictagger/init(tagschemes_options_).md>) — 使用指定的标签方案和选项创建语言标记器实例。_(已废弃)_
- [string](nslinguistictagger/string.md) — 语言标记器正在分析的字符串。_(已废弃)_
