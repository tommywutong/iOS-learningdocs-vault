---
title: 为 beta 测试和发布分发你的 App
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/distributing-your-app-for-beta-testing-and-releases
source_url: 'https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/distributing-your-app-for-beta-testing-and-releases.json'
content_hash: 'sha256:02aad3b32491c97e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 为 beta 测试和发布分发你的 App

<sub>文章</sub>

将你的 App 发布给 beta 测试者和用户。

## 概述

在你于 Xcode 中彻底测试你的 App 之后，将它分发给 beta 测试者，或发布给用户以在他们的个人设备上运行。根据你的 App 所在的平台、开发阶段，以及你是否加入了 Apple Developer Program，选择一种分发方式。在你向用户发布你的 App 之前，请使用其中一种 beta 测试方法分发你的最终构建版本。

如有需要，在按照这些分发步骤操作之前，请查阅 [Preparing your app for distribution](preparing-your-app-for-distribution.md) 以完成你项目的配置。

> [!note] 来自 WWDC23 的相关场次
> 场次 10224：[Simplify distribution in Xcode and Xcode Cloud](https://developer.apple.com/videos/play/wwdc2023/10224)

### 加入 Apple Developer Program

分发方式从将你的 App 导出到测试设备，到将其上传至 App Store Connect，种类繁多。你可以使用 TestFlight 向测试者分发 beta 构建版本并收集反馈。如果你想将你的 App 分发到已注册的设备、通过 TestFlight 分发给 beta 测试者，或者通过 App Store 分发，请加入 Apple Developer Program。加入 Apple Developer Program 之后，Apple 会为你创建一个 App Store Connect 账户，你就可以开始上传构建版本了。

加入 Apple Developer Program 可以让你使用这些分发方式，还能为你的 App 添加各种功能（capability）。功能会为你的 App 授予对 Apple 提供的某项 App 服务的访问权限，例如 CloudKit、Game Center 或 App 内购买。要了解有关功能的更多信息，请参阅 [Adding capabilities to your app](adding-capabilities-to-your-app.md)。

Xcode 使用云管理的签名证书自动对你的 App 进行代码签名。这些签名证书与你的 Apple 开发者账户相关联，你可以在 App Store Connect 中管理这些证书的访问权限。有关为你的团队管理证书资源访问权限的信息，请参阅 [Add and edit users](https://developer.apple.com/help/app-store-connect/manage-your-team/add-and-edit-users)。

要了解有关加入该计划的更多信息，请参阅 [Apple Developer Program](https://developer.apple.com/programs/)。

### 在一个项目或购买项中合并多平台 App

如果你在不同平台上提供相关的 App，将它们合并到一个 Xcode 项目或一次 App Store 购买中，可以让用户的安装更加方便。要让你的用户能够以通用购买或 App 捆绑包的形式从 App Store 一起购买相关的 App，请参阅 [Offering Universal Purchase](https://developer.apple.com/support/universal-purchase/)。

### 创建你的 App 的归档

要使用任何一种分发方式，首先要创建你的 App 的归档。_归档_ 是你的 App 的一个构建版本，包含调试信息，Xcode 会将其存储在一个 bundle 中。Xcode 会根据你为分发选择的分发配置来重新打包该归档的内容。

在你的 Xcode 项目的主窗口中，从 Scheme 工具栏菜单中选择一个 scheme 和一个要构建的运行目标。然后选择 Product ＞ Archive，以针对你选择的设备类别构建该 scheme 中包含的目标，并创建一个显示在 Archives 管理器中的归档。

![Archives 管理器的屏幕截图，显示了一个被选中的归档和 Distribute App 按钮。](../../../attachments/394197047da27d4eb6d4dc6ffe161cf4/distributing-your-app-for-beta-testing-and-releases-1@2x.png)

你可以通过选择 Window ＞ Organizer 直接打开 Archives 管理器。如果你想在尚未提交之前确认你的 App 已准备好提交给 TestFlight 或 App Store，请选择你的归档，然后点按 Validate App。Xcode 会对该 App 执行有限的自动初步验证并提供反馈。

对于使用 Mac Catalyst 构建的 Mac App，请为 iPad 版本和 Mac 版本创建各自独立的归档。在为 Mac 版本创建归档时，选择 My Mac 作为运行目标。

> [!note] 注意
> 早期版本的 Xcode 不允许你以模拟器作为运行目标来构建归档。在 Xcode 15 及更高版本中，选择以模拟器作为运行目标构建归档，会构建一个包含在该类别设备上运行所需全部 CPU 架构的归档。

### 选择一种分发方式

你可以导出该归档，或将其上传到 App Store Connect。如果你导出该归档，就可以在 App Store 之外分发它。否则，将该归档上传到 App Store Connect，以通过 TestFlight 或 App Store 分发它。

在 Xcode 的 Organizer 窗口中，在侧栏选择 Archives，然后点按 Distribute App。

![](../../../attachments/ba54e01600bd0fc98291583e7215d2bd/distributing-your-app-for-beta-testing-and-releases-2@2x.png)

<sub>Archives 管理器的屏幕截图，显示了 Select a method for distribution 对话框，其中预先配置好的 TestFlight & App Store 选项处于选中状态。</sub>

选择以下选项之一，使用推荐设置进行分发：

- **TestFlight & App Store** — 通过 TestFlight 分发并提交到 App Store 的默认设置。使用此选项来更新你的归档中内容的构建号、执行自动代码签名，并上传带有符号的 App。
- **TestFlight Internal Only** — 通过 TestFlight 分发并将访问权限限制在你的团队内的默认设置。使用此选项可以防止你的 App 的开发构建版本被提交到 App Store。
- **Release Testing** — 在发布之前分发一个版本以进行测试的默认设置。使用此选项可以执行与 App Store 分发选项类似的自动代码签名，并导出以安装到你的团队在 App Store Connect 中注册的设备上。此分发方式不适用于为 Mac 构建的 App。
- **Enterprise** — 分发给你所在组织成员的默认设置。如果你是 [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise) 的成员，请使用此选项。此分发方式不适用于为 Mac 构建的 App。
- **Direct Distribution** — 直接分发 macOS App 的默认设置。使用此选项可以为直接分发对 Developer ID App 进行公证。此分发方式仅适用于为 Mac 构建的 App。
- **Debugging** — 分发用于调试的版本的默认设置。使用此选项可以导出一个版本，安装并在你的团队在 App Store Connect 中注册的设备上进行调试。这会为支持沙盒测试环境的部分[功能](capabilities.md)启用该环境。

选择一个分发选项之后，点按 Distribute 按钮。Xcode 会开始处理、打包和上传。点按末尾的链接以访问该 App 在 App Store Connect 上的构建版本页面，或点按 Export 按钮以在本地访问这些资源。

> [!note] 注意
> 在你首次将你的 App 上传到 App Store 之前，请创建一个 App 记录，以在 App Store Connect 中注册你的 App。如果你尚未这样做，Xcode 会向你询问它为你创建此记录所需的信息。有关更多信息，请参阅 [Create an app record](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app)。

### 创建自定分发

要开始一次允许你配置自己的设置的自定分发，请点按 Custom 选项。

![分发方式选择步骤的屏幕截图，显示了 Ad Hoc 分发选项处于选中状态。](../../../attachments/1ebd7fcf079ce9cf3d0331cfa2c7c518/distributing-your-app-for-beta-testing-and-releases-3@2x.png)

从以下分发方式中选择：

- **App Store Connect** — 使用 TestFlight 或通过 App Store 分发。
- **Ad Hoc** — 分发给你在 App Store Connect 中注册的有限数量的设备。有关向你注册的设备分发的更多信息，请参阅 [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md)。
- **Enterprise** — 如果你是 [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise) 的成员，并准备好将你的 App 发布给你所在组织中的用户，则分发给你所在组织的成员。
- **Developer ID** — 在 App Store 之外分发一个由 Apple 公证或使用 Developer ID 签名的 macOS App。此分发方式仅适用于为 Mac 构建的 App。
- **Development** — 分发给你在 App Store Connect 中注册的有限数量的设备。有关向你注册的设备分发的更多信息，请参阅 [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md)。
- **Copy App** — 分发未经代码签名的 macOS App。此分发方式仅适用于为 Mac 构建的 App。

如果你选择 App Store Connect 或 Developer ID 作为分发方式，你还需要选择一个目的地选项。你可以选择将你的构建版本上传到 App Store，或将你的构建版本导出到本地以便稍后上传。

![分发流程的屏幕截图，显示了带有 Upload 或 Export 选项的目的地选项，其中 Upload 处于选中状态。](../../../attachments/42129fbe9643b7d6d49e6b714d240933/distributing-your-app-for-beta-testing-and-releases-4@2x.png)

在 TestFlight 或 App Store 上分发你的 App 时，选择如何管理符号和构建号：

![](../../../attachments/c9577bec89092a11e40b6ff4c8528605/distributing-your-app-for-beta-testing-and-releases-5@2x.png)

<sub>分发流程的屏幕截图，显示了 App Store Connect 的分发选项，包含 Upload you app's symbols、Manage version and build numbers 和 TestFlight internal testing only 的复选框。Upload you app's symbols 和 Manage version and build numbers 复选框处于选中状态。</sub>

- **Strip Swift symbols** — 通过从 Swift 标准库中剥离符号来减小你的 App 的大小。此设置仅在你的项目嵌入了 Swift 库时可用。
- **Upload your app's symbols** — 允许 Apple 为你提供已符号化的崩溃日志和其他诊断信息。已符号化的日志会将日志中的内存地址替换为人类可读的函数名和行号。这些符号在测试你的 App 与 Apple 产品和服务的兼容性时也很有用。
- **Manage version and build number** — 允许 Xcode 更新你的归档中所有内容的构建号。
- **TestFlight internal testing only** — 为通过 TestFlight 分发准备该 App，并将访问权限限制在你的团队内。使用此选项可以防止你的 App 的开发构建版本被提交到 App Store。

在选择涉及代码签名的分发方式时，选择一种代码签名方法。

![](../../../attachments/f018d363495f18c2d8872aeb7d2a48c6/distributing-your-app-for-beta-testing-and-releases-6@2x.png)

<sub>分发流程的屏幕截图，显示了 Automatic manage signing 和 Manually manage signing 分发方式的复选框。Automatic manage signing 复选框处于选中状态。</sub>

选择“Automatically manage signing”可以让 Xcode 为你管理签名。要手动为你的 App 签名，你需要使用签名证书。有关共享签名证书的信息，请参阅 [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md)。

在使用 Ad Hoc 或 Development 选项进行自我分发打包时，选择是启用还是禁用 App Thinning，并配置按需资源设置。有关 App Thinning 和按需资源的更多信息，请参阅 [Reducing your app's size](reducing-your-app-s-size.md) 和 [Doing advanced optimization to further reduce your app's size](doing-advanced-optimization-to-further-reduce-your-app-s-size.md)。

![](../../../attachments/8701513eaeb5a39fbda9c970a6f685c5/distributing-your-app-for-beta-testing-and-releases-7@2x.png)

<sub>分发流程的屏幕截图，显示了 Ad Hoc 分发设置。该对话框包括选择了 None 选项的 App Thinning 弹出式菜单，以及 Additional Options，其中有一个标记为 Include manifest for over-the-air installation 的复选框。</sub>

### 分发 beta 版本

要分发你的 App 的 beta 版本，以提供即将发布版本的预览，请选择与你的测试资源相匹配的分发方式：

- 使用 TestFlight 向内部和外部测试者分发你的 App 的 beta 版本。TestFlight App 允许受邀用户安装、进行 beta 测试、提供反馈，并获取你的 App 的更新。Apple 会为你分发该 beta 版本，你在 App Store Connect 中管理构建版本和用户。要了解更多信息，请参阅 [TestFlight overview](https://developer.apple.com/help/app-store-connect/test-a-beta-version/overview-of-testflight)。
- 向你的开发者账户中已注册的设备分发 beta 版本。仅当你可以为 beta 测试预留一部分有限的开发设备时，才选择此选项。要了解更多信息，请参阅 [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md)。
- 对于 macOS App，在通过 App Store 分发该 App 之前，向测试者分发一个经过 Apple 公证的构建版本。要了解更多信息，请参阅 [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md)。

![App Store Connect 的屏幕截图，显示了从 Xcode 上传的构建版本。](../../../attachments/c67e305f2a0af926d2c0551f08aebb1d/distributing-your-app-for-beta-testing-and-releases-8@2x.png)

### 在 App Store 上发布

在对你的最终构建版本进行 beta 测试之后，将其提交给 App 审核，然后在 App Store 上提供它。有关发布流程的更多信息，请参阅 [Overview of publishing an app](https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/overview-of-publishing-your-app)。

前往 [App Review](https://developer.apple.com/app-store/review/) 查看 App Store 和《人机界面指南》。有关特定平台的指导，请参阅 [Submit your apps today](https://developer.apple.com/app-store/submitting)。

在你将你的 App 提交给 App 审核之前，你可能需要在 App Store Connect 中输入额外的信息。在你的 App 上传或发布之后，你无法更改其中一些元数据，因此谨慎选择你的设置十分重要。有关这些元数据的更多信息，请前往 App Store Connect Help 中的 [Required, localizable, and editable properties](https://developer.apple.com/help/app-store-connect/reference/required-localizable-and-editable-properties)。

如果你使用 TestFlight 分发了一个 beta 版本，并输入了 App Store 发布所需的额外信息，只需将 App Store Connect 中显示的最后一个构建版本提交给 App 审核即可。

![App Store Connect 的屏幕截图，显示了版本信息和 Submit for Review 按钮。](../../../attachments/f389379a6a5d46bc29c152f5d19920d5/distributing-your-app-for-beta-testing-and-releases-9@2x.png)

如果你没有使用 TestFlight 分发最终构建版本，请为分发准备你的 App 并创建你的 App 的归档。在继续之前验证该归档并修复任何验证错误。然后，将它上传到 App Store Connect，并等待其通过 App Store Connect 的验证测试。

要将该构建版本提交给 App 审核，请前往 [Submit for review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/submit-for-review)。

### 在 App Store 之外分发

对于 macOS App，你可以导出一个经过公证的 App，以便在 App Store 之外分发，但你可能首先需要禁用那些需要 Apple Developer Program 会员资格的功能，然后自行将该 App 分发给用户。对你在 App Store 之外分发的所有软件进行公证，这也包括系统扩展和驱动程序。要了解更多信息，请参阅 [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md)。

### 分发企业 App

分发商业、定制或内部使用的 App 也有若干选项。有关详细信息，请参阅 [Find the best way to reach your users](https://developer.apple.com/business/distribute/)。如果你加入了 [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise/)，请参阅 [Develop and distribute an enterprise app](https://help.apple.com/xcode/mac/current/#/devba5e7054d)，了解导出你的 App 的企业专属 Xcode 步骤。

### 查看崩溃、诊断和指标报告

如果你使用 TestFlight 或通过 App Store 分发你的 App，你可以在管理器中查看 Apple 为你生成的崩溃和诊断报告。你也可以使用管理器查看 beta 测试者的反馈。如果你通过 App Store 分发你的 App，你还可以在管理器中查看指标报告。有关更多信息，请参阅 [Acquiring crash reports and diagnostic logs](acquiring-crash-reports-and-diagnostic-logs.md) 和 [Viewing and responding to feedback from beta testers](viewing-and-responding-to-feedback.md)。有关性能改进的更多信息，请参阅 [Improving your app's performance](improving-your-app-s-performance.md) 和 [Analyzing the performance of your shipping app](analyzing-the-performance-of-your-shipping-app.md)。

## 另请参阅

### 分发与发布

- [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md) — 在你的开发者账户中注册设备，并将你的 App 部署到这些设备上进行测试。
- [Packaging Mac software for distribution](packaging-mac-software-for-distribution.md) — 构建一个 zip 归档、磁盘映像或安装程序包，以分发你的 Mac 软件。
