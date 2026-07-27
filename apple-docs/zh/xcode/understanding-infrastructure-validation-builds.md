---
title: 了解 Xcode Cloud 基础设施验证构建
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-infrastructure-validation-builds
source_url: 'https://developer.apple.com/documentation/xcode/understanding-infrastructure-validation-builds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-infrastructure-validation-builds.json'
content_hash: 'sha256:8b6a9ea1447e445e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 了解 Xcode Cloud 基础设施验证构建

<sub>文章</sub>

了解基础设施验证构建，以及你是否需要选择停用。

## 概述

Xcode Cloud 偶尔可能会在你的主要生产构建之外同时运行验证构建，以确保 Xcode Cloud 的新功能和优化适用于你的特定工作流。

在这些验证期间，你可能会注意到 Xcode Cloud：

- 针对同一提交发出额外的检出请求
- 在主要构建之外运行你的自定构建脚本
- 向构建脚本调用的外部服务发送重复请求

这些临时的重复 Xcode Cloud 构建不会出现在 Xcode Cloud UI 中，也不会消耗你的构建分钟数或上传到 App Store 或 TestFlight。

在基础设施验证期间，你的源代码仍受到充分保护。所有构建均符合 Xcode Cloud 的安全保证。有关保护数据的更多信息，请参阅 [Xcode Cloud 安全性](https://developer.apple.com/xcode-cloud/security/)

### 在 App Store Connect 中停用基础设施验证构建

如果你的工作流有特定要求，可以随时选择停用。例如，如果自定构建脚本会与不应收到重复请求的外部服务交互，就可以停用这项功能。

要停用基础设施验证构建：

1. 在 [App Store Connect](https://appstoreconnect.apple.com) 中，点按 Users and Access。
2. 点按标签页栏中的 Xcode Cloud，然后点按边栏中的 Infrastructure Validation。
3. 要为所有产品停用，请在详情区域关闭「Infrastructure Validation」。
4. 要为特定产品或工作流停用，请取消选中该产品或工作流旁边的复选框。

要更快前往 Infrastructure Validation 页面，请将以下 URL 中的 `[Team ID]` 替换为你的 Team ID：`https://appstoreconnect.apple.com/teams/[Team ID]/access/ci/infrastructure-validation`。

> [!note] 注意
> 如果遇到与基础设施验证构建相关的任何问题，请停用这项功能并联系 [Apple Developer Support](https://developer.apple.com/support/)。

## 另请参阅

### 工作流

- [为 Xcode Cloud 制定工作流策略](developing-a-workflow-strategy-for-xcode-cloud.md) — 了解如何以最佳方式创建自定 Xcode Cloud 工作流，从而改进持续集成与交付实践。
- [Xcode Cloud 工作流参考](xcode-cloud-workflow-reference.md) — 配置元数据、启动条件、操作、后续操作等，以创建自定 Xcode Cloud 工作流。
- [创建用于构建 App 以供分发的工作流](creating-a-workflow-that-builds-your-app-for-distribution.md) — 配置工作流以构建并签名你的 App，以便通过 TestFlight 向测试人员分发、在 App Store 中分发，或作为经过公证的 App 分发。
