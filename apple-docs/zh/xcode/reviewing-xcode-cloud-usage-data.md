---
title: 查看 Xcode Cloud 使用数据
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reviewing-xcode-cloud-usage-data
source_url: 'https://developer.apple.com/documentation/xcode/reviewing-xcode-cloud-usage-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reviewing-xcode-cloud-usage-data.json'
content_hash: 'sha256:c4a9293e4fb67534'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 查看 Xcode Cloud 使用数据

<sub>文章</sub>

访问 Xcode Cloud 使用信息，了解你和你团队如何使用 Xcode Cloud。

## 概述

Xcode Cloud 会并行化各项任务来构建和验证你的 App，并使用 Apple 基础设施来构建、测试和分发你的 App，从而创建一个有助于打造高质量 App 的持续集成与交付（CI/CD）流程。由于 Xcode Cloud 并行执行构建步骤和操作以更快地为你提供结果，因此完成一次构建所花费的时间与 Xcode Cloud 报告的使用时间是不同的。根据你选择的订阅方案，你可支配一定量的 Xcode Cloud 使用额度。这使得查看你自己以及团队的 Xcode Cloud 使用情况变得十分重要。

要了解更多关于可用 Xcode Cloud 订阅方案的信息，请参阅[开始使用 Xcode Cloud](http://developer.apple.com/xcode-cloud/get-started)。

### 在「Apple Developer」App 中访问使用信息并购买订阅方案

「Apple Developer」App 允许你访问团队的 Xcode Cloud 使用信息，并提供购买额外使用时间的功能。要查看你团队的使用情况，请前往「Account」，然后前往「Xcode Cloud」部分。如果你拥有 Account Holder 角色，且你的团队使用 Xcode Cloud，可以使用该 App 购买提供额外 Xcode Cloud 使用时间的订阅方案。

### 在 App Store Connect 中访问更详细的使用数据

App Store Connect 允许你访问 Xcode Cloud 使用信息。它会显示使用趋势，并允许你查看团队以及每个单独 App 的详细使用信息——例如已创建的构建数量和构建持续时间。此外，你还可以将使用信息导出为 `.csv` 文件——例如用于创建自定报告。

登录 [App Store Connect](https://appstoreconnect.apple.com) 后：

- 前往「Users and Access」，然后前往「Xcode Cloud」选项卡，查看你团队整体的 Xcode Cloud 使用情况。
- 选择一个 App，前往该 App 的「Xcode Cloud」选项卡，查看该 App 的 Xcode Cloud 使用情况。

> [!note] 注意
> 每个拥有 App Store Connect 访问权限的团队成员都可以查看团队的使用数据，但他们只能查看自己有权限访问的 App 的使用信息。

以下屏幕截图展示了来自 [Food Truck：构建一个 SwiftUI 多平台 App](../swiftui/food-truck-building-a-swiftui-multiplatform-app.md) 的 Food Truck 示例代码 App 的使用情况仪表盘。它显示了 30 天内的构建数量和使用情况——包括趋势。

![](../../../attachments/629a79febcaba86e0a88cc1885289880/reviewing-usage-data@2x.png)

<sub>App Store Connect 网站的屏幕截图。它展示了 Food Truck App 的使用情况仪表盘，显示了 30 天内的使用趋势信息，包括构建数量和使用情况。</sub>
