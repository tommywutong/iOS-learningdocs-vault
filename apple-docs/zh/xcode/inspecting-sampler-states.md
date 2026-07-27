---
title: 检查采样器状态
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/inspecting-sampler-states
source_url: 'https://developer.apple.com/documentation/xcode/inspecting-sampler-states'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/inspecting-sampler-states.json'
content_hash: 'sha256:669a7fec8034f8b2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal debugger](metal-debugger.md)

# 检查采样器状态

<sub>文章</sub>

通过检查采样器状态的属性来验证其配置。

## 概述

Metal 调试器允许你使用采样器状态查看器检查采样器状态。打开采样器状态后，你可以查看其关联的属性并预览采样行为。要了解更多信息，请参阅 [Inspecting the bound resources for a command](inspecting-the-bound-resources-for-a-command.md) 或 [Analyzing memory usage](analyzing-memory-usage.md)。

### 浏览你的采样器状态

采样器状态查看器在左侧显示你的采样器状态的属性（由 [MTLSamplerDescriptor](../metal/mtlsamplerdescriptor.md) 配置），在右侧显示预览。预览展示了在使用你的采样器状态时纹理中的像素外观。

![](../../../attachments/814897e16f068945b3e238d74cdd1b6c/gputools-metal-debugger-sv-outline@2x.png)

<sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边缘寻址模式的采样器状态。</sub>

预览中心的方形区域对应于 `0.0` 到 `1.0` 范围内的 UV 坐标。

![](../../../attachments/50883e4e70e74eb4664a9a4377a816ae/gputools-metal-debugger-sv-outline-green@2x.png)

<sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边缘寻址模式的采样器状态。边界内的区域已高亮显示。</sub>

你可以使用预览快速验证采样器状态的配置。例如，如果你希望纹理镜像显示，但它却绘制了一个常量值，你可以检查该采样器状态。在下方的屏幕截图中，采样器状态被配置为钳制到不透明黑色的边框颜色，而不是使用镜像重复作为寻址模式：

![](../../../attachments/947607b5464280b963c5b2aae0363c80/gputools-metal-debugger-sv-nearest-clamp-border-black-plus-overview@2x.png)

<sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边框寻址模式的采样器状态。边框颜色为不透明黑色。</sub>

### 尝试不同组合

你在创建采样器状态时配置的属性决定了纹理在采样时的外观。与过滤相关的属性控制着当采样范围大于或小于一个像素、或者处于 mipmap 级别之间时像素如何组合。寻址模式决定了当读取超出纹理边界时每个像素处的纹理坐标。你可以尝试使用不同的过滤和寻址模式组合，直到达到你想要的效果。

