---
title: 自动特性跟踪
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/automatic-trait-tracking
source_url: 'https://developer.apple.com/documentation/uikit/automatic-trait-tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/automatic-trait-tracking.json'
content_hash: 'sha256:a64da2b13aa7f5db'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [在 iPad、Mac 和 Apple Vision Pro 上进行多任务处理](multitasking-on-ipad-mac-and-apple-vision-pro.md)

# 自动特性跟踪

<sub>API 集合</sub>

在支持自动特性跟踪的方法或闭包（closure）中使用特性（trait）时，减少手动注册特性变化的需要。

## 概述

自动特性跟踪是 UIKit 的一项功能。当你在受支持的方法或闭包中使用特性时，它可以免去手动注册特性变化的需要。这项功能可减少需要编写和维护的代码量、提高性能，并鼓励在受支持 API 的作用域内使用特性这一最佳实践。有关更多信息，请参阅[在特性发生变化时适配 App](adapting-your-app-when-traits-change.md)。

某些属性不适合在 [- layoutSubviews](<uiview/layoutsubviews().md>) 期间更改，例如，设置其值会产生使视图布局失效这一副作用的属性。请在视图的 [- updateProperties](<uiview/updateproperties().md>) 方法或视图控制器（view controller）的 [- updateProperties](<uiviewcontroller/updateproperties().md>) 方法中更新这些属性。这些方法支持自动特性跟踪，也支持对使用 [Observable()](<../observation/observable().md>) 宏的对象进行自动观察跟踪。若要通知对象其属性还有其他更新，请对视图调用 [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>)，或对视图控制器调用 [- setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>)。若要强制对象立即更新其属性，请对视图调用 [- updatePropertiesIfNeeded](<uiview/updatepropertiesifneeded().md>)，或对视图控制器调用 [- updatePropertiesIfNeeded](<uiviewcontroller/updatepropertiesifneeded().md>)。有关自动观察属性更新的更多信息，请参阅[使用 UIKit 中的观察跟踪自动更新视图](updating-views-automatically-with-observation-tracking-in-uikit.md)。

> [!important] 重要
> 请避免在 [- layoutSubviews](<uiview/layoutsubviews().md>) 中进行会更新对象在 [- updateProperties](<uiview/updateproperties().md>) 中所跟踪属性、或会使视图布局失效的更改，以免导致过多更新。

下面列出了支持自动特性跟踪的全部 API。

## 主题

### 视图

- [- updateProperties](<uiview/updateproperties().md>) — 在布局前配置视图的内容和样式属性。
- [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>) — 调用此方法可手动请求更新视图属性。多个请求可能会合并为单次更新，与下一次布局过程一同执行。
- [- updatePropertiesIfNeeded](<uiview/updatepropertiesifneeded().md>) — 强制立即更新此视图（以及其视图控制器，如适用）和所有子视图的属性，包括其子树中的所有视图控制器或视图。
- [- layoutSubviews](<uiview/layoutsubviews().md>) — 布置子视图。
- [- updateConstraints](<uiview/updateconstraints().md>) — 更新视图的约束。
- [- drawRect:](<uiview/draw(__).md>) — 在传入的矩形内绘制视图图像。
- [属性](uiview/invalidations/properties.md)

### 视图控制器

- [- updateProperties](<uiviewcontroller/updateproperties().md>) — 配置视图控制器的内容和样式属性。
- [- setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>) — 调用此方法可手动请求更新视图控制器属性。多个请求可能会合并为单次更新，与下一次布局过程一同执行。
- [- updatePropertiesIfNeeded](<uiviewcontroller/updatepropertiesifneeded().md>) — 强制立即更新此视图控制器及其视图的属性，包括此子树中的所有视图控制器和视图。
- [- viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) — 通知视图控制器，其视图即将布置子视图。
- [- viewDidLayoutSubviews](<uiviewcontroller/viewdidlayoutsubviews().md>) — 在视图完成子视图布局时通知视图控制器。
- [- updateViewConstraints](<uiviewcontroller/updateviewconstraints().md>) — 在视图需要更新约束时通知视图控制器。
- [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) — 针对提供的状态更新内容不可用配置。

### 呈现控制器

- [- containerViewWillLayoutSubviews](<uipresentationcontroller/containerviewwilllayoutsubviews().md>) — 通知呈现控制器，容器视图中的视图即将开始布局。
- [- containerViewDidLayoutSubviews](<uipresentationcontroller/containerviewdidlayoutsubviews().md>) — 在容器视图中的视图结束布局时通知呈现控制器。

### 按钮

- [- updateConfiguration](<uibutton/updateconfiguration().md>) — 响应按钮状态变化来更新按钮配置。
- [configurationUpdateHandler](uibutton/configurationupdatehandler-swift.property.md) — 一个在按钮状态发生变化时执行的闭包。

### 集合视图（collection view）单元格

- [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) — 使用当前状态更新单元格配置。
- [configurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-7rqbu.md) — 一个 block，用于使用当前状态处理单元格配置的更新。

### 表格视图（table view）单元格

- [updateConfiguration(using:)](<uitableviewcell/updateconfiguration(using_).md>) — 使用当前状态更新单元格配置。
- [configurationUpdateHandler](uitableviewcell/configurationupdatehandler-974.md) — 一个 block，用于使用当前状态处理单元格配置的更新。

### 表格视图页眉和页脚

- [updateConfiguration(using:)](<uitableviewheaderfooterview/updateconfiguration(using_).md>) — 使用当前状态更新视图配置。
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-49slo.md) — 一个 block，用于使用当前状态处理视图配置的更新。

### 集合视图组合式布局

- [UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md) — 一个闭包，用于创建并返回布局的各个区段。

## 另请参阅

### 适配性

- [UITraitCollection](uitraitcollection.md) — 一组数据，表示 App 用户界面中单个元素所处的环境。
- [UITraitEnvironment](uitraitenvironment.md) — 一组方法，让 App 能够获取 iOS 界面环境。
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — 一组方法，与呈现控制器配合使用，决定如何响应 App 中的特性变化。
- [UIContentContainer](uicontentcontainer.md) — 一组方法，用于使视图控制器的内容适配尺寸和特性变化。
