---
title: 通过素材目录配置 App 图标
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-your-app-icon
source_url: 'https://developer.apple.com/documentation/xcode/configuring-your-app-icon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-your-app-icon.json'
content_hash: 'sha256:140bdb4b8b519612'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [素材管理](asset-management.md)

# 通过素材目录配置 App 图标

<sub>文章</sub>

将 App 图标的变体添加至素材目录，使其在 App Store、主屏幕、设置和搜索结果等位置中代表你的 App。

## 概述

> [!important] 重要
> 若要通过 Icon Composer 为所有变体（包括不同平台和外观）创建 App 图标，请参阅[使用 Icon Composer 创建 App 图标](creating-your-app-icon-using-icon-composer.md)。

每个 App 都有独特的 App 图标，用以传达 App 的用途，并使其在整个系统中易于识别。App 需要多个 App 图标变体，以便在不同场景中呈现良好效果。Xcode 可以借助单张高分辨率图像自动生成这些变体，你也可以通过项目素材目录中 App 图标的图像集来配置 App 图标变体。visionOS 和 tvOS 的 App 图标由多层堆叠的图像层构成，你可以在项目的素材目录中进行配置。iOS 和 iPadOS 的 App 图标支持深色和着色样式。

有关 App 图标的设计指导，请参阅[人机界面指南 \> App 图标](../design/human-interface-guidelines/app-icons.md)。

### 创建 App 图标

当你从模板创建项目时，系统会自动包含一个包含 `AppIcon` 的默认素材目录（`Assets.xcassets`）。若你没有默认素材目录或现有 `AppIcon`，或者想要提供替代方案，可以手动将 App 图标添加到素材目录：

1. 在项目导航器中，选择一个素材目录。
2. 单击大纲视图底部的添加按钮 (+)。
3. 在弹出的菜单中，选择 _OS 变体_ \> _OS 变体_ App 图标。Xcode 会创建一个名为 `AppIcon` 的新 App 图标集或图像栈。

### 指定 App 图标变体

App 图标的变体会出现在系统的各处，例如主视图、设置和搜索结果中：

- iOS、iPadOS、tvOS 和 watchOS App 可以从一张 1024×1024 像素的图像自动生成所有图标变体。这是新建 iOS、iPadOS、tvOS 和 watchOS App，或在素材目录中新建图标时的默认行为。若你已有提供多种变体的现有项目，当图标仅需一种尺寸时，可以考虑只提供一个尺寸。不过，如果你想要自定义 App 的图标变体（例如在更大尺寸下显示更多细节），可以为各变体提供单独的素材。
- 对于 macOS 和 tvOS，你需要为每种尺寸提供素材。
- 对于 visionOS，你需要提供一张 1024x1024 像素的素材。

为你 App 支持的每个平台，选择在素材目录中使用单一尺寸还是提供所有尺寸：

![](../../../attachments/60bda3e29a3e0ef837fa9090387bb980/configuring-your-app-icon-1@2x.png)

<sub>Xcode 中素材目录的截图。大纲视图中选中了名为 AppIcon 的 App 图标集。检查器区域显示多个图像槽，并附有描述所需图像尺寸、分辨率和用途的标签。</sub>

1. 在项目导航器中，选择一个素材目录。
2. 在素材目录中，选择该图标。
3. 要查看和编辑属性，请从 Xcode 的“视图”菜单中选择“检查器”\>“属性”。
4. 从你要更改的平台对应的弹出菜单中，选择“单一尺寸”或“所有尺寸”。

为你 App 支持的每个平台，添加一张 Xcode 可用来生成图标变体的图像，或者为素材目录中图标集的每个图标变体添加一张图像：

![](../../../attachments/499364dc68d2a0b800e392c8c0b123b6/configuring-your-app-icon-2@2x.png)

<sub>Xcode 中素材目录的截图。大纲视图中选中了名为 AppIcon 的 App 图标集。详细信息区域显示多个图像槽，并附有描述所需图像尺寸、分辨率和用途的标签。</sub>

1. 在项目导航器中，选择一个素材目录。
2. 在素材目录中，选择该图标。
3. 从“访达”中，将 App 图标的图像变体拖到 Xcode 素材目录详细信息区域中与其分辨率和用途匹配的图像槽中。visionOS 和 tvOS App 图标会组合由多个图像层构成的图像栈，以营造景深感。对于 tvOS App，素材目录包含一个“App 图标与推荐项目图像”文件夹，其中包含不同的 App 图标和启动图像集。

### 为 iOS 和 iPadOS 添加深色和着色图标变体

iOS 和 iPadOS 支持三种 App 图标样式变体：浅色、深色和着色。你可以创建自己的变体，以确保每个变体都完全符合你的预期。

![](../../../attachments/95e7712fe79245cdc1cd52f581ad484f/configuring-your-app-icon-5@2x.png)

<sub>Xcode 中素材目录的截图。大纲视图中选中了名为 AppIcon 的 App 图标集。检查器区域显示多个图像槽，并附有描述任意、深色和着色图标外观的标签。</sub>

要将这些图标变体添加到你的 App：

1. 在项目导航器中，选择一个素材目录。
2. 在素材目录中，选择该图标。
3. 从 Xcode 菜单中选择“视图”\>“检查器”\>“属性”。
4. 从 iOS 弹出菜单中选择“单一尺寸”。
5. 然后从“外观”弹出菜单中选择“任意”、“深色”或“着色”。

从弹出菜单中选择“外观”后，会显示两个图像槽。将你的深色和着色 App 图标拖到相应的图像槽中。请提供灰度图像作为着色 App 图标。提供具有透明背景的深色 App 图标，以便系统提供的背景可以透出。

