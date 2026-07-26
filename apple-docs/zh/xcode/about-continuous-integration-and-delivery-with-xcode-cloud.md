---
title: 关于使用 Xcode Cloud 进行持续集成与交付
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud.json'
content_hash: 'sha256:89c3665a90feb7ad'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 关于使用 Xcode Cloud 进行持续集成与交付

<sub>文章</sub>

了解使用 Xcode Cloud 进行持续集成与交付如何帮助你打造高质量的 App 和框架。

## 概述

Xcode 由一整套工具组成，你用它们来为 Apple 平台构建、测试和发布 App 与框架。当你添加新特性、支持更多设备和平台时，你的 App 或框架及其代码库会变得越来越复杂，这让确保其质量变得更加困难。借助 Xcode Cloud，你可以采用 _持续集成与交付_（CI/CD）——这是一种用于监控、保障并提升 App 和框架质量的标准做法。

Xcode Cloud 是一套使用 Git 进行源代码管理的 CI/CD 系统，它为你提供了一套集成系统，以确保你代码库的质量与稳定性。它还能帮助你高效地发布 App。通过将 [Xcode](https://developer.apple.com/xcode/) 与 Apple 用于构建和测试代码的云基础设施相结合——再加上 [TestFlight](https://developer.apple.com/testflight/) 和 [App Store Connect](https://appstoreconnect.apple.com)——Xcode Cloud 让你能够轻松做到以下几点：

- 自动构建和测试你的代码。
- 频繁且自动地在模拟器中的 Apple 设备上测试你的 App。
- 接收来自 Xcode Cloud 的通知，在错误演变成严重问题之前发现它们。
- 使用 TestFlight 向团队成员和测试人员分发你 App 的新版本。
- 在将 App 的新版本发布到 App Store 之前，先让它们进入 App 审核。
- 借助 Xcode 和 Apple 的云基础设施进行协同软件开发。

![](../../../attachments/bca93b3fc3895d146eeb3773171a9c1f/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud-1@2x.png)

<sub>展示持续集成与交付迭代过程的示意图，该过程由构建、测试、分发以及收集反馈以修复问题和验证变更这几个环节组成。</sub>

你不需要一次性引入持续集成与交付的方方面面。相反，可以采取循序渐进、稳扎稳打的方式，先使用 [Git](https://git-scm.com) 来管理你项目的源代码。等你熟悉了 Git 的工作流程和流程规范后，再将你的项目配置为在最基础的层面使用 Xcode Cloud——用于持续构建和测试你的项目。随着你对 Xcode Cloud 工作原理的了解逐渐加深，你可以开始利用它的 CD 特性，比如通过 TestFlight 分发测试版构建。

### 源代码管理的作用

管理 App 代码的变更可能并不容易，尤其是在你同时处理多项变更时更是如此。为了帮助你组织、管理并记录源代码的变更，Xcode 支持通过 Git 进行源代码管理。通过使用源代码管理，你可以跟踪和审查代码变更，从而提升项目质量。

由于源代码管理在 CI/CD 中扮演着如此基础的角色，Xcode Cloud 要求你的代码存放在 Git 仓库中。它支持以下 _源代码管理_（SCM）提供方：

- [Bitbucket Cloud](https://bitbucket.org) 和 [Bitbucket Server](https://bitbucket.org/product/enterprise)
- [GitHub](https://github.com) 和 [GitHub Enterprise](https://github.com/enterprise)
- [GitLab](https://gitlab.com) 和 [self-managed GitLab](https://about.gitlab.com/install)

> [!note] 注意
> Xcode Cloud 自带对 [Git LFS](https://git-lfs.github.com/) 的支持。

要进一步了解 Xcode 的源代码管理，请参阅 [Source control management](source-control-management.md)。

### 自动化构建与测试的重要性

典型的开发流程始于修改代码，然后构建项目，并在模拟器或测试设备上运行你的 App。你的流程甚至可能包括：通过运行你用 [Swift Testing](../testing.md) 或 [XCTest](../xctest.md) 创建的单元测试，以及运行集成测试、性能测试或用户界面测试，在本地验证变更。

尽管 Xcode 可以缩短完成这些任务所需的时间，但它们仍然会占用你大量的时间。对于支持众多设备和操作系统的复杂 App 或框架来说尤其如此。而借助 Xcode Cloud，你可以用比传统方式更短的时间，在多台模拟设备上构建、运行和测试你的项目。

![](../../../attachments/2427429f22f500f2ccc63735bf2e77bc/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud-2@2x.png)

<sub>展示自动化构建与测试各个步骤的示意图：一次变更会引发自动化构建、测试以及其他用于验证该变更的操作。</sub>

在验证一项变更后，Xcode Cloud 会自动通过电子邮件通知你结果。你也可以在 Xcode 或 App Store Connect 中查看结果。这能帮助你在错误演变成问题之前就发现它们，让你对代码的稳定性与质量更加放心。

关于使用 Xcode Cloud 自动构建项目的更多信息，请参阅 [Configuring your first Xcode Cloud workflow](configuring-your-first-xcode-cloud-workflow.md)。

关于测试代码的更多信息，请参阅 [Testing](testing.md)。

### 持续交付

持续集成（CI）的另一面是持续交付（CD）。虽然自动化构建与测试对打造高质量的 App 和框架至关重要，但它并不能取代团队成员和测试人员进行的实际动手测试。当 Xcode Cloud 验证完对代码的一项变更后（CI），它可以通过 [TestFlight](https://developer.apple.com/testflight/) 自动将你 App 的新版本交付（CD）给内部测试人员。Xcode Cloud 还可以为你的 App 签名，以便通过 TestFlight 进行外部测试，以及提交给 App 审核。你也可以将导出的 App 归档或框架上传到自己的服务器。

![](../../../attachments/35478ba6fa547f5adb9387b9e78b99b6/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud-3@2x.png)

<sub>展示 CI 通过之后 CD 各个步骤的示意图：分发给内部测试人员、外部测试人员，以及 App Store。</sub>

### 使用 Xcode Cloud 进行协同软件开发

使用 Git 进行源代码管理能帮助你管理代码变更。例如，Git 分支让你可以在不影响已验证、稳定的代码库的情况下进行修改。此外，当你以团队形式开发 App 或框架时，分支也很有用。不过，合并变更、解决冲突以及验证代码变更可能会很耗时。

为了让代码审查和合并更轻松，SCM 提供方支持 _拉取请求_（PR，又称合并请求）。当你创建一个 PR 时，就是在告知团队某项变更已准备好接受审查，你和团队成员可以互相查看对方的代码变更，并在合并分支之前给出和处理反馈。

![](../../../attachments/352978554e67a633b443c9a585695f1f/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud-4@2x.png)

<sub>展示使用 Git 进行协同软件开发工作流的示意图。团队成员创建一个 PR，收集反馈，处理反馈，最终合并分支。</sub>

如果你以团队形式开发代码，或者同时处理多项变更，一种常见的做法是为每项变更单独建立分支，然后创建 PR 以接受同事的代码审查。这引入了另一道验证环节，帮助你在错误演变成严重问题之前发现它们。

如果你将 Git 仓库托管在 [Bitbucket Server](https://bitbucket.org/product/enterprise)、[GitHub](https://github.com) 或 [GitHub Enterprise](https://github.com/enterprise) 上，Xcode 允许你创建、查看和评论 PR，并将变更合并到你的代码库中。

![](../../../attachments/b158559eb1ebf931b65b806796cc8445/About-Continuous-Integration-and-Delivery-with-Xcode-Cloud-5@2x.png)

<sub>展示 Xcode Cloud 如何与拉取请求集成的示意图。当有人创建拉取请求时，Xcode Cloud 会检测到这一变更，构建项目，运行已配置的测试，并将状态发布到该拉取请求上。</sub>

你还可以将 Xcode Cloud 配置为检测新的 PR，或对现有 PR 的变更。当它检测到变更时，Xcode Cloud 会在一个临时构建环境中合并相关分支，并自动构建你的项目、运行测试，以验证合并后的代码。验证完变更后，Xcode Cloud 会在该 PR 上添加一条状态消息，告知你结果。

> [!tip] 提示
> 借助你 SCM 提供方的网站，你可以要求 Xcode Cloud 构建成功后，团队成员才能完成该 PR 并合并分支。

## 另请参阅

### Essentials

- [Getting started with Xcode Cloud](getting-started-with-xcode-cloud.md) — 在开发过程中使用 Xcode Cloud 在云端构建和测试你的 App。
- [Distributing your Xcode Cloud builds through TestFlight](distributing-your-xcode-cloud-builds-through-testflight.md) — 为内部测试人员创建一个 TestFlight 分发工作流。
- [Setting up your project to use Xcode Cloud](setting-up-your-project-to-use-xcode-cloud.md) — 在配置你的项目或工作区以使用 Xcode Cloud 之前，先了解账户、项目和源代码管理方面的要求。
- [Configuring your first Xcode Cloud workflow](configuring-your-first-xcode-cloud-workflow.md) — 配置你的项目或工作区以使用 Xcode Cloud，并采用持续集成与交付。
