---
title: 识别词性
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/identifying-parts-of-speech
source_url: 'https://developer.apple.com/documentation/foundation/identifying-parts-of-speech'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/identifying-parts-of-speech.json'
content_hash: 'sha256:a376c9f52a3bbae4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSLinguisticTagger](nslinguistictagger.md)

# 识别词性

<sub>文章</sub>

对字符串中的名词、动词、形容词及其他词性进行分类。

## 概述

识别自然语言文本中各个单词的词性，可以帮助你的程序理解句子的含义。例如，给定用户所说请求的转录文本，你可能只需查看其中的名词和动词就能确定大致意图。

下面的示例展示了如何使用 [NSLinguisticTagger](nslinguistictagger.md) 来枚举自然语言文本，并识别每个单词的词性。

```swift
let text = "The ripe taste of cheese improves with age."
let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
tagger.string = text
let range = NSRange(location: 0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
    if let tag = tag {
        let word = (text as NSString).substring(with: tokenRange)
        print("\(word): \(tag)")
    }
}
```

首先，创建一个 [NSLinguisticTagger](nslinguistictagger.md) 实例，并指定使用 [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) 作为标注方案。接着，将语言标注器的 [string](nslinguistictagger/string.md) 属性设置为该自然语言文本。最后，语言标注器在整个字符串范围内进行枚举，指定 [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) 作为标注单元、[NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) 作为标注方案，并省略任何标点符号或空白字符。在枚举代码块中，词性由 `tag` 提供，每个单词则通过在 `tokenRange` 处截取原始文本的子串获得。

运行后，这段代码会将每个单词及其词性逐行输出，如下所示：

| 单词 | 词性 |
|---|---|
| The | [NSLinguisticTagDeterminer](nslinguistictag/determiner.md) |
| ripe | [NSLinguisticTagAdjective](nslinguistictag/adjective.md) |
| taste | [NSLinguisticTagNoun](nslinguistictag/noun.md) |
| of | [NSLinguisticTagPreposition](nslinguistictag/preposition.md) |
| cheese | [NSLinguisticTagNoun](nslinguistictag/noun.md) |
| improves | [NSLinguisticTagVerb](nslinguistictag/verb.md) |
| with | [NSLinguisticTagPreposition](nslinguistictag/preposition.md) |
| age | [NSLinguisticTagNoun](nslinguistictag/noun.md) |

## 另请参阅

### 相关文档

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md) — 枚举字符串中的单词。

### 枚举语言标注

- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md) — 使用语言标注器对字符串执行命名实体识别。
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) — 在字符串的给定范围内按特定单元进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_scheme_options_using_).md>) — 在字符串的给定范围内进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<nslinguistictagger/enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — 在给定字符串上进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [Options](nslinguistictagger/options.md) — 用于语言标注器枚举的常量，指定要省略哪些标记以及是否合并姓名。
</content>
