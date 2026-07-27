---
title: 设置项目以使用 Xcode Cloud
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/setting-up-your-project-to-use-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/setting-up-your-project-to-use-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/setting-up-your-project-to-use-xcode-cloud.json'
content_hash: 'sha256:cb0218680bc80ec0'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 设置项目以使用 Xcode Cloud

<sub>文章</sub>

在配置项目或工作区以使用 Xcode Cloud 之前，检查账户、项目和源代码控制要求。

## 概述

Xcode 可帮助你配置项目或工作区以使用 Xcode Cloud。为确保配置过程顺利，请检查使用 Xcode Cloud 的要求，并根据需要进行更改。然后，配置项目或工作区以使用 Xcode Cloud，开始实践持续集成和交付（CI/CD）。

### 设置 App Store Connect 账户

要使用 Xcode Cloud，你需要：

- 加入 [Apple Developer Program](https://developer.apple.com/programs/)。
- 使用 Xcode 15 或更高版本。
- 在 Xcode 设置的 Accounts 中添加你的 Apple 账户。
- 在 [App Store Connect](https://developer.apple.com/help/app-store-connect/) 中拥有 App 的记录，或拥有创建该记录所需的角色或权限。

要创建 App 记录，你需要在团队中拥有 App Manager、Admin 或 Account Holder 角色。如果你拥有 Developer 角色，则需要 Create Apps 权限。如果你没有所需的角色或权限，请与拥有这些权限的团队成员合作。有关更多信息，请参阅[在 App Store Connect 中创建 App 记录](configuring-xcode-cloud-for-your-team.md#Create-an-app-record-in-App-Store-Connect)。

> [!note] 注意
> 根据 Xcode Cloud 的使用量，你可能需要可选的 Xcode Cloud 订阅方案。管理 Xcode Cloud 订阅方案需要 Account Holder 角色。有关订阅方案的更多信息，请参阅[开始使用 Xcode Cloud](https://developer.apple.com/xcode-cloud/get-started/)。

有关 App Store Connect 角色的更多信息，请参阅[角色权限](https://developer.apple.com/help/app-store-connect/reference/role-permissions)。

### 配置项目和工作区

如果你从模板创建项目，默认设置会自动满足 Xcode Cloud 要求。如果你有现有项目，请确保它满足以下项目和工作区要求：

- 使用一致的 Xcode 项目或工作区。
- 使用共享方案。有关共享方案的信息，请参阅[自定项目的构建方案](customizing-the-build-schemes-for-a-project.md)。
- 为构建 App 或框架的方案启用归档操作。
- 确保 Xcode Cloud 可以使用依赖项和其他第三方工具。有关更多信息，请参阅[使依赖项可供 Xcode Cloud 使用](making-dependencies-available-to-xcode-cloud.md)。
- 允许 Xcode 为你管理签名。若要使用自动代码签名，请在项目编辑器的 Signing & Capabilities 面板中打开“Automatically manage signing”复选框。
- 在 Xcode 项目或工作区的 Signing & Capabilities 面板中设置 App 目标的捆绑包标识符。如果你使用 `.xcconfig` 文件设置捆绑包标识符，请参阅[检查 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md#Review-Xcode-Cloud-workflows)了解更多信息。

> [!important] 重要
> Xcode Cloud 要求使用一个持续存在且保持一致的 Xcode 项目或工作区。如果你使用第三方工具动态生成或编辑项目或工作区，Xcode Cloud 的初始配置和后续构建可能会失败。

### 使用远程源代码控制仓库

要使用 Xcode Cloud，你需要一个使用 Git 的远程仓库。若要进一步了解如何在 Xcode 中使用 Git 进行源代码控制，请参阅[源代码控制管理](source-control-management.md)。

Xcode Cloud 支持以下源代码管理（SCM）提供商：

- [Bitbucket Cloud](https://bitbucket.org) 和 [Bitbucket Server](https://bitbucket.org/product/enterprise)
- [GitHub](https://github.com) 和 [GitHub Enterprise](https://github.com/enterprise)
- [GitLab](https://gitlab.com) 和[自行管理的 GitLab 实例](https://about.gitlab.com/install)

如果你在自托管或云端 SCM 提供商（例如 Bitbucket Server 或 GitHub Enterprise）上使用 IP 允许列表，请确保 Xcode Cloud 可以访问 Git 服务器。检查防火墙的入站 HTTPS 允许列表，并添加以下 IP 地址范围，允许 Xcode Cloud 访问 Git 服务器：

```other
57.103.0.0/22
57.103.64.0/18
2a01:b747:3000:200::/56
2a01:b747:3001:200::/56
2a01:b747:3002:200::/56
2a01:b747:3003:200::/56
2a01:b747:3005:200::/56
2a01:b747:3006:200::/56
2a01:b747:3004:200::/56
```

此外，你需要特定权限或角色才能将 Xcode Cloud 连接到 Git 仓库。具体权限取决于你使用的 SCM 提供商：

- 如果代码托管在 Bitbucket Cloud 或 Bitbucket Server 上，你需要管理员权限。
- 如果代码托管在 GitHub 或 GitHub Enterprise 上，你需要是组织所有者；如果不使用 GitHub 组织，则需要管理员权限。
- 如果代码托管在 GitLab 或自行管理的 GitLab 实例上，你需要维护者权限。

如果你没有所需的角色或权限，请与拥有这些权限的团队成员合作。有关更多信息，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

## 另请参阅

### 基础

- [开始使用 Xcode Cloud](getting-started-with-xcode-cloud.md) — 在开发期间使用 Xcode Cloud 在云端构建并测试你的 App。
- [通过 TestFlight 分发 Xcode Cloud 构建版本](distributing-your-xcode-cloud-builds-through-testflight.md) — 为内部测试员创建 TestFlight 分发工作流程。
- [关于使用 Xcode Cloud 进行持续集成和交付](about-continuous-integration-and-delivery-with-xcode-cloud.md) — 了解如何通过 Xcode Cloud 的持续集成和交付来创建高质量的 App 和框架。
- [配置第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md) — 设置项目或工作区以使用 Xcode Cloud，并采用持续集成和交付。
