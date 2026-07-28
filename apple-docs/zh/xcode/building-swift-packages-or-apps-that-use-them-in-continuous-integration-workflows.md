---
title: 在持续集成工作流中构建 Swift 软件包或使用它们的 App
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows
source_url: 'https://developer.apple.com/documentation/xcode/building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows.json'
content_hash: 'sha256:56705cf0369dd96a'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift 软件包](swift-packages.md)

# 在持续集成工作流中构建 Swift 软件包或使用它们的 App

<sub>文章</sub>

使用现有的持续集成设置构建 Swift 软件包，并在现有 CI 流水线中准备使用软件包依赖项的 App。

## 概述

*持续集成（continuous integration，CI）*是对 App 的构建、分析、测试、归档（archiving）和发布进行自动化与简化的过程，以确保 App 始终处于可发布状态。使用 [Xcode Cloud](xcode-cloud.md)，或在其他 CI 系统上直接使用 `xcodebuild` 命令，来构建 Swift 软件包和使用它们的 App。

大多数包含 Swift 软件包或依赖 Swift 软件包的项目都不需要额外配置。不过，请务必将项目的 `Package.resolved` 文件提交到 Git 仓库。这可以确保 CI 工作流可靠，并始终使用软件包依赖项的预期版本。如果项目依赖需要认证的软件包，或者你需要使用 Mac 的 Git 工具而不是 Xcode 随附的工具，则可能需要执行额外配置。

> [!important] 重要
> 虽然你可以使用 Xcode 在本地构建独立 Swift 软件包，但 Xcode Cloud 要求软件包属于某个项目或工作区。要了解如何使用 Xcode Cloud 构建 Swift 软件包，请参阅[使用 Xcode Cloud 构建 Swift 软件包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md)。

### 使用软件包依赖项的预期版本

为确保 CI 工作流可靠，请确保它使用适当的软件包依赖项版本。Xcode 将每个软件包依赖项的确切版本存储在名为 `Package.resolved` 的文件中。当 Xcode 项目或 `Package.swift` 清单文件中的软件包要求发生变化时，该文件会自动更新。请将此文件提交到 Git 仓库，以确保 CI 环境中的文件始终是最新的，避免 CI 使用非预期的软件包依赖项版本构建项目。

> [!tip] 提示
> 你可以在 `.xcodeproj` 目录内的 _[appName]_`.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved` 中找到 `Package.resolved` 文件。

如果 CI 流水线直接使用 `xcodebuild` 命令，还应传递 `-disableAutomaticPackageResolution` 标志。此标志可确保 CI 流水线始终使用 `Package.resolved` 文件中定义的软件包依赖项。

### 提供凭证

如果 Xcode 项目仅依赖公开可用的 Swift 软件包，则无需执行额外配置步骤。Xcode Cloud 或 `xcodebuild` 命令会自动解析软件包依赖项。不过，要解析需要认证的软件包依赖项或*私有软件包*，需要向 CI 设置提供凭证。有关授予 Xcode Cloud 对私有依赖项访问权限的信息，请参阅[使 Xcode Cloud 可访问依赖项](making-dependencies-available-to-xcode-cloud.md)。

如果直接使用 `xcodebuild` 命令，请为软件包使用基于 SSH 的 Git URL，并配置 SSH 凭证。在运行 CI 任务的 macOS 用户的 `~/.ssh` 目录中设置 `known_hosts` 文件。`xcodebuild` 会遵循 SSH 配置，无需额外设置。

如果 SSH 密钥受密码保护，请按照 [Tech Note 2449](https://developer.apple.com/library/archive/technotes/tn2449/_index.html) 中的说明修改 SSH 配置文件，以便在调用 `xcodebuild` 之前将密钥添加到 SSH 代理。

### 使用系统的 Git 工具

直接使用 `xcodebuild` 时，它会使用 Xcode 内建的 Git 工具连接到仓库。在许多情况下，你无需更改 `xcodebuild` 连接仓库的方式。不过，某些用例需要使用为 Mac 上所安装 Git 设置的配置。例如：

- URL 重映射
- 代理配置
- 高级 SSH 配置，例如停用 `StrictHostKeyChecking` 设置

要让 `xcodebuild` 使用 Mac 的 Git 安装和配置，请向 `xcodebuild` 命令传递 `-scmProvider system`。

有关使用 `xcodebuild` 的更多信息，请参阅 [Technical Note 2339](https://developer.apple.com/library/archive/technotes/tn2339/_index.html)。
