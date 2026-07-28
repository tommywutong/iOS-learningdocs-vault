---
title: 更改 bundle identifier
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/changing-the-bundle-identifier
source_url: 'https://developer.apple.com/documentation/xcode/changing-the-bundle-identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/changing-the-bundle-identifier.json'
content_hash: 'sha256:f36f1226519c9020'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 更改 bundle identifier

<sub>文章</sub>

修改你的 App 的 bundle identifier，并在所有出现的位置进行更新。

## 概述

如果你想在向 App Store Connect 上传构建版本之前更改 App 的 bundle ID，你需要在多个位置进行更改。如果你的 App 使用某些依赖于 bundle ID 的功能，那么更新以下所有位置的 bundle ID 尤为重要。

*bundle ID* 是一个信息属性列表键，在整个系统中唯一标识你的 App。某些功能会使用你项目中包含主 bundle ID 的信息属性列表或 entitlement 键。

如果你在代码中引用了 bundle ID，请将其替换为返回调用代码 bundle 的 [bundle()](<../foundation/bundle().md>) 宏。

> [!note] 注意
> 如果你使用 [Xcode Cloud](xcode-cloud.md)，请先将项目更改提交到远程仓库，然后再创建工作流程。

## 更改主 bundle ID

首先，在你的 Xcode 项目中更改 bundle ID：

1. 在项目导航器中，选择项目。
2. 在右侧的项目编辑器中，选择目标。
3. 点按“Signing & Capabilities”标签页，如有必要，展开“Signing”。
4. 在“Bundle Identifier”文本字段中输入新的 bundle ID，然后按下 Return 键。

![](../../../attachments/2756129698d148f3db5d030a998f2fd1/changing-the-bundle-identifier@2x.png)

<sub>项目编辑器的 Xcode 截图，显示已选中“Signing & Capabilities”标签页，并展开了 Signing 设置，光标位于“Bundle Identifier”文本字段中。</sub>

Xcode 会更改 app bundle 中对应的 [CFBundleIdentifier](../bundleresources/information-property-list/cfbundleidentifier.md) 信息属性列表键。

## 更新配套目标的 bundle ID

更改任何从主 bundle ID 派生出来的目标 bundle ID，例如 watchOS、App 扩展（app extension）和轻 App（App Clip）目标的 bundle ID。

在项目编辑器中，选择侧边栏中的每个目标，并在右侧的“Signing & Capabilities”窗格的“Bundle Identifier”字段中更新其 bundle ID。

对于 watchOS 目标，Xcode 会更新对应的 [WKCompanionAppBundleIdentifier](../bundleresources/information-property-list/wkcompanionappbundleidentifier.md) 和 [WKAppBundleIdentifier](../bundleresources/information-property-list/wkappbundleidentifier.md) 信息属性列表键。

## 更改依赖于主 bundle ID 的键

更新任何其他包含主 bundle ID 的信息属性列表键和 entitlement 键。

例如，如果你使用轻 App（App Clip），请更改关联的 [com.apple.developer.associated-appclip-app-identifiers](../bundleresources/entitlements/com.apple.developer.associated-appclip-app-identifiers.md) 和 [Parent Application Identifiers Entitlement](../bundleresources/entitlements/com.apple.developer.parent-application-identifiers.md) 键。如果你有 App 扩展，请务必也更改 [com.apple.developer.app-migration.data-container-access](../bundleresources/entitlements/com.apple.developer.app-migration.data-container-access.md) 键。

## 在 App Store Connect 中更新 bundle ID

> [!important] 重要
> 如果你之前已向 App Store Connect 上传过构建版本，则无法更改 bundle ID。请改用该 bundle ID 创建新的 App 记录，而不是更新现有的 App 记录。有关更多信息，请参阅[添加新 App](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app)。

如果你计划通过 App Store 分发 App，并且已经创建了 App 记录，但尚未上传构建版本，那么你仍然可以在 App 记录中更改 bundle ID，使其与你的 Xcode 项目匹配。在 Xcode 项目中更改 bundle ID 后，要在 App Store Connect 的 App 记录中更新 bundle ID：

1. 在设备上构建并运行你的 App，以注册新的 bundle ID 并更新配置描述文件（provisioning profile）。
2. 在 App Store Connect 中，选择“Apps”，然后选择你的 App。
3. 在“Distribution”窗格中，选择侧边栏中“General”下的“App Information”。
4. 在右侧“General Information”下的“Bundle ID”弹出菜单中选择新的标识符，然后点按“Save”。

有关更多信息，请参阅[查看和编辑 App 信息](https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information)。

更新 App Store Connect 中任何其他使用了 bundle ID 的设置，例如 App 内购买设置。重新向 Apple 申请任何需要批准的特别 entitlement。删除现有的 App 记录并不会使其 bundle ID 变得可用。

> [!note] 注意
> 如果你使用任何依赖于 App 的 bundle ID 的第三方服务，请通知它们更新你的 App 的 bundle ID。

## 更新手动管理的配置描述文件

如果你使用手动配置描述文件，请更新这些配置描述文件中的 App ID，使其与项目中的 bundle ID 匹配。有关更多信息，请参阅开发者帐户帮助中的[编辑、下载或删除配置描述文件](https://developer.apple.com/help/account/provisioning-profiles/edit-download-or-delete-profiles)。在开发者帐户中更新配置描述文件后，你可以通过 Xcode > Settings > Accounts，在选择你的帐户后，使用“Download Manual Profiles”按钮进行下载。

如果你切换“Signing & Capabilities”窗格中的“Automatically manage signing”复选框，Xcode 会为你更新配置描述文件。

## 另请参阅

### 设置与维护

- [让依赖项对 Xcode Cloud 可用](making-dependencies-available-to-xcode-cloud.md) — 审查依赖项并使其对 Xcode Cloud 可用，然后再配置项目以使用 Xcode Cloud。
- [为你的团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 以团队形式开始使用 Xcode Cloud 进行持续集成和交付。
- [跨 Xcode Cloud 工作流程共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定义别名与多个工作流程共享配置。
- [跨 Xcode Cloud 工作流程共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 通过使用共享的环境变量，将通用配置应用于多个工作流程。
- [使用 Xcode Cloud 构建 Swift package 和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将你的 Swift package 或 Swift Playgrounds App 项目添加到 Xcode 项目中，以便在 Xcode Cloud 中构建它。
- [为 Xcode Cloud 构建版本设置下一个构建编号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 从自定义构建编号开始为现有的 Mac App 构建版本编号，以避免版本冲突。
- [在 App 的 beta 版本中包含给测试者的备注](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 向 Xcode 项目添加文本文件，以便向 beta 测试者提供关于测试内容的备注。
- [从 Xcode Cloud 中移除你的项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 中移除你的项目以删除 App 和工作流程数据、断开 Git 仓库连接，并移除 Slack 集成。
