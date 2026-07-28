---
title: 配置 Wallet 支持
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-wallet-support
source_url: 'https://developer.apple.com/documentation/xcode/configuring-wallet-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-wallet-support.json'
content_hash: 'sha256:3f4e03134bc93089'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [功能](capabilities.md)

# 配置 Wallet 支持

<sub>文章</sub>

访问用户的 Wallet，以添加、更新和显示你 App 的凭证。

## 概述

iOS 与 watchOS 上的 Wallet App 允许用户管理其 _凭证_——门票、礼品卡、会员卡、登机牌以及他们在 Apple Pay 中使用的支付卡。通过与 [PassKit（Apple Pay 与 Wallet）](../passkit.md) 集成，你的 App 可以访问任何相关的凭证，并让用户管理它们。

要在你的 App 中使用 Wallet，请通过在 Xcode 中配置 App 的目标来添加该功能，并可选地指定你的 App 支持哪些凭证类型。请按照[向 App 添加功能](adding-capabilities-to-your-app.md)中的[添加功能](adding-capabilities-to-your-app.md#Add-a-capability)部分的说明操作。当进入功能库时，选择 Wallet。对于具有独立 WatchKit 扩展的 watchOS App，请将功能添加到 WatchKit Extension 的目标。macOS 或 tvOS 不支持此功能。

![](../../../attachments/82b23f93b839a1ee3d5d8904cf391802/wallet@2x.png)

<sub>Xcode 功能库的截图。顶部是一个过滤器按钮，旁边是包含占位文本“功能”的搜索字段。下方左侧窗格中列出了各种功能，例如网络扩展、Siri 和 Wallet。Wallet 功能处于选中状态。右侧是一个信息窗格，其中包含文本：“Wallet 为用户提供了一种整理凭证、门票、礼品卡、信用卡和会员卡的方式。使用 PassKit 框架 API 来显示、添加或更新用户 Wallet 中的项目。”</sub>

添加 Wallet 功能后，Xcode 会更新你的目标的 entitlement 文件，以包含 [Pass Type IDs Entitlement](../bundleresources/entitlements/com.apple.developer.pass-type-identifiers.md)——这是一个数组，包含单个通配符值 `$(TeamIdentifierPrefix)*`。此值允许你的 App 访问你在开发者账户中定义的每种凭证类型的凭证；使用该功能的配置选项，将可访问的凭证类型范围缩小到你的 App 所需的那些。

> [!important] 重要
> 该功能会获取并显示你在开发者账户中注册的凭证类型标识符；Xcode 不提供在本地注册它们的方式。有关更多信息，请参阅[创建 Wallet 标识符和证书](https://developer.apple.com/help/account/configure-app-capabilities/create-wallet-identifiers-and-certificates)。

### 将你的 App 限制为凭证类型子集

为最大程度降低潜在安全风险并帮助保护用户隐私，请按以下步骤为你的 App 仅提供其正常运行所需的凭证类型标识符的访问权限：

1. 在 Xcode 的项目导航器中选择你的项目。
2. 从 Targets 列表中选择 App 的目标。
3. 在项目编辑器中点击“签名与功能（Signing & Capabilities）”标签页。
4. 找到 Wallet 功能。
5. 选择“启用凭证类型子集（Enable subset of pass types）”选项。
6. Xcode 默认启用所有凭证类型标识符；通过取消勾选相应的复选框来禁用个别标识符。

![](../../../attachments/d40f513c0ae43a77a40ec87f2187f868/subset-of-pass-types@2x.png)

<sub>将 Wallet 功能添加到 App 的目标后的截图。“允许凭证类型子集（Allow subset of pass types）”选项处于启用状态，列出的三个凭证类型标识符中有两个也已启用。</sub>

Xcode 会更新 App 的 entitlement 文件中的 `com.apple.developer.pass-type-identifiers` 数组，使其仅包含已启用的凭证类型标识符，如果存在通配符值，则将其移除。

在启用所需的凭证类型标识符后，使用 [PKPassLibrary](../passkit/pkpasslibrary.md) 的 [passes()](<../passkit/pkpasslibrary/passes().md>) 方法来检索你的 App 可访问的凭证，或使用 [pass(withPassTypeIdentifier:serialNumber:)](<../passkit/pkpasslibrary/pass(withpasstypeidentifier_serialnumber_).md>) 来获取特定的凭证。有关创建、分发和更新凭证的更多信息，请参阅 [Wallet 凭证](../walletpasses.md)。

## 另请参阅

### 商业

- [配置 Apple Pay 支持](configuring-apple-pay-support.md) — 使用用户存储在设备上的支付信息在你的 App 中处理付款。
- [配置通过 Apple 登录支持](configuring-sign-in-with-apple.md) — 允许用户使用他们的 Apple 账户创建账户并登录你的 App。
