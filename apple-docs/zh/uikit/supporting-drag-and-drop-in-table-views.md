---
title: 支持表格视图中的拖放
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-drag-and-drop-in-table-views
source_url: 'https://developer.apple.com/documentation/uikit/supporting-drag-and-drop-in-table-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-drag-and-drop-in-table-views.json'
content_hash: 'sha256:c5c9fe0ae494a771'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [表格视图](table-views.md)

# 支持表格视图中的拖放

<sub>文章</sub>

从表格视图发起拖动并处理放置。

## 概述

表格视图（table view）通过专门针对所显示行的 API 支持拖放（drag and drop）。要支持拖动，请定义拖动委托（delegate）对象（即采用 [UITableViewDragDelegate](uitableviewdragdelegate.md) 协议的对象），并将其分配给表格视图的 [dragDelegate](uitableview/dragdelegate.md) 属性。要处理放置，请定义放置委托对象（即采用 [UITableViewDropDelegate](uitableviewdropdelegate.md) 协议的对象），并将其分配给表格视图的 [dropDelegate](uitableview/dropdelegate.md) 属性。

### 从表格视图拖动行

表格视图会管理大多数与拖动相关的交互，但你需要指定要拖动的行。拖动手势发生时，表格视图会创建拖动会话，并调用拖动委托对象的 [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) 方法。（当用户拖动某个所选行时，会对所选内容中的每一行各调用一次此方法。如果没有选择任何行，只会对底层行调用一次此方法。）如果返回非空数组，表格视图就会开始拖动你指定的行。如果不允许用户从指定索引路径拖动内容，则返回空数组。

> [!note] 注意
> 使用 [UITableViewDragDelegate](uitableviewdragdelegate.md) 协议的其他方法管理更多拖动相关交互。例如，你可以自定正在拖动的行的外观，并允许用户向当前拖动会话添加条目。

在实现 [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) 方法时，请执行以下操作：

1. 创建一个或多个 [NSItemProvider](../foundation/nsitemprovider.md) 对象。使用条目提供程序表示表格各行的数据。
2. 将每个条目提供程序对象包装在 [UIDragItem](uidragitem.md) 对象中。
3. 考虑为每个拖动条目的 [localObject](uidragitem/localobject.md) 属性分配一个值。此步骤可选，但会加快在同一 App 内拖放内容的速度。
4. 从方法返回拖动条目。

使用所提供的索引路径确定要为哪一行创建拖动条目。如果目标行属于当前所选行，表格视图会自动拖动所有所选行。如果该行不属于当前所选内容，表格视图会将其添加到已经进行中的拖动操作。

有关发起拖动的更多信息，请参阅 [UITableViewDragDelegate](uitableviewdragdelegate.md)。

### 接收放置的内容

当内容被拖入表格视图的边界内时，表格视图会询问其放置委托，以确定能否接收拖动的数据。最初，表格视图只会调用放置委托的 [- tableView:canHandleDropSession:](<uitableviewdropdelegate/tableview(__canhandle_).md>) 方法，以确定你能否将指定数据纳入数据源。如果可以纳入数据，表格视图就会开始调用其他方法，以确定可以将数据放在何处。

随着用户手指移动，表格视图会跟踪潜在放置位置，并在每次位置变化时调用委托的 [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<uitableviewdropdelegate/tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) 方法来通知委托。实现此方法是可选的，但建议实现，因为这样能让表格视图提供视觉反馈，展示如何纳入拖动的内容。在实现中，请创建 [UITableViewDropProposal](uitableviewdropproposal.md) 对象，其中包含你会如何响应在指定索引路径处放置的信息。例如，你可能想将内容作为新行插入数据源，也可能将数据添加到指定索引路径处的现有行中。由于系统会频繁调用此方法，请尽快返回建议。如果不实现此方法，表格视图就不会针对如何处理放置提供视觉反馈。

