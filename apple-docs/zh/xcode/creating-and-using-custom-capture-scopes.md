---
title: 创建和使用自定捕获范围
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-and-using-custom-capture-scopes
source_url: 'https://developer.apple.com/documentation/xcode/creating-and-using-custom-capture-scopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-and-using-custom-capture-scopes.json'
content_hash: 'sha256:e4fdf9014412efb0'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 开发者工作流程](metal-developer-workflows.md)

# 创建和使用自定捕获范围

<sub>文章</sub>

通过使用自定捕获范围，捕获特定的 GPU 命令。

## 概述

当你点击 Xcode 调试栏中的 Metal Capture 按钮，使用默认捕获范围（capture scope）捕获一帧时，所得到的捕获结果包含单帧的全部数据。在某些情况下，你可能希望调试部分帧而非整帧。为此，你可以设置并使用自定捕获范围，精确选择要记录哪些 Metal 命令。

> [!note] 注意
> 不要自行分配自定捕获范围。而是应该调用 [MTLCaptureManager](../metal/mtlcapturemanager.md) 的以下某个方法：[makeCaptureScope(device:)](<../metal/mtlcapturemanager/makecapturescope(device_).md>) 或 [makeCaptureScope(commandQueue:)](<../metal/mtlcapturemanager/makecapturescope(commandqueue_)-1rozd.md>)。

### 定义捕获边界

在你的捕获范围上调用 [begin()](<../metal/mtlcapturescope/begin().md>)，以指示 Metal 调试器记录 App 后续的 Metal 活动。要停止记录一帧并呈现 Metal 调试器，调用 [end()](<../metal/mtlcapturescope/end().md>)。

```swift
// 在渲染循环之外创建 myCaptureScope。
myCaptureScope.begin()

if let commandBuffer = commandQueue.makeCommandBuffer() {
    // 执行 Metal 工作。
    commandBuffer.commit()
}

myCaptureScope.end()
```

> [!important] 重要
> 在渲染或计算循环之外创建捕获范围，将你的调用置于 [begin()](<../metal/mtlcapturescope/begin().md>) 和 [end()](<../metal/mtlcapturescope/end().md>) 之间。要让 Metal 捕获正常工作，你需要在捕获范围所涵盖的工作持续期间，持有对该活跃捕获范围的强引用。

### 为捕获范围加上标签

要在从 Metal Capture 弹出窗口捕获跟踪信息时识别你的自定捕获范围，请设置捕获范围的 label 属性。

```swift
myCaptureScope.label = "My Capture Scope"
```

当你准备好捕获一帧时，点击调试栏中的 Metal Capture 按钮。在那里，你可以在可捕获列表中找到带有匹配标签的自定捕获范围。

只要你希望该选项在 Xcode 中可见，就应在代码中持有对该捕获范围的强引用。

### 将自定捕获范围设为默认范围

当你从 Xcode 执行捕获时，默认使用 [defaultCaptureScope](../metal/mtlcapturemanager/defaultcapturescope.md) 指定的捕获范围。如果该属性的值为 `nil`，Xcode 会使用可绘制对象的呈现边界来定义默认捕获范围；例如，使用你对 [present(_:)](<../metal/mtlcommandbuffer/present(__).md>) 或 [present()](<../metal/mtldrawable/present().md>) 方法的调用。

要更改默认范围，创建一个 [MTLCaptureScope](../metal/mtlcapturescope.md) 实例，并将其赋值给 [defaultCaptureScope](../metal/mtlcapturemanager/defaultcapturescope.md)。

```swift
MTLCaptureManager.shared().defaultCaptureScope = myCaptureScope
```

## 另请参阅

### 为调试准备项目

- [构建包含内嵌着色器源代码的项目](building-your-project-with-embedded-shader-sources.md) — 通过在构建中包含源代码，为调试项目的着色器做好准备。
- [命名资源和命令](naming-resources-and-commands.md) — 借助标签和分组，增强对 Metal App 的调试。
