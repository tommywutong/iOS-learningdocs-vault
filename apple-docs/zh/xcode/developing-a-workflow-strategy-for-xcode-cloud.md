---
title: 为 Xcode Cloud 制定工作流策略
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud.json'
content_hash: 'sha256:2bb809b0eb108c79'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 为 Xcode Cloud 制定工作流策略

<sub>文章</sub>

审视如何以最佳方式创建自定 Xcode Cloud 工作流，以改进持续集成与交付实践。

## 概述

你可以使用 Xcode 配置项目或工作区以使用 Xcode Cloud，创建第一个工作流并开始第一次构建。Xcode Cloud 成功完成第一次构建后，请审视如何以最佳方式创建自定 Xcode Cloud 工作流，以实践持续集成与交付（CI/CD）。然后，规划改进 CI/CD 实践的后续步骤，确保你的 App 或框架始终处于可发布状态。

![](../../../attachments/bca93b3fc3895d146eeb3773171a9c1f/Developing-a-Workflow-Strategy-for-Xcode-Cloud-1@2x.png)

<sub>图中显示构建、测试、分发和收集反馈的迭代式持续集成与交付实践，以修复问题并验证更改。</sub>

如果你刚开始接触 CI/CD，请参阅[关于使用 Xcode Cloud 进行持续集成与交付](about-continuous-integration-and-delivery-with-xcode-cloud.md)，了解使用 Xcode Cloud 的 CI/CD 如何帮助你创建高质量的 App 和框架。若要进一步了解如何创建第一个工作流，请参阅[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)。

