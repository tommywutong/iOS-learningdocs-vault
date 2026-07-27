---
title: 解决常见的配置和构建问题
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/resolving-common-configuration-and-build-issues
source_url: 'https://developer.apple.com/documentation/xcode/resolving-common-configuration-and-build-issues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/resolving-common-configuration-and-build-issues.json'
content_hash: 'sha256:8dbf197847bde9bc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 解决常见的配置和构建问题

<sub>文章</sub>

查看常见的配置和构建问题，并了解如何解决它们。

## 概述

Xcode 会引导你完成配置项目以使用 Xcode Cloud 以及创建工作流程的过程。不过，你仍有可能遇到问题。对于代码库复杂、依赖项众多的项目，这种情况更容易发生。为了帮助你诊断构建失败的原因，可以在 Xcode 的构建报告中或 [App Store Connect](https://appstoreconnect.apple.com) 网站上查看日志，并下载构建报告。

### 查看构建日志

要了解构建失败的原因，请打开你的项目或工作区，前往「报告」导航器。选择一次构建，展开一个失败的操作，然后选择「Logs」查看构建日志。要下载构建日志和其他任何构建制品——例如一个结果包——请为该失败的操作选择「Artifacts」。

或者，也可以在 App Store Connect 网站的「Xcode Cloud」选项卡中选择一次构建，查看该构建的详细信息。

### 在本地复现构建失败

在本地复现构建失败通常是修复其成因的关键。要快速在本地复制失败构建的源代码状态：

1. 打开你的 Xcode 项目或工作区，前往「报告」导航器，选择一次构建以查看其构建报告概览。
2. 点按概览右上角的「Switch To」，然后按照屏幕上的提示，选择切换到该分支的最新提交，或者检出失败构建的特定提交。
3. 在 Xcode Cloud 中执行失败的操作，在本地复现该问题并解决它。

如果你的工作流程不会针对最新的更改自动启动新的构建，请按照下方[开始新的构建](resolving-common-configuration-and-build-issues.md#Start-a-new-build)中的描述手动启动一次新的构建。

### 解决配置问题

要在首次配置项目或工作区以使用 Xcode Cloud 时解决问题：

- 如果 Xcode 没有列出你的产品，请为在 Xcode 中构建你 App 或框架的 Scheme 启用归档操作。
- 如果你无法授予 Xcode Cloud 访问你 Git 仓库的权限，请检查你是否拥有将 Xcode Cloud 连接到你 Git 仓库所需的权限或角色。更多信息，请参阅[授予 Xcode Cloud 访问你源代码的权限](configuring-your-first-xcode-cloud-workflow.md#Grant-Xcode-Cloud-access-to-your-source-code)。
- 如果某个工作流程的操作没有列出 Scheme，请确保你已共享该 Scheme。有关共享 Scheme 的信息，请参阅 [Xcode 帮助](https://help.apple.com/xcode/mac/#/dev5426ddfcf)。

### 解决构建问题

要解决构建问题：

- 在「报告」导航器中按住 Control 点按你的工作流程，点按「Edit Workflow」，验证环境设置是否使用了构建你项目所需的 macOS 和 Xcode 版本。
- 检查你的项目或工作区是否使用了 Xcode 的新构建系统。有关新构建系统的更多信息，请参阅 [Xcode 10 构建系统发行说明](../xcode-release-notes/build-system-release-notes-for-xcode-10.md)。有关如何启用新构建系统的详细信息，请参阅[选择构建系统](https://help.apple.com/xcode/mac/#/dev396bc94c7)。
- 检查你项目的依赖项和所需的其他工具，确保 Xcode Cloud 能够访问它们。更多信息，请参阅[使依赖项对 Xcode Cloud 可用](making-dependencies-available-to-xcode-cloud.md)。
- 如果你使用 [CocoaPods](https://cocoapods.org) 管理依赖项，请检查你是否已将 `Podfile` 和 `Podfile.lock` 文件提交到 Git，并按照[使 CocoaPods 依赖项对 Xcode Cloud 可用](making-dependencies-available-to-xcode-cloud.md#Make-CocoaPods-dependencies-available-to-Xcode-Cloud)中的说明正确安装了 CocoaPods。
- 如果某个第三方工具提示存在网络问题，请将其配置为遵循 `HTTP_PROXY` 和 `HTTPS_PROXY` 环境变量，并按需调整其代理设置。
- 如果你的构建因提示缺少 App 功能的错误而失败，请检查你在配置第一个 Xcode Cloud 工作流程时使用的 App ID 是否已启用所有必需的功能。有关功能的更多信息，请参阅[启用 App 功能](https://developer.apple.com/help/account/manage-identifiers/enable-app-capabilities)。

### 解决 Swift 包依赖问题

Xcode Cloud 支持在你的项目中使用 Swift 包依赖项。如果你的项目需要 Swift 包依赖项才能成功构建，请务必阅读[使用 Swift 包依赖项和 Git 子模块](making-dependencies-available-to-xcode-cloud.md#Use-Swift-package-dependencies-and-Git-submodules)。

构建失败的一个常见原因是，Xcode Cloud 无法访问解析你 Swift 包依赖项所需的 `Package.resolved` 文件。要解决与 `Package.resolved` 文件相关的问题，请确保：

- 将该文件提交并推送到你的 Git 仓库。
- 你的 `.gitignore` 文件没有包含该文件。

### 开始新的构建

当你为解决某个构建问题对项目或工作区做出更改后，请启动一次新的构建，以验证该更改是否解决了问题：

- 要手动启动一次包含任何新更改的构建，请在「报告」导航器中按住 Control 点按该工作流程，然后点按「Start Build」。
- 要基于同一个 Git 提交启动一次构建，请在「报告」导航器中按住 Control 点按该次构建，然后选择「Rebuild」。

## 另请参阅

### 疑难解答

- [解决 GitHub Enterprise 连接问题](resolve-github-enterprise-connection-issues.md) — 验证 Xcode Cloud 能否访问你的 GitHub Enterprise 仓库，并修复配置问题。
- [为 Xcode Cloud 报告反馈](reporting-feedback-for-xcode-cloud.md) — 就你在使用 Xcode Cloud 构建时遇到的问题提供反馈。
