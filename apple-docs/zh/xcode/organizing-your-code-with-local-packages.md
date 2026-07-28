---
title: 使用本地包组织代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/organizing-your-code-with-local-packages
source_url: 'https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/organizing-your-code-with-local-packages.json'
content_hash: 'sha256:ce17e92add9916d8'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift 包](swift-packages.md)

# 使用本地包组织代码

<sub>文章</sub>

将 App 的代码组织到本地 Swift 包（local Swift package）中，以简化维护、提升模块化并鼓励复用。

## 概述

在开发 App 时，通过创建 Swift 包（Swift package）并将其作为_本地包（local package）_ 使用，以模块化的方式组织代码，使其更易于维护。

首先，识别适合模块化的代码；例如，网络逻辑、包含工具类的源文件等。然后，将代码移入本地包，步骤如下：

1. 打开 Xcode 项目，选择“文件（File）”>“新建（New）”>“包（Package）”（或在 Xcode 15 之前的版本中选择“Swift 包（Swift Package）”），将本地 Swift 包作为项目的一部分创建。
2. 若要创建预配置为库的包，在包模板对话框顶部选择“多平台”，选择“库（Library）”模板，然后点按“下一步”。选择对话框中的其他模板，可为其他类型的内容创建预配置的包。
3. 选择项目和组，但如果你的 App 已在版本控制之下，则不要创建新的 Git 仓库；然后创建新的 Swift 包。
4. 在项目导航器中将代码移至新包，并根据需要对_包清单（package manifest）_ 进行必要的更新。具体配置取决于你的需求。例如，你可能需要将代码以库产品（library product）的形式提供，并声明包的目标（target）。要了解更多关于配置 Swift 包的信息，请参阅[使用 Xcode 创建独立的 Swift 包](creating-a-standalone-swift-package-with-xcode.md)。
5. 在项目导航器中选择你的项目，然后选择你的 App target，并导航到其“通用”面板。
6. 点按“框架、库和嵌入内容（Frameworks, Libraries, and Embedded Content）”部分中的“+”按钮，选择本地包的库产品，并将其添加为依赖项（dependency）。

使用本地包组织 App 的代码库时，你的 Swift 包代码与 App 代码属于同一个仓库。当创建更多 App 时，可以考虑将本地包移至其自己的 Git 仓库，并将其作为包依赖项添加到你的 App 中，以实现跨 App 的代码复用。你甚至可以考虑与其他开发者分享它们。更多信息，请参阅[使用 Xcode 发布 Swift 包](publishing-a-swift-package-with-xcode.md)。

## 另请参阅

### 创建包

- [使用 Xcode 创建独立的 Swift 包](creating-a-standalone-swift-package-with-xcode.md) — 将可执行或可共享的代码打包为独立的 Swift 包。
- [使用 Swift 包捆绑资源](bundling-resources-with-a-swift-package.md) — 将资源文件添加到你的 Swift 包中，并在代码中访问它们。
- [本地化包资源](localizing-package-resources.md) — 确保你的 Swift 包为多种语言提供本地化资源。
- [将二进制框架作为 Swift 包分发](distributing-binary-frameworks-as-swift-packages.md) — 通过创建包含一个或多个 XCFramework 的 Swift 包，使二进制文件可供其他开发者使用。
- [同步开发 Swift 包与 App](developing-a-swift-package-in-tandem-with-an-app.md) — 将已发布的 Swift 包作为本地包添加到你的 App 项目中，同步开发包和 App。
- [PackageDescription](../packagedescription.md) — 创建可复用代码，以轻量级方式组织代码，并在你的项目之间以及与其他开发者之间共享。
