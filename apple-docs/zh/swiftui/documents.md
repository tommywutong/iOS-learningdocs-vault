---
title: 文稿
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/documents
source_url: 'https://developer.apple.com/documentation/swiftui/documents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documents.json'
content_hash: 'sha256:5502788fa14a1f40'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# 文稿

<sub>API 集合</sub>

让人们能够打开和管理文稿。

## 概述

创建用于打开和编辑文稿的用户界面。

![](../../../attachments/9f0133f6a85bd81cbf87453f28384847/documents-hero@2x.png)

使用 [ReadableDocument](readabledocument.md) 和 [WritableDocument](writabledocument.md) 协议来定义你的文稿模型；当你的文稿需要同时支持读取和写入时，可采用 [Document](document.md)——一个把二者合并起来的便捷协议。它们让你可以直接访问文件 URL、与 Swift 并发集成，并支持进度汇报。你也可以使用基于 SwiftData 的文稿，方法是使用诸如 [init(editing:contentType:editor:prepareDocument:)](<documentgroup/init(editing_contenttype_editor_preparedocument_).md>) 这样的初始化方法。

SwiftUI 支持人们对基于文稿的 App 所期望的标准行为，并适配每个平台，例如多窗口支持、打开和存储面板。相关设计指导参见《人机界面指南》中的[设计模式](../design/human-interface-guidelines/patterns.md)。

## 主题

### 创建文稿

- [创建基于文稿的 App](creating-a-document-based-app.md) — 构建让人们可以用协调的文件访问来打开、编辑和存储文件的 App。
- [处理高级文稿场景](handling-advanced-document-scenarios.md) — 扩展你的基于文稿的 App，以支持自定文件格式、按需文件访问和进度汇报。
- [更新你的基于文稿的 App](updating-your-document-based-app.md) — 迁移现有 App，采用基于 URL 的文稿读取与写入并结合 Swift 并发。
- [使用 SwiftUI 构建基于文稿的 App](building-a-document-based-app-with-swiftui.md) — 在多平台 App 中创建、存储和打开文稿。
- [使用 SwiftData 构建基于文稿的 App](building-a-document-based-app-using-swiftdata.md) — 跟随 WWDC 演讲者一起，用 SwiftData 改造一个 App。
- [DocumentGroup](documentgroup.md) — 一种启用打开、创建和存储文稿支持的场景。

### 在引用类型实例中存储文稿数据

- [Document](document.md) — 一种同时支持读取和写入的文稿。 _(beta)_
- [ReadableDocument](readabledocument.md) — 一种支持从文件读取的文稿类型。 _(beta)_
- [WritableDocument](writabledocument.md) — 一种支持写入文件的文稿类型。 _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — 已打开文稿的配置，存储其文件 URL、最后修改日期和相关元数据。 _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — 关于文稿如何被创建的上下文。 _(beta)_
- [DocumentBaseBox](documentbasebox.md) — 一种 Box，允许设置其 Document 基础对象，而无需调用者知道该 box 及其基础对象的确切类型。

### 访问文稿配置

- [documentConfiguration](environmentvalues/documentconfiguration.md) — [DocumentGroup](documentgroup.md) 中某个文稿的配置。
- [DocumentConfiguration](documentconfiguration.md) — [DocumentGroup](documentgroup.md) 中某个文稿的配置。
- [undoManager](environmentvalues/undomanager.md) — 用于注册视图撤销操作的撤销管理器。

### 读取和写入文稿

- [DocumentReadConfiguration](documentreadconfiguration.md) — SwiftUI 传递给 [reader(configuration:)](<readabledocument/reader(configuration_).md>) 的上下文。 _(beta)_
- [DocumentWriteConfiguration](documentwriteconfiguration.md) — SwiftUI 传递给 [writer(configuration:)](<writabledocument/writer(configuration_).md>) 的上下文。 _(beta)_
- [DocumentReader](documentreader.md) — 一种从文件读取文稿内容的类型。 _(beta)_
- [DocumentWriter](documentwriter.md) — 一种把文稿内容写入文件的类型。 _(beta)_
- [FileWrapperDocumentReader](filewrapperdocumentreader.md) — 一种把 `FileWrapper` 反序列化为快照的文稿读取器。 _(beta)_
- [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) — 一种把快照序列化为 `FileWrapper` 的文稿写入器。 _(beta)_