如果愿意，你可以利用系统自动为所有 App 图标应用的处理效果。该效果经过智能设计，可以保留设计意图并保持清晰易读。这也有助于在主屏幕上维持一致的视觉效果。

有关针对 iOS 和 iPadOS 的设计指导，请参阅[人机界面指南 \> App 图标](https://developer.apple.com/design/human-interface-guidelines/app-icons)。

### 配置图像栈的图层

默认情况下，visionOS 和 tvOS App 图标由三个图层构成。这是 visionOS 图标支持的最大图层数，但在构建 tvOS 图标时，你最多可以使用五个图层。要添加图层，请单击添加按钮，选择 _OS 变体_ \> _OS 变体_ App 图标图层。要移除图层，请选择该图层并单击移除按钮 (-)。

![](../../../attachments/f83d49f055d93a97e77b6e445dc0a9a6/configuring-your-app-icon-3@2x.png)

<sub>Xcode 中素材目录的截图。大纲视图中选中了名为 AppIcon 的 App 图标栈。详细信息区域显示栈中每个图层的图像槽及其标签。</sub>

通过从“访达”中将图像拖到 Xcode 素材目录详细信息区域的图像槽中，为每个图层添加图像。有关如何使用图层的信息，请参阅 App 图标指南中的 [visionOS](../design/human-interface-guidelines/app-icons.md#visionOS) 和 [tvOS](../design/human-interface-guidelines/app-icons.md#tvOS) 部分。

> [!note] 注意
> 你可以使用 Parallax Previewer app 或 Parallax Exporter 插件来创建和预览图层源表示（`.lsr` 和 `.xlsr`）文件，然后将其导入到 Xcode 的素材目录中。以 LSR 文件格式保存文件以将 tvOS 图标导入 Xcode，以 XLSR 文件格式保存以导入 visionOS 图标。请从 [Apple 设计资源](https://developer.apple.com/design/resources) 网站下载这些文件。

### 指定 App Store 图标

如果你通过 App Store 分发 App，则必须提供 App 图标图像以在 App Store 中使用。在项目导航器中，选择一个素材目录，然后将图标图像添加到 App 图标集或图像栈中相应的图像槽中。App Store 图像槽的位置因平台而异。

| 平台 | App Store 图标位置 |
|---|---|
| iOS | 将图标图像拖至 iOS 1024pt 图像槽。 |
| iMessage | 对于 iOS 目标，将图标图像拖至 `AppIcon` 集中的 iOS 1024pt 图像槽。对于 iMessage 扩展目标，将图标拖至 `iMessage App Icon` 集中的“Messages App Store”图像槽。 |
| Sticker Pack | 将图标图像拖至 iOS 1024pt 图像槽和“Messages App Store”图像槽。 |
| macOS | 将图标图像拖至“App Store - 2x”图像槽。 |
| tvOS | 将图像拖至“App 图标与推荐项目图像”文件夹中“App 图标 - App Store”栈的图层图像槽。App Store 会根据图像栈的图层生成图标。 |
| visionOS | 将图像拖至你 visionOS App 图标栈的图层图像槽。App Store 会根据图像栈的图层生成图标。 |
| watchOS | 对于 iOS 目标，将图标图像拖至 iOS 1024pt 图像槽。对于 WatchKit App 目标，将图标图像拖至 watchOS 图像槽。 |

### 更改默认 App 图标集

如果你不是从模板创建的项目，或者想要更改默认的 App 图标集，可以在目标的构建设置中指定要使用的图标集。

1. 在项目导航器中选择项目，然后在项目编辑器中选择目标。
2. 在“通用”面板的“App 图标与启动屏幕”部分，从“App 图标来源”弹出菜单中选择 App 图标集。

![](../../../attachments/7f8ca1d3b817399313a5f211452716ca/configuring-your-app-icon-4@2x.png)

<sub>目标设置的截图，显示选中了“通用”标签。“App 图标与启动屏幕”部分显示了一个名为“App 图标来源”的字段，其中列出了要从素材目录使用的 App 图标集的名称。</sub>

如果你不选中“包含所有 App 图标素材”选项，Xcode 在构建 App 时只会包含你在“App 图标来源”弹出菜单中指定的 App 图标集。如果你希望在 Debug 和 Release 构建中使用不同的图标，但又不想在 Release App 包中包含 Debug 图标，则可以不选中此选项。你可以通过修改“构建设置”标签中的“主要 App 图标集名称”构建设置，分别为 Debug 和 Release 配置 App 图标。

Xcode 还会包含你在“备用 App 图标集”构建设置下指定的任何其他 App 图标集。请包含你的 App 可以通过 [setAlternateIconName(_:completionHandler:)](<../uikit/uiapplication/setalternateiconname(__completionhandler_).md>) 选择或在 App Store 产品页中使用的所有图标集。

有关配置在 App Store Connect 中使用图标的测试，请参阅[产品页面优化](https://developer.apple.com/app-store/product-page-optimization)。

## 另请参阅

### App 图标与启动屏幕

- [使用 Icon Composer 创建 App 图标](creating-your-app-icon-using-icon-composer.md) — 使用 Icon Composer 为不同平台和外观设计不同样式的 App 图标。
- [配置 App 以使用备用 App 图标](configuring-your-app-to-use-alternate-app-icons.md) — 将备用 App 图标添加到 App，并让人们选择要显示的图标。
- [指定 App 的启动屏幕](specifying-your-apps-launch-screen.md) — 通过自定义启动屏幕，让你的 iOS App 启动体验更快、响应更迅速。
