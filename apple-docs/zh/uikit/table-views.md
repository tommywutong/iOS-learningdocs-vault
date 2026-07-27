---
title: 表格视图
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/table-views
source_url: 'https://developer.apple.com/documentation/uikit/table-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/table-views.json'
content_hash: 'sha256:8b44092c3599fde3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md)

# 表格视图

<sub>API 集合</sub>

在单列中显示可自定义的行数据。

## 概述

表格视图以单列的形式显示纵向滚动的内容，并划分为行和分区。表格的每一行显示与你 App 相关的一条信息。分区让你可以将相关的行归为一组。例如，通讯录 App 使用表格来显示用户联系人的姓名。

![通讯录 App 的屏幕截图，它使用表格将用户的各个联系人组织成一个可滚动的列表。](../../../attachments/c3bbc132299c757114b6ed3a962aa36a/uitableview-1@2x.png)

表格视图由许多不同的对象协作构成，包括：

- 单元格。单元格提供内容的视觉呈现。你可以使用 UIKit 提供的默认单元格，也可以根据 App 需要定义自定义单元格。
- 表格视图控制器。你通常使用 [UITableViewController](uitableviewcontroller.md) 对象来管理某个表格视图。你也可以使用其他视图控制器，但某些与表格相关的特性需要表格视图控制器才能正常工作。
- 你的数据源对象。该对象遵循 [UITableViewDataSource](uitableviewdatasource.md) 协议，为表格提供数据。
- 你的委托对象。该对象遵循 [UITableViewDelegate](uitableviewdelegate.md) 协议，管理用户与表格内容的交互。

## 主题

### 基础

- [UITableView](uitableview.md) — 一个视图，以单列中的多行来呈现数据。

### Data

- [Filling a table with data](filling-a-table-with-data.md) — 使用数据源对象动态创建和配置表格的单元格，或从故事板中静态提供这些单元格。
- [Asynchronously loading images into table and collection views](asynchronously-loading-images-into-table-and-collection-views.md) — 异步存储和获取图像，使你的 App 响应更迅速。
- [UITableViewDataSource](uitableviewdatasource.md) — 一个对象为管理数据并为表格视图提供单元格而遵循的方法。
- [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) — 一个协议，提前告知表格视图的数据需求，让你能够提早启动可能耗时较长的数据操作。
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — 你用来管理数据并为表格视图提供单元格的对象。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 某个视图中数据在特定时间点状态的表示。
- [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) — 一个对象，为带有分区索引的表格视图组织、排序并本地化数据。
- [UIDataSourceTranslating](uidatasourcetranslating.md) — 一个用于管理数据源对象的高级接口。
- [UIRefreshControl](uirefreshcontrol.md) — 一个标准控制，可以发起滚动视图内容的刷新。

### Table management

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md) — 为你表格视图的表头、表尾和行提供高度估算值，确保滚动能准确反映内容的大小。
- [UITableViewController](uitableviewcontroller.md) — 一个专门用于管理表格视图的视图控制器。
- [UITableViewDelegate](uitableviewdelegate.md) — 用于管理选择、配置分区表头和表尾、删除和重新排序单元格，以及在表格视图中执行其他操作的方法。
- [UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md) — 一个上下文对象，提供与从一个视图到另一个视图的特定焦点更新相关的信息。

### Cells, headers, and footers

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md) — 通过在故事板中定义一个或多个原型单元格，指定表格各行的外观和内容。
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md) — 创建支持动态字体的表格视图单元格，并使用系统间距约束来调整文本标签周围的间距。
- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md) — 通过为表格视图的分区添加表头和表尾视图，从视觉上区分各组行。
- [UITableViewCell](uitableviewcell.md) — 表格视图中单行的视觉呈现。
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) — 一个可复用视图，放置在表格分区的顶部或底部，用于显示该分区的附加信息。

### Row actions

- [UISwipeActionsConfiguration](uiswipeactionsconfiguration.md) — 在表格行上滑动时要执行的一组操作。
- [UIContextualAction](uicontextualaction.md) — 用户滑动表格行时要显示的一个操作。
- [UITableViewRowAction](uitableviewrowaction.md) — 用户在表格行中水平滑动时呈现的单个操作。_(已废弃)_

### Selection management

- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md) — 检测用户何时点按了表格视图单元格，以便你的 App 采取相应的后续操作。
- [Selecting multiple items with a two-finger pan gesture](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — 使用表格视图和集合视图上的多选手势，加快用户对多个项目的选择速度。

### Drag and drop

- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md) — 从表格视图发起拖动并处理放置。
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md) — 演示如何为表格视图启用并实现拖放。
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — 从表格视图发起拖动的接口。
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — 在表格视图中处理放置的接口。
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — 一个用于协调你与表格视图相关的自定义放置操作的接口。
- [UITableViewDropItem](uitableviewdropitem.md) — 与被放置到表格视图中的某个项目相关联的数据。
- [UITableViewDropProposal](uitableviewdropproposal.md) — 你针对在表格视图中处理某次放置所提出的方案。

### Placeholder cells

- [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md) — 一个对象，用于跟踪你在放置操作期间添加到表格中的占位单元格。
- [UITableViewDropPlaceholder](uitableviewdropplaceholder.md) — 一个支持自定义放置预览参数的占位单元格。
- [UITableViewPlaceholder](uitableviewplaceholder.md) — 一个对象，包含关于正在插入表格中的占位单元格的信息。

## 另请参阅

### Container views

- [Autosizing views for localization in iOS](../xcode/autosizing-views-for-localization-in-ios.md) — 为你的 App 添加自动布局约束，以实现可本地化的视图。
- [Collection views](collection-views.md) — 使用可配置且高度可自定义的布局显示嵌套视图。
- [UIStackView](uistackview.md) — 一个简化的接口，用于以列或行的形式布局一组视图。
- [UIScrollView](uiscrollview.md) — 一个视图，允许对其包含的视图进行滚动和缩放。
- [UILookToScrollInteraction](uilooktoscrollinteraction.md) _(beta)_