当用户从屏幕抬起相关手指并确认放置时，表格视图会调用放置委托的 [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) 方法。你必须实现此方法来处理放置的数据。在实现中，获取拖动的数据、更新表格视图的数据源，并将任何必要的行插入表格视图本身。如果内容源自表格视图，你可以使用现有表格视图 API 从当前位置删除拖动的行，并将其插入新位置。对于来自表格视图外部的内容，请使用 [localObject](uidragitem/localobject.md) 属性（如果内容源自你的 App 内部）或 [NSItemProvider](../foundation/nsitemprovider.md) 对象获取并插入数据。

在实现 [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) 方法时，请执行以下操作：

1. 迭代所提供的放置协调器（drop coordinator）对象的 `items` 属性。
2. 对每个条目，确定要如何处理其内容：

- 如果条目的 `sourceIndexPath` 包含值，该条目就源自表格视图。使用批量更新从当前位置删除该条目，并将其插入新的索引路径。
- 如果拖动条目的 [localObject](uidragitem/localobject.md) 属性已设置，该内容就源自你的 App 中的其他位置，因此你必须插入一行或更新现有条目。
- 如果没有其他选项可用，请使用拖动条目 [itemProvider](uidragitem/itemprovider.md) 属性中的 [NSItemProvider](../foundation/nsitemprovider.md) 异步获取数据，并插入或更新条目。

1. 更新数据源，并在表格视图中插入或移动必要的条目。

对于已经位于你的 App 本地的内容，通常可以直接更新表格视图的数据源和界面。例如，可以使用批量更新在表格视图内删除并插入拖动的行。完成后，调用放置协调器的 [- dropItem:toRowAtIndexPath:](<uitableviewdropcoordinator/drop(__torowat_).md>) 方法，以动画方式将拖动的内容插入表格视图。

对于必须使用 [NSItemProvider](../foundation/nsitemprovider.md) 对象检索的数据，请在能够检索实际数据之前向表格视图插入占位符。只有在向表格视图插入新行时，才需要插入占位符。占位符充当临时行，在实际数据可用前呈现你想显示的默认内容。例如，可以提供一个占位符行，其中的文本字段说明内容当前正在加载。

要向表格视图插入占位符，请执行以下操作：

1. 调用所提供 [UITableViewDropCoordinator](uitableviewdropcoordinator.md) 对象的 `drop(_:toPlaceholderInsertedAt:withReuseIdentifier:rowHeight:cellUpdateHandler:)` 方法，将占位符行插入表格视图。使用 `cellUpdateHandler` 参数中的 block 配置占位符单元格的内容。
2. 开始从 [NSItemProvider](../foundation/nsitemprovider.md) 对象异步加载数据。

当 [NSItemProvider](../foundation/nsitemprovider.md) 对象返回实际数据时，请提交插入，并用最终单元格替换占位符单元格。具体而言，请调用创建占位符后所收到的上下文对象的 [- commitInsertionWithDataSourceUpdates:](<uitableviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) 方法。在传给该方法的 block 中，更新模型对象和表格视图的数据源。此方法返回时，表格视图会自动删除占位符并插入最终行，使更新后的数据反映在新单元格中。请在放置协调器的 `destinationIndexPath` 属性所指定的位置插入占位符。

## 另请参阅

### 拖放

- [在表格视图中采用拖放](adopting-drag-and-drop-in-a-table-view.md) — 演示如何为表格视图启用和实现拖放。
- [UITableViewDragDelegate](uitableviewdragdelegate.md) — 用于从表格视图发起拖动的接口。
- [UITableViewDropDelegate](uitableviewdropdelegate.md) — 用于处理表格视图中的放置的接口。
- [UITableViewDropCoordinator](uitableviewdropcoordinator.md) — 用于协调自定放置相关操作与表格视图的接口。
- [UITableViewDropItem](uitableviewdropitem.md) — 与正在放入表格视图的条目相关联的数据。
- [UITableViewDropProposal](uitableviewdropproposal.md) — 你为处理表格视图中的放置而提出的方案。
