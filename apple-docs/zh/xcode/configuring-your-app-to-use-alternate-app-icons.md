---
title: 将 App 配置为使用备用 App 图标
framework: xcode
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-your-app-to-use-alternate-app-icons
source_url: 'https://developer.apple.com/documentation/xcode/configuring-your-app-to-use-alternate-app-icons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-your-app-to-use-alternate-app-icons.json'
content_hash: 'sha256:09250a5337acf321'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [素材管理](asset-management.md)

# 将 App 配置为使用备用 App 图标

<sub>示例代码</sub>

为你的 App 添加备用 App 图标，让人们可以选择显示哪个图标。

## 概述

此示例代码项目演示了如何配置你的 App，以便人们可以更改主屏幕、“聚焦”以及系统其他位置显示的图标。人们可以在 App 界面中，从你提供的一组图标里选择一个备用图标。

### 为备用图标添加图标文件

对于每个备用 App 图标，项目需要一个 Icon Composer 文件。使用 Icon Composer 创建你的 App 图标，然后将其添加到 Xcode 项目的项目导航器中。更多信息，请参阅[使用 Icon Composer 创建你的 App 图标](creating-your-app-icon-using-icon-composer.md)。有关设计指导，请参阅[App 图标](../design/human-interface-guidelines/app-icons.md)。

### 配置素材目录编译器

系统从 App 的 `Info.plist` 文件的顶层键 [CFBundleIcons](../bundleresources/information-property-list/cfbundleicons.md) 中收集有关 App 图标的信息。Xcode 会针对项目在“素材目录编译器 - 选项”（Asset Catalog Compiler - Options）下的构建设置中指定的图标，在该文件中添加条目。

对于项目在“备用 App 图标集”（Alternate App Icon Sets）构建设置中按名称指定的每个图标文件，Xcode 会在键 [CFBundleAlternateIcons](../bundleresources/information-property-list/cfbundleicons/cfbundlealternateicons.md) 下添加一个条目。

Xcode 会在键 [CFBundlePrimaryIcon](../bundleresources/information-property-list/cfbundleicons/cfbundleprimaryicon.md) 下，填入“主要 App 图标集名称”（Primary App Icon Set Name）构建设置中指定的主要 App 图标名称。你也可以在“通用”（General）面板的“App 图标与启动屏幕”（App Icons and Launch Screen）部分找到此设置。有关构建设置的更多信息，请参阅[构建设置参考](build-settings-reference.md)。

> [!important] 重要
> 要更改 `CFBundleIcons`、`CFBundleAlternateIcons` 和 `CFBundlePrimaryIcon` 的值，请修改它们的相关构建设置。不要手动从 `Info.plist` 文件中编辑或移除这些键。

或者，你可以使用构建配置文件来指定备用 App 图标。向 Xcode 项目添加一个构建配置文件，然后将 `ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES` 构建设置添加到配置文件中。将 `ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES` 设置为与备用 App 图标名称匹配的字符串列表。

```
ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES = AppIcon-Green AppIcon-Blue AppIcon-Orange AppIcon-Pink AppIcon-Purple AppIcon-Teal AppIcon-Yellow
```

有关构建配置文件的更多信息，请参阅[向你的项目添加构建配置文件](adding-a-build-configuration-file-to-your-project.md)。

### 更改 App 图标

当人们在 App 界面中选择备用图标时，App 会调用 [setAlternateIconName(_:completionHandler:)](<../uikit/uiapplication/setalternateiconname(__completionhandler_).md>) 并传入新图标的名称。这会告知系统为此 App 显示新图标。系统自动显示一个提醒，通知人们这一更改。传入 `nil` 则显示 App 的主要图标。

```swift
UIApplication.shared.setAlternateIconName(iconName) { error in
    if let error {
        self.logger.error("Failed request to update the app’s icon: \(error)")
    }
}

```

当前图标的名称可通过属性 [alternateIconName](../uikit/uiapplication/alternateiconname.md) 获取。

## 另请参阅

### App 图标与启动屏幕

- [使用 Icon Composer 创建你的 App 图标](creating-your-app-icon-using-icon-composer.md) — 使用 Icon Composer 为不同平台和外观设计你的 App 图标样式。
- [使用素材目录配置你的 App 图标](configuring-your-app-icon.md) — 向素材目录中添加 App 图标变体，用于在 App Store、主屏幕、设置和搜索结果等位置展示你的 App。
- [指定你的 App 的启动屏幕](specifying-your-apps-launch-screen.md) — 通过自定义启动屏幕，让你的 iOS App 启动体验更快、响应更迅速。

## 下载

- [ConfiguringYourAppToUseAlternateAppIcons.zip](https://docs-assets.developer.apple.com/published/1bbbd245213e/ConfiguringYourAppToUseAlternateAppIcons.zip)
