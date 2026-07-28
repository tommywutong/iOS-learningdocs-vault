---
title: 测试 beta 版操作系统
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/testing-a-beta-os
source_url: 'https://developer.apple.com/documentation/xcode/testing-a-beta-os'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/testing-a-beta-os.json'
content_hash: 'sha256:7a5bd7f4923c63fd'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [分发](distribution.md)

# 测试 beta 版操作系统

<sub>文章</sub>

通过测试 beta 版操作系统（beta OS）版本来管理 App 中非预期的差异。

## 概述

要发现 API 问题或不兼容性，请在 beta 版发布周期中，在每个已发布的 beta 版本上测试你的 App。Beta 版软件可能会在你的 App 中引入新问题。为了降低这些问题影响用户的可能性，请在 beta 版发布周期中尽早识别、报告并解决它们。随着 beta 版发布周期的推进，以及 Apple 将 beta 版提升为 Release Candidate（候选发布版），在不引起其他不稳定的情况下进行更改会变得更加困难，因此请在发现问题后立即报告。

### 安装 beta 版操作系统

要开始在 beta 版操作系统上测试你的 App，请在你打算用于测试的设备上下载并安装 beta 版操作系统。在你的 App 可用的每个平台（Mac、Apple TV、Apple Watch、iPhone 或 iPad）的 beta 版操作系统上测试你的 App。要查找每个平台的最新 beta 版操作系统，以及有关准备安装 beta 版操作系统的信息，请参阅[使用 Apple Beta 版软件](https://developer.apple.com/support/beta-software/)。

### 安装你的 App

要发现用户在新版操作系统上使用当前版本的 App 时可能遇到的问题，请从 [App Store](https://www.apple.com/app-store/) 或 [TestFlight](https://developer.apple.com/testflight/) 将当前版本的 App 安装到你的测试设备上。使用 beta 版 SDK 重新构建你的 App 可能会引入用户在当前版本的 App 中不会遇到的额外变化。

### 测试 API 行为的变化

你使用的系统框架中的 API 的行为在不同版本之间可能会发生变化。要识别行为变化，请通过执行 App 中的所有代码路径来彻底测试你的 App。针对你的 App 支持的每个主要操作系统版本，在用户使用的每类设备中至少在一台设备上进行测试。设备类别具有相同的架构、屏幕分辨率和硬件能力。至少，使用模拟器（Simulator）测试你的 iOS、iPadOS、tvOS、visionOS 和 watchOS App。但是，模拟器提供的测试覆盖范围有限，不能替代具有实际内存和性能限制的物理硬件。

如果你没有注意到任何问题或 API 行为的变化，则无需对 App 进行任何更改，但你仍需测试每个 beta 版本。如果你注意到 App 的某部分行为发生了变化，这可能是由 beta 版操作系统中 API 行为的变化引起的。

一旦你识别出 App 行为的变化，请定位代码中与那个行为相关的部分。在这部分代码中，找出涉及的系统框架 API，然后使用 [Feedback Assistant](https://developer.apple.com/bug-reporting/) 报告 API 行为的变化。提交反馈时，请附上一个可重现问题的可运行 Xcode 项目，并提供对问题的清晰描述，详细说明观察到的行为与预期行为之间的差异。

请记得为每个后续的 beta 版本更新你的反馈。在 beta 版发布周期中尽早并经常报告问题，可以在操作系统修订版公开发布之前获得问题解决的最佳机会。

### 处理 API 行为的变化

如果你观察到的行为变化是由代码中的 Bug 引起的，你可以直接解决该问题。要调试该问题，请使用包含你正在测试的 beta 版操作系统的 SDK 的 Xcode beta 版重新构建你的 App。

使用新的 SDK 重新构建你的 App 可能会导致 API 行为的进一步变化，因此在重新构建后，遵循相同的 beta 版测试流程来识别和报告新的变化。此外，使用新的 SDK 重新构建你的 App 可能会导致 App 在旧版操作系统上运行时发生变化。为避免遗漏可能发生在独特设备配置上的问题，每当你使用新的 SDK 重新构建 App 时，请在用户可能拥有的每种设备配置上进行测试。

[开发者论坛（Developer Forums）](https://developer.apple.com/forums/) 是讨论代码问题的可能变通方案和解决方案的绝佳资源。

> [!important] 重要
> 使用 Feedback Assistant 报告所有问题。在开发者论坛上讨论问题是在你报告问题之后的有用第二步。

如果你发现 API 行为的变化在较旧的非 beta 版操作系统上也可以重现，请使用 [Feedback Assistant](https://developer.apple.com/bug-reporting/) 报告该问题。在你的反馈中提及所有可以重现该问题的操作系统版本，并同时附上一个能演示该问题的可运行 Xcode 项目。如果你在调查该问题的变通方案时需要帮助，请[提交开发者技术支持事件（Developer Technical Support Incident）](https://developer.apple.com/support/technical/)以获取 Apple 开发者技术支持团队（DTS）的帮助。

## 另请参阅

### 测试

- [测试发布版本](testing-a-release-build.md) — 在模拟的用户环境中运行你的 App，以发现并识别部署错误。