### 以编程方式打开文稿

- [newDocument](environmentvalues/newdocument.md) — 环境中用于呈现新文稿的操作。
- [openDocument](environmentvalues/opendocument.md) — 环境中用于呈现现有文稿的操作。
- [OpenDocumentAction](opendocumentaction.md) — 一种呈现现有文稿的操作。

### 配置文稿启动体验

- [DocumentGroupLaunchScene](documentgrouplaunchscene.md) — 面向基于文稿的应用程序的启动场景。
- [documentLaunchTitle(_:)](<scene/documentlaunchtitle(__).md>) — 设置文稿启动卡片上显示的标题。 _(beta)_
- [documentLaunchSubtitle(_:)](<scene/documentlaunchsubtitle(__).md>) — 设置文稿启动卡片上标题下方显示的副标题。 _(beta)_
- [DocumentLaunchView](documentlaunchview.md) — 启动文稿相关用户体验时呈现的视图。
- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — 设置文稿启动卡片上显示的标题。 _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — 设置文稿启动卡片上标题下方显示的副标题。 _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — 向 `DocumentLaunchView` 添加以选中文件列表作为参数的操作。
- [DocumentLaunchGeometryProxy](documentlaunchgeometryproxy.md) — 用于访问场景框架及其标题视图的代理。
- [DefaultDocumentGroupLaunchActions](defaultdocumentgrouplaunchactions.md) — 文稿组启动场景和文稿启动视图的默认操作。
- [NewDocumentButton](newdocumentbutton.md) — 一种创建并打开新文稿的按钮。
- [DefaultNewDocumentButtonLabel](defaultnewdocumentbuttonlabel.md) — 新文稿按钮使用的默认标签。 _(beta)_
- [DocumentCreationSource](documentcreationsource.md) — 描述用于创建新文稿的来源。 _(beta)_

### 重命名文稿

- [RenameButton](renamebutton.md) — 一种触发标准重命名操作的按钮。
- [renameAction(_:)](<view/renameaction(__).md>) — 设置重命名操作要运行的闭包。
- [rename](environmentvalues/rename.md) — 激活标准重命名交互的操作。
- [RenameAction](renameaction.md) — 激活标准重命名交互的操作。

### 已废弃

- [FileDocument](filedocument.md) — 用于把文稿与文件相互序列化的类型。 _(已废弃)_
- [FileDocumentConfiguration](filedocumentconfiguration.md) — 已打开文件文稿的属性。 _(已废弃)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — 读取文件内容的配置。 _(已废弃)_
- [FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md) — 序列化文件内容的配置。 _(已废弃)_
- [NewDocumentAction](newdocumentaction.md) — 一种呈现新文稿的操作。 _(已废弃)_
- [ReferenceFileDocument](referencefiledocument.md) — 用于把引用类型文稿与文件相互序列化的类型。 _(已废弃)_
- [ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md) — 已打开引用文件文稿的属性。 _(已废弃)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各个部分的用户界面分组。
- [窗口](windows.md) — 在一个窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在人的周围环境中显示无边界的内容。
- [导览](navigation.md) — 让人们能够在场景内的 App 视图层级结构的不同部分之间移动。
- [模态呈现](modal-presentations.md) — 在提供专注交互的单独视图中呈现内容。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [搜索](search.md) — 让人们能够在你的 App 中搜索文本或其他内容。
- [App 扩展](app-extensions.md) — 把 App 的基本功能扩展到系统的其他部分，例如添加小组件。
