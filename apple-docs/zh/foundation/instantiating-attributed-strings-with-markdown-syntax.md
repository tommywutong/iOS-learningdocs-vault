---
title: 使用 Markdown 语法实例化属性字符串
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/instantiating-attributed-strings-with-markdown-syntax
source_url: 'https://developer.apple.com/documentation/foundation/instantiating-attributed-strings-with-markdown-syntax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/instantiating-attributed-strings-with-markdown-syntax.json'
content_hash: 'sha256:c2e35ebb30e8475d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [AttributedString](attributedstring.md)

# 使用 Markdown 语法实例化属性字符串

<sub>API 集合</sub>

使用 Markdown 语法字符串，以标准或自定义属性初始化一个属性字符串。

## 概述

你可以使用熟悉的 Markdown 语法来初始化一个属性字符串，同时指定其初始文本以及诸如行内样式和链接之类的属性。在许多情况下，这样产生的代码比手动在现有属性字符串的某些范围上设置属性更易读。

```swift
if let attString = try? AttributedString(
    markdown: "See the *latest* news at [our website](https://example.com)."),
    let websiteRange = attString.range(of: "our website"),
    let link = attString[websiteRange].link {
    print("\(link)") // Prints "https://example.com".
}
```

在这个示例中，`attString` 包含五个片段（run），其属性是从 `markdown` 参数中的语法解析而来：

- `“See the “`，没有属性。
- `“latest”`，带有一个 [InlinePresentationIntentAttribute](attributescopes/foundationattributes/inlinepresentationintentattribute.md)，其值为 [NSInlinePresentationIntentEmphasized](inlinepresentationintent/emphasized.md)。
- `“ news at “`，没有属性。
- `“our website”`，带有一个 [LinkAttribute](attributescopes/foundationattributes/linkattribute.md)，其值为一个 [URL](url.md)。
- `“.”`，没有属性。

你也可以在 Markdown 字符串中使用通过 [MarkdownDecodableAttributedStringKey](markdowndecodableattributedstringkey.md) 协议定义的自定义属性。为此，请使用 Apple 的 Markdown 扩展语法：`^[text](attribute1: value1, attribute2: value2, …)`。

在使用系统提供之外的属性时，请务必使用带有 `scope` 参数的初始化方法，并提供定义了这些自定义属性的作用域。

> [!tip] 提示
> 带有 `localized` 参数的 [AttributedString](attributedstring.md) 初始化方法同样可以使用 Markdown 语法。这些初始化方法允许你在 App 的字符串文件中使用 Markdown。

## 主题

### 从 Markdown 字符串初始化

- [init(markdown:options:baseURL:)](<attributedstring/init(markdown_options_baseurl_)-52n3u.md>) — 使用提供的选项，从一个 Markdown 格式的字符串创建一个属性字符串。
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-4m51b.md>) — 使用提供的选项和属性作用域，从一个 Markdown 格式的字符串创建一个属性字符串。
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-89e48.md>) — 使用提供的选项以及某个键路径所标识的属性作用域，从一个 Markdown 格式的字符串创建一个属性字符串。

### 从 Markdown 数据初始化

- [init(markdown:options:baseURL:)](<attributedstring/init(markdown_options_baseurl_)-2sg1o.md>) — 使用提供的选项，从 Markdown 格式的数据创建一个属性字符串。
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-4co46.md>) — 使用提供的选项和属性作用域，从 Markdown 格式的数据创建一个属性字符串。
- [init(markdown:including:options:baseURL:)](<attributedstring/init(markdown_including_options_baseurl_)-5nap7.md>) — 使用提供的选项以及某个键路径所标识的属性作用域，从 Markdown 格式的数据创建一个属性字符串。

### 从 URL 内容中使用 Markdown 初始化

- [init(contentsOf:options:baseURL:)](<attributedstring/init(contentsof_options_baseurl_).md>) — 使用提供的选项，从包含 Markdown 格式数据的指定 URL 的内容创建一个属性字符串。
- [init(contentsOf:including:options:baseURL:)](<attributedstring/init(contentsof_including_options_baseurl_)-1x6fz.md>) — 使用提供的选项和属性作用域，从包含 Markdown 格式数据的指定 URL 的内容创建一个属性字符串。
- [init(contentsOf:including:options:baseURL:)](<attributedstring/init(contentsof_including_options_baseurl_)-1fcpy.md>) — 使用提供的选项以及某个键路径所标识的属性作用域，从指定的 Markdown URL 的内容创建一个属性字符串。

### 指定 Markdown 解析选项

- [MarkdownParsingOptions](attributedstring/markdownparsingoptions.md) — 影响将 Markdown 内容解析为属性字符串的选项。
</content>
