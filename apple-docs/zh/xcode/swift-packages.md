---
title: Swift 包
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/swift-packages
source_url: 'https://developer.apple.com/documentation/xcode/swift-packages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/swift-packages.json'
content_hash: 'sha256:9215cb78892628a1'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md)

# Swift 包

创建可复用代码，以轻量级方式组织代码，并跨 Xcode 项目共享，与其他开发者分享。

## 概述

![一张图示，展示了 Xcode 如何支持将代码、资源和二进制文件打包到 Swift 包中。](../../../attachments/e8b388997f04b268375040a5b9e59ef5/swift-packages@2x.png)

Swift 包是 Swift、Objective-C、Objective-C++、C 或 C++ 代码的可复用组件，供开发者在项目中使用。它们将源文件、二进制文件和资源打包到一起，以便在你的 App 项目中轻松使用。

Xcode 支持创建和发布 Swift 包，也支持添加、移除及管理包依赖。它对 Swift 包的支持基于开源的 Swift Package Manager 项目构建。

要了解在包清单中使用的 API，请参阅 [Package](../packagedescription/package.md)。要了解更多关于 Swift Package Manager 的信息，请参见 [Swift.org](https://swift.org/package-manager/) 和开源 [Swift Package Manager 仓库](https://github.com/apple/swift-package-manager)。

## 主题

### 包依赖

- [为你的 App 添加包依赖](adding-package-dependencies-to-your-app.md) — 集成包依赖，以便在项目之间共享代码，或利用其他开发者编写的代码。
- [识别二进制依赖](identifying-binary-dependencies.md) — 了解包依赖是否引用了二进制文件，并验证二进制文件的真实性。
- [将包依赖作为本地包进行编辑](editing-a-package-dependency-as-a-local-package.md) — 通过将包依赖添加为本地包来覆盖它并编辑其内容。

### 包创建

- [使用 Xcode 创建独立的 Swift 包](creating-a-standalone-swift-package-with-xcode.md) — 将可执行或可共享的代码打包到独立的 Swift 包中。
- [将资源与 Swift 包捆绑](bundling-resources-with-a-swift-package.md) — 向 Swift 包添加资源文件并在代码中访问它们。
- [本地化包资源](localizing-package-resources.md) — 确保你的 Swift 包为多种语言区域提供本地化资源。
- [以 Swift 包形式分发二进制框架](distributing-binary-frameworks-as-swift-packages.md) — 通过创建包含一个或多个 XCFramework 的 Swift 包，让二进制文件可供其他开发者使用。
- [将 Swift 包与 App 协同开发](developing-a-swift-package-in-tandem-with-an-app.md) — 将已发布的 Swift 包作为本地包添加到你的 App 项目中，并协同开发包和 App。
- [使用本地包组织你的代码](organizing-your-code-with-local-packages.md) — 通过将 App 的代码组织到本地 Swift 包中，简化维护、促进模块化并鼓励复用。
- [PackageDescription](../packagedescription.md) — 创建可复用代码，以轻量级方式组织代码，并在你的项目之间以及与其它开发者共享。

### 包分发

- [使用 Xcode 发布 Swift 包](publishing-a-swift-package-with-xcode.md) — 私下发布 Swift 包，或与全球其他开发者分享。

### 持续集成

- [在持续集成工作流中构建 Swift 包或使用它们的 App](building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows.md) — 使用现有的持续集成（CI）设置构建 Swift 包，并在现有 CI 流水线中准备使用包依赖的 App。

## 另请参阅

### 代码

- [源代码编辑器](source-editor.md) — 使用源代码编辑器编辑源文件、定位问题并进行必要修改。
- [代码智能](coding-intelligence.md) — 使用智能体帮助你探索代码、添加功能、优化界面，以及运用本地化和辅助功能等技能。
- [Bundle 与 Framework](bundles-and-frameworks.md) — 在 Bundle 和 Framework 中组织代码与资源。
