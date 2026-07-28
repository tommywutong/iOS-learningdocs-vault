---
title: 使用 Xcode Cloud 构建 Swift 软件包和 Swift Playgrounds App 项目
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.json'
content_hash: 'sha256:72ec8dea3b56b0e3'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 使用 Xcode Cloud 构建 Swift 软件包和 Swift Playgrounds App 项目

<sub>文章</sub>

将 Swift 软件包或 Swift Playgrounds App 项目添加到 Xcode 项目，以便在 Xcode Cloud 中构建。

## 概述

Xcode Cloud 支持 Swift Package Manager，在 App 项目中使用 Swift 软件包依赖项几乎不需要任何配置。但是，Xcode Cloud 无法构建独立的 Swift 软件包。要使用 Xcode Cloud 构建 Swift 软件包：

1. 在 Xcode 中创建 App 项目或工作区。
2. 按照[使用本地软件包整理代码](organizing-your-code-with-local-packages.md)中的说明，将 Swift 软件包作为本地软件包添加。
3. 提交 `Package.resolved` 文件。
4. 按照[配置首个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中的说明创建首个工作流。

Xcode Cloud 启动构建时，会将 Swift 软件包作为 App 项目的一部分进行构建。

类似地，Xcode Cloud 无法构建使用 [Swift Playgrounds](https://www.apple.com/swift/playgrounds/) 创建的独立 App。要构建使用 Swift Playgrounds 创建的 App，请将 Swift Playground App 项目存储到 Mac，按照上述说明将其添加到 Xcode 项目，然后为 Xcode 项目配置首个工作流。

> [!note] 注意
> 要进一步了解如何使用 Xcode Cloud 构建需要 Swift 软件包依赖项的项目，请参阅[使用 Swift 软件包依赖项和 Git 子模块](making-dependencies-available-to-xcode-cloud.md#Use-Swift-package-dependencies-and-Git-submodules)。

## 另请参阅

### 设置与维护

- [使 Xcode Cloud 可访问依赖项](making-dependencies-available-to-xcode-cloud.md) — 在配置项目以使用 Xcode Cloud 之前，检查依赖项并使 Xcode Cloud 可访问它们。
- [为团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 以团队形式开始使用 Xcode Cloud 的持续集成和交付。
- [在 Xcode Cloud 工作流之间共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定义别名与多个工作流共享配置。
- [在 Xcode Cloud 工作流之间共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 使用共享环境变量将通用配置应用于多个工作流。
- [设置 Xcode Cloud 构建的下一个构建号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 为现有 Mac App 从自定义构建号开始编号，以避免版本冲突。
- [随 App 的 Beta 版本包含供测试人员查看的备注](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 向 Xcode 项目添加文本文件，为 Beta 测试人员提供测试内容的备注。
- [从 Xcode Cloud 移除项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 移除项目，以删除 App 和工作流数据、断开 Git 仓库连接，并移除 Slack 集成。
- [更改软件包标识符](changing-the-bundle-identifier.md) — 修改 App 的软件包标识符，并在其出现的所有位置更新。
