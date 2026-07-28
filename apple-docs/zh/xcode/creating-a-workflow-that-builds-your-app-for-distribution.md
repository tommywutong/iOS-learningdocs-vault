---
title: 创建用于构建 App 以进行分发的工作流程
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution
source_url: 'https://developer.apple.com/documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution.json'
content_hash: 'sha256:758384be73e7e060'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 创建用于构建 App 以进行分发的工作流程

<sub>文章</sub>

配置工作流程，以构建并签名你的 App，从而通过 TestFlight 分发给测试人员、在 App Store 中分发，或作为已公证的 App 分发。

## 概述

将 App 版本通过 TestFlight 分发给测试人员、上传可提交至 App Review 的版本、或共享收件人可以信任的已公证版本，这些都是持续部署（continuous deployment，CD）实践中的关键任务。根据你的偏好、需求以及由此产生的工作流程策略，配置一个能执行多个任务的 Xcode Cloud 工作流程，或创建独立的工作流程。

如果你不熟悉持续集成和交付（CI/CD），请参阅[关于使用 Xcode Cloud 进行持续集成和交付](about-continuous-integration-and-delivery-with-xcode-cloud.md)。有关制定工作流程策略的更多信息，请参阅[为 Xcode Cloud 制定工作流程策略](developing-a-workflow-strategy-for-xcode-cloud.md)。

### 配置工作流程

在创建新的工作流程以生成 App 的新版本，用于通过 TestFlight、App Store 或公证分发时，请确保：

- 限制对工作流程“通用”设置的编辑。如果你希望创建可提交至 App Review 或进行公证的构建版本，此步骤是必需的。
- 在工作流程的“环境”设置中，选择“清空（Clean）”来配置工作流程，使其在启动构建时不使用缓存数据。有关更多信息，请参阅[执行清空构建](xcode-cloud-workflow-reference.md#Perform-a-clean-build)。
- 为你希望在此工作流程中包含的每个适用平台配置一个归档操作。例如，如果你想通过一个工作流程分发 iOS 和 macOS 版本的 App，则添加两个归档操作——一个用于 iOS，一个用于 macOS。
- 如果你希望通过 TestFlight 向团队成员分发开发版本，请在归档操作的设置中选择“TestFlight（仅限内部测试）”。
- 如果你希望创建可用于 TestFlight 公开测试以及在 App Store 上架的 App 二进制文件，请在归档操作的设置中选择“TestFlight 和 App Store”。请注意，外部测试需经过 Beta 版 App Review，同样，在 App Store 上架前也需要提交 App 进行审核。
- 检查你的新工作流程是否包含测试操作。如果你使用单独的工作流程来运行全面的测试，则可能不需要配置测试操作。如果其他工作流程不运行全面测试，则可以考虑配置一个执行全面验证的测试操作。
- 选择适合你 App 测试和发布流程的启动条件。常见的启动条件是发布分支上的变更，或创建以 `release` 开头的 Git 标签。如果想手动启动工作流程的构建，可以配置一个实际永远不会启动构建的启动条件。
- 为通过 TestFlight 进行的内部或外部测试添加一个后置操作（post-action）。如果你选择外部测试，之后可以决定使用 App Store Connect 将该版本提交给 App Review。
- 在你添加的后置操作中，向 TestFlight 添加个人测试人员或测试人员分组。你添加的人员或群组便会在其测试设备上收到更新。
- 如果你打算通过自己的渠道分发 macOS App，请添加一个后置操作来公证该 App。这会将归档文件发送到公证服务以生成凭证，并将凭证信息固定到归档文件中。有关更多信息，请参阅[在分发前公证 macOS 软件](../security/notarizing-macos-software-before-distribution.md)。
- 在构建完成后，按照[下载并归档构建产物](configuring-your-first-xcode-cloud-workflow.md#Download-and-archive-build-artifacts)中的描述下载并归档构建产物。

当 Xcode Cloud 成功构建你的 App 并使其可供 TestFlight 中的测试人员使用时，并且你已将工作流程配置为创建可用于提交 App Review 的二进制文件，请按照发布 App 的必要步骤操作。有关如何使用 App Store Connect 和 TestFlight 以及在 App Store 中发布 App 的更多信息，请参阅 [App Store Connect 帮助](https://developer.apple.com/help/app-store-connect/)。

如果你的工作流程包含一个公证 App 的后置操作，你可以从成功构建操作的产物中下载已公证的版本。导航到构建操作的“产物（Artifacts）”，然后选择要下载的 App。

## 另请参阅

### 工作流程

- [为 Xcode Cloud 制定工作流程策略](developing-a-workflow-strategy-for-xcode-cloud.md) — 了解如何最好地创建自定义 Xcode Cloud 工作流程，以优化你的持续集成和交付实践。
- [Xcode Cloud 工作流程参考](xcode-cloud-workflow-reference.md) — 配置元数据、启动条件、操作、后置操作等，以创建自定义的 Xcode Cloud 工作流程。
- [了解 Xcode Cloud 基础设施验证构建](understanding-infrastructure-validation-builds.md) — 了解基础设施验证构建以及你是否需要选择退出。
