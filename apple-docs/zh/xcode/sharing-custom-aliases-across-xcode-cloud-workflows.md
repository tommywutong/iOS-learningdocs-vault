---
title: 在 Xcode Cloud 工作流程之间共享 macOS 和 Xcode 版本
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows
source_url: 'https://developer.apple.com/documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows.json'
content_hash: 'sha256:3b2ac5ad14cf1666'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 在 Xcode Cloud 工作流程之间共享 macOS 和 Xcode 版本

<sub>文章</sub>

使用自定别名与多个工作流程共享配置。

## 概述

通过自定别名，你可以设置和管理通用的 Xcode 与 macOS 配置，并将其应用于多个工作流程。例如，创建自定别名即可在一处更改多个工作流程所用的 Xcode 版本。你可以在 Xcode 和 App Store Connect 中管理自定别名。

开始之前，请配置项目以使用 Xcode Cloud，并创建两个或更多要与之共享自定别名的工作流程。

### 在 Xcode 中管理自定别名

在 Xcode 中创建自定别名：

1. 打开项目，点按导航栏中的 Report navigator 按钮，然后点按 Cloud 按钮。
2. 在边栏中，按住 Control 键点按项目名称，然后从弹出式菜单中选择 Manage Custom Aliases。
3. 在表单左下角，点按 Add 按钮（+），然后从出现的弹出式菜单中选择别名的配置（macOS 或 Xcode）。
4. 在出现的表单中输入别名名称，然后从 Version 菜单中选择要与别名关联的 macOS 或 Xcode 版本。
5. 若要按团队角色限制别名编辑，请在 Restrict Editing 部分选择 Only the Account Holder 复选框。
6. 点按 Save，然后在 Custom Aliases 表单中点按 Done。

若要在关闭 Custom Aliases 表单前快速修改别名，请按住 Control 键点按别名，然后从弹出式菜单中选择 Edit 或 Delete。若要更改权限，请从菜单中选择 Restrict Editing 或 Remove Restrictions。

> [!tip] 提示
> 你也可以选择 Integrate \> [你的项目名称] \> Manage Custom Aliases 来创建、编辑或删除自定别名。

在 Xcode 中将自定别名应用于工作流程：

1. 在 Report navigator 中，按住 Control 键点按项目名称，然后从弹出式菜单中选择 Manage Workflows。
2. 在表单的详细信息区域中，按住 Control 键点按要应用自定别名的工作流程，然后从弹出式菜单中选择 Edit。
3. 在出现的表单边栏中，点按 Environment。
4. 从 Xcode Version 或 macOS Version 弹出式菜单中选择你的自定别名。
5. 点按 Save。

若要创建另一个自定别名，请从 Environment 表单的 Version 弹出式菜单中选择 New [Xcode | macOS] Version Alias 或 Manage Custom Aliases。

### 在 App Store Connect 中管理自定别名

你还可以通过以下步骤，在 App Store Connect 中将自定别名应用于工作流程：

1. 登录 App Store Connect 账户并前往 App 页面。
2. 点按 Xcode Cloud 标签页。
3. 在边栏中点按 Settings。
4. 点按 Custom Aliases 标签页。
5. 在 Custom Aliases 旁边点按 Add 按钮，然后从出现的弹出式菜单中选择别名的配置（macOS 或 Xcode）。
6. 输入别名名称，然后从 Version 菜单中选择要与别名关联的 macOS 或 Xcode 版本。
7. 若要按团队角色限制别名编辑，请选择 Only the Account Holder 复选框。

若要编辑或删除自定别名，请点按别名旁边的 More（…），然后从弹出式菜单中选择 Edit 或 Delete。

在 App Store Connect 中将自定别名应用于工作流程：

1. 在 App 的 Xcode Cloud 页面上，点按边栏中的 Manage Workflows。
2. 选择要应用自定别名的工作流程。
3. 从 Xcode Version 或 macOS Version 弹出式菜单中选择你的自定别名。
4. 点按 Save。

## 另请参阅

### 设置和维护

- [使依赖项可供 Xcode Cloud 使用](making-dependencies-available-to-xcode-cloud.md) — 在配置项目以使用 Xcode Cloud 之前，检查依赖项并使其可供 Xcode Cloud 使用。
- [为团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 以团队形式开始使用 Xcode Cloud 进行持续集成和交付。
- [在 Xcode Cloud 工作流程之间共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 使用共享环境变量将通用配置应用于多个工作流程。
- [使用 Xcode Cloud 构建 Swift 软件包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将 Swift 软件包或 Swift Playgrounds App 项目添加到 Xcode 项目，以便在 Xcode Cloud 中构建。
- [设置 Xcode Cloud 构建版本的下一个构建号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 为现有 Mac App 从自定构建号开始编号，以避免版本冲突。
- [随 App 的 Beta 版本附上测试员备注](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 将文本文件添加到 Xcode 项目，为 Beta 测试员提供测试内容的说明。
- [从 Xcode Cloud 移除项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 移除项目，以删除 App 和工作流程数据、断开 Git 仓库连接并移除 Slack 集成。
- [更改捆绑包标识符](changing-the-bundle-identifier.md) — 修改 App 的捆绑包标识符，并在其出现的所有位置更新它。
