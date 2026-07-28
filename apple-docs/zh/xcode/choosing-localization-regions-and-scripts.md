---
title: 选择本地化区域与书写系统
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/choosing-localization-regions-and-scripts
source_url: 'https://developer.apple.com/documentation/xcode/choosing-localization-regions-and-scripts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/choosing-localization-regions-and-scripts.json'
content_hash: 'sha256:ab0d479ec296a4d6'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 选择本地化区域与书写系统

<sub>文章</sub>

添加仅语言的本地化（localization），或针对区域变体与特定书写系统的本地化。

## 概述

当你本地化你的 App 时，通过选择一种语言，然后（可选）从 Xcode 菜单中选取一个区域和书写系统来添加本地化。Apple 建议你选择最具体的本地化，而不仅仅是语言。例如，如果你只支持英语且是美式英语，请选择 English (United States) (en-US) 而不是 English (en)。

在 Xcode 菜单中，你为本地化选择一个人类可读的名称，但在项目文件和导出的文件中，本地化人员理解的语言标识符（language identifier）指定了语言、区域和书写系统。Xcode 本地化目录（一个带有 `.xcloc` 文件扩展名的文件夹）使用语言标识符作为后缀，例如 `en.xcloc` 和 `de.xcloc` 分别对应英语和德语的目录名称。

有关 `Bundle` 对象如何在你 App 支持的本地化与用户的语言和区域设置之间找到最佳匹配的信息，请参阅 [Bundle](../foundation/bundle.md)。

### 了解语言标识符

**语言标识符**（language identifier）是一种复合语法，表示语言、区域变体和书写系统的组合。它包含一个语言代码（language code），以及可选的区域代码（region code）和书写系统代码（script code）。

对于在许多区域使用的语言，只需使用表示该语言的**语言代码**（language code）（`[language code]`）。例如，要指定塞尔维亚语，请使用 `sr` 语言代码。使用两个字母的 ISO 639-1 标准（首选），或者如果特定语言没有可用的代码，则使用 ISO 639-2 标准。

为了区分不同的语言和区域变体，请使用带有区域代码的语言代码，之间用连字符分隔（`[language code]-[region code]`）。**区域代码**（region code）表示国家或区域。使用 ISO 3166-1 标准，这是一个两个字母的大写代码，例如 `US`、`GB`、`AU` 和 `FR`。例如，要指定德语的瑞士变体，请使用 `de-CH`。如果无法使用 ISO 3166-1 标准创建语言标识符，请使用联合国 M.49 标准，这是一个数字代码。

要指定书写系统，请将语言代码与 ISO 3166-1 标准中的**书写系统代码**（script code）结合，之间用连字符分隔（`[language code]-[script code]`），例如 `az-Cyrl` 表示使用西里尔字母的阿塞拜疆语。要表示在台湾使用的、用繁体中文书写的中文，请使用 `zh-Hant-TW`。

此表展示了一些常见语言标识符及其语言、区域和书写系统代码：

| 语法 | 描述 | 示例 |
|---|---|---|
| [language code] | 仅指定语言 | `en` 表示英语 |
|  |  | `fr` 表示法语 |
|  |  | `de` 表示德语 |
| [language code]-[region code] | 指定语言的区域变体 | `en-AU` 表示在澳大利亚使用的英语 |
|  |  | `en-GB` 表示在英国使用的英语 |
|  |  | `fr-FR` 表示在法国使用的法语 |
|  |  | `fr-CA` 表示在加拿大使用的法语 |
|  |  | `de-AT` 表示在奥地利使用的德语 |
|  |  | `de-CH` 表示在瑞士使用的德语 |
| [language code]-[script code] | 指定语言的书写系统 | `az-Cyrl` 表示使用西里尔字母的阿塞拜疆语 |
|  |  | `sr-Latn` 表示使用拉丁字母的塞尔维亚语 |
|  |  | `uz-Cyrl` 表示使用西里尔字母的乌兹别克语 |
|  |  | `zh-Hans` 表示使用简体中文的中文 |
|  |  | `zh-Hant` 表示使用繁体中文的中文 |

## 另请参阅

### 语言与区域

- [为语言与区域添加支持](adding-support-for-languages-and-regions.md) — 为你支持的每种语言和区域选择要本地化的资源。
