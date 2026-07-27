---
title: 配置你 Xcode Cloud 工作流的操作
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions
source_url: 'https://developer.apple.com/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-your-xcode-cloud-workflow-s-actions.json'
content_hash: 'sha256:ec0f33643c737c99'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Xcode Cloud workflow reference](xcode-cloud-workflow-reference.md)

# 配置你 Xcode Cloud 工作流的操作

<sub>文章</sub>

为 Xcode Cloud 工作流添加操作，以便在执行构建时对你的 App 或框架进行构建、测试、分析和归档。

## 概述

借助 Xcode Cloud，你可以创建自定工作流，采用灵活的持续集成与交付（CI/CD）实践。例如，配置一个通过构建和测试来验证更改的工作流，一个执行深入验证的工作流，另一个定期向测试人员分发新版本 App 的工作流，等等。每个工作流的核心，都是 Xcode Cloud 在构建期间执行的操作。

如果你刚开始创建自定工作流，请参阅[为 Xcode Cloud 制定工作流策略](developing-a-workflow-strategy-for-xcode-cloud.md)。有关其他工作流设置的更多信息，请参阅 [Xcode Cloud 工作流参考](xcode-cloud-workflow-reference.md)。

你需要先使用 Xcode 来初始配置你的项目或工作区以使用 Xcode Cloud。不过，在你开始第一次构建之后，你既可以在 Xcode 中，也可以在 [App Store Connect](https://appstoreconnect.apple.com) 中编辑和创建工作流。

有关 Xcode Cloud 工作流的更多信息，请参阅 [Explore Xcode Cloud workflows](https://developer.apple.com/wwdc21/10268) 和 [Customize your advanced Xcode Cloud workflows](https://developer.apple.com/wwdc21/10269)。

### 查看操作

一个工作流可以执行一个或多个与你项目或工作流方案操作相匹配的操作。可从以下操作中选择：

- Build
- Test
- Analyze
- Archive

例如，配置一个工作流，为每个平台执行构建、测试和归档操作。

使用 Xcode Cloud 时值得遵循的一个良好实践，是创建一组各自执行不同操作的工作流。例如，你可以有一个工作流，在分支或拉取请求发生更改时执行构建和测试操作；再有一个工作流，在你把代码合并到 `main` 分支时执行构建、测试、分析和归档操作。

![一幅插图，展示了 Xcode Cloud 作为某个操作的一部分所执行的不同步骤。](../../../attachments/0afec4810e2050809f0c42ba211c2a3f/Configuring-Your-Xcode-Cloud-Workflow-s-Actions-1@2x.png)

当 Xcode Cloud 执行一个操作时，它会：

- 创建一个临时构建环境。
- 从连接的仓库中克隆你的源代码。
- 解析依赖项。
- 如果适用，按照[编写自定构建脚本](writing-custom-build-scripts.md)中所述运行自定构建脚本。
- 执行该操作。
- 保存构件。

> [!note] 注意
> Xcode Cloud 在一个临时构建环境中分别执行每个操作。因此，某个操作的构件可能无法供其他操作使用。例如，测试操作的测试结果包，其他操作是无法使用的。

### 向工作流添加操作

要向工作流添加操作，首先在 Xcode 中或在 [App Store Connect](https://appstoreconnect.apple.com) 网站的 Xcode Cloud 标签页中打开或创建一个工作流。点按“Actions”旁边的添加按钮（+），选择一个操作，输入所需信息，从可用设置中做出选择，然后保存该工作流。之后，手动开始一次新的构建，或者等待 Xcode Cloud 开始新的构建。

下面的屏幕截图展示了 Xcode 中一个执行全部四种可用操作的工作流的“Edit Workflow”表单：

![Xcode 中一个执行全部四种可用操作的工作流的“Edit Workflow”表单的屏幕截图。](../../../attachments/55b95c6caf84cce6829eaae92d8fb8e8/Configuring-Your-Xcode-Cloud-Workflow-s-Actions-2@2x.png)

### 添加一个构建操作

验证某项更改始终能够编译通过，是 CI/CD 的关键任务之一。借助 Xcode Cloud，你可以通过一个构建操作自动执行这项验证。

要为工作流配置构建操作：

1. 在 Xcode 中或在 App Store Connect 网站的 Xcode Cloud 标签页中打开或创建一个工作流。
2. 点按“Actions”旁边的添加按钮，选择“Build”。
3. 选择一个平台和一个方案；例如，选择 macOS 以及你 macOS App 对应的方案，来构建你的 Mac App。
4. 选择你是要为任意设备还是为任意模拟器目标构建 App。对于 Mac App，可在构建 macOS 目标和 Mac Catalyst 目标之间选择。

下面的屏幕截图展示了 [Fruta app](https://developer.apple.com/documentation/swiftui/fruta_building_a_feature-rich_app_with_swiftui) 的一个 Xcode Cloud 工作流。它包含两个构建操作：一个操作构建 iOS App，另一个操作构建 macOS App：

![](../../../attachments/da28e12048d60f6e72c45475abf22e30/Configuring-Your-Xcode-Cloud-Workflow-s-Actions-3@2x.png)

<sub>一张屏幕截图，展示了 Xcode 中一个包含两个构建操作的工作流：一个用于 macOS App 的构建操作，一个用于 iOS App 的构建操作。</sub>

当 Xcode Cloud 执行构建操作时，它会访问你的源代码，并运行 `xcodebuild build` 命令来创建构建产物。完成后，Xcode Cloud 会提供以下构件：构建产物、构建日志和结果包。

### 添加一个测试操作

通过运行测试来验证某项更改，是 CI/CD 实践中的另一项关键任务。虽然每个项目都有各自独特的需求，但通常合理的做法是配置两个执行测试操作的工作流：

- 一个频繁运行基础、耗时较短测试的工作流。
- 一个较少频率运行更广泛、耗时较长测试的工作流。

> [!note] 注意
> 添加测试操作会为测试构建你的 App 或框架。你不需要再添加构建操作来运行测试。

要向工作流添加测试操作：

1. 在 Xcode 中或在 [App Store Connect](https://appstoreconnect.apple.com) 网站的 Xcode Cloud 标签页中打开或创建一个工作流。
2. 点按“Actions”旁边的添加按钮，选择“Test”。
3. 为测试操作选择一个平台和一个方案。
4. 决定当测试操作失败时是否要使构建失败，然后相应地选择“Required To Pass”或“Not Required to Pass”。
5. 如果你希望测试操作使用所选方案的配置，请选择“Use Scheme Settings”。或者，如果你使用测试计划，可以选择一个测试计划。有关测试计划的更多信息，请参阅 [Testing in Xcode](https://developer.apple.com/videos/play/wwdc2019/413/) 和 [Get your test results faster](https://developer.apple.com/videos/play/wwdc2020/10221/)。
6. 点按添加按钮，至少添加一个目标。可用的目标取决于工作流的环境设置。目标数量越多，Xcode Cloud 完成一次构建所需的时间也越长。

下面的屏幕截图展示了 [Fruta app](https://developer.apple.com/documentation/swiftui/fruta_building_a_feature-rich_app_with_swiftui) 的一个 Xcode Cloud 工作流。它包含两个测试操作：一个操作测试 iOS App，另一个操作测试 macOS App。

![](../../../attachments/0a4d155813ece3cbc70d8f2e4a216021/Configuring-Your-Xcode-Cloud-Workflow-s-Actions-4@2x.png)

<sub>一张屏幕截图，展示了 Xcode 中一个包含两个测试操作的工作流：一个用于 iOS App 的测试操作，一个用于 macOS App 的测试操作。</sub>

一个测试操作分两个独立阶段运行：在第一阶段，Xcode Cloud 访问你的源代码，并使用 `xcodebuild build-for-testing` 命令创建测试产物。在第二阶段，Xcode Cloud 使用它在第一阶段创建的测试产物，通过 `xcodebuild test-without-building` 命令运行你的测试。

> [!note] 注意
> 在 Xcode Cloud 运行第二阶段测试时，源代码是不可用的。

当 Xcode Cloud 完成测试操作时，它会提供测试产物以及包含测试结果的结果包作为构件。

有关使用 Xcode Cloud 运行测试的更多信息，请参阅 [Author fast and reliable tests for Xcode Cloud](https://developer.apple.com/wwdc22/110361)。

### 添加一个分析操作

除了构建和测试你的代码之外，使用 Xcode 对代码进行分析还能帮助你验证代码中没有内存泄漏和其他问题。不过，由于分析代码需要时间，你可能不会经常进行分析，从而导致问题不断累积。为 Xcode Cloud 工作流添加分析操作，可以确保你定期分析代码，在问题真正成为麻烦之前就发现错误。

要向工作流添加分析操作：

1. 在 Xcode 中或在 [App Store Connect](https://appstoreconnect.apple.com) 网站的 Xcode Cloud 标签页中打开或创建一个工作流。
2. 点按“Actions”旁边的添加按钮，选择“Analyze”。
3. 为分析操作选择一个平台和一个方案。
4. 决定当分析操作失败时是否要使构建失败，然后相应地选择“Required To Pass”或“Not Required to Pass”。

当 Xcode Cloud 执行分析操作时，它会访问你的源代码，并运行 `xcodebuild analyze` 命令来执行静态代码分析。完成后，Xcode Cloud 会提供构建日志作为构件。

### 添加一个归档操作

当你准备好向测试人员分发你的 App 或框架，或者准备发布它时，通常会用 Xcode 对你的 App 或框架进行归档。要自动完成这项任务，请为 Xcode Cloud 工作流添加归档操作。实际上，如果你要通过 TestFlight 向测试人员分发新版本的 App，或在 App Store 上发布，归档操作是必需的。

如果你配置一个工作流来归档某个 App，“Deployment Preparation”设置就是一项关键设置。它决定了 Xcode Cloud 如何为你的 App 签名。

可从以下选项中选择：

- **None** — 导出的 App 归档不适合通过 TestFlight 分发，也不适合在 App Store 上发布。如果你没有将工作流配置为分发 App，请使用此设置。
- **TestFlight（仅限内部测试）** — 导出的 App 归档适合通过 TestFlight 分发给测试人员。由于该 App 归档不适合在 App Store 上发布，请使用此设置为在你团队内部分发或通过 TestFlight 分发给内部测试人员做准备。例如，可为每夜构建、拉取请求或开发分支选择此项。
- **TestFlight and App Store** — 导出的 App 归档既适合通过 TestFlight 分发给测试人员，也适合在 App Store 上发布。对于你要分发给外部测试人员、并计划在 App Store 上发布的构建，请选择此选项。请注意，外部测试须经过 beta App 审核。

要向工作流添加归档操作：

1. 在 Xcode 中或在 [App Store Connect](https://appstoreconnect.apple.com) 的 Xcode Cloud 标签页中打开或创建一个工作流。
2. 点按“Actions”旁边的添加按钮，选择“Archive”。
3. 选择一个平台和一个方案。
4. 为“Deployment Preparation”设置选择适合你需求的选项。

当 Xcode Cloud 执行归档操作时，它会访问你的代码，并运行 `xcodebuild archive` 命令来创建导出的 App 归档或框架包。完成后，Xcode Cloud 会提供导出的 App 归档或框架包以及构建日志作为构件。
