---
title: 集合视图
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/collection-views
source_url: 'https://developer.apple.com/documentation/uikit/collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/collection-views.json'
content_hash: 'sha256:25fe31659c3ee278'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md)

# 集合视图

<sub>API 集合</sub>

使用可配置且高度自定的布局来显示嵌套视图。

## 概述

集合视图（collection view）管理一组有序内容（例如「照片」App 中的照片网格），并以可视化方式呈现这些内容。

![「照片」App 的截屏，其中显示了按「月」视图组织的照片。](../../../attachments/cb3507c54de8fcaa8b77daa7c94110f6/collection-views-1@2x.png)

集合视图需要许多不同对象协同工作，包括：

- 单元格。单元格提供每项内容的视觉表示。
- 布局。布局定义集合视图中内容的视觉排布。
- 你的数据源对象。此对象采用 [UICollectionViewDataSource](uicollectionviewdatasource.md) 协议，并为集合视图提供数据。
- 你的委托（delegate）对象。此对象采用 [UICollectionViewDelegate](uicollectionviewdelegate.md) 协议，并管理用户与集合视图内容之间的交互，例如选择和高亮显示。
- 集合视图控制器。通常使用 [UICollectionViewController](uicollectionviewcontroller.md) 对象来管理集合视图。你也可以使用其他视图控制器（view controller），但某些集合相关功能需要集合视图控制器才能工作。

## 主题

### 视图

- [UICollectionView](uicollectionview.md) — 管理一组有序数据条目并使用可自定布局呈现这些条目的对象。
- [UICollectionViewController](uicollectionviewcontroller.md) — 专门用于管理集合视图的视图控制器。

### 数据

- [使用可差分数据源更新集合视图](updating-collection-views-using-diffable-data-sources.md) — 使用包含标识符的可差分数据源（diffable data source），简化集合视图中数据的显示和更新。
- [实现现代集合视图](implementing-modern-collection-views.md) — 为你的 App 引入组合式布局（compositional layout），并使用可差分数据源简化用户界面更新。
- [构建高性能列表和集合视图](building-high-performance-lists-and-collection-views.md) — 通过预取和图像准备，提升你 App 中列表和集合的性能。
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) — 用于管理数据并为集合视图提供单元格的对象。
- [UICollectionViewDataSource](uicollectionviewdatasource.md) — 由用于管理数据并为集合视图提供单元格的对象所采用的方法。
- [UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md) — 一种协议，为集合视图提前提供数据需求的预警，从而可以触发异步数据加载操作。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 特定时间点视图中数据状态的表示。
- [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) — 特定时间点布局区段中数据状态的表示。
- [UIRefreshControl](uirefreshcontrol.md) — 一种可以启动滚动视图内容刷新的标准控制。

### 单元格

- [UICollectionViewCell](uicollectionviewcell.md) — 数据条目位于集合视图可见边界内时，用于表示该条目的单个单元格。
- [UICollectionViewListCell](uicollectionviewlistcell.md) — 提供列表功能和默认样式的集合视图单元格。
- [UICollectionReusableView](uicollectionreusableview.md) — 定义集合视图呈现的所有单元格和附加视图行为的视图。

### 布局

- [实现现代集合视图](implementing-modern-collection-views.md) — 为你的 App 引入组合式布局，并使用可差分数据源简化用户界面更新。
- [布局](layouts.md) — 以高度可配置的布局排布集合视图内容。

### 选择管理

- [更改所选和高亮显示单元格的外观](changing-the-appearance-of-selected-and-highlighted-cells.md) — 向用户提供有关单元格状态以及状态之间过渡的视觉反馈。
- [使用双指平移手势选择多个条目](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — 在表格视图和集合视图中使用多选手势，加快用户选择多个条目的速度。

### 拖放（drag and drop）

- [支持集合视图中的拖放](supporting-drag-and-drop-in-collection-views.md) — 从集合视图发起拖动并处理放置。
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — 用于从集合视图发起拖动的接口。
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — 用于处理集合视图中的放置的接口。
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — 用于协调自定放置相关操作与集合视图的接口。
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — 在集合视图上放置的条目的占位符。
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — 你为处理集合视图中的放置而提出的方案。
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — 与正在放入集合视图的条目相关联的数据。
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — 包含集合视图中占位符相关信息的对象。
- [UIDataSourceTranslating](uidatasourcetranslating.md) — 用于管理数据源对象的高级接口。
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — 在集合视图上拖动或放置的条目的占位符。

## 另请参阅

### 容器视图

- [在 iOS 中为本地化自动调整视图大小](../xcode/autosizing-views-for-localization-in-ios.md) — 向你的 App 添加 Auto Layout 约束，以实现可本地化的视图。
- [表格视图（table view）](table-views.md) — 在由可自定行组成的单列中显示数据。
- [UIStackView](uistackview.md) — 用于将一组视图排布成一列或一行的简化接口。
- [UIScrollView](uiscrollview.md) — 允许滚动和缩放其中所含视图的滚动视图（scroll view）。
- [UILookToScrollInteraction](uilooktoscrollinteraction.md) _(beta)_
