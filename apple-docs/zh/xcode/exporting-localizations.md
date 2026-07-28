---
title: 导出本地化
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/exporting-localizations
source_url: 'https://developer.apple.com/documentation/xcode/exporting-localizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/exporting-localizations.json'
content_hash: 'sha256:24c67383fbb6df00'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 导出本地化

<sub>文章</sub>

将项目中的可本地化文件提供给本地化人员。

## 概述

针对你准备支持的语言和地区，导出本地化。你可以从 Xcode 项目中导出所有需要本地化的文件，也可以仅导出特定本地化的文件。你也可以向导出的文件夹中添加文件，以提供上下文，然后将这些文件交给本地化人员。

### 使用 Xcode 导出本地化

在项目导航器中，选择项目，然后选取“产品”>“导出本地化”。在出现的对话框中，输入文件夹名称，选择位置，选择本地化语言，然后点击“导出”。

![导出本地化表单的截图，你可以在其中输入文件夹名称并选择本地化语言。](../../../attachments/4620465e0438b0d81ea1d2bd241250e3/exporting-localizations-1@2x.png)

> [!important] 重要
> 要在导出中包含所有可本地化的文本，请为你的项目启用 [Use Compiler to Extract Swift Strings](https://developer.apple.com/documentation/xcode/build-settings-reference#Use-Compiler-to-Extract-Swift-Strings) 构建设置。该设置仅影响 Swift 字符串。Objective-C 字符串提取无需任何额外构建设置即可工作。

如果在测试本地化时生成了屏幕快照，请点击“包含屏幕快照”，将特定于本地化的屏幕快照包含在导出文件中的 `Notes` 文件夹中，从而为本地化人员提供上下文。要过滤屏幕快照，请点击“自定”，取消选择你不希望包含的屏幕快照，然后点击“完成”。

Xcode 会创建一个 Xcode 本地化目录（Xcode Localization Catalog，即一个文件扩展名为 `.xcloc` 的文件夹），其中包含每种语言和地区的可本地化资源。你可以在 Xcode 中打开并编辑此文件，也可以使用任何支持此文件类型的第三方工具。Xcode 为你管理 App 中的可本地化字符串，方式如下：

- 从以下文件类型中提取字符串：源代码、storyboard、XIB、`.strings`、`.stringsdict` 和 Siri 意图定义。将提取的字符串添加到一个标准的 XML 本地化交换文件格式（XLIFF）中，该格式对本地化人员来说很熟悉。
- 为每种导出的语言，将正确的 `.stringsdict` 复数变体添加到 XLIFF 文件中。
- 为信息属性列表文件中可本地化的属性创建一个字符串文件。
- 将所有可本地化的资源复制到 `Source Contents` 文件夹中，以向本地化人员提供上下文。

Xcode 会提取你传递给 [Text](../swiftui/text.md) 结构体、[NSLocalizedString](../foundation/nslocalizedstring.md) 宏（macro）以及代码中类似 API 的字符串。例如，如果你将带有注释的字符串传递给 [NSLocalizedString](../foundation/nslocalizedstring.md) 宏，Xcode 会将注释包含在 XLIFF 文件中。

此外，目录中的每个本地化文件夹仅包含你标记为可本地化的资源和素材资源。在本地化之前，该文件是开发语言文件的副本——一个为本地化人员提供上下文的占位文件。

### 向 Xcode 本地化目录添加文件

在将目录交给本地化人员之前，你可以向 `Notes` 文件夹添加更多文件以提供更多上下文。Xcode 本地化目录文件夹包含：

| 项目 | 描述 |
|---|---|
| `contents.json` | 一个 JSON 文件，包含有关目录的元数据，例如开发区域（development region）、语言区域（locale）、工具（Xcode）及其版本号、目录版本号。 |
| `Localized Contents` | 一个包含可本地化资源的文件夹，包括一个包含可本地化字符串的 XLIFF 文件。 |
| `Notes` | 一个包含供本地化人员使用的额外信息的文件夹，例如屏幕快照、影片或文本文件。 |
| `Source Contents` | 一个包含用于生成内容的素材资源的文件夹，该内容为本地化人员提供上下文，例如用户界面文件和其他资源。 |

### 使用命令导出本地化

你也可以使用 `xcodebuild` 命令和 `-exportLocalizations` 参数来导出本地化文件：

`xcodebuild -exportLocalizations -project <projectname> -localizationPath <dirpath> [[-exportLanguage <targetlanguage>] ...]`

要在上述命令中包含测试本地化时生成的屏幕快照，请添加 `-includeScreenshots` 参数。

## 另请参阅

### 翻译与适配

- [为本地化人员创建 App 屏幕快照](creating-screenshots-of-your-app-for-localizers.md) —— 与本地化人员共享 App 的屏幕快照，为翻译提供上下文。
- [编辑 XLIFF 和字符串目录文件](editing-xliff-and-string-catalog-files.md) —— 为你从项目中导出的语言和地区翻译或适配可本地化文件。
- [导入本地化](importing-localizations.md) —— 将你为某个语言和地区翻译或适配的文件导入到你的项目中。
- [在 storyboard 和 XIB 文件中锁定视图](locking-views-in-storyboard-and-xib-files.md) —— 在对面向用户的字符串进行本地化时，防止对你的 Interface Builder 文件进行更改。
