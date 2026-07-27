---
title: 检查绘制命令的几何图形
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-the-geometry-of-a-draw-command
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-the-geometry-of-a-draw-command'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-the-geometry-of-a-draw-command.json'
content_hash: 'sha256:ebcb4df09c09194a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 检查绘制命令的几何图形

<sub>文章</sub>

通过检查当前几何图形，找出你的 App 的顶点、对象或网格函数中的问题。

## 概述

打开某个几何图形后，你可以使用几何图形查看器查看其线框。首先，点击相机属性按钮并配置透视矩阵。然后，使用鼠标和触控板手势，你可以从不同角度查看几何图形以检查问题。你还可以在场景视图中按住 Control 点击，以启用不同顶点属性的可视化。当你点击某个单独的图元来选中它时，Xcode 会在数据视图中显示其对应顶点的值。此外，你可以在着色器调试器中检查所选图元，对你的着色器进行修改，并实时查看更新后的结果。要了解更多信息，请参阅 [Inspecting the bound resources for a command](inspecting-the-bound-resources-for-a-command.md)。

### 更改投影矩阵

几何图形查看器会向你展示顶点或网格着色器阶段的输出几何图形。为了将几何图形从裁剪空间还原到视图空间，默认情况下，几何图形查看器会应用一个逆投影，使用近平面值为 `0.1`、远平面值为 `100`、视场角为 `65º` 的透视矩阵。但是，如果你使用的是不同的投影矩阵，你的几何图形看起来可能会被压扁或拉伸。

要解决这个问题，你可以点击控制栏左下角的选项按钮，并自定义投影矩阵，使其与你在顶点着色器中使用的投影矩阵一致。

![几何图形查看器中相机属性弹出窗口的屏幕截图，突出显示了投影矩阵控制。](../../../attachments/6d83629a9e812f94549acd110faa6c2a/gputools-metal-debugger-gv-camera-options@2x.png)

### 从不同角度查看你的几何图形

你可以使用鼠标和触控板手势在场景视图中围绕你的几何图形导览。这使你能够放大到特定区域以检查错误的几何图形，或找出最初可能不在视野内的多余几何图形。

![](../../../attachments/4ab409a6e4f7ae9a32a02ff47e064f02/gputools-metal-debugger-gv-rotate@2x.png)

<sub>几何图形查看器的屏幕截图，在场景视图中显示几何图形，并在表格中列出顶点。所选顶点及其同级顶点在场景视图和表格中均已高亮显示。</sub>

### 可视化你的顶点属性

有时候，你的几何图形的某个属性可能存在问题。在这种情况下，几何图形查看器可以使用该属性为你的几何图形着色，以便更容易找出任何不正确的值。要执行此操作，请在场景视图中按住 Control 点击，选择可视化顶点属性，然后选择你想要显示的属性。

![](../../../attachments/661a547446ebf21b7dc02a66f5264da0/gputools-metal-debugger-gv-visualize-attribute@2x.png)

<sub>场景视图上下文菜单的屏幕截图，可视化顶点属性菜单项已高亮显示，法线值子菜单已选中。</sub>

> [!tip] 提示
> 你还可以按住 Control 点击以禁用显示线框和显示顶点，从而更容易看清属性可视化效果。

### 检查顶点值

当你发现某个图元位置错误或形状异常时，问题可能出在你传入顶点、对象或网格着色器的数据中。请检查底部的数据视图，以确保着色器的输入和输出正确无误。要查看某个特定图元的所有属性，请在场景视图中点击该图元以将其选中，然后 Xcode 会在数据视图中高亮显示该图元的顶点。

如果你的着色器有多个输出，请参考输出位置右侧的附加列。你可以重新排列或隐藏列，以便更容易比较各个值。

![](../../../attachments/98df51b27a8397ac32b1fe5acff60acf/gputools-metal-debugger-gv-vertex-selection@2x.png)

<sub>几何图形查看器的屏幕截图，在场景视图中显示几何图形，并在表格中列出顶点。所选顶点及其同级顶点在场景视图和表格中均已高亮显示。</sub>

### 调试你的几何图形

有些几何图形可能位置错误，或者数值不正确。要确定问题是否出在着色器代码中，你可以使用着色器调试器调试你的顶点、对象或网格着色器。在场景视图中，选择一个位置错误或形状异常的图元，然后点击调试。

![](../../../attachments/16ea05dc5f61c0925153da5d7004f0a3/gputools-metal-debugger-gv-shader-debugger@2x.png)

<sub>Metal 调试器的屏幕截图，并排显示着色器编辑器和几何图形查看器。几何图形查看器中某个顶点已高亮显示，控制栏中的调试按钮也已高亮显示。</sub>

该着色器会显示在 Xcode 的主编辑器中。要找出问题的原因，请逐行单步执行代码，并在右侧窗格中检查每个变量的值，直到发现任何异常。有关调试着色器的更多信息，请参阅 [Debugging the shaders within a draw command or compute dispatch](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md)。

## 另请参阅

### Metal 命令分析

- [Inspecting the bound resources for a command](inspecting-the-bound-resources-for-a-command.md) — 通过检查编码器中任意点的绑定资源来发现问题。
- [Inspecting the attachments of a draw command](inspecting-the-attachments-of-a-draw-command.md) — 通过检查各个像素和采样点来发现附件问题。
- [Debugging the shaders within a draw command or compute dispatch](debugging-the-shaders-within-a-draw-command-or-compute-dispatch.md) — 使用着色器调试器识别并修复你的 App 中有问题的着色器。
- [Analyzing draw command and compute dispatch performance with GPU counters](analyzing-draw-command-and-compute-dispatch-performance-with-gpu-counters.md) — 通过检查性能计数器来识别帧捕获中的问题。
- [Analyzing draw command and compute dispatch performance with pipeline statistics](analyzing-draw-command-and-compute-dispatch-performance-with-pipeline-statistics.md) — 通过检查管线统计信息来识别帧捕获中的问题。
