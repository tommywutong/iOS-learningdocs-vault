---
title: 与 App 协同开发 Swift 软件包
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/developing-a-swift-package-in-tandem-with-an-app
source_url: 'https://developer.apple.com/documentation/xcode/developing-a-swift-package-in-tandem-with-an-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/developing-a-swift-package-in-tandem-with-an-app.json'
content_hash: 'sha256:be72c7c63ad00f39'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift 软件包](swift-packages.md)

# 与 App 协同开发 Swift 软件包

<sub>文章</sub>

将已发布的 Swift 软件包作为本地软件包添加到 App 项目，并协同开发软件包和 App。

## 概述

Swift 软件包是一种方便、轻量的解决方案，可用于创建模块化 App 架构，并在你的多个 App 之间或与其他开发者复用代码。随着时间推移，你可能想与 App 协同开发已发布的 Swift 软件包，或创建一个示例 App 来展示其功能。若要与 App 协同开发 Swift 软件包，你可以利用本地软件包会覆盖同名软件包依赖项的行为：

1. 按照[将软件包依赖项作为本地软件包进行编辑](editing-a-package-dependency-as-a-local-package.md)中的说明，将 Swift 软件包作为软件包依赖项而非本地软件包添加到 App。
2. 协同开发 App 和 Swift 软件包，并将更改推送到各自的仓库。
3. 如果你发布了 Swift 软件包的新版本，或想停止使用本地软件包，请从项目中移除本地软件包，以重新使用软件包依赖项。

## 另请参阅

### 创建软件包

- [使用 Xcode 创建独立 Swift 软件包](creating-a-standalone-swift-package-with-xcode.md) — 将可执行代码或可共享代码捆绑到独立 Swift 软件包中。
- [在 Swift 软件包中捆绑资源](bundling-resources-with-a-swift-package.md) — 将资源文件添加到 Swift 软件包，并在代码中访问它们。
- [本地化软件包资源](localizing-package-resources.md) — 确保你的 Swift 软件包为多种区域设置提供本地化资源。
- [以 Swift 软件包形式分发二进制框架](distributing-binary-frameworks-as-swift-packages.md) — 创建包含一个或多个 XCFramework 的 Swift 软件包，使二进制文件可供其他开发者使用。
- [使用本地软件包组织代码](organizing-your-code-with-local-packages.md) — 通过将 App 代码组织到本地 Swift 软件包中，简化维护、促进模块化并鼓励复用。
- [PackageDescription](../packagedescription.md) — 创建可复用代码，以轻量方式组织代码，并在你的各个项目之间或与其他开发者共享。
