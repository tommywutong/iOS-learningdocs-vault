---
title: 向你的 Xcode 项目添加图像
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adding-images-to-your-xcode-project
source_url: 'https://developer.apple.com/documentation/xcode/adding-images-to-your-xcode-project'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adding-images-to-your-xcode-project.json'
content_hash: 'sha256:e7ea819e9023d7eb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Asset management](asset-management.md)

# 向你的 Xcode 项目添加图像

<sub>文章</sub>

将图像导入你的项目，管理它们的外观和变体，并在运行时加载它们。

## 概述

Xcode 项目通常包含许多图像，并且需要管理每张图像的多个变体，才能为你 App 运行所在的所有设备和平台打造出色的视觉体验。例如，你的 App 可能会根据设备屏幕尺寸、分辨率、语言、外观、色域以及许多其他因素，显示某张图像的不同版本。如果你的 App 使用图像，你可以使用素材目录（asset catalog），通过图像集来简化对这些图像的管理。

### 创建一个新的图像集

_图像集_ 代表你打算在运行时加载的一张图像。每个图像集都包含单张图像的多个变体，你可以对这些变体进行自定，以支持不同的设备特征。如果你的 App 中有多张图像，你需要为每张图像创建一个图像集。

要创建图像集，请在 Xcode 之外生成一个图像素材，然后将其导入素材目录。构建项目时，系统会将该图像格式转换为最合适的表示形式。

1. 在项目导航器中，选择一个素材目录：一个扩展名为 `.xcassets` 的文件。
2. 将一张图像从访达（Finder）拖到大纲视图中。大纲视图中会出现一个新的图像集，并且该图像素材会出现在详情区域的某个池（well）中。
3. 双击大纲视图中的图像集名称，为该图像集重命名一个描述性名称，然后按 Return 键。

![](../../../attachments/fde3f2c3641843d417853ca4df14f28c/adding-images-to-your-xcode-project-1@2x.png)

<sub>Xcode 中一个素材目录的截图。一个名为 Image 的图像集，在详情区域的 1x 池中包含一张橙子的图片。</sub>

### 为图像选择支持的外观和变体

默认情况下，Xcode 会为每个图像集创建 @1x、@2x 和 @3x 分辨率对应的池。如果你导入的图像文件名以 `@2x` 或 `@3x` 结尾，Xcode 会自动将该图像放入对应分辨率的池中。请为你 App 支持的所有设备，提供所有图像的高分辨率版本。

除了分辨率之外，你的图像素材还可能因其他设备特征而有所不同。使用 Attributes 检查器，来添加、移除和编辑要包含在图像集中的图像变体。你可以在素材目录中或在 Interface Builder 中完成此任务。

1. 在项目导航器中，选择素材目录。
2. 在大纲视图中，选择图像集。
3. 在检查器区域，选择 Attributes 检查器。
4. 在 Attributes 检查器中，添加、移除和编辑设备特征设置，以显示你想要自定的各个变体所对应的额外图像池。

![Attributes 检查器的截图，选中了默认的 Universal 选项。](../../../attachments/039f3c8fc6decb8e7e250da05956b546/adding-images-to-your-xcode-project-2@2x.png)

有关图像尺寸和分辨率的更多信息，请参阅[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/ios)中的[图像尺寸和分辨率](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution)。

### 将图像拖到变体池中

为你的图像集选择好所需的特征设置后，通过将其他图像拖到图像集中对应的池里，来提供图像变体。

1. 在项目导航器中，选择素材目录。
2. 在大纲视图中，选择图像集。
3. 在访达中，将该图像的其他变体拖到详情区域中与其分辨率或其他特征相匹配的池中。

### 从代码中加载图像素材

要在代码中使用该图像，请用图像集的名称初始化一个图像。不要包含文件扩展名。

```swift
// SwiftUI
let image = Image("ImageName")

// UIKit
let image = UIImage(named: "ImageName")

// AppKit
let image = NSImage(named: "ImageName")
```

## 另请参阅

### 图像

- [Creating custom symbol images for your app](../uikit/creating-custom-symbol-images-for-your-app.md) — 使用 SF Symbols 创建、组织并标注符号图像。
