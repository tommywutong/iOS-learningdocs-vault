---
title: RegexBuilder
framework: RegexBuilder
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder
source_url: 'https://developer.apple.com/documentation/regexbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder.json'
content_hash: 'sha256:fa20ae80e04c9f12'
translated: true
---

> 导航：[Technologies](technologies.md)

# RegexBuilder

<sub>框架</sub>

使用富有表现力的领域特定语言构建正则表达式，用于文本中的搜索和替换等操作。

## 概述

正则表达式（也称为 regex）是在文本中匹配模式的强大工具。Swift 支持多种创建正则表达式的方式，包括通过字符串、作为字面量，以及使用这个 DSL。例如：

```swift
let word = OneOrMore(.word)
let emailPattern = Regex {
    Capture {
        ZeroOrMore {
            word
            "."
        }
        word
    }
    "@"
    Capture {
        word
        OneOrMore {
            "."
            word
        }
    }
}

let text = "My email is my.name@example.com."
if let match = text.firstMatch(of: emailPattern) {
    let (wholeMatch, name, domain) = match.output
    // wholeMatch is "my.name@example.com"
    // name is "my.name"
    // domain is "example.com"
}
```

## 主题

### Components

- [CharacterClass](regexbuilder/characterclass.md) — 在正则表达式中匹配的一类字符。
- [Anchor](regexbuilder/anchor.md) — 在输入字符串中特定位置匹配特定条件的正则表达式组件。
- [Lookahead](regexbuilder/lookahead.md) — 一种正则表达式组件，只有当其内容在给定位置匹配时才允许匹配继续。
- [NegativeLookahead](regexbuilder/negativelookahead.md) — 一种正则表达式组件，只有当其内容在给定位置不匹配时才允许匹配继续。
- [ChoiceOf](regexbuilder/choiceof.md) — 一种正则表达式组件，在匹配时从其组成的正则表达式组件中恰好选择一个。

### Quantifiers

- [One](regexbuilder/one.md) — 恰好匹配其底层组件一次出现的正则表达式组件。
- [Optionally](regexbuilder/optionally.md) — 匹配其底层组件零次或一次出现的正则表达式组件。
- [ZeroOrMore](regexbuilder/zeroormore.md) — 匹配其底层组件零次或多次出现的正则表达式组件。
- [OneOrMore](regexbuilder/oneormore.md) — 匹配其底层组件一次或多次出现的正则表达式组件。
- [Repeat](regexbuilder/repeat.md) — 匹配其底层组件可选定次数出现的正则表达式组件。
- [Local](regexbuilder/local.md) — 表示原子组的正则表达式组件。

### Captures

- [Capture](regexbuilder/capture.md) — 一种正则表达式组件，用于保存匹配的子字符串或转换后的结果，以便在正则表达式匹配中访问。
- [TryCapture](regexbuilder/trycapture.md) — 一种正则表达式组件，尝试转换匹配的子字符串，如果成功则保存结果，如果转换失败则回溯。
- [Reference](regexbuilder/reference.md) — 对正则表达式中被捕获部分的引用。

### Builders

- [RegexComponentBuilder](regexbuilder/regexcomponentbuilder.md) — 一种自定参数属性，用于从闭包构建正则表达式。
- [AlternationBuilder](regexbuilder/alternationbuilder.md) — 一种自定参数属性，用于从闭包构建正则表达式的多选项。

### 运算符

- [...(_:_:)](<regexbuilder/'...(____)-16g2a.md>) — 返回一个包含给定范围内字符的字符类。
- [...(_:_:)](<regexbuilder/'...(____)-629xh.md>) — 返回一个包含给定范围内 Unicode 标量的字符类。
