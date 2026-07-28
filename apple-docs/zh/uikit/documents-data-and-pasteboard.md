---
title: 文稿、数据和粘贴板
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/documents-data-and-pasteboard
source_url: 'https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/documents-data-and-pasteboard.json'
content_hash: 'sha256:5b3253276b823117'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 文稿、数据和粘贴板

<sub>API 集合</sub>

整理 App 的数据，并通过粘贴板共享这些数据。

## 主题

### 文稿

- [UIDocument](uidocument.md) — 用于管理 App 数据中独立部分的抽象基类。
- [UIManagedDocument](uimanageddocument.md) — 与 Core Data 集成的托管文稿对象。
- [在 iCloud 环境中同步文稿](synchronizing-documents-in-the-icloud-environment.md) — 跨多台设备管理文稿，打造无缝的编辑和协作体验。

### 文稿呈现

- [UIDocumentViewController](uidocumentviewcontroller.md) — 管理并呈现存储在本地或云端的文稿的视图控制器（view controller）。

### 数据管理

- [UIDataSourceModelAssociation](uidatasourcemodelassociation.md) — 定义接口的一组方法，用于为 App 中的数据对象提供持久引用。

### 粘贴板

- [UIPasteControl](uipastecontrol.md) — 用户轻点后可将粘贴板内容放入 App 的按钮。
- [Configuration](uipastecontrol/configuration-swift.class.md) — 决定粘贴按钮颜色、圆角样式、图标和文本的对象。
- [DisplayMode](uipastecontrol/displaymode.md) — 决定粘贴按钮显示图标、文本标签还是二者的选项。
- [UIPasteboard](uipasteboard.md) — 帮助用户在 App 内部不同位置之间，以及从你的 App 向其他 App 共享数据的对象。
- [UIPasteConfiguration](uipasteconfiguration.md) — 对象为声明其能够接受用于粘贴和拖放（drag and drop）活动的特定数据类型而实现的接口。
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — 用于确定响应器对象是否支持粘贴配置的接口。

## 另请参阅

### App 结构

- [App 和环境](app-and-environment.md) — 管理生命周期事件和 App 的 UI 场景（scene），并获取有关特性和 App 运行环境的信息。
- [资源管理](resource-management.md) — 管理用于实现 App 界面的图像、字符串、Storyboard 和 nib 文件。
- [App 扩展](app-extensions.md) — 将 App 的基本功能扩展到系统的其他部分。
- [进程间通信](interprocess-communication.md) — 向用户显示基于活动的服务。
- [Mac Catalyst](mac-catalyst.md) — 创建可供用户在 Mac 设备上运行的 iPad App 版本。
