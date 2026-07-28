---
title: 为 App、框架与包编写文档
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/documenting-apps-frameworks-and-packages
source_url: 'https://developer.apple.com/documentation/xcode/documenting-apps-frameworks-and-packages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/documenting-apps-frameworks-and-packages.json'
content_hash: 'sha256:49514da2db0db97f'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [编写文档](writing-documentation.md)

# 为 App、框架与包编写文档

<sub>文章</sub>

通过源码注释创建开发者文档，添加包含代码片段的文章，以及提供引导式学习教程。

## 概述

DocC，即*文档编译器（Documentation Compiler）*，让你能够轻松地为自己的 App、框架与 Package 创建内容丰富且引人入胜的开发者文档。该编译器通过将源码注释与扩展文件、文章以及 Xcode 中与项目一并存放的其他资源结合起来，构建出文档。

该编译器直接与 Xcode 集成，从而增强你现有的工作流程，包括代码补全、快速帮助（Quick Help）等功能。

要更深入地了解 DocC 以及如何使用它为框架和包编写文档，请访问 [为 Swift 框架或包编写文档（Swift.org）](https://www.swift.org/documentation/docc) 提供的文档。

### 从源码注释构建基础文档

要让 DocC 编译你的文档，请构建你的项目。Xcode 会将有关框架公开 API 以及 App 目标内部 API 的补充信息，与编译后的产物一同存储。DocC 会使用这些信息，并将文档编译成一个 DocC 归档。此过程会为你目标所依赖的每个框架或 Package 重复执行。

![](../../../attachments/f769db70372edebeaa3a0b4bde7d9c44/docc-compilation-default@2x.png)

<sub>示意图，展示了编译器如何将代码转化为 App 或框架，并将其公开 API 的信息提供给文档编译器，文档编译器再利用这些信息生成 DocC 归档。</sub>

要为项目构建文档，请选择“产品（Product）”>“构建文档（Build Documentation）”。DocC 会编译文档，并在 Xcode 的文档查看器中将其打开。

![Xcode 文档查看器的截图，显示了 DocC 生成的一个基本符号参考页面。](../../../attachments/2210963c6ca4eefe5c1115f5165ff14a/basic-documentation@2x.png)

### 构建多语言文档

DocC 会从 Swift 编译器和 Objective-C 编译器中获取信息，并将其合并，形成一个展示两种语言文档的单一文档归档。对于同时包含 Swift 和 Objective-C 代码的目标，DocC 会自动构建多语言文档。对于那些仅用一种语言编写但打算同时被 Swift 和 Objective-C 代码使用的目标，可以选择输出多语言文档。要启用此功能，请执行以下操作：

1. 在 Xcode 中，于项目导航器（Project navigator）中选择你的项目。
2. 在项目编辑器中选中该目标。
3. 点击“构建设置（Build Settings）”标签页。
4. 在搜索框中输入 “multi-language documentation”，以定位到 “Build Multi-Language Documentation for Swift Only Targets” 或 “Build Multi-Language Documentation for Objective-C Only Targets” 设置（具体取决于你实现该目标所用的语言）。
5. 从该设置的弹出式按钮中选择“是（Yes）”，以启用此构建设置。

![](../../../attachments/c6f71458412fd7e798466e845f06e88a/multi-language-documentation-build-settings@2x.png)

<sub>一张 Xcode 截图，显示 “Build Multi-Language Documentation for Swift Only Targets” 设置为启用状态，而 “Build Multi-Language Documentation for Objective-C Only Targets” 设置为禁用状态。</sub>

> [!note] 注意
> 你无法在 Swift Package 中使用此构建设置。

### 配置更丰富的文档体验

DocC 将从 Swift 编译器和 Objective-C 编译器获取的公开 API 信息与文档目录的内容结合起来，以生成更为丰富的 DocC 归档。

要往已有项目中添加文档目录，请遵循以下步骤：

1. 在 Xcode 中，于项目导航器中选择你的项目或 Package。
2. 选择“文件（File）”>“新建（New）”>“来自模板的文件（File from Template）”。
3. 在“文档（Documentation）”部分中选择“文档目录（Documentation Catalog）”模板，然后点击“下一步（Next）”。
4. 输入文件名并点击“创建（Create）”。

![](../../../attachments/df4db4754f5252055a747320655ccdfd/add-documentation-catalog@2x.png)

<sub>Xcode 的文件模板选择器截图，其中“文档”部分中的“文档目录”模板处于选中状态。</sub>

### 将文档纳入构建流程

除了通过选择“产品（Product）”>“构建文档（Build Documentation）”按需构建文档之外，你还可以启用 DocC 提供的一项构建设置，从而在每次构建框架时自动编译文档。

要启用文档编译器构建设置，请执行以下操作：

1. 在 Xcode 中，于项目导航器中选择你的项目。
2. 在项目编辑器中选中该目标。
3. 点击“构建设置（Build Settings）”标签页。
4. 在搜索框中输入 “build documentation”，以定位到 “Build Documentation during ‘Build’” 设置。
5. 从该设置的弹出式按钮中选择“是（Yes）”，以启用此构建设置。

![一张 Xcode 截图，显示 “Build Documentation during ‘Build’” 设置为启用状态。](../../../attachments/e58c242e97d168d078bd4af264eb7cae/build-documentation-build-setting@2x.png)

> [!note] 注意
> 对于现有项目，只有在添加文档目录之后，该构建设置才会出现。你无法在 Swift Package 中使用此构建设置。

DocC 还与 `xcodebuild` 集成，这意味着你可以从命令行构建文档。如果你想将文档构建纳入持续集成流程，这会非常有用。更多信息，请参阅[向其他开发者分发文档](distributing-documentation-to-other-developers.md)。
