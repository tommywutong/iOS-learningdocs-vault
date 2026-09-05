---
title: 通过颜色空间确定颜色值
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/determining-color-values-with-color-spaces
source_url: 'https://developer.apple.com/documentation/uikit/determining-color-values-with-color-spaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/determining-color-values-with-color-spaces.json'
content_hash: 'sha256:8e70fc008b522e0e'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [绘图](drawing.md) · [UIColor](uicolor.md)

# 通过颜色空间确定颜色值

<sub>文章</sub>

通过选择颜色空间（color space），改变系统在显示时对颜色值的解释方式。

## 概述

[UIColor](uicolor.md) 对象通常把它的颜色值作为 Core Graphics 颜色（[CGColor](../coregraphics/cgcolor.md)）存储在 Core Graphics 颜色空间（[CGColorSpace](../coregraphics/cgcolorspace.md)）中。创建自定义颜色时，底层颜色空间以及每个颜色分量的取值范围会因 iOS 版本而异。

### 使用颜色空间创建颜色

对于运行 iOS 9 及更早版本的 App，颜色使用以下两种颜色空间之一：

- 依赖设备的灰度
- 依赖设备的 RGB

这些设备颜色空间与 sRGB 颜色空间的显示特性十分接近。这些颜色空间内的分量值处于 `0.0` 到 `1.0` 的范围内。创建颜色时，颜色对象会钳制这些值，确保它们落在该范围内。

### 使用扩展颜色空间

对于运行 iOS 10 或更高版本的 App，颜色使用以下扩展颜色空间：

- [extendedGray](../coregraphics/cgcolorspace/extendedgray.md)
- [extendedSRGB](../coregraphics/cgcolorspace/extendedsrgb.md)

在扩展颜色空间中，[UIColor](uicolor.md) 不会钳制值来使其落在色域（color gamut）之内。分量值可能小于 `0.0` 或大于 `1.0`。在 sRGB 显示器上，这类颜色在色域之外，无法准确呈现。不过，当你想要一种扩展颜色空间能够转换成其他颜色空间的像素格式和表示方式时，扩展颜色空间就非常有用。例如，即使某个颜色不在 sRGB 色域内，你仍然可以把它从 display P3 颜色空间转换为扩展 sRGB 格式。转换这类颜色时，它的部分值会落在 `0.0` 到 `1.0` 范围之外。但在配备 P3 显示色域的设备上，该颜色仍能正确呈现。

使用自定义颜色时，请用扩展颜色空间来存储你的颜色值。在需要尽可能如实地表示颜色时，将该颜色从扩展颜色空间转换到目标颜色空间。

## 另请参阅

### 获取颜色信息

- [CGColor](uicolor/cgcolor.md) — 与该颜色对象对应的 Quartz 颜色。
- [CIColor](uicolor/cicolor.md) — 与该颜色对象对应的 Core Image 颜色。
- [- getHue:saturation:brightness:alpha:](<uicolor/gethue(__saturation_brightness_alpha_).md>) — 返回在 HSB 颜色空间中构成该颜色的各分量。
- [- getRed:green:blue:alpha:](<uicolor/getred(__green_blue_alpha_).md>) — 返回在 RGB 颜色空间中构成该颜色的各分量。
- [- getWhite:alpha:](<uicolor/getwhite(__alpha_).md>) — 返回该颜色的灰度分量。
- [linearExposure](uicolor/linearexposure.md) — 生成该颜色时所应用的线性亮度乘数。UIColor 通过曝光创建的颜色会生成带有 contentHeadroom 标签值的 CGColor。没有 contentHeadroom 标签的 CGColor 从 CGColorGetHeadroom 返回 0，而以类似方式生成的 UIColor 则返回 1.0 的 linearExposure。
- [accessibilityName](uicolor/accessibilityname.md) — 用于辅助功能属性的颜色本地化描述。
