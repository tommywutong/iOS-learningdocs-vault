---
title: 自动观察跟踪
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/automatic-observation-tracking
source_url: 'https://developer.apple.com/documentation/uikit/automatic-observation-tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/automatic-observation-tracking.json'
content_hash: 'sha256:0c48b8ab1dc89057'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 自动观察跟踪

<sub>API 集合</sub>

在支持自动观察跟踪（automatic observation tracking）的方法中进行更新，从而简化数据变化时的视图更新。

## 概述

使用自动观察跟踪，在模型对象发生变化时更新视图，而无需手动使视图失效。使用 [Observable](../observation/observable.md) 宏标记模型类，然后在 [- updateProperties](<uiview/updateproperties().md>) 或 [- layoutSubviews](<uiview/layoutsubviews().md>) 等方法中读取模型属性。UIKit 会跟踪你访问的属性，并在这些属性发生变化时自动再次调用这些方法。这种方式无需在更新模型数据后手动调用 [- setNeedsLayout](<uiview/setneedslayout().md>) 或 [- setNeedsDisplay](<uiview/setneedsdisplay().md>) 等方法，减少了出现错误和显示过时内容的机会。

视图、视图控制器（view controller）、呈现控制器（presentation controller）、按钮、集合视图（collection view）单元格、表格视图（table view）单元格，以及表格视图页眉和页脚中的以下方法支持自动观察跟踪。有关更多信息，请参阅[使用 UIKit 中的观察跟踪自动更新视图](updating-views-automatically-with-observation-tracking-in-uikit.md)。

## 主题

### 观察视图中的数据

- [- updateProperties](<uiview/updateproperties().md>) — 在布局前配置视图的内容和样式属性。
- [- layoutSubviews](<uiview/layoutsubviews().md>) — 布置子视图。
- [- updateConstraints](<uiview/updateconstraints().md>) — 更新视图的约束。
- [- drawRect:](<uiview/draw(__).md>) — 在传入的矩形内绘制视图图像。

### 观察视图控制器中的数据

- [- updateProperties](<uiviewcontroller/updateproperties().md>) — 配置视图控制器的内容和样式属性。
- [- viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) — 通知视图控制器，其视图即将布置子视图。
- [- viewDidLayoutSubviews](<uiviewcontroller/viewdidlayoutsubviews().md>) — 在视图完成子视图布局时通知视图控制器。
- [- updateViewConstraints](<uiviewcontroller/updateviewconstraints().md>) — 在视图需要更新约束时通知视图控制器。
- [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) — 针对提供的状态更新内容不可用配置。

### 观察呈现控制器中的数据

- [- containerViewWillLayoutSubviews](<uipresentationcontroller/containerviewwilllayoutsubviews().md>) — 通知呈现控制器，容器视图中的视图即将开始布局。
- [- containerViewDidLayoutSubviews](<uipresentationcontroller/containerviewdidlayoutsubviews().md>) — 在容器视图中的视图结束布局时通知呈现控制器。

### 观察按钮中的数据

- [- updateConfiguration](<uibutton/updateconfiguration().md>) — 响应按钮状态变化来更新按钮配置。
- [configurationUpdateHandler](uibutton/configurationupdatehandler-swift.property.md) — 一个在按钮状态发生变化时执行的闭包（closure）。

### 观察集合视图单元格中的数据

- [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) — 使用当前状态更新单元格配置。
- [configurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-7rqbu.md) — 一个 block，用于使用当前状态处理单元格配置的更新。

### 观察表格视图单元格中的数据

- [updateConfiguration(using:)](<uitableviewcell/updateconfiguration(using_).md>) — 使用当前状态更新单元格配置。
- [configurationUpdateHandler](uitableviewcell/configurationupdatehandler-974.md) — 一个 block，用于使用当前状态处理单元格配置的更新。

### 观察表格页眉和页脚视图中的数据

- [updateConfiguration(using:)](<uitableviewheaderfooterview/updateconfiguration(using_).md>) — 使用当前状态更新视图配置。
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-49slo.md) — 一个 block，用于使用当前状态处理视图配置的更新。

### 观察集合视图布局中的数据

- [UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md) — 一个闭包，用于创建并返回布局的各个区段。
- [- initWithSectionProvider:](<uicollectionviewcompositionallayout/init(sectionprovider_).md>) — 使用区段提供程序创建组合式布局（compositional layout）对象，由该提供程序提供布局的各个区段。
- [- initWithSectionProvider:configuration:](<uicollectionviewcompositionallayout/init(sectionprovider_configuration_).md>) — 使用区段提供程序和附加配置创建组合式布局对象。

## 另请参阅

### 数据观察

- [使用 UIKit 中的观察跟踪自动更新视图](updating-views-automatically-with-observation-tracking-in-uikit.md) — 使用 Swift Observation 和自动跟踪，在模型数据更新时更新视图。
