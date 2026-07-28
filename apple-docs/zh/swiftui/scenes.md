---
title: 场景
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenes
source_url: 'https://developer.apple.com/documentation/swiftui/scenes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenes.json'
content_hash: 'sha256:855c2a748721f254'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 场景

<sub>API 集合</sub>

声明构成 App 各部分的用户界面（UI）分组。

## 概述

场景代表 App 用户界面的一部分，其生命周期由系统管理。[App](app.md) 实例呈现其包含的场景，而每个 [Scene](scene.md) 则充当 [View](view.md) 层级结构的根元素。

![](../../../attachments/0ae322d333458f9341bc3aa57f4e8250/scenes-hero@2x.png)

系统根据场景的类型、平台和上下文，以不同方式呈现场景。场景可能填满整个屏幕、部分屏幕、窗口、窗口中的标签页，或其他形式。在某些情况下，你的 App 也可能同时显示场景的多个实例，例如，当用户同时打开多个基于 App 中单个 [WindowGroup](windowgroup.md) 声明的窗口时。关于主要内置场景类型的更多信息，请参阅 [窗口](windows.md) 和 [文稿](documents.md)。

你可以像配置视图一样，使用修饰符来配置场景。例如，你可以使用 [windowStyle(_:)](<scene/windowstyle(__).md>) 修饰符来调整包含场景的窗口的外观——如果场景恰好出现在一个窗口中。同样，你可以使用 [commands(content:)](<scene/commands(content_).md>) 修饰符添加菜单命令，这些命令在场景位于某些平台的前台时变为可用。

## 主题

### 创建场景

- [Scene](scene.md) — App 用户界面的一部分，其生命周期由系统管理。
- [SceneBuilder](scenebuilder.md) — 一种结果构建器（result builder），用于将一组场景组合成单个复合场景。

### 监控场景生命周期

- [scenePhase](environmentvalues/scenephase.md) — 场景的当前阶段。
- [ScenePhase](scenephase.md) — 场景运行状态的指示。

### 管理设置（Settings）窗口

- [Settings](settings.md) — 一个场景，用于呈现查看和修改 App 设置的界面。
- [SettingsLink](settingslink.md) — 一个视图，用于打开 App 定义的 Settings 场景。
- [OpenSettingsAction](opensettingsaction.md) — 一个操作，用于呈现 App 的 Settings 场景。
- [openSettings](environmentvalues/opensettings.md) — 存储在视图环境中的 Settings 呈现操作。

### 构建菜单栏

- [使用 SwiftUI 构建和自定义菜单栏](building-and-customizing-the-menu-bar-with-swiftui.md) — 通过为 iPadOS 和 macOS 构建原生菜单栏，提供无缝的跨平台用户体验。

### 创建菜单栏附加内容

- [MenuBarExtra](menubarextra.md) — 一个场景，它本身渲染为系统菜单栏中的一个持久控制（control）。
- [menuBarExtraStyle(_:)](<scene/menubarextrastyle(__).md>) — 设置由此场景创建的菜单栏附加内容的样式。
- [MenuBarExtraStyle](menubarextrastyle.md) — 菜单栏附加内容场景的外观和行为规范。

### 创建 watch 通知

- [WKNotificationScene](wknotificationscene.md) — 一个场景，在收到指定类别的远程或本地通知时出现。

### 在外部显示器上呈现内容

- [sceneAccessory(content:)](<view/sceneaccessory(content_).md>) — 定义与 `self` 关联的任何场景附件。_(beta)_
- [SceneAccessoryContent](sceneaccessorycontent.md) — 符合此协议的类型代表为场景附件定义内容的项。_(beta)_
- [ExternalNonInteractiveAccessory](externalnoninteractiveaccessory.md) — 一个场景附件，用于在外部显示器上呈现非交互内容。_(beta)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [窗口](windows.md) — 在窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在用户周围显示无边界的内容。
- [文稿](documents.md) — 让用户能够打开和管理文稿。
- [导航](navigation.md) — 使用户能够在场景内你的 App 视图层级结构的不同部分之间移动。
- [模态呈现方式](modal-presentations.md) — 在提供专注交互的独立视图中呈现内容。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [搜索](search.md) — 让用户能够在你的 App 中搜索文本或其他内容。
- [App 扩展](app-extensions.md) — 将 App 的基础功能扩展到系统的其他部分，例如通过添加小组件（Widget）。
