---
title: 使用 SwiftUI 创建 App 界面
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-your-app-s-interface-with-swiftui
source_url: 'https://developer.apple.com/documentation/xcode/creating-your-app-s-interface-with-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-your-app-s-interface-with-swiftui.json'
content_hash: 'sha256:d52f047521860a6e'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md)

# 使用 SwiftUI 创建 App 界面

<sub>文章</sub>

使用 SwiftUI 开发 App，借助交互式预览保持代码与布局同步。

## 概述

如果选择 SwiftUI 框架来开发 App，你会在布置用户界面时看到画布中的交互式预览。Xcode 会保持你对源代码、界面布局和画布所做的更改同步。例如，在源代码编辑器中编辑视图时，Xcode 会更新画布中对应的视图。

如果你的项目是从“多平台”模板创建的，或者在选择其他模板时选择 SwiftUI 作为界面，Xcode 会自动为 SwiftUI 代码添加默认的预览宏。否则，你可以通过代码智能生成预览，或自行添加预览宏。

有关 Xcode 模板的更多信息，请参阅[为 App 创建 Xcode 项目](creating-an-xcode-project-for-an-app.md)。有关添加预览的更多详细信息，请参阅[在 Xcode 中预览 App 界面](previewing-your-apps-interface-in-xcode.md)。

### 显示 SwiftUI 预览

要显示预览，请在项目导航器中选择包含预览宏的文件，如有必要，请选择“编辑器”>“画布”以显示画布。然后点击画布右上角的“恢复（Resume）”按钮开始预览。Xcode 会构建并运行代码，直接在画布中显示结果。

![屏幕截图，显示在项目导航器中选定了一个 SwiftUI 文件，并在画布中显示预览。](../../../attachments/68c5d648f4b4d7f25dcf2194a9f248e5/creating-your-app-s-interface-with-swiftui-1@2x.png)

使用画布底部的控制来切换不同的预览模式、添加不同外观的变体、选择方向等设备设置以及更改设备。

> [!note] 注意
> 如果向文件添加了多个预览和 playground 宏，你可以使用画布顶部显示的选项卡在它们之间切换。要向 Swift 代码添加 playground，请参阅[使用 playground 宏运行代码片段](running-code-snippets-using-the-playground-macro.md)。

### 使用资源库添加视图和修饰符

你可以从资源库向代码添加视图和修饰符，Xcode 会保持预览与更改同步。

要打开资源库，请选择“显示”>“显示资源库”（按住 Option 键可将其作为窗口打开）。然后点击工具栏中的“视图”或“修饰符”按钮，将用户界面元素从资源库拖到源代码中。要更快地找到元素，请在资源库顶部的搜索栏中输入元素名称。

![屏幕截图，显示已选中“视图”标签的资源库，并选中了一个 SwiftUI 元素。](../../../attachments/d0060b8a4c49daf47b1750025833c2d8/creating-your-app-s-interface-with-swiftui-2@2x.png)

### 编辑用户界面元素

编辑源代码中的用户界面元素，即可在预览中看到更改。要突出显示预览中出现的源代码中的元素，请点击画布下方的“可选（Selectable）模式”，然后点击预览中的元素。之后返回默认的“实时（Live）模式”，即可在预览中测试并与视图交互。

![](../../../attachments/59407de53b479558caf20e5d720b04b3/creating-your-app-s-interface-with-swiftui-3@2x.png)

<sub>屏幕截图，显示右侧预览中选中了一个元素，左侧源代码编辑器中关联的代码被高亮显示。</sub>

然后使用代码补全、代码智能和代码片段资源库来协助编写 Swift 和 SwiftUI 代码。有关更多信息，请参阅[在 Xcode 中编辑源文件](editing-source-files-in-xcode.md)和[在 Xcode 中使用智能编写代码](writing-code-with-intelligence-in-xcode.md)。

## 另请参阅

### 基础

- [为 App 创建 Xcode 项目](creating-an-xcode-project-for-an-app.md) — 通过从模板创建 Xcode 项目来开始开发你的 App。
- [在 Xcode 中预览 App 界面](previewing-your-apps-interface-in-xcode.md) — 快速迭代设计，并在不同 Apple 设备上预览 App 的显示效果。
- [构建并运行 App](building-and-running-an-app.md) — 编译源文件并组装 App 包，以在设备或模拟器上运行。
- [Xcode 更新](../updates/xcode.md) — 了解 Xcode 的重要变更。
