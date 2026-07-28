---
title: 配置你的第一个 Xcode Cloud 工作流程
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-your-first-xcode-cloud-workflow
source_url: 'https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-your-first-xcode-cloud-workflow.json'
content_hash: 'sha256:3030a34c276a9143'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 配置你的第一个 Xcode Cloud 工作流程

<sub>文章</sub>

设置你的项目或工作区，以使用 Xcode Cloud 并采用持续集成和持续交付。

## 概述

Xcode 可以帮助你配置项目或工作区，以使用 Xcode Cloud。它会分析你的项目，建议让你能够通过 Xcode Cloud 快速构建 App 或框架的配置，并让你在完成首次构建后能够轻松优化你的持续集成实践。

有关 Xcode Cloud 的更多信息，请参阅[认识 Xcode Cloud](https://developer.apple.com/wwdc21/10267)、[探索 Xcode Cloud 工作流程](https://developer.apple.com/wwdc21/10268)、[自定义你的高级 Xcode Cloud 工作流程](https://developer.apple.com/wwdc21/10269)以及[充分利用 Xcode Cloud](https://developer.apple.com/videos/play/wwdc2022-110374)。

> [!important] 重要
> 为了在配置第一个工作流程时避免问题并节省时间，在配置项目或工作区以使用 Xcode Cloud 之前，请先查阅[将项目设置为使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) 中的 Xcode Cloud 使用要求。此外，如果你的项目需要依赖项，请确保 Xcode Cloud 可以访问它们。要了解更多信息，请参阅[让 Xcode Cloud 可访问依赖项](making-dependencies-available-to-xcode-cloud.md)。

### 查看 Xcode Cloud 工作流程

当你开始配置项目或工作区以使用 Xcode Cloud 时，Xcode 会分析你的项目以检测其设置，然后创建其 App 和框架的列表——称为*产品（products）*。选择产品后，Xcode 会为其建议一个初始工作流程。工作流程是你希望 Xcode Cloud 执行的步骤的配置。

工作流程包含以下设置：

- 通用信息，例如工作流程的名称和描述。
- 临时构建环境的 Xcode 和 macOS 版本。请注意，Xcode Cloud 可能会定期更新可用的 macOS 和 Xcode 版本，并要求你更新工作流程，以便它们能继续成功构建。
- 定义 Xcode Cloud 何时运行工作流程的启动条件。
- Xcode Cloud 执行的操作。你可以为工作流程配置多个操作。可用的操作包括：构建、分析、测试和归档。
- Xcode Cloud 执行的后置操作。例如，你可以配置自定义通知，或通过 [TestFlight](https://developer.apple.com/testflight/) 向测试人员分发新版本的 App。
- 用于执行特定任务（例如安装第三方工具）的自定义构建脚本。更多信息，请参阅[编写自定义构建脚本](writing-custom-build-scripts.md)。

在查看建议的工作流程后，你将 Xcode Cloud 连接到你的 Git 仓库并运行工作流程，这称为*构建（build）*。

> [!note] 注意
> Xcode Cloud 会在一个私有、隔离且临时的构建环境中克隆你的仓库。它不会存储你的源代码，并安全地处理任何已存储的数据（例如你的派生数据），并保持其私密性。Xcode Cloud 使用的临时构建环境包含 macOS 和 Xcode 附带的工具（如 Python），以及 [Homebrew](https://brew.sh)，以支持安装第三方依赖项和工具。更多信息，请参阅[让 Xcode Cloud 可访问依赖项](making-dependencies-available-to-xcode-cloud.md)。

Xcode Cloud 完成构建后，它会：

- 发送一封电子邮件，其中包含有关构建的信息，包括指向 Xcode 和 [App Store Connect](https://appstoreconnect.apple.com) 中构建报告的链接。
- 存储构建的*构建产物（artifacts）*，并使其可以在 Xcode 或 App Store Connect 中下载。

Xcode Cloud 创建的构建产物包括：

- 详细的构建日志
- 导出的 App 归档、App 二进制文件或框架
- 测试结果包，包括你在自动化用户界面测试中创建的屏幕截图

> [!important] 重要
> 你可以从 Xcode Cloud 完成构建的那一刻起，在 30 天内访问构建信息和构建产物。对于将在 App Store 上发布 App 的工作流程，请务必下载并存档构建产物。更多信息，请参阅下面的[下载并存档构建产物](configuring-your-first-xcode-cloud-workflow.md#Download-and-archive-build-artifacts)。

使用 Xcode 来初始配置你的项目或工作区以使用 Xcode Cloud。完成首次构建后，使用 Xcode 或 App Store Connect 来配置额外的工作流程、访问构建信息等。更多信息，请参阅[在 Xcode 中创建额外的工作流程](configuring-your-first-xcode-cloud-workflow.md#Create-additional-workflows-in-Xcode)。

> [!note] 注意
> 如果你使用 `.xcconfig` 文件来设置 Bundle Identifier，或使用它们来自动更改 Bundle Identifier，你需要额外步骤才能开始使用 Xcode Cloud。首先，在项目或工作区的“签名与功能”面板中为你的 App target 设置 Bundle Identifier。然后按照下文所述配置你的第一个工作流程。对每个 Bundle Identifier 重复此过程。请注意，你需要使用 App Store Connect 来查看你的工作流程和构建，因为 Xcode 依靠显式设置的 Bundle Identifier 来显示它们。

### 选择归档操作

对于你想要使用 Xcode Cloud 构建的每个 App 或框架，请确保其对应的 Scheme 使用了归档操作。选择“Product”>“Scheme”>“Edit Scheme”。在侧边栏中，点击“Build”，然后在详细信息区域中，为目标选中“Archive”复选框。

![一张截图，显示了 Fruta App 的 Scheme，其中启用了归档操作。](../../../attachments/e945f8514d710390e42820ba221438d6/Configuring-Your-First-Xcode-Cloud-Workflow-1@2x.png)

要找出项目中的哪些 Scheme 使用了归档操作，请在终端中运行以下命令：

```bash
xcodebuild -project Example.xcodeproj -describeAllArchivableProducts -json
```

Xcode 使用相同的命令来查找可以使用 Xcode Cloud 构建的可用产品。

### 选择产品

要配置你的项目或工作区以使用 Xcode Cloud，请在 Xcode 中打开你的项目或工作区。在报告导览中，点击“Cloud”按钮，然后点击“Get Started”。

> [!important] 重要
> 如果你开发 WatchKit App 和 watchOS App 扩展，你可以为它们配置 Xcode Cloud 工作流程，但如果你未在开发者帐户中注册它们的 Bundle ID，它们可能会失败。要使用 Xcode Cloud 成功构建它们，请先登录你的[开发者帐户](http://developer.apple.com/account/)，导航到“Certificates, Identifiers & Profiles”部分，并在为它们配置 Xcode Cloud 工作流程之前，手动添加你的 WatchKit App 和 watchOS App 扩展的 Bundle ID。

Xcode 会分析你的项目或工作区，然后在“Select a Product”表单中为其找到的产品创建一个列表。选择与你的 App 或框架匹配的产品，然后点击“Next”。

![一张 Xcode 中“Select a Product”表单的截图，列出了 Fruta App 的所有产品。](../../../attachments/07ee5eb73ec5e84c53b4716d0a544368/Configuring-Your-First-Xcode-Cloud-Workflow-3@2x.png)

如果你的项目包含使用相同 Bundle Identifier 的 target，Xcode Cloud 会将它们视为一个产品。请注意，一个产品只能有一个 Bundle ID，并且一个 Bundle ID 总是恰好匹配一个 Xcode Cloud 产品。如果你的工作区或项目包含多个 App target：

- 如果可能，请在你的 App 的各个平台版本之间共享相同的 Bundle ID。例如，为你的 App 的 iOS、macOS 和 watchOS 版本使用相同的 Bundle ID。
- 如果每个版本的 App 都使用不同的 Bundle ID——例如，iOS 版本使用 `com.example.myiosapp` 而 macOS App 使用 `com.example.mymacapp`——Xcode 会检测到多个产品。在创建第一个工作流程时选择其中一个，稍后再为其他产品配置额外的工作流程。

你可能属于多个 Apple Developer Program 团队。在这种情况下，Xcode 会要求你选择一个团队。选择你打算用于通过 TestFlight 向测试人员分发，以及在 App Store 中发布 App 的团队。

### 查看建议的工作流程

根据你选择的产品，Xcode 会建议一个初始工作流程，该工作流程：

- 针对你的 Git 仓库默认分支的每次更改，以及针对目标为默认分支的每个拉取请求，启动一次构建
- 为其临时构建环境使用最新的已发布 macOS 和 Xcode 版本
- 使用归档操作
- 发送一封包含构建信息的电子邮件，包括指向 Xcode 和 App Store Connect 中构建报告的链接

在开始你的首次构建之前，请查看建议的工作流程；例如，验证 Xcode 是否选择了正确的 Scheme。

查看建议的工作流程：

1. 在“Review Workflow”表单中点击“Edit Workflow”。
2. 在显示工作流程信息的表单中，仅在必要时进行更改并保存。
3. 在“Review Workflow”表单中，点击“Next”并按照步骤授予 Xcode Cloud 对你源代码仓库的访问权限。

![一张 Xcode 中为 Fruta App 建议的工作流程的截图。](../../../attachments/f00fe5c3b5dd12f29978feca81c98da4/Configuring-Your-First-Xcode-Cloud-Workflow-4@2x.png)

> [!tip] 提示
> 让你的第一个工作流程保持简单，如果可能的话，使用建议的设置。这样，你就能熟悉 Xcode Cloud，而无需担心错误配置第一个工作流程。当 Xcode Cloud 成功完成你的首次构建后，编辑工作流程以满足你的需求，或在 Xcode 或 App Store Connect 中创建额外的工作流程来优化你的 CI/CD 实践。

### 授予 Xcode Cloud 对你源代码的访问权限

Xcode Cloud 需要访问包含你代码的 Git 仓库。它使用此访问权限在你进行更改时自动构建和测试你的代码。当你配置项目或工作区以使用 Xcode Cloud 时，Xcode 会分析它以检测你使用的源代码管理（SCM）提供商。在“Grant Access to Your Source Code”表单中，点击“Grant Access”，让 Xcode 引导你完成 SCM 提供商的授权过程。

> [!important] 重要
> 确保你具有授予 Xcode Cloud 访问你的 Git 仓库所需的权限或角色。此外，如果你使用自托管的 SCM 提供商——例如 Bitbucket Server 或 GitHub Enterprise——请确保 Xcode Cloud 可以访问你的 Git 仓库。有关所需权限、角色以及 Xcode Cloud 使用的 IP 地址范围的信息，请参阅[使用远程源代码管理仓库](setting-up-your-project-to-use-xcode-cloud.md#Use-a-remote-source-control-repository)。

![一张 Xcode 中“Grant Access to Your Source Code”表单的截图。](../../../attachments/370da2c2fcf558030fd8b44500dac3b6/Configuring-Your-First-Xcode-Cloud-Workflow-5@2x.png)

在允许 Xcode Cloud 访问你的 Git 仓库后，Xcode 会指示它可以访问你的源代码。点击“Next”，然后在下一个表单中点击“Complete”。

> [!note] 注意
> 构建你的项目可能需要访问多个自托管 SCM 提供商实例——这是大型团队的常见情况。例如，你可能使用两个不同的 GitHub Enterprise 实例，其中一个托管你的 App 代码，另一个托管你的依赖项。如果你遇到这种情况，请先在 Xcode 中完成项目的初始用户引导工作流程，并连接托管 App 代码的实例，然后让首次构建失败。构建失败后，Xcode 会提供一个连接另一个实例的修复建议。

关于授予 Xcode Cloud 对你源代码访问权限的更多指导，请参阅[源代码管理设置](source-code-management-setup.md)。

### 创建 App 记录

Xcode Cloud 将 Xcode、[TestFlight](https://developer.apple.com/testflight/) 和 App Store Connect 整合到一个强大的 CI/CD 系统中。因此，你需要在 App Store Connect 中为你的 App 创建一条 App 记录。

如果你已经在 App Store Connect 中拥有 App 记录，Xcode Cloud 会自动使用它。如果你没有 App 记录，Xcode 会在你授予 Xcode Cloud 访问你的 Git 仓库后帮助你创建一个。

> [!note] 注意
> 使用 Xcode Cloud 构建框架不需要 App 记录。

要创建 App 记录，你需要对你的团队拥有“App 管理”、“管理员”或“帐户持有者”角色。如果你具有“开发者”角色，则需要“创建 App”权限。如果你没有所需的角色或权限，请参阅[在 App Store Connect 中创建 App 记录](configuring-xcode-cloud-for-your-team.md#Create-an-app-record-in-App-Store-Connect)。

### 开始你的首次构建

在授予 Xcode Cloud 访问你的 Git 仓库的权限，并在必要时创建 App 记录后，你就可以开始首次构建了。从弹出菜单中选择一个分支，然后点击“Start Build”。Xcode Cloud 会检出该分支并开始构建你的代码。

![一张 Xcode 中 Fruta App 的“Start Build”表单的截图。](../../../attachments/7450d7c337f31cf4f7a578035b6be55c/Configuring-Your-First-Xcode-Cloud-Workflow-6@2x.png)

要在编辑器面板中查看进行中构建的信息，请在报告导览中选择该构建。要查看详细的构建日志，请在报告大纲中展开一个操作并点击“Logs”。如果报告大纲不可见，请使用编辑器面板右上角的“Adjust Editor Options”按钮启用它。

当 Xcode Cloud 完成构建你的项目后，它会发送一封包含构建信息的电子邮件，包括构建状态、用于构建的提交，以及指向 Xcode 或 App Store Connect 中构建报告的链接。

> [!note] 注意
> 如果你开始为现有的 Mac App 使用 Xcode Cloud，你可能需要配置 Xcode Cloud，使其以 `1` 以外的值开始递增构建编号。更多信息，请参阅[为 Xcode Cloud 构建设置下一个构建编号](setting-the-next-build-number-for-xcode-cloud-builds.md)。

### 了解构建失败的原因

你的首次构建有可能会失败。这对于复杂的代码库和具有许多依赖项的项目尤其可能。要了解构建失败的原因，请在报告导览中选择一个构建，在报告大纲中展开一个失败的操作，并点击“Logs”查看构建日志。

![一张 Xcode 的截图，在编辑器面板中显示了失败的归档操作的详细构建信息。](../../../attachments/ba9dafa2ed0f6e806ddcbfc73e585049/Configuring-Your-First-Xcode-Cloud-Workflow-7@2x.png)

你也可以点击“Artifacts”下载构建报告。有关更多指导，请参阅[解决常见的配置和构建问题](resolving-common-configuration-and-build-issues.md)。

除了在 Xcode 中查看构建日志，你还可以按照以下步骤在 App Store Connect 中探索构建日志：

1. 登录 App Store Connect 并进入你的 App 页面。
2. 点击“Xcode Cloud”标签页。
3. 点击侧边栏中的“Builds”。
4. 展开一个工作流程并选择一个构建。
5. 在侧边栏中展开一个操作并点击“Logs”。

### 优化你的持续集成实践

在配置了第一个工作流程并成功完成首次构建后，花时间规划下一步来优化你的 CI/CD 过程，并考虑以下事项：

- 如[将你的个人 SCM 账户连接到 Xcode Cloud](configuring-xcode-cloud-for-your-team.md#Connect-your-personal-SCM-account-to-Xcode-Cloud) 所述，请同事开始使用 Xcode Cloud。
- 更改你的第一个工作流程的名称和描述。
- 为你的第一个工作流程添加一个运行单元测试的测试操作。
- 更改你的第一个工作流程的启动条件，使其仅在你更新自定义分支时启动构建，或添加启动条件。
- 添加一个后置操作，以通过 [TestFlight](https://developer.apple.com/testflight/) 向测试人员分发新版本的 App。
- 创建额外的工作流程来执行需要更长时间才能完成的高级验证；例如，配置一个每周运行一次自动化 UI 测试的工作流程。
- 为你在创建第一个工作流程时 Xcode 检测到的其他产品创建工作流程。
- 跨工作流程共享构建配置。更多信息，请参阅[在 Xcode Cloud 工作流程间共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md)和[在 Xcode Cloud 工作流程间共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md)。
- 在 [Slack](https://slackhq.com) 中接收构建信息，这是一个流行的协作工具。更多信息，请参阅[将 Xcode Cloud 连接到 Slack](connecting-xcode-cloud-to-slack.md)。
- 要求在可以合并拉取请求之前，Xcode Cloud 构建必须成功。更多信息，请参阅[配置合并拉取请求的要求](configuring-requirements-for-merging-a-pull-request.md)。

### 在 Xcode 中创建额外的工作流程

要在 Xcode 中配置和创建额外的工作流程，或对现有工作流程进行更改：

1. 点击报告导览中的“Cloud”按钮。
2. 按住 Control 键点击你的 App 名称或某个工作流程，然后选择“Manage Workflows”。
3. 在“Manage Workflows”表单中，双击一个工作流程对其进行更改，或使用添加按钮（+）添加新的工作流程。

有关创建自定义工作流程的更多信息，请参阅[为 Xcode Cloud 制定工作流程策略](developing-a-workflow-strategy-for-xcode-cloud.md)和[Xcode Cloud 工作流程参考](xcode-cloud-workflow-reference.md)。

### 在 App Store Connect 中编辑和创建工作流程

你需要在 Xcode 中配置你的第一个 Xcode Cloud 工作流程。Xcode Cloud 与 Xcode 的深度集成实现了一个集成开发流程，你可以在其中编写代码、审查更改、查看构建信息和配置工作流程。但是，团队中可能有专门的基础设施工程师或发布经理不熟悉 Xcode。为了适应他们，也为你提供一种配置工作流程和查看构建信息的额外方式，App Store Connect 也与 Xcode Cloud 深度集成。

要在 App Store Connect 中查看、编辑或创建工作流程：

1. 登录 App Store Connect 并进入你的 App 页面。
2. 点击“Xcode Cloud”标签页。
3. 点击侧边栏中的“Manage Workflows”。
4. 点击“Manage Workflows”旁边的添加按钮来创建工作流程，或点击一个工作流程来查看和编辑其设置。

通过点击工作流程的更多按钮（···），你还可以编辑、复制、停用或删除工作流程。

### 下载并存档构建产物

当 Xcode Cloud 完成工作流程的构建时，它会创建一组构建产物，其中包括构建信息、App 二进制文件、符号信息、测试结果等。Xcode Cloud 会在构建完成后最多存储构建产物 30 天。

除了需要存档过去的构建之外，下载并存档你在 App Store 上分发的 App 版本的构建产物尤其重要。这是因为在存档你的 App 时，Xcode Cloud 会创建符号信息，你可能需要这些信息来使用崩溃报告诊断问题。

要下载构建信息和构建产物，你可以使用 Xcode 或 App Store Connect。或者，使用 App Store Connect API 来自动执行下载构建产物的任务。

有关使用 App Store Connect API 自动化 Xcode Cloud 的信息，请参阅 [Xcode Cloud 工作流程和构建](../appstoreconnectapi/xcode-cloud-workflows-and-builds.md)。有关符号信息和崩溃报告的信息，请参阅[使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md)。

## 另请参阅

### 基础

- [Xcode Cloud 入门](getting-started-with-xcode-cloud.md)——在开发过程中使用 Xcode Cloud 在云端构建和测试你的 App。
- [通过 TestFlight 分发你的 Xcode Cloud 构建](distributing-your-xcode-cloud-builds-through-testflight.md)——为内部测试人员创建一个 TestFlight 分发工作流程。
- [关于使用 Xcode Cloud 进行持续集成和交付](about-continuous-integration-and-delivery-with-xcode-cloud.md)——了解如何使用 Xcode Cloud 进行持续集成和交付，以帮助你创建高质量的 App 和框架。
- [将项目设置为使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md)——在配置项目或工作区以使用 Xcode Cloud 之前，请检查帐户、项目和源代码管理要求。
