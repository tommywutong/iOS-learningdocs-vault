---
title: 使用颜色空间确定颜色值
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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# 使用颜色空间确定颜色值

<sub>文章</sub>

通过选择颜色空间，改变系统对颜色值的显示解读。

## 概述

[UIColor](uicolor.md) 对象通常将其颜色值存储为 Core Graphics 颜色（[CGColor](../coregraphics/cgcolor.md)），位于 Core Graphics 颜色空间（[CGColorSpace](../coregraphics/cgcolorspace.md)）中。创建自定颜色时，底层颜色空间以及每个颜色分量的取值范围会因 iOS 版本而异。

### 使用颜色空间创建颜色

对于运行在 iOS 9 及更早版本的 App，颜色使用以下两种颜色空间之一：

- 设备相关的灰度
- 设备相关的 RGB

这些设备颜色空间与 sRGB 颜色空间的显示特性密切相关。这些颜色空间中的分量值范围为 `0.0` 到 `1.0`。创建颜色时，颜色对象会对值进行钳制，以确保它们落在该范围内。

### 使用扩展颜色空间

对于运行在 iOS 10 或更高版本的 App，颜色使用以下扩展颜色空间：

- [extendedGray](../coregraphics/cgcolorspace/extendedgray.md)
- [extendedSRGB](../coregraphics/cgcolorspace/extendedsrgb.md)

在扩展颜色空间中，[UIColor](uicolor.md) 不会对值进行钳制以使其位于颜色色域内。分量值可能小于 `0.0` 或大于 `1.0`。在 sRGB 显示设备上，此类颜色超出色域，无法准确渲染。然而，扩展颜色空间在需要一个像素格式与表示形式，能够转换为其他颜色空间时很有用。例如，即使某颜色不在 sRGB 色域内，你仍可以将显示 P3 颜色空间中的颜色转换为扩展 sRGB 格式。转换此类颜色时，其部分值会落在 `0.0` 到 `1.0` 范围之外。不过，颜色在具有 P3 显示色域的设备上仍能正确渲染。

在使用自定颜色时，使用扩展颜色空间存储颜色值。在尽可能准确地表示颜色时，将颜色从扩展颜色空间转换到目标颜色空间。

## 另请参阅

### 获取颜色信息

- [CGColor](uicolor/cgcolor.md) — 与颜色对象对应的 Quartz 颜色。
- [CIColor](uicolor/cicolor.md) — 与颜色对象对应的 Core Image 颜色。
- [- getHue:saturation:brightness:alpha:](<uicolor/gethue(__saturation_brightness_alpha_).md>) — 返回 HSB 颜色空间中组成颜色的分量。
- [- getRed:green:blue:alpha:](<uicolor/getred(__green_blue_alpha_).md>) — 返回 RGB 颜色空间中组成颜色的分量。
- [- getWhite:alpha:](<uicolor/getwhite(__alpha_).md>) — 返回颜色的灰度分量。
- [linearExposure](uicolor/linearexposure.md) — 生成此颜色时所应用的线性亮度乘数。使用 exposure 创建的颜色，其 CGColor 会被标记 contentHeadroom 值。而未标记 contentHeadroom 的 CGColor 从 CGColorGetHeadroom 返回 0，类似方式生成的 UIColor 的 linearExposure 则返回 1.0。
- [accessibilityName](uicolor/accessibilityname.md) — 颜色的本地化描述，用于辅助功能属性。
