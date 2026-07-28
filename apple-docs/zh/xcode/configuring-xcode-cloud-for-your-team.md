---
title: 为你的团队配置 Xcode Cloud
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-xcode-cloud-for-your-team
source_url: 'https://developer.apple.com/documentation/xcode/configuring-xcode-cloud-for-your-team'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-xcode-cloud-for-your-team.json'
content_hash: 'sha256:4dfd244cea572e8e'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 为你的团队配置 Xcode Cloud

<sub>文章</sub>

开始以团队形式使用 Xcode Cloud 进行持续集成和交付。

## 概述

若要采用 Xcode Cloud 进行持续集成和交付（CI/CD），你需要先配置项目或工作区以使用 Xcode Cloud，再创建第一个工作流程，然后启动第一次构建。然而，以团队形式开始使用 Xcode Cloud 可能需要额外的步骤以及在团队成员和管理员之间进行协调——尤其是在企业环境中。

为了成功将团队的项目或工作区配置为使用 Xcode Cloud，请先阅读[设置项目以使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) 中描述的必要角色和权限。根据你的角色和权限，你可能需要与他人协调来完成以下工作：

- 允许 Xcode Cloud 访问团队的 Git 仓库。
- 在 App Store Connect 中创建 App 记录。

如果你拥有完成上述任务所需的角色和权限，或者其他人已经完成了这些工作，请按[配置你的第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md) 中的描述配置团队的项目或工作区。不过，团队可能会限制可以管理 Git 仓库和 App Store Connect 账户的人数。在企业环境中，甚至可能存在专门的基础设施团队，这意味着在开始使用 Xcode Cloud 之前，你需要与他们协作。

有关以团队形式使用 Xcode Cloud 的更多信息，请参阅[深入了解团队如何使用 Xcode Cloud](https://developer.apple.com/wwdc22/110375)。

### 将 Xcode Cloud 连接到由管理员管理的 Git 仓库

要开始使用 Xcode Cloud，你需要拥有[设置项目以使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) 中列出的权限，才能授予 Xcode Cloud 访问团队 Git 仓库的权限。如果你没有所需的角色或权限，请与团队的源代码管理（SCM）管理员合作，并请他们配置你的项目以使用 Xcode Cloud。

你只需在将团队的第一个 App 或框架接入 Xcode Cloud 时与 SCM 管理员协作。当 SCM 管理员为一个项目或工作区配置 Xcode Cloud，并将团队的 SCM 提供商连接到 Xcode Cloud 后，你在同一提供商处托管的其他项目都可以复用该连接。例如，假设你的团队将其仓库托管在 Bitbucket Cloud 上，管理员为一个项目配置了 Xcode Cloud。当你为后续同样使用 Bitbucket Cloud 的项目开始使用 Xcode Cloud 时，你可以复用管理员配置好的 Bitbucket Cloud 连接。

要将 Xcode Cloud 连接到由管理员管理的 Git 仓库：

1. 如果管理员还不是团队成员，请先将他们添加到你的团队。
2. 让管理员配置你的项目以使用 Xcode Cloud。即使你的仓库管理员不具备 Apple 平台开发经验，也可以让他们配置项目或工作区以使用 Xcode Cloud，并允许首次构建失败。
3. 如下文[将个人 SCM 账户连接到 Xcode Cloud](configuring-xcode-cloud-for-your-team.md#Connect-your-personal-SCM-account-to-Xcode-Cloud)所述，开始使用 Xcode Cloud，并修复任何构建问题。

> [!tip] 提示
> 如果你使用 [GitHub](https://github.com) 或 [GitHub Enterprise](https://github.com/enterprise) 托管代码，Xcode Cloud 会帮助你与 GitHub 组织的管理员协作。按照[配置你的第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md) 中的描述开始初始配置。当 Xcode Cloud 请求访问团队仓库的权限时，你可以请求 _organization owner_（组织所有者）或拥有 _admin_（管理员）角色的人安装用于管理团队仓库访问权限的 Xcode Cloud GitHub App。当他们安装好 App 后，你就可以完成后续的初始配置了。

### 在 App Store Connect 中创建 App 记录

Xcode Cloud 将 [Xcode](https://developer.apple.com/xcode/)、[TestFlight](https://developer.apple.com/testflight/) 和 [App Store Connect](https://appstoreconnect.apple.com) 整合为一个强大的 CI/CD 系统。因此，你需要为你的 App 在 App Store Connect 中创建一条 App 记录才能使用 Xcode Cloud。如果你尚未为 App 创建 App 记录，在你配置项目或工作区以使用 Xcode Cloud 时，Xcode 会帮助你创建。

> [!note] 注意
> 使用 Xcode Cloud 构建框架时，不需要创建 App 记录。

有关创建 App 记录要求的更多信息，请参阅[设置你的 App Store Connect 账户](setting-up-your-project-to-use-xcode-cloud.md#Set-up-your-App-Store-Connect-account)。如果你无法创建 App 记录，请让拥有相应角色或权限的人在 App Store Connect 中创建 App 记录。然后，按[配置你的第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md) 中的描述配置你的项目或工作区以使用 Xcode Cloud。

### 将个人 SCM 账户连接到 Xcode Cloud

Xcode Cloud 使用你的个人 SCM 账户来监控 Git 仓库的变更。因此，你需要将你的 Xcode Cloud 连接到 SCM 账户。为此，请打开一个由其他团队成员配置为使用 Xcode Cloud 的项目或工作区。如果你尚未将个人 SCM 账户连接到 Xcode Cloud，Xcode 会在工具栏中显示“Cloud Issues”按钮。点击该按钮，并授权 Xcode Cloud 将你的源代码管理账户与你的 Apple 账户关联起来。

## 另请参阅

### 设置与维护

- [使依赖项可用于 Xcode Cloud](making-dependencies-available-to-xcode-cloud.md) — 在配置项目以使用 Xcode Cloud 之前，检查并确保依赖项可用于 Xcode Cloud。
- [跨 Xcode Cloud 工作流程共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定义别名为多个工作流程共享配置。
- [跨 Xcode Cloud 工作流程共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 通过使用共享环境变量将通用配置应用于多个工作流程。
- [使用 Xcode Cloud 构建 Swift 包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将你的 Swift 包或 Swift Playgrounds App 项目添加到 Xcode 项目中，以便在 Xcode Cloud 中构建。
- [为 Xcode Cloud 构建设置下一个构建版本号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 从自定义构建编号开始为现有 Mac App 的构建编号，以避免版本冲突。
- [在 App 的 beta 版本中包含面向测试人员的说明](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 向 Xcode 项目添加文本文件，以便向 beta 版测试人员提供关于测试内容的说明。
- [从 Xcode Cloud 中移除项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 中移除你的项目，以删除 App 和工作流程数据、断开 Git 仓库连接以及移除 Slack 集成。
- [更改 Bundle Identifier](changing-the-bundle-identifier.md) — 修改你的 App 的 Bundle Identifier，并在其出现的所有位置进行更新。
