---
title: 使用 playground 宏运行代码片段
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/running-code-snippets-using-the-playground-macro
source_url: 'https://developer.apple.com/documentation/xcode/running-code-snippets-using-the-playground-macro'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/running-code-snippets-using-the-playground-macro.json'
content_hash: 'sha256:8a820011bf72b164'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Source editor](source-editor.md)

# 使用 playground 宏运行代码片段

<sub>文章</sub>

将 playground 添加到你的代码中，在画布上运行并显示结果。

## 概述

你可以使用直接添加到 Swift 文件中的 playground，来探索和实验你的代码。Xcode 会立即在画布中显示运行 playground 的结果。Xcode 还可以针对你代码中的符号或所选内容，为你生成 playground。

![](../../../attachments/fb9d0187765b7ad5bcadeb5ced13183e/running-playgrounds-canvas-output@2x.png)

<sub>屏幕截图显示了左侧的「项目」导航器、中间源代码编辑器中打开的一个 SwiftUI 文件（包含一个 playground 和一个预览），以及右侧显示 playground 结果的画布。</sub>

> [!tip] 提示
> 你添加到 SwiftUI 文件中的预览也会出现在画布中。有关添加预览的信息，请参阅[在 Xcode 中预览你 App 的界面](previewing-your-apps-interface-in-xcode.md)。

### 将 playground 添加到你的 Swift 文件

你可以在一个 Swift 文件中添加一个或多个 playground。首先，在你的 Swift 文件中导入 Playgrounds 框架。然后将你想要运行的代码片段用 `#Playground` 宏包裹起来，例如：

```swift
import MapKit
import Playgrounds

#Playground {
    // 金门公园
    let latitude = 37.768552
    let longitude = -122.481616
    let location = CLLocationCoordinate2D(latitude: latitude, longitude: longitude)
}
```

如果画布未打开，请选择「Editor」\>「Canvas」以显示画布。然后点按「Resume」按钮，运行 playground 并在画布中查看结果。

### 在画布中查看结果

在画布中，使用每行代码下方的控件来查看详细信息。例如，点按变量名下方的显示三角形，可以显示或隐藏其值。

如果某行代码包含可查看的对象——例如图像、颜色或位置——Xcode 会将其显示在画布中。要折叠该视图，请将眼睛按钮切换为关闭状态。例如，如果某行代码打印了一个值，Xcode 会显示该值。如果某行代码设置了一个 [CLLocationCoordinate2D](../corelocation/cllocationcoordinate2d.md) 变量，Xcode 会在地图上显示该位置。

![](../../../attachments/25772e77c023c7a5f6689521b7c563aa/running-playgrounds-line-of-code@2x.png)

<sub>画布的屏幕截图，显示了一个可查看的 CLLocationCoordinate2D 变量在地图上的展示情况，变量名下方的显示三角形处于打开状态，眼睛按钮处于开启状态。</sub>

### 在多个 playground 和预览之间切换

如果你添加了多个 playground，你可以使用画布顶部出现的选项卡，在这些 playground 以及你添加到同一文件中的任何预览之间切换。当你点按某个选项卡时，Xcode 会运行相应的 playground 或预览，并在画布中显示结果。playground 选项卡的名称前面带有烧杯图标，预览选项卡的名称前面带有眼睛图标。

### 从你的代码生成 playground

要快速添加一个 playground，可以让编码助手根据你代码中的所选内容为你生成一个。

在源代码编辑器中，选中一个符号并点按出现的编码助手图标，或者按住 Control 点按某个符号，然后从弹出菜单中选择「Show Coding Tools」\>「Show Coding Tools」。在出现的编码工具弹出窗口中，点按「Generate a Playground」以添加一个 playground。

![](../../../attachments/61b5ca67c0c86f92b216d045d8ac8690/running-playgrounds-generate-playground@2x.png)

<sub>屏幕截图显示了侧边栏中的「项目」导航器、源代码编辑器中打开的一个 Swift 文件（其中有一个高亮显示的符号），以及在「Show Coding Tools」弹出窗口中被选中的「Generate a Playground」按钮。</sub>

Xcode 会在画布区域显示该 playground 的结果，对于 SwiftUI 文件，还会显示预览。如果画布未打开，请选择「Editor」\>「Canvas」以显示它，然后点按「Resume」。

编码工具与编码助手用来编写代码的同一个大语言模型进行通信，以生成该 playground。更多信息，请参阅[在 Xcode 中借助智能功能编写代码](writing-code-with-intelligence-in-xcode.md)。

## 另请参阅

### 源文件的创建、组织与编辑

- [在 Xcode 中编辑源文件](editing-source-files-in-xcode.md) — 使用源代码编辑器的各项功能，帮助你更快地编写、导览、记录和理解代码。
- [在源代码编辑器中使用编码智能功能](using-coding-intelligence-in-the-source-editor.md) — 在你想要修改代码的位置直接提交提示词。
