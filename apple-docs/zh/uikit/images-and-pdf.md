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

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 图像与 PDF

<sub>API 集合</sub>

创建和管理图像，包括使用位图和 PDF 格式的图像。

## 主题

### 表示形式

- [UIImage](uiimage.md) — 管理 App 中图像数据的对象。
- [SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md) — 包含应用于符号图像的特定字体、大小、样式和粗细属性的对象。
- [Configuration](uiimage/configuration-swift.class.md) — 包含系统在选择当前图像变体时使用的特性的配置对象。

### 图像创建

- [Supporting HDR images in your app](supporting-hdr-images-in-your-app.md) — ​ 使用 SwiftUI 和 Core Image 加载、显示、编辑和保存 HDR 图像。​
- [UIImageJPEGRepresentation](<uiimage/jpegdata(compressionquality_).md>) — 返回包含 JPEG 格式图像的数据对象。
- [UIImagePNGRepresentation](<uiimage/pngdata().md>) — 返回包含指定图像的 PNG 格式的数据对象。

### 相册

- [UIImageWriteToSavedPhotosAlbum](<uiimagewritetosavedphotosalbum(________).md>) — 将指定图像添加到用户的相机胶卷相册。
- [UISaveVideoAtPathToSavedPhotosAlbum](<uisavevideoatpathtosavedphotosalbum(________).md>) — 将指定路径的影片添加到用户的相机胶卷相册。
- [UIVideoAtPathIsCompatibleWithSavedPhotosAlbum](<uivideoatpathiscompatiblewithsavedphotosalbum(__).md>) — 返回指示指定视频是否可保存到用户的相机胶卷相册的布尔值。

### PDF 创建

- [UIGraphicsBeginPDFContextToData](<uigraphicsbeginpdfcontexttodata(______).md>) — 创建以指定可变数据对象为目标的 PDF 图形上下文。
- [UIGraphicsBeginPDFContextToFile](<uigraphicsbeginpdfcontexttofile(______).md>) — 创建以指定路径的文件为目标的 PDF 图形上下文。
- [UIGraphicsEndPDFContext](<uigraphicsendpdfcontext().md>) — 关闭 PDF 图形上下文并将其从当前上下文栈弹出。
- [UIGraphicsBeginPDFPage](<uigraphicsbeginpdfpage().md>) — 标记 PDF 上下文中新页面的开始，并使用默认值进行配置。
- [UIGraphicsBeginPDFPageWithInfo](<uigraphicsbeginpdfpagewithinfo(____).md>) — 标记 PDF 上下文中新页面的开始，并使用指定的自定值进行配置。
- [UIGraphicsGetPDFContextBounds](<uigraphicsgetpdfcontextbounds().md>) — 返回当前页面边界。
- [UIGraphicsAddPDFContextDestinationAtPoint](<uigraphicsaddpdfcontextdestinationatpoint(____).md>) — 在当前页面创建跳转目的地。
- [UIGraphicsSetPDFContextDestinationForRect](<uigraphicssetpdfcontextdestinationforrect(____).md>) — 将当前页面上的矩形区域链接到指定的跳转目的地。
- [UIGraphicsSetPDFContextURLForRect](<uigraphicssetpdfcontexturlforrect(____).md>) — 将当前页面上的矩形区域链接到指定的 URL。

### PDF 截图

- [UIScreenshotService](uiscreenshotservice.md) — 协调创建 App 内容 PDF 截图的对象。

## 另请参阅

### 图形、绘制与打印

- [Drawing](drawing.md) — 使用颜色、渲染器、绘制路径、字符串和阴影配置 App 的绘制环境。
- [Printing](printing.md) — 显示系统打印面板并管理打印过程。
