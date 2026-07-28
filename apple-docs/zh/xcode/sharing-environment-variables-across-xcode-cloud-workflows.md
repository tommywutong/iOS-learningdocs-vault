---
title: 在 Xcode Cloud 工作流程之间共享环境变量
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows
source_url: 'https://developer.apple.com/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows.json'
content_hash: 'sha256:d2430238758cd707'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 在 Xcode Cloud 工作流程之间共享环境变量

<sub>文章</sub>

使用共享环境变量将通用配置应用于多个工作流程。

## 概述

你可以在自定构建脚本中使用共享环境变量来扩展工作流程。例如，使用共享环境变量表示 IPA 文件的位置。这样，你就可以在一处编辑通用环境变量的值。

开始之前，请配置项目以使用 Xcode Cloud，并创建两个或更多要与之共享环境变量的工作流程。

### 在 Xcode 中管理共享环境变量

在 Xcode 中创建共享环境变量：

1. 打开项目，点按导航栏中的 Report navigator 按钮，然后点按 Cloud 按钮。
2. 在边栏中，按住 Control 键点按项目名称，然后从弹出式菜单中选择 Manage Environment Variables。
3. 在表单左下角，点按 Add 按钮（+）。
4. 在 Shared Environment Variables 表单中，输入变量的名称和值。
5. 若要安全地存储变量并确保它不会出现在任何日志中，请在 Secret 部分选择“Keep value redacted”复选框。
6. 若要按团队角色限制别名编辑，请在 Restrict Editing 部分选择 Only the Account Holder 复选框。
7. 点按 Next。
8. 在 Select Workflows 表单中，选择要应用环境变量的工作流程，然后点按 Save。
9. 在 Shared Environment Variables 表单中点按 Done。

若要在点按 Done 前编辑或删除 Shared Environment Variables 表单中的环境变量，请按住 Control 键点按该变量，然后选择 Edit 或 Delete。

> [!tip] 提示
> 你也可以选择 Integrate \> [你的项目名称] \> Manage Shared Environment Variables 来创建、编辑或删除环境变量。

在 Xcode 中将环境变量应用于工作流程：

1. 在 Report navigator 中，按住 Control 键点按项目名称，然后从弹出式菜单中选择 Manage Workflows。
2. 在表单的详细信息区域中，按住 Control 键点按要应用环境变量的工作流程，然后从弹出式菜单中选择 Edit。
3. 在边栏中点按 Environment。
4. 在 Environment Variables 下，选择要应用于工作流程的环境变量。
5. 点按 Save。

若要创建另一个环境变量，请点按 Add 按钮，然后从弹出式菜单中选择 New Shared Environment Variable。

### 在 App Store Connect 中管理共享环境变量

你还可以通过以下步骤，在 App Store Connect 中将共享环境变量应用于工作流程：

1. 登录 App Store Connect 账户并前往 App 页面。
2. 点按 Xcode Cloud 标签页。
3. 在边栏中点按 Settings。
4. 点按 Shared Environment Variables 标签页。
5. 在 Shared Environment Variables 旁边点按 Add 按钮。
6. 在 New Shared Environment Variable 表单中输入变量的名称和值。
7. 若要安全地存储变量并确保它不会出现在任何日志中，请选择 Secret 复选框。
8. 若要按团队角色限制别名编辑，请选择 Only the Account Holder 复选框。
9. 点按 Next。
10. 在 Select Workflows 表单中，选择要应用环境变量的工作流程。
11. 点按 Save。

若要编辑或删除自定别名，请点按环境变量旁边的 More（…），然后从弹出式菜单中选择 Edit 或 Delete。

## 另请参阅

### 设置和维护

- [使依赖项可供 Xcode Cloud 使用](making-dependencies-available-to-xcode-cloud.md) — 在配置项目以使用 Xcode Cloud 之前，检查依赖项并使其可供 Xcode Cloud 使用。
- [为团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 以团队形式开始使用 Xcode Cloud 进行持续集成和交付。
- [在 Xcode Cloud 工作流程之间共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定别名与多个工作流程共享配置。
- [使用 Xcode Cloud 构建 Swift 软件包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将 Swift 软件包或 Swift Playgrounds App 项目添加到 Xcode 项目，以便在 Xcode Cloud 中构建。
- [设置 Xcode Cloud 构建版本的下一个构建号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 为现有 Mac App 从自定构建号开始编号，以避免版本冲突。
- [随 App 的 Beta 版本附上测试员备注](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 将文本文件添加到 Xcode 项目，为 Beta 测试员提供测试内容的说明。
- [从 Xcode Cloud 移除项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 移除项目，以删除 App 和工作流程数据、断开 Git 仓库连接并移除 Slack 集成。
- [更改捆绑包标识符](changing-the-bundle-identifier.md) — 修改 App 的捆绑包标识符，并在其出现的所有位置更新它。
