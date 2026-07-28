---
title: 配置通过 Apple 登录支持
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-sign-in-with-apple
source_url: 'https://developer.apple.com/documentation/xcode/configuring-sign-in-with-apple'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-sign-in-with-apple.json'
content_hash: 'sha256:1f0e9a2b78a746cf'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Capabilities](capabilities.md)

# 配置通过 Apple 登录支持

<sub>文章</sub>

允许用户使用其 Apple 账户创建账户并登录你的 App。

## 概述

通过 Apple 登录让用户可以选择使用其现有的 Apple 账户登录你的 App，而无需单独创建用户名和密码。所有 Apple 设备均支持通过 Apple 登录。有关在浏览器中使用此功能的信息，请参阅 [Sign in with Apple JS](../signinwithapplejs.md)。

要在 App 中使用通过 Apple 登录，请通过 Xcode 配置 App 的 target 来添加该功能，设置用户界面与必要的授权，并向 Apple 的中继服务注册你的域名，以确保能够向用户的个人收件箱发送电子邮件。

> [!note] 注意
> 如果你的 App 面向的操作系统版本早于通过 Apple 登录的推出时间，请使用 JavaScript 库来提供相同功能。更多信息请参阅 [将通过 Apple 登录整合到其他平台](../signinwithapple/incorporating-sign-in-with-apple-into-other-platforms.md)。

### 向 App 添加“通过 Apple 登录”功能

请按照 [向你的 App 添加功能](adding-capabilities-to-your-app.md) 中 [添加功能](adding-capabilities-to-your-app.md#Add-a-capability) 一节的说明操作。进入 Capabilities 库后，选择 Sign in with Apple。对于包含独立 WatchKit 扩展的 watchOS App，请将该功能添加到 WatchKit 扩展的 target 上。

![](../../../attachments/143aa5f00cf1ae88b7a3ef75cb88d5ec/sign-in-with-apple@2x.png)

<sub>Xcode Capabilities 库截图。顶部有一个筛选按钮，旁边是一个显示占位文字 Capabilities 的搜索栏。下方左侧窗格列出了若干功能，如 Network Extensions、Wallet 和 Sign in with Apple。Sign in with Apple 功能处于选中状态。右侧信息窗格显示：启用 Sign in with Apple 后，用户可以使用其 Apple 账户进行身份验证。</sub>

添加该功能后，Xcode 将更新 target 的 entitlements，以包含 [Sign in with Apple Entitlement](../bundleresources/entitlements/com.apple.developer.applesignin.md)——这是一个数组，内含一个字符串 `Default`，该值表示正常操作。若你配置 Xcode 自动管理 App 签名，Xcode 还会在你的开发者账户中为 App 的 App ID 启用通过 Apple 登录。

> [!note] 注意
> 如果之后在 Xcode 中移除了通过 Apple 登录功能，你必须在开发者账户中手动更新 App ID 的配置，以停用通过 Apple 登录。

用户必须先提供同意，Apple 才能与你的 App 共享任何信息。如果你有多个相关联的 App——例如一个 iOS App 和一个 macOS App——请将它们的 App ID 分组，这样用户只需在首次使用的设备上提供一次同意。更多信息请参阅 [为通过 Apple 登录而将 App 分组](https://developer.apple.com/help/account/configure-app-capabilities/group-apps-for-sign-in-with-apple/)。

### 提示用户使用其 Apple 账户登录

将“通过 Apple 登录”功能添加到 Xcode 项目后，更新 App 的用户界面，让用户能够使用其 Apple 账户登录。以下步骤的参考实现，请参阅示例代码 [实现通过 Apple 登录的用户认证](../authenticationservices/implementing-user-authentication-with-sign-in-with-apple.md)。

- 使用 [ASAuthorizationAppleIDButton](../authenticationservices/asauthorizationappleidbutton.md) 或 [WKInterfaceAuthorizationAppleIDButton](../watchkit/wkinterfaceauthorizationappleidbutton.md) 将“通过 Apple 登录”按钮添加到 App 的用户界面。
- 为按钮添加一个用于创建 [ASAuthorizationAppleIDRequest](../authenticationservices/asauthorizationappleidrequest.md) 实例的处理程序。请务必设置请求的 [requestedScopes](../authenticationservices/asauthorizationopenidrequest/requestedscopes.md) 属性。更多信息请参阅 [ASAuthorization.Scope](../authenticationservices/asauthorization/scope.md)。
- 使用 [ASAuthorizationController](../authenticationservices/asauthorizationcontroller.md) 执行授权请求，提示用户使用其 Apple 账户登录，并同意 Apple 与你的 App 共享其详细信息。
- 实现 [ASAuthorizationControllerDelegate](../authenticationservices/asauthorizationcontrollerdelegate.md) 协议以确定授权请求的结果，若成功，则接收 _credential_（凭证）——一个包含用户详细信息的 [ASAuthorizationAppleIDCredential](../authenticationservices/asauthorizationappleidcredential.md) 实例。

若你的 App 将账户信息存储在远程服务器上，请将该凭证的内容发送到服务器。远程服务器在创建或更新用户账户之前，会通过 Apple 账户服务器验证数据的合法性。更多信息请参阅 [通过 Apple 登录认证用户](../signinwithapple/authenticating-users-with-sign-in-with-apple.md)。

### 接收有关 Apple 账户变动的更新

如果 App 使用远程服务器管理用户账户，请开启服务器到服务器通知，这样当用户对 Apple 账户做出更改时，Apple 账户服务器便会通知你。当用户更改邮件转发偏好、删除 App 账户或永久删除 Apple 账户时，Apple 账户服务器会发送通知。利用这些通知来维护一份规范化的用户列表。更多信息请参阅 [启用服务器到服务器通知](https://developer.apple.com/help/account/configure-app-capabilities/enabling-server-to-server-notifications/)。

### 向用户的隐藏收件箱发送电子邮件

如果在提示用户授权时包含了 [email](../authenticationservices/asauthorization/scope/email.md) scope，系统将提供一个选项，允许用户隐藏真实电子邮件地址，改为使用 Apple 提供的唯一、随机的转发电子邮件地址。为防止垃圾邮件，并确保发往用户的电子邮件源自你注册的域名和电子邮件地址，请遵循以下步骤：

- 注册用于电子邮件通信的域名及子域名。
- 注册一份用于发送电子邮件的唯一电子邮件地址列表。
- 使用发件人策略框架（Sender Policy Framework，SPF）与域名密钥识别邮件（DomainKeys Identified Mail，DKIM）协议对你的注册域名进行身份验证。

你必须先完成以上步骤，才能向用户的隐藏收件箱发送电子邮件。更多信息请参阅 [配置私人电子邮件中继服务](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service/)。

## 另请参阅

### 商务

- [配置 Apple Pay 支持](configuring-apple-pay-support.md) — 利用用户存储在其设备上的支付信息，在 App 内处理付款。
- [配置钱包支持](configuring-wallet-support.md) — 访问用户的钱包，以添加、更新和展示 App 的通行证。
