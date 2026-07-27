---
title: 为分发准备你的 App
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preparing-your-app-for-distribution
source_url: 'https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preparing-your-app-for-distribution.json'
content_hash: 'sha256:f60dbacd196e1e40'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 为分发准备你的 App

<sub>文章</sub>

在分发你的 App 之前，配置信息属性列表并添加图标。

## 概述

在将构建版本上传到 App Store Connect 或导出构建版本以便在 App Store 之外分发之前，先为分发准备好你的 Xcode 项目。提供关于你 App 的所有必要信息——例如唯一的 bundle ID、构建字符串、App 图标和启动画面。请仔细选择这些设置，因为大部分信息在你通过 TestFlight 或 App Store 分发构建版本之后就无法编辑了。

有关在 App Store Connect 中需要填写的其他信息，请参阅 App Store Connect 帮助中的[必填、可本地化和可编辑的属性](https://developer.apple.com/help/app-store-connect/reference/required-localizable-and-editable-properties/)和 [App 信息](https://developer.apple.com/help/app-store-connect/reference/app-information)（其中包含更多详情）。

### 设置 bundle ID

当你从模板创建 Xcode 项目时，bundle ID（[CFBundleIdentifier](../bundleresources/information-property-list/cfbundleidentifier.md)）——它在整个系统中唯一标识你的 App——默认值为你输入的组织 ID 加上 App 名称，按反向 DNS 格式拼接，例如，bundle ID 会变成 `com.example.mycompany.HelloWorld`。

如果你的组织 ID 在所有开发者中是唯一的，并且你的 App 名称在你的组织内是唯一的，那么你的默认 bundle ID 应该也是唯一的。例如，使用你组织的域名作为组织 ID，以确保 bundle ID 的唯一性。

要通过 TestFlight 和 App Store 分发你的 App，你需要在 App Store Connect 中[创建一个 App 记录](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app)，并输入一个与项目中一致的 bundle ID。在项目编辑器中将 bundle ID 添加到你的项目：

![](../../../attachments/7ca1104158f695dc569a6959caef7ff5/preparing-your-app-for-distribution-1@2x.png)

<sub>屏幕截图显示「签名与功能」面板中「签名」部分已展开，露出「自动管理签名」复选框，其下方是用于选择你的团队的弹出式菜单，以及用于输入 Bundle Identifier 的文本栏。这些控制下方还有若干区域，用于输入特定于平台的设置，目前处于折叠状态。图片展示了你在何处选择目标。</sub>

1. 选择目标。
2. 点按「签名与功能」面板。
3. 展开「签名」。
4. 在「Bundle Identifier」文本栏中输入 bundle ID。

在你将第一个构建版本上传到 App Store Connect 之后，就无法再更改 bundle ID，因此请在创建项目时谨慎选择组织 ID，或者事后编辑 bundle ID。在你将 App 提交给 App 审核之前，你都可以编辑 App 的名称。

### 设置多个 bundle ID 以提供独立的平台版本

默认情况下，多平台 App 在所有平台上构建时都使用相同的 bundle ID，这样你就可以在 App Store 上将这些 App 作为通用购买一起提供（参阅[提供通用购买](https://developer.apple.com/support/universal-purchase/)）。

要提供你 App 的特定平台版本，请在 App Store Connect 中为每个平台变体创建 App 记录，并为每个版本添加一个不同的 bundle ID。在项目编辑器中，选择「签名与功能」面板并展开「签名」。在「签名」下，展开每个平台对应的区域：

1. 输入一个不同的 bundle ID。
2. 配置签名设置。

如果你有应用内购买项目或订阅，请在 App Store Connect 中为每个 App 版本重新创建它们。更多信息请参阅 App Store Connect 帮助中的[创建消耗型或非消耗型应用内购买项目](https://developer.apple.com/help/app-store-connect/manage-in-app-purchases/create-consumable-or-non-consumable-in-app-purchases)和[提供自动续期订阅](https://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions)。

### 将项目分配给一个团队

如果你还没有这样做，请把项目分配给一个团队。例如，如果你想使用 TestFlight 或通过 App Store 分发你的 App，请把项目中的所有目标都分配给一个属于 [Apple 开发者计划](https://developer.apple.com/programs/)的团队。当你上传或导出构建版本时，Xcode 会在相关联的开发者账户中创建必要的签名资源。

在项目编辑器中，选择「签名与功能」面板，然后从「团队」弹出式菜单中选择一个团队。

### 设置支持的目标设备

指明你的 App 支持哪些设备和平台。在项目编辑器中：

![](../../../attachments/e7f4a82d6044e3ddeb33328ce40a10ec/preparing-your-app-for-distribution-2@2x.png)

<sub>屏幕截图显示「通用」面板中「支持的目标设备」和「标识」部分已展开。「支持的目标设备」部分包含一个表格，带有添加按钮（+）和移除按钮（-）。「标识」部分包含一个「App 类别」弹出式菜单，其上方是用于输入显示名称、Bundle Identifier、版本和构建版本的文本栏。图片展示了你在何处选择目标。</sub>

1. 选择目标。
2. 选择「通用」面板。
3. 展开「支持的目标设备」部分。
4. 点按添加按钮（+），选择一个设备和平台。要移除某个目标设备，请选中它并点按移除按钮（-）。

### 设置 App 类别

类别可以帮助顾客在 App Store 上发现你的 App。在 App Store Connect 中，你可以设置你希望 App 出现在 App Store 哪个主要类别和次要类别下。对于 macOS App，你还需要在项目中为你的 App 设置一个类别。

选择一个与你在 App Store Connect 中设置的主要类别相匹配或密切相关的类别：

1. 选择目标。
2. 选择「通用」面板。
3. 展开「标识」部分。
4. 从「App 类别」弹出式菜单中选择一个类别。

有关如何选择最准确、最有效的类别的指导，请参阅[选择类别](https://developer.apple.com/app-store/categories/)。

### 设置版本号和构建字符串

版本号（[CFBundleShortVersionString](../bundleresources/information-property-list/cfbundleshortversionstring.md)）和构建字符串（[CFBundleVersion](../bundleresources/information-property-list/cfbundleversion.md)）在整个系统中唯一标识你 App 的构建版本。版本号会显示在 App Store 中。对于通过 TestFlight 或 App Store 分发的 App，Xcode Organizer 会为该 App 每个版本的每个构建版本显示崩溃报告和现场报告。对于 macOS App，版本号和构建字符串也可能出现在「关于」窗口中，参阅 [credits](../appkit/nsapplication/aboutpaneloptionkey/credits.md)。版本号和构建字符串应采用 [Major].[Minor].[Patch] 的格式，其中 _Patch_ 表示维护版本，如 10.14.1。App Store 要求这两个键都必须提供。对于 macOS App，你必须在分发新的构建版本之前递增构建字符串。

在创建 App 的新版本时递增版本号。更多信息请参阅 App Store Connect 中的[创建新的 App 版本](https://developer.apple.com/help/app-store-connect/update-your-app/create-a-new-version)。

当你将新的归档上传到 App Store 时，Xcode 可以更新构建号。要利用这一点，请使用 Xcode Organizer 中预先配置好的某种分发方式，或者为你的自定分发方式在 App Store Connect 分发选项中启用「管理版本和构建号」设置。

如果你使用自定分发方式并禁用「管理版本和构建号」选项，你就需要自行管理构建字符串，并确保在归档你想要分发的构建版本之前递增该构建字符串。在项目编辑器中，选择「通用」面板，展开「标识」，然后设置版本号和构建字符串。

> [!note] 注意
> Mac App 的构建字符串必须在你 App 的所有版本之间递增。为其他平台构建的 App 的构建字符串则可以在新版本中从 1 重新开始。

### 编辑部署信息设置

对于 iOS 和 iPadOS App，请选择你 App 支持的设备方向。

![](../../../attachments/8c6c3a8a70d1b91850f72db42a3d4972/preparing-your-app-for-distribution-3@2x.png)

<sub>屏幕截图显示「通用」面板中「部署信息」部分已展开，露出用于配置你 App 支持的方向的复选框，以及一个用于配置多窗口支持的链接。</sub>

要配置你的 App 支持多窗口，请点按「支持多窗口」旁边的箭头。有关详情，请参阅[指定你 App 支持的场景](../uikit/specifying-the-scenes-your-app-supports.md)；有关示例代码，请参阅[在 iPad 上支持多窗口](../uikit/supporting-multiple-windows-on-ipad.md)。

### 添加 App 图标和 App Store 图标

添加一个图标，用于在设备上的各个位置以及 App Store 中代表你的 App。你可以使用支持 [Liquid Glass](../technologyoverviews/liquid-glass.md) 的单个多层 Icon Composer 文件，也可以使用图标资源目录来表示你的图标。如果你使用资源目录，系统会为你自动为该图标应用 Liquid Glass 效果。

要使用 Icon Composer 文件，请参阅[使用 Icon Composer 创建你的 App 图标](creating-your-app-icon-using-icon-composer.md)；要使用资源目录，请参阅[使用资源目录配置你的 App 图标](configuring-your-app-icon.md)。

有关 App 图标设计指导，请参阅[人机界面指南 \> 基础 \> App 图标](https://developer.apple.com/design/human-interface-guidelines/app-icons)。

### 提供启动画面

_启动画面_ 是一个界面文件，在你的 App 启动时立即出现，随后很快被你 App 的第一个画面取代。对于使用启动画面的 App 和平台而言，启动画面的作用只是在你的 App 启动期间为用户提供一些可看的内容，从而提升用户体验。

编辑 `LaunchScreen.storyboard` 文件，当你从模板创建 Xcode 项目时，该文件会包含在项目中。否则，你也可以为现有项目添加启动画面文件，参阅[管理 Xcode 项目中的文件和文件夹](managing-files-and-folders-in-your-xcode-project.md)。

有关设计启动画面的信息，请阅读人机界面指南中的[启动](https://developer.apple.com/design/human-interface-guidelines/patterns/launching)。

### 提供使用说明以访问受保护的资源

当你的 App 首次尝试访问受保护的资源时，系统会提示用户授权。随后系统会生成一个对话框，其中包含你 App 的名称以及你提供的 _使用说明_。例如，访问位置数据的使用说明可能是「你的位置信息将用于为你提供前往目的地的逐向导航」。如果用户授予权限，系统会记住这一点，之后不会再针对该资源进行提示。如果用户拒绝授权，对该资源的访问以及后续任何尝试都会失败。

你必须在[信息属性列表](../bundleresources/information-property-list.md)中，为你 App 访问的所有受保护资源提供使用说明，例如某人的位置、日历、提醒事项和联系人。同时也要为配件提供使用说明，例如相机和麦克风。

要了解更多信息，请参阅[请求访问受保护的资源](../uikit/requesting-access-to-protected-resources.md)。

### 配置 App 沙盒化和强化运行时（macOS）

如果你通过 App Store 分发你的 macOS App，则必须[启用 App 沙盒化](https://help.apple.com/xcode/mac/current/#/devbd04af149)。如果你要对 macOS App 进行公证以便在 App Store 之外分发，则必须[启用强化运行时](https://help.apple.com/xcode/mac/current/#/devf87a2ac8f)，并且可以选择同时启用 App 沙盒化。

要了解更多有关强化运行时的信息，请参阅[强化运行时](../security/hardened-runtime.md)。有关公证的信息，请参阅[在分发前对 macOS 软件进行公证](../security/notarizing-macos-software-before-distribution.md)。

### 设置版权键（macOS）

对于 macOS App，请在将你的 App 上传到 App Store Connect 之前，在信息属性列表中[设置版权键](https://help.apple.com/xcode/mac/current/#/dev2ec588bbf)（[NSHumanReadableCopyright](../bundleresources/information-property-list/nshumanreadablecopyright.md)）。

在 macOS 中，如果你没有向显示「关于」窗口的 [orderFrontStandardAboutPanel(_:)](<../appkit/nsapplication/orderfrontstandardaboutpanel(__).md>) 方法显式传递版权字符串，「关于」窗口中会改为显示版权键的本地化版本。例如，如果你把版权键设置为 `@2002-2019 My Company`，它就会出现在「关于」窗口的底部。你可以为你支持的每种语言本地化信息属性列表。

### 添加出口合规性信息

如果你在美国或加拿大以外分发你的 App，你的 App 将受美国出口法律的约束。如果你的 App 使用了加密技术，它就要遵守美国出口合规性要求。你可以通过在[信息属性列表](../bundleresources/information-property-list.md)中提供出口合规性信息，绕过 App Store Connect 每次你提交 App 审核时都会询问的问题。

要了解更多信息，请参阅[遵守加密出口规定](../security/complying-with-encryption-export-regulations.md)。

## 另请参阅

### 基础

- [更改 bundle 标识符](changing-the-bundle-identifier.md) — 修改你 App 的 bundle 标识符，并在其出现的所有位置进行更新。
</content>
