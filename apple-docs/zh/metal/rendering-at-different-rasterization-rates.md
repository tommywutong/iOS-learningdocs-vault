---
title: 以不同光栅化速率渲染
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/rendering-at-different-rasterization-rates
source_url: 'https://developer.apple.com/documentation/metal/rendering-at-different-rasterization-rates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/rendering-at-different-rasterization-rates.json'
content_hash: 'sha256:48e15c81d677f1ce'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md)

# 以不同光栅化速率渲染

<sub>文章</sub>

配置光栅化速率贴图，根据所需细节量改变光栅化速率。

## 概述

在复杂的 3D 应用中，你需要执行大量计算来渲染输出图像中的每个像素，从而生成高质量的结果。然而，随着渲染目标变大、屏幕分辨率提高，以高质量渲染如此多像素的开销会变得过大。

一种常见的解决方案是先以较低分辨率渲染中间图像，然后再拉伸这些图像以生成最终结果。虽然这种方案会产生额外的图像缩放开销，但它能大幅降低渲染所需的内存与性能成本。当较低的图像质量可以接受或不易察觉、且渲染节省的成本大于缩放开销时，这个方案最为有用。

另一种降低渲染成本的方法是：当渲染图像中的某些部分不需要细节，或者 App 会在后续渲染过程中丢弃这些部分时，避免在这些部分执行复杂计算。例如，如果你计划在后处理步骤中对图像的某个部分应用模糊效果，就不需要为以精细细节渲染那些像素而付出代价，因为模糊效果会去除这些细节。

### 实现可变光栅化速率

在 Metal 中，你可以通过使用可变光栅化速率（VRR）来结合这两种解决方案。你可以为渲染目标的不同部分指定不同的光栅化速率。当你需要细节时，就以全分辨率渲染目标的那些区域；在不需要细节的区域，你可以指定较低的分辨率速率，这意味着这些区域所需的像素更少，片段着色器的调用次数也更少。

在以下情况下使用 VRR：

- 你希望以不同的质量级别渲染渲染目标的不同部分。
- 渲染每个像素的开销高到一定程度，降低光栅化速率能带来可观的渲染时间节省，且这些节省大于将图像缩放为全速率图像所增加的开销。

要使用 VRR，你需要创建一个光栅化速率贴图，将渲染目标划分为若干区域，并为每个区域指定水平和垂直方向的光栅化速率。创建好速率贴图后，你需要分配用于保存中间图像的纹理。这些纹理比最终的渲染目标图像更小，因为你只分配了保存渲染像素所需的内存。

使用速率贴图完成中间数据的渲染后，你需要执行额外的绘制命令，将中间数据拉伸并复制到另一张分辨率更高的纹理中，例如由 Metal 可绘制对象提供、用于显示的纹理。这个最终目标被称为 _全速率图像_，因为它在整个图像上统一使用正常的光栅化。生成全速率图像之后，你可以对其应用额外的处理。例如，你通常会希望在全速率图像之上渲染用户界面元素。

### 检查是否支持 VRR

并非所有 GPU 都支持 VRR。在尝试使用它之前，请在设备对象上检查是否支持：

**Swift**

```swift
func supportsVariableRasterizationRateOn(_ device: MTLDevice) -> Bool {
    device.supportsRasterizationRateMap(layerCount: 1)
}
```

**Objective-C**

```objective-c
- (BOOL)supportsVariableRasterizationRateOn:(id<MTLDevice>)device {
    return [device supportsRasterizationRateMapWithLayerCount:1];
}

// Metal-CPP
bool supportsVariableRasterizationRate(MTL::Device* pDevice)
{
    return pDevice->supportsRasterizationRateMap(1);
}
```

## 另请参阅

### 光栅化设置

- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — 为渲染目标的每个部分定义光栅化速率。
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — 创建屏幕外纹理以保存中间光栅化数据。
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — 使用速率贴图数据将内容缩放至填满目标纹理。
- [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) — 一个用于配置新光栅化速率贴图的对象。
- [MTLRasterizationRateMap](mtlrasterizationratemap.md) — 一个已编译的只读实例，决定渲染时如何应用可变光栅化速率。
- [MTLCoordinate2D](mtlcoordinate2d.md) — 视口中的一个坐标。
- [MTLCoordinate2DMake](<mtlcoordinate2dmake(____).md>) — 返回一个具有指定坐标的新 2D 点。
