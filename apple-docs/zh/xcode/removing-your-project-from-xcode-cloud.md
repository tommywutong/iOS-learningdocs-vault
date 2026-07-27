---
title: 从 Xcode Cloud 中移除你的项目
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/removing-your-project-from-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/removing-your-project-from-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/removing-your-project-from-xcode-cloud.json'
content_hash: 'sha256:2d992b97518a6d1e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 从 Xcode Cloud 中移除你的项目

<sub>文章</sub>

从 Xcode Cloud 中移除你的项目，以删除 App 和工作流程数据、断开你 Git 仓库的连接，并移除 Slack 集成。

## 概述

当你的 App 或框架不再处于积极开发状态时，你可能想要做一些常规清理工作，比如：

- 从 Xcode Cloud 中移除你的 App 及其任何数据。
- 断开 Xcode Cloud 与你 SCM 提供方之间的连接。
- 断开 Xcode Cloud 与你团队 [Slack](https://slack.com/) 工作区之间的连接。
- 移除你配置过的任何 Webhook。

### 从 Xcode Cloud 删除你的数据

当你从 Xcode Cloud 删除数据时，你将无法恢复它，且该数据会立即变得不可访问。

同样地，删除一个工作流程会删除该工作流程的构建历史记录和制品。只有当你确信不再需要某个工作流程或你的数据的构建历史记录或制品时，才删除它或你在 Xcode Cloud 中的数据。对于不再需要的工作流程，请改为按照[停用工作流程而非删除它](developing-a-workflow-strategy-for-xcode-cloud.md#Deactivate-a-workflow-instead-of-deleting-it)中的描述将其停用。

要停止为你的 App 或框架使用 Xcode Cloud 并删除其关联数据：

- 在 Xcode 中，前往「报告」导航器，按住 Control 点按你的 App，选择「Delete Xcode Cloud Data for」，然后确认你想要永久删除所有 Xcode Cloud 数据。
- 在 [App Store Connect](https://appstoreconnect.apple.com) 中，前往你 App 的页面，选择「Xcode Cloud」选项卡，选择「Settings」\> 「Delete Xcode Cloud Data」，点按「Delete」，然后确认你想要永久删除所有 Xcode Cloud 数据。

有关删除和停用工作流程之间区别的更多信息，请参阅[停用工作流程而非删除它](developing-a-workflow-strategy-for-xcode-cloud.md#Deactivate-a-workflow-instead-of-deleting-it)。

### 在 Xcode Cloud 中断开你的 Git 仓库连接

如果你将 Git 仓库迁移到另一个源代码管理（SCM）提供方，你会想要从 Xcode Cloud 配置中移除旧的提供方。

要断开 Xcode Cloud 与 [Bitbucket Server](https://bitbucket.org/product/enterprise)、[GitHub Enterprise](https://github.com/enterprise) 或[自管理的 GitLab 实例](https://about.gitlab.com/install)之间的连接：

1. 登录 [App Store Connect](https://appstoreconnect.apple.com)，前往「Users and Access」。
2. 选择「Xcode Cloud」选项卡。
3. 将光标移到你想要移除的 SCM 提供方上，然后点按「移除」按钮（-），并确认你想要断开 Xcode Cloud 与该提供方的连接。

要断开 Xcode Cloud 与 [Bitbucket](https://bitbucket.org)、[GitHub](https://github.com) 或 [GitLab](https://gitlab.com) 之间的连接：

1. 登录 [App Store Connect](https://appstoreconnect.apple.com)，点按网站右上角的账户，然后点按「Edit Profile」，前往你的个人资料设置。
2. 选择「Xcode Cloud」选项卡。
3. 在侧边栏中选择「Integrations」。
4. 点按你不再使用的 SCM 提供方旁边的「Unlink」，并确认你想要移除 Xcode Cloud 与该提供方之间的连接。

### 移除个人访问令牌或 App

要彻底移除你 SCM 提供方上 Xcode Cloud 的所有痕迹，你需要移除曾允许 Xcode Cloud 访问该仓库的 App 或个人访问令牌。此过程因每个 SCM 提供方而异：

- **[Bitbucket Cloud](https://bitbucket.org)** — 登录你的 Bitbucket Cloud 账户，前往你的个人设置。在「Access Management」分组中选择「App authorization」，撤销 Xcode Cloud 的应用程序授权。
- **[Bitbucket Server](https://bitbucket.org/product/enterprise)** — 登录你的 Bitbucket Server 账户，前往你的账户设置。选择「HTTP access tokens」，使用「Actions」\>「Revoke」按钮撤销 Xcode Cloud 的令牌。
- **[GitHub](https://github.com)** — 登录你的 GitHub 账户。如果你使用 GitHub 组织，且该组织拥有你的 Git 仓库，请遵循 GitHub Enterprise 部分描述的步骤操作。如果你不使用 GitHub 组织，请前往你的账户设置。选择「Applications」，点按 Xcode Cloud App 旁边的「Configure」，然后点按「Uninstall」以将该 GitHub App 从你的账户和仓库中移除。
- **[GitHub Enterprise](https://github.com/enterprise)** — 登录你的 GitHub Enterprise 账户，前往你的账户设置。选择「Applications」\>「Configure」，然后点按你 GitHub App 设置底部的「Uninstall」。这会将该 GitHub App 从你的仓库中移除。接下来，选择「Developer Settings」\>「GitHub Apps」，并点按 Xcode Cloud 的 GitHub App 旁边的「Edit」。前往「Advanced」部分，从你的 GitHub Enterprise 账户或组织中删除该 App。
- **[GitLab](https://gitlab.com)** — 登录你的 GitLab 账户，前往你的用户偏好设置。点按「Applications」，然后向下滚动到已授权 App 列表，撤销 Xcode Cloud App 的授权。
- **[自管理的 GitLab 实例](https://about.gitlab.com/install)** — 登录你自管理 GitLab 实例的账户，前往你的账户设置。选择「Applications」，然后删除 Xcode Cloud 对应的 App。

### 移除 Slack 集成

如果你将团队的 Slack 工作区连接到了 Xcode Cloud，那么在你删除工作流程或移除项目时，Xcode Cloud 与你 Slack 工作区之间的连接仍会保留。要移除 Slack 集成，你需要从团队的 Slack 工作区中卸载 Slack App：

1. 在浏览器中打开你的 Slack 工作区，点按「Manage」。或者，也可以点按 Slack App 中你工作区的名称，选择「Settings & administration」\>「Manage apps」。
2. 在侧边栏中选择「Installed Apps」，然后选择 Xcode Cloud App。
3. 移除该 App，并确认你想要删除 Xcode Cloud 的 Slack App。

> [!note] 注意
> 根据你团队 Slack 工作区的配置情况，你可能需要请团队的 Slack 管理员来移除该 Slack App。

## 另请参阅

### 设置与维护

- [使依赖项对 Xcode Cloud 可用](making-dependencies-available-to-xcode-cloud.md) — 在配置项目以使用 Xcode Cloud 之前，检查依赖项并使其对 Xcode Cloud 可用。
- [为你的团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 作为团队开始使用 Xcode Cloud 进行持续集成与交付。
- [跨 Xcode Cloud 工作流程共享 macOS 与 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定别名在多个工作流程之间共享配置。
- [跨 Xcode Cloud 工作流程共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 通过使用共享环境变量，将通用配置应用于多个工作流程。
- [使用 Xcode Cloud 构建 Swift 包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将你的 Swift 包或 Swift Playgrounds App 项目添加到 Xcode 项目中，以在 Xcode Cloud 中构建它。
- [为 Xcode Cloud 构建版本设置下一个构建号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 从自定构建号开始为你现有的 Mac App 编号构建版本，以避免版本冲突。
- [在 App 的 Beta 版本中为测试者提供说明](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 将文本文件添加到你的 Xcode 项目中，为 Beta 测试者提供关于测试内容的说明。
- [更改包标识符](changing-the-bundle-identifier.md) — 修改你 App 的包标识符，并在其出现的所有位置更新它。
