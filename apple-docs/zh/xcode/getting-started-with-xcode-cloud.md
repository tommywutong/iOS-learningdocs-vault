---
title: 开始使用 Xcode Cloud
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/getting-started-with-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/getting-started-with-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/getting-started-with-xcode-cloud.json'
content_hash: 'sha256:fb406f90c7ce9d23'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 开始使用 Xcode Cloud

<sub>文章</sub>

在开发期间使用 Xcode Cloud 在云端构建和测试你的 App。

## 概述

Xcode Cloud 是内置于 Xcode 中的持续集成与交付 (CI/CD) 系统，用于为 Apple 平台创建 App 和框架。

在你编写代码、于开发期间快速迭代新功能，以及之后进行分发时，Xcode Cloud 会在云端跨多台设备和多个操作系统版本并行构建和测试你的 App。Xcode Cloud 能帮助你在提交更改时发现衰退、错误和性能问题。

要将你的项目添加到 Xcode Cloud，你需要：

1. 选择你的 App 或框架。
2. 将你的远程仓库连接到 Xcode Cloud。
3. 开始你的第一次构建。
4. 在报告导览器中查看状态。

将项目添加到 Xcode Cloud 后，你可以根据具体的开发和分发需求自定配置。更多信息请参阅[设置项目以使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) 和[配置你的第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md)。

之后，若要开始收集人们对你的 beta 构建版本的反馈，请参阅[通过 TestFlight 分发你的 Xcode Cloud 构建版本](distributing-your-xcode-cloud-builds-through-testflight.md)。

## 开始之前

在开始使用 Xcode Cloud 之前，你需要：

- 加入 Apple Developer Program。
- 在「Apple 帐户」设置中将你的帐户添加到 Xcode。
- 将你的项目分配给一个团队，以创建你的描述文件。
- 拥有远程源代码仓库的管理员权限。
- 将你项目的最新更改推送到远程仓库。

有关 Apple Developer Program 的信息，请参阅[成为会员](https://developer.apple.com/programs/enroll/)。

## 为你的项目配置 Xcode Cloud

要在你的项目中使用 Xcode Cloud：

1. 在 Xcode 中打开你的项目。
2. 在报告导览器中，点按 Cloud 标签页。
3. 点按下方出现的「开始使用」按钮。

![](../../../attachments/f4deb87a8597b2d337d90c0462f1ab78/xcode-cloud-get-started@2x.png)

<sub>项目窗口的截图，显示左侧报告导览器中已选中 Cloud 标签页，下方是有关 Xcode Cloud 的信息和「开始使用」按钮。</sub>

> [!note] 注意
> 如果你没有远程仓库，Xcode 会为你提供创建一个的选项。

## 在你的项目中选择产品

在出现的「选择产品」表单中，找到你的 App 或框架：

1. 从 Xcode 检测到的产品列表中选择你的 App 或框架。
2. 如有必要，为该 App 或框架选择团队。
3. 点按「下一步」。

![「选择产品」表单的截图，显示了一个可供选择的 App 以及右下角的「下一步」按钮。](../../../attachments/9e1b04c654ee8e2cb2519654886aa622/xcode-cloud-add-your-app@2x.png)

## 连接你的源代码仓库

在「连接源代码仓库」表单中，点按你仓库旁边的「连接」以授予 Xcode Cloud 访问权限。

1. 在出现的浏览器窗口中，如有必要，登录你的 App Store Connect 帐户。
2. 按照出现的说明操作，授权 Xcode Cloud 访问你的远程仓库。
3. 完成后，在 Xcode 中点按「继续」。
4. 在 Xcode 中，点按「下一步」，将你项目的远程仓库添加到 Xcode Cloud。

> [!note] 注意
> Xcode Cloud 仅在临时虚拟机上启动构建时获取你的代码。构建完成后，Xcode Cloud 会删除你的文件，绝不存储你的代码。

## 查看工作流程并开始你的第一次构建

在「设置完成」表单中，Xcode 会向你展示一个默认工作流程，该流程会：

- 在你的 `main` 分支每次发生更改时启动构建。
- 使用最新版本的 macOS 和 Xcode。
- 归档你的 App 或框架。

![](../../../attachments/14fa0c1cfb78ba50e66bf4608e8b8322/xcode-cloud-setup-complete@2x.png)

<sub>「设置完成」表单的截图，显示了「工作流程」行中的「详细信息」按钮，以及右下角的「开始第一次构建」按钮。</sub>

先使用这个基本的工作流程，之后再自定它。要编辑工作流程，点按「开始第一次构建」上方「工作流程」行中的「详细信息」，然后在出现的表单中进行更改。有关选择启动条件的更多信息，请参阅[配置启动条件](configuring-start-conditions.md)。

要开始使用 Xcode Cloud，点按「开始第一次构建」。

> [!note] 注意
> Xcode 会将有关该产品的元数据存储在你项目包中的 `xcshareddata/xcodecloud/manifest.json` 文件里。将此文件的更改推送到你的远程仓库，这样你的团队才能在 Xcode 中访问该产品。

## 查看构建进度

在报告导览器中，你可以观察构建运行。在 Cloud 面板中，展开该产品并点按工作流程。Xcode 会在右侧显示工作流程详细信息。

![](../../../attachments/0c74ec2bb3474edfd6d7fdf8acdf96be/xcode-cloud-build-report@2x.png)

<sub>报告导览器的截图，左侧是 Cloud 面板，右侧是该工作流程的构建详细信息。</sub>

如果你遇到构建问题，请参阅[解决常见的配置和构建问题](resolving-common-configuration-and-build-issues.md)。

## 在同一工作区中构建另一个目标

在报告导览器的 Cloud 面板中，从导览器左下角的「更多」弹出式菜单中选择「创建工作流程」（「集成」\> 「创建工作流程」）。在「选择产品」表单中，选择目标并点按「下一步」。在「设置完成」表单中，从「分支」弹出式菜单中选择目标分支，然后点按「开始第一次构建」。Xcode 会将一个用于构建该目标的工作流程添加到 Cloud 面板。

## 另请参阅

### 基础知识

- [通过 TestFlight 分发你的 Xcode Cloud 构建版本](distributing-your-xcode-cloud-builds-through-testflight.md) — 为内部测试人员创建 TestFlight 分发工作流程。
- [关于使用 Xcode Cloud 进行持续集成与交付](about-continuous-integration-and-delivery-with-xcode-cloud.md) — 了解使用 Xcode Cloud 进行持续集成与交付如何帮助你创建高质量的 App 和框架。
- [设置项目以使用 Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) — 在配置你的项目或工作区以使用 Xcode Cloud 之前，先了解帐户、项目和源代码控制方面的要求。
- [配置你的第一个 Xcode Cloud 工作流程](configuring-your-first-xcode-cloud-workflow.md) — 设置你的项目或工作区以使用 Xcode Cloud 并采用持续集成与交付。
