---
title: 绘图
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/drawing
source_url: 'https://developer.apple.com/documentation/uikit/drawing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/drawing.json'
content_hash: 'sha256:9f3ca9ef5a60ed07'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 绘图

<sub>API 集合</sub>

使用颜色、渲染器、绘图路径、字符串和阴影配置 App 的绘图环境。

## 主题

### UI 更新

- [UIUpdateLink](uiupdatelink.md) — 用于观察、参与和影响 UI 更新过程的对象。
- [UIUpdateInfo](uiupdateinfo.md) — 包含当前 UI 更新状态详细信息的对象。
- [UIUpdateActionPhase](uiupdateactionphase.md) — 定义 UI 更新过程中特定阶段的对象。

### 颜色

- [UIColor](uicolor.md) — 存储颜色数据，有时也存储不透明度的对象。

### 图形上下文

- [UIGraphicsRenderer](uigraphicsrenderer.md) — 用于创建图形渲染器的抽象基类。
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md) — 图形渲染器绘图环境的基类。
- [UIGraphicsRendererFormat](uigraphicsrendererformat.md) — 表示图形渲染器上下文配置的一组绘图属性。
- [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) — 用于创建由 Core Graphics 支持的图像的图形渲染器。
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md) — 图像渲染器的绘图环境。
- [UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md) — 表示图像渲染器上下文配置的一组绘图属性。
- [UIGraphicsPDFRenderer](uigraphicspdfrenderer.md) — 用于创建 PDF 的图形渲染器。
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md) — PDF 渲染器的绘图环境。
- [UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md) — 表示 PDF 渲染器上下文配置的一组绘图属性。

### 路径

- [UIBezierPath](uibezierpath.md) — 由直线和曲线线段组成、可在自定视图中渲染的路径。
- [UIRectFill](<uirectfill(__).md>) — 使用当前颜色填充指定矩形。
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — 使用指定的融合模式和当前填充颜色填充矩形。
- [UIRectFrame](<uirectframe(__).md>) — 沿指定矩形的内部绘制边框。
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — 使用指定的融合模式沿矩形内部绘制边框。

### 字符串

- [NSStringDrawingContext](nsstringdrawingcontext.md) — 管理绘制属性字符串所用度量的对象。
- [NSStringDrawingOptions](nsstringdrawingoptions.md) — 指定绘制字符串时所用渲染选项的常量。
- [UIBaselineAdjustment](uibaselineadjustment.md) — 垂直调整选项。

### 阴影

- [NSShadow](nsshadow.md) — 用于指定属性，以便在绘图操作期间创建和设置投影样式的对象。

### 图形上下文基元

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — 返回当前图形上下文。
- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — 将指定的图形上下文设为当前上下文。
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — 从栈顶移除当前图形上下文，并恢复上一个上下文。
- [UIGraphicsBeginImageContextWithOptions](<uigraphicsbeginimagecontextwithoptions(______).md>) — 使用指定选项创建基于位图的图形上下文。_(已废弃)_
- [UIRectClip](<uirectclip(__).md>) — 通过与指定矩形相交来修改当前裁剪路径。

### 基元类型转换

- [cgAffineTransform(for:)](<../foundation/nscoder/cgaffinetransform(for_).md>) — 返回与给定字符串中的数据对应的 Core Graphics 仿射变换结构。
- [cgPoint(for:)](<../foundation/nscoder/cgpoint(for_).md>) — 返回与给定字符串中的数据对应的 Core Graphics 点结构。
- [cgRect(for:)](<../foundation/nscoder/cgrect(for_).md>) — 返回与给定字符串中的数据对应的 Core Graphics 矩形结构。
- [cgSize(for:)](<../foundation/nscoder/cgsize(for_).md>) — 返回与给定字符串中的数据对应的 Core Graphics 大小结构。
- [cgVector(for:)](<../foundation/nscoder/cgvector(for_).md>) — 返回与给定字符串中的数据对应的 Core Graphics 向量。
- [string(for:)](<../foundation/nscoder/string(for_)-6yx6n.md>) — 返回经格式化后包含仿射变换数据的字符串。
- [string(for:)](<../foundation/nscoder/string(for_)-6ix86.md>) — 返回经格式化后包含点数据的字符串。
- [string(for:)](<../foundation/nscoder/string(for_)-4qz0a.md>) — 返回经格式化后包含矩形数据的字符串。
- [string(for:)](<../foundation/nscoder/string(for_)-2f1xb.md>) — 返回经格式化后包含大小数据结构的字符串。
- [string(for:)](<../foundation/nscoder/string(for_)-4omzv.md>) — 返回经格式化后包含向量数据结构的字符串。

## 另请参阅

### 图形、绘图和打印

- [图像和 PDF](images-and-pdf.md) — 创建和管理图像，包括使用位图和 PDF 格式的图像。
- [打印](printing.md) — 显示系统打印面板并管理打印过程。
