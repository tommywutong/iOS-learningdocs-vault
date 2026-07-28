---
title: 使用 asset catalog 管理资源
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/managing-assets-with-asset-catalogs
source_url: 'https://developer.apple.com/documentation/xcode/managing-assets-with-asset-catalogs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/managing-assets-with-asset-catalogs.json'
content_hash: 'sha256:0760bcf313b9af61'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [资源管理](asset-management.md)

# 使用 asset catalog 管理资源

<sub>文章</sub>

通过 asset catalog 在 Xcode 项目中添加、整理和编辑资源集合。

## 概述

asset catalog 帮助你快速整理和管理 App 的资源。在 asset catalog 中，每个 _asset set（资源集合）_ 代表一种资源，例如一张图片、一个颜色或一个数据文件，你的 App 在运行时加载这些资源。一个 asset set 包含该资源的一个或多个变体，用于适配不同的设备特性，例如平台、屏幕尺寸、分辨率、外观和语言。当你在代码中引用某个资源时，系统会根据当前设备的特性在运行时决定显示哪个变体。

### 创建新的 asset set

当你通过模板创建项目时，它会自动包含一个名为 `Assets.xcassets` 的 asset catalog，该文件显示在项目导航器中。这个默认的 asset catalog 包含用于 App 强调色和 App 图标的空 asset set。你可以在这个默认的 asset catalog 中添加更多的 asset set。

要将资源导入到你的项目中，首先，在你的 asset catalog 中创建一个新的 asset set。

1. 在项目导航器中，选择该 asset catalog。
2. 点击大纲视图（outline view）底部的添加按钮（+）。
3. 在弹出的菜单中，选择要创建的 asset set 的类型。

新的空 asset set 会出现在大纲视图中，并在详情区域打开。

![](../../../attachments/6815e8fa31b70609d264f979266fa596/managing-assets-with-asset-catalogs-1@2x.png)

<sub>Xcode 中默认 asset catalog 的截图。左侧的大纲视图显示了三个 asset set——accent color（强调色）、app icon（App 图标）和 image（图片）。其中 image（图片）集被选中，在右侧详情区域显示了三个带有 1x、2x 和 3x 标签的空图像槽。</sub>

若要使用支持 [Liquid Glass](../technologyoverviews/liquid-glass.md) 的多层 Icon Composer 文件来代替图标 asset set，请参阅[使用 Icon Composer 创建 App 图标](creating-your-app-icon-using-icon-composer.md)。

### 添加新资源

接下来，将你的资源添加到空的 asset set 中。在大纲视图中选中新的 asset set 后，将你想要从访达（Finder）导入的资源拖放到详情区域的某个槽中。

![](../../../attachments/fde3f2c3641843d417853ca4df14f28c/managing-assets-with-asset-catalogs-2@2x.png)

<sub>Xcode 中 asset catalog 的截图。一个名为 Image 的图片集在详情区域的 1x 槽中包含了一张橙子的图片。</sub>

asset set 包含一个或多个_槽（well）_，你可以通过这些槽为不同的设备特性指定资源的变体。每个槽都有一个标签，描述了适用于它的特定特性集。如果你希望提供更多资源变体，可以将每个资源文件拖拽到对应的槽中。你可以在属性检查器（Attributes inspector）中选择更多选项来显示额外的槽。

### 创建新的 asset catalog

如果你希望创建额外的 asset catalog 来整理更多 App 资源，可以手动创建一个 asset catalog。

1. 选择“文件（File）”>“新建（New）”>“从模板新建文件（File from Template）”。
2. 选择“资源（Resource）”>“Asset Catalog”，然后点击“下一步（Next）”。
3. 为 asset catalog 命名，选择位置，然后点击“创建（Create）”。

新的 asset catalog 会出现在项目导航器中，并在编辑区打开。
