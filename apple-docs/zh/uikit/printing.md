---
title: 打印
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/printing
source_url: 'https://developer.apple.com/documentation/uikit/printing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/printing.json'
content_hash: 'sha256:b606c06be44b23ed'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 打印

<sub>API 集合</sub>

显示系统打印面板并管理打印过程。

## 主题

### 打印面板

- [UIPrintInteractionController](uiprintinteractioncontroller.md) — 管理 iOS 中文稿、图像和其他可打印内容打印的用户界面。
- [UIPrinterPickerController](uiprinterpickercontroller.md) — 显示用于选择打印机的标准界面的视图控制器。

### 渲染器

- [UIPrintPageRenderer](uiprintpagerenderer.md) — 绘制要打印的页面内容的对象，可选择借助打印格式化器。
- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md) — 通过支持原生控制、多窗口、共享、打印、菜单和键盘快捷键改进你的 iPadOS App 的 Mac Catalyst 版本。

### 任务信息

- [UIPrinter](uiprinter.md) — 网络上的打印机。
- [UIPrintInfo](uiprintinfo.md) — 系统打印时使用的打印任务信息。
- [UIPrintPaper](uiprintpaper.md) — 打印任务的纸张大小以及内容打印所在的矩形区域。

### 格式化器

- [UIPrintFormatter](uiprintformatter.md) — 打印格式化器的抽象基类，这类对象可布局可跨页边界的自定可打印内容。
- [UIViewPrintFormatter](uiviewprintformatter.md) — 为视图的绘制内容布局以供打印的对象。
- [UISimpleTextPrintFormatter](uisimpletextprintformatter.md) — 为纯文本布局以供打印的对象，可能跨越多页。
- [UIMarkupTextPrintFormatter](uimarkuptextprintformatter.md) — 为多页打印任务布局 HTML 文本的对象。

### 打印机服务发现

- [UIPrintServiceExtension](uiprintserviceextension.md) — 在没有配置描述文件的情况下定位并设置打印机的扩展。
- [UIPrinterDestination](uiprinterdestination.md) — 单个打印机的描述。

### 键盘快捷键

- [UIApplicationSupportsPrintCommand](../bundleresources/information-property-list/uiapplicationsupportsprintcommand.md) — 指示 App 是否支持 Command-P 键盘快捷键的布尔值。

## 另请参阅

### 图形、绘制与打印

- [Images and PDF](images-and-pdf.md) — 创建和管理图像，包括使用位图和 PDF 格式的图像。
- [Drawing](drawing.md) — 使用颜色、渲染器、绘制路径、字符串和阴影配置 App 的绘制环境。
