---
title: 图像与 PDF
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/images-and-pdf
source_url: 'https://developer.apple.com/documentation/uikit/images-and-pdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/images-and-pdf.json'
content_hash: 'sha256:72c68d9be789711c'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 图像与 PDF

<sub>API 集合</sub>

创建和管理图像，包括使用位图和 PDF 格式的图像。

## 主题

### 表示形式

- [UIImage](uiimage.md) — 在你的 App 中管理图像数据的对象。
- [SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md) — 包含要应用于符号图像的特定字体、大小、样式和字重属性的对象。
- [Configuration](uiimage/configuration-swift.class.md) — 一个配置对象，包含系统选择当前图像变体时所用的特性。

### 图像创建

- [在你的 App 中支持 HDR 图像](supporting-hdr-images-in-your-app.md) — 使用 SwiftUI 和 Core Image 加载、显示、编辑和保存 HDR 图像。
- [UIImageJPEGRepresentation](<uiimage/jpegdata(compressionquality_).md>) — 返回包含 JPEG 格式图像的数据对象。
- [UIImagePNGRepresentation](<uiimage/pngdata().md>) — 返回包含指定图像的 PNG 格式的数据对象。

### 照片相册

- [UIImageWriteToSavedPhotosAlbum](<uiimagewritetosavedphotosalbum(________).md>) — 把指定图像添加到用户的相机胶卷相册。
- [UISaveVideoAtPathToSavedPhotosAlbum](<uisavevideoatpathtosavedphotosalbum(________).md>) — 把指定路径的视频添加到用户的相机胶卷相册。
- [UIVideoAtPathIsCompatibleWithSavedPhotosAlbum](<uivideoatpathiscompatiblewithsavedphotosalbum(__).md>) — 返回一个布尔值，表示指定视频是否兼容保存到用户的相机胶卷相册。

### PDF 创建

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — 创建一个以指定可变数据对象为目标的 PDF 图形上下文。
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — 创建一个以指定路径的文件为目标的 PDF 图形上下文。
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — 关闭一个 PDF 图形上下文，并将其从当前上下文栈中弹出。
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — 标记 PDF 上下文中新一页的开始，并使用默认值进行配置。
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — 标记 PDF 上下文中新一页的开始，并使用指定的自定义值进行配置。
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — 返回当前页面的边界。
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — 在当前页面中创建一个跳转目的地。
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — 把当前页面上的一个矩形区域链接到指定的跳转目的地。
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — 把当前页面上的一个矩形区域链接到指定的 URL。

### PDF 屏幕快照

- [UIScreenshotService](uiscreenshotservice.md) — 协调创建 App 内容的 PDF 屏幕快照的对象。

## 另请参阅

### 图形、绘图与打印

- [绘图](drawing.md) — 使用颜色、渲染器、绘制路径、字符串和阴影配置你的 App 的绘图环境。
- [打印](printing.md) — 显示系统打印面板并管理打印过程。
