---
title: 标准颜色
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/standard-colors
source_url: 'https://developer.apple.com/documentation/uikit/standard-colors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/standard-colors.json'
content_hash: 'sha256:e5a33fabcca54f06'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drawing](drawing.md) · [UIColor](uicolor.md)

# 标准颜色

<sub>API 集合</sub>

为红色、蓝色、绿色、黑色、白色等特定色调定义标准颜色对象。

## 概述

当你想在 UI 中使用特定色调时，请使用标准颜色对象。要查看这些颜色的色样，请参阅 [系统颜色](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/color/#system-colors)。

当你使用所提供的 [UIColor](uicolor.md) 对象时，系统颜色对象会自动适配深色模式变化，但固定色调的颜色不会适配。如果你检索颜色值——无论是直接检索还是使用诸如 [CGColor](../coregraphics/cgcolor.md) 之类的其他类型——你必须自行处理深色模式变化。有关支持深色模式的更多信息，请参阅 [在界面中支持深色模式](supporting-dark-mode-in-your-interface.md)。

## 主题

### 可适配颜色

- [systemBlueColor](uicolor/systemblue.md) — 一种自动适配当前特性环境的蓝色。
- [systemBrownColor](uicolor/systembrown.md) — 一种自动适配当前特性环境的棕色。
- [systemCyanColor](uicolor/systemcyan.md) — 一种自动适配当前特性环境的青色。
- [systemGreenColor](uicolor/systemgreen.md) — 一种自动适配当前特性环境的绿色。
- [systemIndigoColor](uicolor/systemindigo.md) — 一种自动适配当前特性环境的靛蓝色。
- [systemMintColor](uicolor/systemmint.md) — 一种自动适配当前特性环境的薄荷色。
- [systemOrangeColor](uicolor/systemorange.md) — 一种自动适配当前特性环境的橙色。
- [systemPinkColor](uicolor/systempink.md) — 一种自动适配当前特性环境的粉色。
- [systemPurpleColor](uicolor/systempurple.md) — 一种自动适配当前特性环境的紫色。
- [systemRedColor](uicolor/systemred.md) — 一种自动适配当前特性环境的红色。
- [systemTealColor](uicolor/systemteal.md) — 一种自动适配当前特性环境的蓝绿色。
- [systemYellowColor](uicolor/systemyellow.md) — 一种自动适配当前特性环境的黄色。

### 可适配灰色

- [systemGrayColor](uicolor/systemgray.md) — 适配环境的标准基础灰色。
- [systemGray2Color](uicolor/systemgray2.md) — 适配环境的第二级灰色调。
- [systemGray3Color](uicolor/systemgray3.md) — 适配环境的第三级灰色调。
- [systemGray4Color](uicolor/systemgray4.md) — 适配环境的第四级灰色调。
- [systemGray5Color](uicolor/systemgray5.md) — 适配环境的第五级灰色调。
- [systemGray6Color](uicolor/systemgray6.md) — 适配环境的第六级灰色调。

### 透明色

- [clearColor](uicolor/clear.md) — 灰度值和 alpha 值均为 `0.0` 的颜色对象。

### 固定颜色

- [blackColor](uicolor/black.md) — sRGB 色彩空间中灰度值为 `0.0`、alpha 值为 `1.0` 的颜色对象。
- [blueColor](uicolor/blue.md) — RGB 值为 `0.0`、`0.0` 和 `1.0`，alpha 值为 `1.0` 的颜色对象。
- [brownColor](uicolor/brown.md) — RGB 值为 `0.6`、`0.4` 和 `0.2`，alpha 值为 `1.0` 的颜色对象。
- [cyanColor](uicolor/cyan.md) — RGB 值为 `0.0`、`1.0` 和 `1.0`，alpha 值为 `1.0` 的颜色对象。
- [darkGrayColor](uicolor/darkgray.md) — 灰度值为 1/3、alpha 值为 `1.0` 的颜色对象。
- [grayColor](uicolor/gray.md) — 灰度值为 `0.5`、alpha 值为 `1.0` 的颜色对象。
- [greenColor](uicolor/green.md) — RGB 值为 `0.0`、`1.0` 和 `0.0`，alpha 值为 `1.0` 的颜色对象。
- [lightGrayColor](uicolor/lightgray.md) — 灰度值为 2/3、alpha 值为 `1.0` 的颜色对象。
- [magentaColor](uicolor/magenta.md) — RGB 值为 `1.0`、`0.0` 和 `1.0`，alpha 值为 `1.0` 的颜色对象。
- [orangeColor](uicolor/orange.md) — RGB 值为 `1.0`、`0.5` 和 `0.0`，alpha 值为 `1.0` 的颜色对象。
- [purpleColor](uicolor/purple.md) — RGB 值为 `0.5`、`0.0` 和 `0.5`，alpha 值为 `1.0` 的颜色对象。
- [redColor](uicolor/red.md) — RGB 值为 `1.0`、`0.0` 和 `0.0`，alpha 值为 `1.0` 的颜色对象。
- [whiteColor](uicolor/white.md) — 灰度值为 `1.0`、alpha 值为 `1.0` 的颜色对象。
- [yellowColor](uicolor/yellow.md) — RGB 值为 `1.0`、`1.0` 和 `0.0`，alpha 值为 `1.0` 的颜色对象。

## 另请参阅

### 获取现有颜色

- [UI 元素颜色](ui-element-colors.md) — 为标签、文本、背景和链接等 UI 元素选择颜色。
- [颜色创建](color-creation.md) — 从素材目录加载颜色，并根据原始分量值创建颜色。
