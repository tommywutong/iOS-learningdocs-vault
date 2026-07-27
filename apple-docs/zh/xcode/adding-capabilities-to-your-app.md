---
title: 向你的 App 添加功能
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adding-capabilities-to-your-app
source_url: 'https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adding-capabilities-to-your-app.json'
content_hash: 'sha256:b6e8e42a24e303fc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Capabilities](capabilities.md)

# 向你的 App 添加功能

<sub>文章</sub>

配置你的 target，加入并自定能够访问 Apple App 服务的功能。

## 概述

_功能（capability）_ 让你的 App 能够访问 Apple 提供的某项 _App 服务_，例如 CloudKit、Game Center 或 App 内购买。要使用某些 App 服务，你需要在 Xcode 中为你的 target 添加一项功能，以正确配置该 App 服务。Xcode 可能会编辑 [Entitlements](../bundleresources/entitlements.md) 和 [Information Property List](../bundleresources/information-property-list.md) 文件、添加相关框架，并配置你的签名资源。

某些 App 服务——例如 Game Center 和 App 内购买——需要在 App Store Connect 和你的开发者账户中进行额外配置。例如，要为使用 Maps 功能的其他 App 提供路线指引，你需要在 App Store Connect 中[上传一份地理覆盖范围文件](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/upload-a-geographic-coverage-file/)。

平台，以及你是否为 [Apple Developer Program](https://developer.apple.com/programs/) 的成员，可能会限制你 App 可用的功能。有关支持的功能，请前往[开发者账户帮助](https://developer.apple.com/help/account/)的参考部分——例如，前往 [Supported capabilities (iOS)](https://developer.apple.com/help/account/reference/supported-capabilities-ios) 查看 iOS App 可用的功能。

开始之前，请在设置中添加你的 Apple 账户，并在项目编辑器中将该项目分配给某个团队，这样 Xcode 才能为你的 App 创建一个描述文件（provisioning profile）。对于 iOS、iPadOS、tvOS、visionOS 和 watchOS App，请在设备上运行你的 App 以注册该设备，并创建一个开发描述文件。更多信息请参阅 [Running your app on simulated or physical devices](running-your-app-on-simulated-or-physical-devices.md)。

> [!important] 重要
> 从模板创建项目时，请使用默认的自动签名。如果你手动为你的 App 签名，则需要自行执行功能配置步骤。有关手动签名的更多信息，请参阅[配置代码签名](distributing-your-app-to-registered-devices.md#Configure-code-signing)。

### 添加一项功能

你可以使用项目编辑器的 Signing & Capabilities 面板，为你的 App 添加功能。

在项目导航器中，选择该项目——即与你 App 同名的根组——然后在右侧出现的项目编辑器中，在边栏里选择相应的 target，再点按 Signing & Capabilities 标签页。

![](../../../attachments/f2f9ef9085e3de4f81e1c911595acd32/signing-capabilities@2x.png)

<sub>Xcode 的截图，显示了打开了 Signing & Capabilities 标签页的项目编辑器。项目导航器中选中了该项目，项目编辑器边栏中选中了一个 target，工具栏中选中了 Signing & Capabilities 标签页，下方显示已添加了一项 Location 功能。</sub>

（可选）选择一个构建配置（All、Debug 或 Release）。例如，如果你只想为 Debug 配置添加该功能，请选择 Debug；否则请选择 All。

在 Signing & Capabilities 工具栏中，点按 Capability 按钮（+）以打开 Capabilities 资源库（或选择 Editor \> Add Capability）。Capabilities 资源库只会显示目标平台和你的项目成员资格下可用的功能。在列表中选择一项功能，即可在右侧查看其说明。使用工具栏中的过滤字段可以快速找到某项功能。

![](../../../attachments/550ae56dcf9df5bbcbeaa2dd9274ac3a/capabilities-library@2x.png)

<sub>Capabilities 资源库的截图，左侧边栏中选中了 Apple Pay 功能，右侧详情区域显示了有关 Apple Pay 的信息。</sub>

要将某项功能添加到 target 中，请双击边栏中的该功能，或将其从资源库拖到 Signing & Capabilities 面板中。该功能会出现在 Signing 部分下方。如果还有更多配置步骤，该功能会展开以显示额外的控制（参见下方的[执行额外的配置步骤](adding-capabilities-to-your-app.md#Perform-additional-configuration-steps)）。要移除某项功能，请点按 Signing & Capabilities 面板中该功能右上角的垃圾桶图标。

![](../../../attachments/0be10bf17ef932245f455cc0b9540e9e/additional-configuration@2x.png)

<sub>Xcode 的截图，显示了打开了 Signing & Capabilities 标签页的项目编辑器，下方是 Associated Domains 功能的额外配置选项。</sub>

如果 Signing 部分出现错误，请阅读相应消息并修正问题。例如，Signing 下 Bundle Identifier 字段中显示的 bundle ID（[CFBundleIdentifier](../bundleresources/information-property-list/cfbundleidentifier.md)）必须是唯一的。bundle ID 的默认值，是你在创建项目时输入的组织标识符与 App 名称拼接而成的。

### 执行额外的配置步骤

对于某些功能，你可能需要在 Xcode、你的开发者账户或 App Store Connect 中执行额外的配置步骤。对于其他功能，你可能需要编写一些代码。

有关具体功能的更多指导，请参阅下表：

| 功能 | 更多信息 |
|---|---|
| App Groups | [配置 App Group](configuring-app-groups.md) |
| App Sandbox | [配置 macOS App 沙盒化](configuring-the-macos-app-sandbox.md) |
| Apple Pay | [配置 Apple Pay 支持](configuring-apple-pay-support.md) |
| Associated Domains | [配置关联的域名](configuring-an-associated-domain.md) |
| Background Modes | [配置后台运行模式](configuring-background-execution-modes.md) |
| ClassKit | [在你的 App 中启用 ClassKit](../classkit/enabling-classkit-in-your-app.md) |
| Family Controls | [配置 Family Controls](configuring-family-controls.md) |
| Fonts | [配置自定字体](configuring-custom-fonts.md) |
| Game Controllers | [配置游戏控制器](configuring-game-controllers.md) |
| Group Activities | [配置 Group Activities](configuring-group-activities.md) |
| Hardened Runtime | [配置强化运行时（hardened runtime）](configuring-the-hardened-runtime.md) |
| HealthKit | [配置 HealthKit 访问权限](configuring-healthkit-access.md) |
| HomeKit | [配置 HomeKit 访问权限](configuring-homekit-access.md) |
| iCloud | [配置 iCloud 服务](configuring-icloud-services.md) |
| In-App Purchase | [配置 App 内购买](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/overview-for-configuring-in-app-purchases) |
| Keychain Sharing | [配置钥匙串共享](configuring-keychain-sharing.md) |
| Maps | [配置 Maps 支持](configuring-maps-support.md) |
| Media Device Discovery | [配置媒体设备发现](configuring-media-device-discovery.md) |
| Network Extensions | [配置网络扩展](configuring-network-extensions.md) |
| On-Demand Install Capable | [使用 Xcode 创建轻 App（App Clip）](../appclip/creating-an-app-clip-with-xcode.md) |
| Push Notifications | [向 APNs 注册你的 App](../usernotifications/registering-your-app-with-apns.md) |
| Sign in with Apple | [配置通过 Apple 登录支持](configuring-sign-in-with-apple.md) |
| Siri | [配置 Siri 支持](configuring-siri-support.md) |
| Wallet | [配置 Wallet 支持](configuring-wallet-support.md) |
