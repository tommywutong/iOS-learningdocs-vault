---
title: 识别人物、地点和组织
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/identifying-people-places-and-organizations
source_url: 'https://developer.apple.com/documentation/foundation/identifying-people-places-and-organizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/identifying-people-places-and-organizations.json'
content_hash: 'sha256:30085566a539f1d5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSLinguisticTagger](nslinguistictagger.md)

# 识别人物、地点和组织

<sub>文章</sub>

使用语言标注器对字符串执行命名实体识别。

## 概述

识别自然语言文本中的命名实体，可以让你的 App 变得更智能。例如，一款消息应用可能会在文本中查找人物和地点的名称，以便显示相关信息，如联系人信息或路线指引。

下面的示例展示了如何使用 [NSLinguisticTagger](nslinguistictagger.md) 来枚举自然语言文本，并识别其中任何命名的人物、地点或组织。

```swift
let text = "The American Red Cross was established in Washington, D.C., by Clara Barton."
let tagger = NSLinguisticTagger(tagSchemes: [.nameType], options: 0)
tagger.string = text
let range = NSRange(location:0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace, .joinNames]
let tags: [NSLinguisticTag] = [.personalName, .placeName, .organizationName]
tagger.enumerateTags(in: range, unit: .word, scheme: .nameType, options: options) { tag, tokenRange, stop in
    if let tag = tag, tags.contains(tag) {
        let name = (text as NSString).substring(with: tokenRange)
        print("\(name): \(tag)")
    }
}
```

首先，创建一个 [NSLinguisticTagger](nslinguistictagger.md) 实例，并指定使用 [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) 作为标注方案。接着，将语言标注器的 [string](nslinguistictagger/string.md) 属性设置为该自然语言文本。最后，语言标注器在整个字符串范围内进行枚举，指定 [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) 作为标注单元、[NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) 作为标注方案，省略任何标点符号或空白字符，并将属于同一个名称的多个单词合并为同一个标记。在枚举代码块中，名称类型由 `tag` 提供，每个单词则通过在 `tokenRange` 处截取原始文本的子串获得。

运行后，这段代码会将每个名称及其类型逐行输出，如下所示：

| 名称 | 类型 |
|---|---|
| The American Red Cross | [NSLinguisticTagOrganizationName](nslinguistictag/organizationname.md) |
| Washington, D.C. | [NSLinguisticTagPlaceName](nslinguistictag/placename.md) |
| Clara Barton | [NSLinguisticTagPersonalName](nslinguistictag/personalname.md) |

## 另请参阅

### 相关文档

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md) — 枚举字符串中的单词。

### 枚举语言标注

- [Identifying Parts of Speech](identifying-parts-of-speech.md) — 对字符串中的名词、动词、形容词及其他词性进行分类。
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) — 在字符串的给定范围内按特定单元进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_scheme_options_using_).md>) — 在字符串的给定范围内进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<nslinguistictagger/enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — 在给定字符串上进行枚举，并为每个标注调用指定的代码块。_(已废弃)_
- [Options](nslinguistictagger/options.md) — 用于语言标注器枚举的常量，指定要省略哪些标记以及是否合并姓名。
</content>