有关 Xcode Cloud 工作流的更多信息，请参阅 [Xcode Cloud 工作流参考](xcode-cloud-workflow-reference.md)、[探索 Xcode Cloud 工作流](https://developer.apple.com/wwdc21/10268) 和 [自定高级 Xcode Cloud 工作流](https://developer.apple.com/wwdc21/10269)。

### 规划后续步骤

你创建的 Xcode Cloud 工作流数量取决于项目复杂度和团队规模等因素。例如，考虑一名独自开发 iOS App 的开发者。他们可以创建一个工作流，在分支每次发生更改时构建 App 并运行单元测试。此外，他们还可以创建第二个工作流，每当创建新的 Git 标签时，在 Simulator 中的其他 Apple 设备上运行测试、归档 App，并通过 [TestFlight](https://developer.apple.com/testflight/) 向测试人员分发新版本。

相比之下，再考虑一个在企业环境中开发覆盖所有 Apple 平台 App 的团队。该团队可以创建多个工作流，用于：

- 构建工作区中的各个项目，并在每个平台的一台模拟设备上运行单元测试
- 每周执行一次额外的长时测试
- 自动向开发团队成员分发每夜构建版本
- 每两周向 QA 团队分发新版本

尽管没有适合所有人的 CI/CD 方案，但随着时间推移，按照以下步骤采用 CI/CD 是值得考虑的良好策略：

1. 确定完整的 CI/CD 实践对你而言应是什么样子。例如，列出你希望 Xcode Cloud 执行的所有验证。
2. 将完整的 CI/CD 实践转换为 Xcode Cloud 工作流。例如，如果你希望每周向测试人员分发一个 App 新版本，该任务可以转化为一个工作流。
3. 将所需工作规划为各个独立任务，逐一完成每个工作流，直到建立起完整的 CI/CD 实践。

### 编辑和创建工作流

采用 CI/CD 后，管理 Xcode Cloud 工作流会成为日常 App 开发的一部分。为了帮助你保持专注并方便使用 Xcode Cloud，请使用 Xcode 编辑 Xcode Cloud 工作流。

若要在 Xcode 中更新现有工作流：

1. 选择「Integrate」\>「Manage Workflows」，打开「Manage Workflows」表单（sheet）。
2. 双击打开现有工作流。

你也可以按住 Control 键点按报告导览器中的工作流，然后选择「Edit Workflow」。

若要在 Xcode 中创建工作流，请选择「Integrate」\>「Create Workflow」。

### 停用工作流而不是将其删除

最终，你可能想停止使用某个工作流。一种方式是在「Manage Workflows」表单中删除该工作流。但是，删除工作流会永久删除其构建历史记录和产物。只有在确定不再需要这些信息时，才应删除工作流。你可以停用工作流而不是删除它，以保留其构建历史记录和产物。

若要停用工作流：

1. 按住 Control 键点按报告导览器中的工作流，然后选择「Edit Workflow」。
2. 将表单左上角工作流名称旁边的开关切换到「Off」位置，并保存更改。

你也可以在「Manage Workflows」表单中按住 Control 键点按工作流并选择「Deactivate」，或者在 App Store Connect 网站的 Xcode Cloud 标签页中停用它。

若要重新开始使用已停用的工作流，可以随时在「Manage Workflows」表单中重新启用它；也可以打开该工作流，并将其名称旁边的开关切换到「On」位置。

![](../../../attachments/87bcce8503098665528b9e2d5973285c/Developing-a-Workflow-Strategy-for-Xcode-Cloud-3@2x.png)

<sub>Xcode 中工作流的屏幕截图，其中高亮标记了可用于启用或停用工作流的开关区域。</sub>

### 进行重大更改前复制工作流

编辑工作流时，某项更改可能会意外导致下一次构建失败。如果出现这种情况，你可以按需撤销对工作流的更改，并开始一次构建，验证它能否成功完成。不过，如果你对工作流进行了重大更改，这可能会花费大量时间。

为避免代价高昂的错误，并避免影响可能使用该工作流的同事，请在进行重大更改前复制工作流。然后，使用副本测试更改，而不影响同事。

若要复制现有工作流：

1. 在 Xcode 中打开项目或工作区，然后选择「Integrate」\>「Manage Workflows」，打开「Manage Workflows」表单。
2. 按住 Control 键点按要更改的工作流，然后选择「Duplicate」打开一个副本。
3. 重新命名副本，确保可以将其与原件区分开。
4. 保存复制的工作流。

> [!note] 注意
> 新工作流默认处于启用状态。因此，除非你停用其中一个工作流，或更改任一工作流的启动条件，否则 Xcode Cloud 会同时运行原始工作流和副本。

### 限制可以编辑工作流的人员

根据项目复杂度，创建工作流并确保 Xcode Cloud 可以成功构建项目可能会花费大量时间。若要防止团队成员无意中更改工作流，请按照以下步骤限制可以编辑它的人员：

1. 在 Xcode 或 [App Store Connect](https://appstoreconnect.apple.com) 网站中打开该工作流。
2. 导览到「General」部分，然后选中「Restrict Editing」复选框。

这样一来，只有团队中具有 Admin 或 App Manager 角色的成员才能更改该工作流。

![](../../../attachments/361a557d6f785e47913557a712cece65/Developing-a-Workflow-Strategy-for-Xcode-Cloud-4@2x.png)

<sub>屏幕截图显示 Xcode 中的工作流。「General」部分可见，并已选中「Restrict Editing」旁边的复选框。</sub>

### 在 App Store Connect 中管理工作流

在某些情况下，尤其是大型团队和企业环境中，团队成员可能更熟悉 [App Store Connect](https://appstoreconnect.apple.com)。为满足这类使用场景，在配置 Xcode 项目或工作区使用 Xcode Cloud 后，你可以在 App Store Connect 中创建和编辑工作流。

若要在 App Store Connect 中管理工作流：

1. 打开 App 页面并点按 Xcode Cloud 标签页。
2. 点按边栏中的「Manage Workflows」，显示工作流列表。
3. 点按工作流旁边的「More Options」按钮（…），然后选择要执行的操作。例如，选择「Edit」来更改工作流。

## 另请参阅

### 工作流

- [Xcode Cloud 工作流参考](xcode-cloud-workflow-reference.md) — 配置元数据、启动条件、操作、后续操作等，以创建自定 Xcode Cloud 工作流。
- [创建用于构建 App 以供分发的工作流](creating-a-workflow-that-builds-your-app-for-distribution.md) — 配置工作流，以构建并签名你的 App，供测试人员通过 TestFlight 使用、在 App Store 中分发，或作为经过公证的 App 分发。
- [了解 Xcode Cloud 基础设施验证构建](understanding-infrastructure-validation-builds.md) — 了解基础设施验证构建，以及你是否需要选择退出。
