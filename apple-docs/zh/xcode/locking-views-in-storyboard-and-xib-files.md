---
title: 锁定 Storyboard 和 XIB 文件中的视图
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/locking-views-in-storyboard-and-xib-files
source_url: 'https://developer.apple.com/documentation/xcode/locking-views-in-storyboard-and-xib-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/locking-views-in-storyboard-and-xib-files.json'
content_hash: 'sha256:65fb578b6a8552e0'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 锁定 Storyboard 和 XIB 文件中的视图

<sub>文章</sub>

在本地化面向用户的字符串时，防止 Interface Builder 文件发生更改。

## 概述

导出本地化内容之前，可以选择锁定 Storyboard 和 XIB 文件中的视图，以免在等待翻译时无意中更改可本地化的属性。如果你希望继续开发 App，并避免稍后导入本地化内容时发生冲突，请使用此功能。你可以选择锁定级别，控制每个视图中可编辑的属性集合。

### 锁定视图

你可以为单个视图或整个用户界面文件设置锁定级别。默认情况下，视图会从其父视图继承锁定特性（lock attribute），而顶层视图会从用户界面文件继承锁定特性。如果设置某个视图的锁定特性，该设置会应用于它的所有后代视图。

要锁定单个视图，请在 Project 导览器中选择用户界面文件（文件扩展名为 `.storyboard` 或 `.xib`），然后在 Interface Builder 中选择该视图。在 Identity 检查器中，从 Document 下的 Lock 弹出式菜单选择一个锁定级别：

- **Inherited - ([locking level])** — 使用父视图的锁定级别。
- **Nothing** — 不锁定任何属性（所有属性均可编辑）。
- **All Properties** — 锁定所有属性。
- **Localizable Properties** — 锁定可本地化的属性，例如面向用户的文本和大小。
- **Non-localizable Properties** — 锁定不可本地化的属性（面向用户的文本和大小属性仍可编辑）。

![视图检查器的截图，其中显示了 Lock 弹出式菜单的位置。](../../../attachments/ec4a9d070923ee61715dc39ffd8f3d42/locking-views-in-storyboard-and-xib-files-1@2x.png)

例如，在等待本地化人员提供翻译时选择 Localizable Properties。如果已导入本地化内容，并且不希望无意中进行其他更改，请选择 Non-localizable Properties。

要锁定所有视图，请在 Project 导览器中选择用户界面文件，然后从 Editor \> Localization Locking 菜单中选择锁定级别。

### 解锁视图

导入本地化内容后，要解锁所有视图，请在 Project 导览器中选择用户界面文件，然后选择 Editor \> Localization Locking \> Reset Locking Controls。要禁止在用户界面文件中进行任何会影响本地化字符串文件的编辑，请选择 Editor \> Localization Locking \> Reset Locking Controls，然后选择 Editor \> Localization Locking \> Localizable Properties。

## 另请参阅

### 翻译与适配

- [为本地化人员创建 App 截图](creating-screenshots-of-your-app-for-localizers.md) — 与本地化人员共享 App 截图，为翻译提供上下文。
- [导出本地化内容](exporting-localizations.md) — 向本地化人员提供项目中的可本地化文件。
- [编辑 XLIFF 和字符串目录文件](editing-xliff-and-string-catalog-files.md) — 为从项目导出的语言和地区翻译或适配可本地化文件。
- [导入本地化内容](importing-localizations.md) — 将你为某种语言和地区翻译或适配的文件导入项目。