| 属性 | 预览 |
|---|---|
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/b9f00a20daf0f04a3f7f885f457908c3/gputools-metal-debugger-sv-nearest-clamp@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边缘寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.mirrorClampToEdge](../metal/mtlsampleraddressmode/mirrorclamptoedge.md) | ![](../../../attachments/fbdbeef91680a8cd6322719b265ae42f/gputools-metal-debugger-sv-nearest-mirror-clamp@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和镜像钳制到边缘寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.repeat](../metal/mtlsampleraddressmode/repeat.md) | ![](../../../attachments/c53b7bf29facfb4610ffc37167a82e26/gputools-metal-debugger-sv-nearest-repeat@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和重复寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.mirrorRepeat](../metal/mtlsampleraddressmode/mirrorrepeat.md) | ![](../../../attachments/83abc3f7fc2fe582cafcfcb09d538224/gputools-metal-debugger-sv-nearest-mirror@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和镜像重复寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToZero](../metal/mtlsampleraddressmode/clamptozero.md) | ![](../../../attachments/ef4df8ec925e3e653f21fb4e8374b813/gputools-metal-debugger-sv-nearest-zero@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到零寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueBlack](../metal/mtlsamplerbordercolor/opaqueblack.md) | ![](../../../attachments/ef4df8ec925e3e653f21fb4e8374b813/gputools-metal-debugger-sv-nearest-clamp-border-black@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边框寻址模式的采样器状态。边框颜色为不透明黑色。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueWhite](../metal/mtlsamplerbordercolor/opaquewhite.md) | ![](../../../attachments/82d1c051bf85e8d1cfbfe8a22960f47c/gputools-metal-debugger-sv-nearest-clamp-border-white@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边框寻址模式的采样器状态。边框颜色为不透明白色。</sub> |
| [MTLSamplerMinMagFilter.nearest](../metal/mtlsamplerminmagfilter/nearest.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.transparentBlack](../metal/mtlsamplerbordercolor/transparentblack.md) | ![](../../../attachments/574d56e7b427682155ee48c7a04b3898/gputools-metal-debugger-sv-nearest-clamp-border-transparent@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为最近过滤和钳制到边框寻址模式的采样器状态。边框颜色为透明黑色。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/84beb927bfd3cfa7311c3c2fef5e1833/gputools-metal-debugger-sv-linear-clamp@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和钳制到边缘寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToEdge](../metal/mtlsampleraddressmode/clamptoedge.md) | ![](../../../attachments/fa81821d87772a5722661d0636aadb2c/gputools-metal-debugger-sv-linear-mirror-clamp@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和镜像钳制到边缘寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.repeat](../metal/mtlsampleraddressmode/repeat.md) | ![](../../../attachments/0b4f5502fbd81fbd0f6d52e97e36550f/gputools-metal-debugger-sv-linear-repeat@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和重复寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.mirrorRepeat](../metal/mtlsampleraddressmode/mirrorrepeat.md) | ![](../../../attachments/3b3e6fab82cacc166e20e196a959e97c/gputools-metal-debugger-sv-linear-mirror@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和镜像重复寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToZero](../metal/mtlsampleraddressmode/clamptozero.md) | ![](../../../attachments/5338855da61a2358e21dcd62d2023092/gputools-metal-debugger-sv-linear-zero@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和钳制到零寻址模式的采样器状态。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueBlack](../metal/mtlsamplerbordercolor/opaqueblack.md) | ![](../../../attachments/5338855da61a2358e21dcd62d2023092/gputools-metal-debugger-sv-linear-clamp-border-black@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和钳制到边框寻址模式的采样器状态。边框颜色为不透明黑色。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.opaqueWhite](../metal/mtlsamplerbordercolor/opaquewhite.md) | ![](../../../attachments/939248a8d3d668eae179561ed6e798bb/gputools-metal-debugger-sv-linear-clamp-border-white@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和钳制到边框寻址模式的采样器状态。边框颜色为不透明白色。</sub> |
| [MTLSamplerMinMagFilter.linear](../metal/mtlsamplerminmagfilter/linear.md), [MTLSamplerAddressMode.clampToBorderColor](../metal/mtlsampleraddressmode/clamptobordercolor.md), [MTLSamplerBorderColor.transparentBlack](../metal/mtlsamplerbordercolor/transparentblack.md) | ![](../../../attachments/f473b96f45e1282b14919a43ad4149f8/gputools-metal-debugger-sv-linear-clamp-border-transparent@2x.png)  <sub>采样器状态查看器的屏幕截图，显示了配置为线性过滤和钳制到边框寻址模式的采样器状态。边框颜色为透明黑色。</sub> |

## 另请参阅

### Metal 资源检查

- [Inspecting acceleration structures](inspecting-acceleration-structures.md) — 通过检查你的加速结构来揭示光线相交瓶颈。
- [Inspecting buffers](inspecting-buffers.md) — 通过检查缓冲区内容来确认你的缓冲区格式。
- [Inspecting pipeline states](inspecting-pipeline-states.md) — 通过检查渲染和计算通道的属性来确定它们的行为。
- [Inspecting shaders](inspecting-shaders.md) — 通过检查和编辑你的着色器来提升你的 App 的着色器性能。
- [Inspecting textures](inspecting-textures.md) — 通过检查纹理内容来发现纹理中的问题。
