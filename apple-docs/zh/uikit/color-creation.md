---
title: 创建颜色
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/color-creation
source_url: 'https://developer.apple.com/documentation/uikit/color-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/color-creation.json'
content_hash: 'sha256:80339d75e5e30dcd'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [绘图](drawing.md) · [UIColor](uicolor.md)

# 创建颜色

<sub>API 集合</sub>

从资源目录加载颜色，并根据原始分量值创建颜色。

## 概述

当你想在 UI 中使用特定颜色时，可以通过调整灰度、RGB、HSB 和 CMYK 所使用的原始分量值来创建颜色对象。你可以设置指定的不透明度和 RGB 分量值，以创建符合需要的个性化颜色。还可以让分量值根据当前有效的特性动态变化，从而动态创建颜色。你可以使用图案颜色设置填充色或描边色。

## 主题

### 根据分量值创建颜色

- [- initWithWhite:alpha:](<uicolor/init(white_alpha_).md>) — 使用指定的不透明度和灰度值创建颜色对象。
- [- initWithHue:saturation:brightness:alpha:](<uicolor/init(hue_saturation_brightness_alpha_).md>) — 使用指定的不透明度和 HSB 色彩空间分量值创建颜色对象。
- [- initWithRed:green:blue:alpha:](<uicolor/init(red_green_blue_alpha_).md>) — 使用指定的不透明度和 RGB 分量值创建颜色对象。
- [- initWithRed:green:blue:alpha:exposure:](<uicolor/init(red_green_blue_alpha_exposure_).md>) — 对红、绿、蓝分量定义的 SDR 颜色应用曝光来生成 HDR 颜色。`red`、`green` 和 `blue` 分量的标称范围是 [0..1]，`exposure` 是大于或等于 0 的值。为生成 HDR 颜色，系统会在线性色彩空间中处理给定颜色，将分量值乘以 `2^exposure`。生成颜色的 `contentHeadroom` 等于线性化后的曝光值。曝光每增加一个整数值，生成的颜色亮度就会增加一倍。
- [- initWithRed:green:blue:alpha:linearExposure:](<uicolor/init(red_green_blue_alpha_linearexposure_).md>) — 对红、绿、蓝分量定义的 SDR 颜色应用曝光来生成 HDR 颜色。`red`、`green` 和 `blue` 分量的标称范围是 [0..1]，`linearExposure` 是大于或等于 1 的值。为生成 HDR 颜色，系统会在线性色彩空间中处理给定颜色，将分量值乘以 `linearExposure `。生成颜色的 `contentHeadroom` 等于 `linearExposure`。`linearExposure` 每增大一倍，生成的颜色亮度就会增加一倍。
- [- initWithDisplayP3Red:green:blue:alpha:](<uicolor/init(displayp3red_green_blue_alpha_).md>) — 使用 Display P3 色彩空间中指定的不透明度和 RGB 分量值创建颜色对象。
- [+ colorNamed:](<uicolor/init(named_).md>) — 使用命名资源中的信息创建颜色对象。
- [init(named:inBundle:compatibleWithTraitCollection:)](<uicolor/init(named_inbundle_compatiblewithtraitcollection_).md>) — 使用与指定特性集合（trait collection）兼容的命名资源创建颜色对象。

### 动态创建颜色

- [- initWithDynamicProvider:](<uicolor/init(dynamicprovider_).md>) — 创建使用指定 block 动态生成颜色数据的颜色对象。

### 根据另一个颜色对象创建颜色

- [init(_:)](<uicolor/init(__).md>) — 创建封装 SwiftUI 颜色的颜色对象。
- [- initWithCIColor:](<uicolor/init(cicolor_)-2z057.md>) — 创建封装 Core Image 颜色的颜色对象。
- [- initWithCGColor:](<uicolor/init(cgcolor_)-27r9g.md>) — 使用指定的 Quartz 颜色引用创建颜色对象。
- [- colorWithAlphaComponent:](<uicolor/withalphacomponent(__).md>) — 创建与接收者具有相同色彩空间和分量值、但采用指定 alpha 分量的颜色对象。

### 创建基于图案的颜色

- [- initWithPatternImage:](<uicolor/init(patternimage_).md>) — 使用指定图像对象创建颜色对象。

### 根据资源创建颜色

- [init(resource:)](<uicolor/init(resource_).md>)

## 另请参阅

### 获取现有颜色

- [UI 元素颜色](ui-element-colors.md) — 为标签、文本、背景和链接等 UI 元素选择颜色。
- [标准颜色](standard-colors.md) — 为红色、蓝色、绿色、黑色、白色等特定色调定义标准颜色对象。
