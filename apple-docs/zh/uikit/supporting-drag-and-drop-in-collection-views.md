---
title: 支持集合视图中的拖放
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-drag-and-drop-in-collection-views
source_url: 'https://developer.apple.com/documentation/uikit/supporting-drag-and-drop-in-collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-drag-and-drop-in-collection-views.json'
content_hash: 'sha256:7e972e5dc5ac5e90'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [集合视图](collection-views.md)

# 支持集合视图中的拖放

<sub>文章</sub>

从集合视图发起拖动并处理放置。

## 概述

集合视图（collection view）通过专门针对所显示条目的 API 支持拖放（drag and drop）。要支持拖动，请定义拖动委托（delegate）对象（即采用 [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) 协议的对象），并将其分配给集合视图的 [dragDelegate](uicollectionview/dragdelegate.md) 属性。要处理放置，请定义放置委托对象（即采用 [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) 协议的对象），并将其分配给集合视图的 [dropDelegate](uicollectionview/dropdelegate.md) 属性。

### 从集合视图拖动条目

集合视图会管理大多数与拖动相关的交互，但你需要指定要拖动的条目。拖动手势发生时，集合视图会创建拖动会话，并调用拖动委托对象的 [- collectionView:itemsForBeginningDragSession:atIndexPath:](<uicollectionviewdragdelegate/collectionview(__itemsforbeginning_at_).md>) 方法。如果从该方法返回非空数组，集合视图就会开始拖动你指定的条目。如果不允许用户从指定索引路径拖动条目，则返回空数组。

> [!note] 注意
> 使用 [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) 协议的其他方法管理更多拖动相关交互。例如，你可以自定正在拖动的条目外观，并允许用户向当前拖动会话添加条目。

在实现 [- collectionView:itemsForBeginningDragSession:atIndexPath:](<uicollectionviewdragdelegate/collectionview(__itemsforbeginning_at_).md>) 方法时，请执行以下操作：

1. 创建一个或多个 [NSItemProvider](../foundation/nsitemprovider.md) 对象。使用条目提供程序表示集合视图条目的数据。
2. 将每个条目提供程序对象包装在 [UIDragItem](uidragitem.md) 对象中。
3. 考虑为每个拖动条目的 [localObject](uidragitem/localobject.md) 属性分配一个值。此步骤可选，但会加快在同一 App 内拖放内容的速度。
4. 从方法返回拖动条目。

使用所提供的索引路径确定要拖动的条目。如果该条目属于当前所选条目集合，集合视图会自动拖动所有所选条目。如果该条目不属于当前所选内容，集合视图会将其添加到拖动操作中。

有关发起拖动的更多信息，请参阅 [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)。

### 接收放置的内容

当内容被拖入集合视图的边界内时，集合视图会询问其放置委托，以确定能否接收拖动的数据。最初，集合视图只会调用放置委托的 [- collectionView:canHandleDropSession:](<uicollectionviewdropdelegate/collectionview(__canhandle_).md>) 方法，以确定你能否将指定数据纳入数据源。如果可以纳入数据，集合视图就会开始调用其他方法，以确定可以将数据放在何处。

随着用户手指移动，集合视图会跟踪潜在放置位置，并在每次位置变化时调用委托的 [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) 方法来通知委托。实现此方法是可选的，但建议实现，因为这样能让集合视图提供视觉反馈，展示如何纳入拖动的条目。在实现中，请创建 [UICollectionViewDropProposal](uicollectionviewdropproposal.md) 对象，其中包含你会如何响应在指定索引路径处放置的信息。例如，你可能想将内容作为新条目插入数据源，也可能将数据添加到指定索引路径处的现有条目中。由于系统会频繁调用此方法，请尽快返回建议。如果不实现此方法，集合视图就不会针对如何处理放置提供视觉反馈。

当用户从屏幕抬起相关手指并确认放置时，集合视图会调用放置委托的 [- collectionView:performDropWithCoordinator:](<uicollectionviewdropdelegate/collectionview(__performdropwith_).md>) 方法。你必须实现此方法来处理放置的数据。在实现中，获取拖动的数据、更新集合视图的数据源，并将任何必要的条目插入集合视图本身。如果条目源自集合视图本身，通常只需使用现有集合视图 API 直接重新排布条目。对于来自集合视图外部的内容，请使用 [localObject](uidragitem/localobject.md) 属性（如果内容源自你的 App 内部）或 [NSItemProvider](../foundation/nsitemprovider.md) 对象获取并插入数据。

在实现 [- collectionView:performDropWithCoordinator:](<uicollectionviewdropdelegate/collectionview(__performdropwith_).md>) 方法时，请执行以下操作：

1. 迭代所提供的放置协调器（drop coordinator）对象的 items 属性。
2. 对每个条目，确定要如何处理其内容：

- 如果条目的 `sourceIndexPath` 包含值，该条目就源自集合视图。使用批量更新从当前位置删除该条目，并将其插入新的索引路径。
- 如果拖动条目的 [localObject](uidragitem/localobject.md) 属性已设置，该条目就源自你的 App 中的其他位置，因此你必须插入一个条目或更新现有条目。
- 如果没有其他选项可用，请使用拖动条目 [itemProvider](uidragitem/itemprovider.md) 属性中的 [NSItemProvider](../foundation/nsitemprovider.md) 异步获取数据，并插入或更新条目。

1. 更新数据源，并在集合视图中插入或移动必要的条目。

对于已经位于你的 App 本地的条目，通常可以直接更新集合视图的数据源和界面。例如，可以使用批量更新删除并插入源自集合视图的条目。完成后，调用放置协调器的 [- dropItem:toItemAtIndexPath:](<uicollectionviewdropcoordinator/drop(__toitemat_).md>) 方法，以动画方式将拖动的内容插入集合视图。

对于必须使用 [NSItemProvider](../foundation/nsitemprovider.md) 对象检索的数据，请在能够检索实际数据之前向集合视图插入占位符。只有在向集合视图插入新条目时，才需要插入占位符。占位符充当集合视图中的临时条目，在实际数据可用前呈现你想显示的默认内容。例如，可以提供一个占位符单元格，其中的文本字段说明内容当前正在加载。

要向集合视图插入占位符，请执行以下操作：

1. 调用所提供 [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) 对象的 [- dropItem:toPlaceholder:](<uicollectionviewdropcoordinator/drop(__to_)-l5tg.md>) 方法，将占位符单元格插入集合视图。
2. 开始从 [NSItemProvider](../foundation/nsitemprovider.md) 对象异步加载数据。

当 [NSItemProvider](../foundation/nsitemprovider.md) 对象返回实际数据时，请提交插入，并用最终单元格替换占位符单元格。具体而言，请调用创建占位符后所收到的上下文对象的 [- commitInsertionWithDataSourceUpdates:](<uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates_).md>) 方法。在传给该方法的 block 中，更新模型对象和集合视图的数据源。此方法返回时，集合视图会自动删除占位符并插入最终条目，使更新后的数据反映在新条目中。

请在放置协调器的 `destinationIndexPath` 属性所指定的位置插入占位符。

## 另请参阅

### 拖放

- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — 用于从集合视图发起拖动的接口。
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — 用于处理集合视图中的放置的接口。
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — 用于协调自定放置相关操作与集合视图的接口。
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — 在集合视图上放置的条目的占位符。
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — 你为处理集合视图中的放置而提出的方案。
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — 与正在放入集合视图的条目相关联的数据。
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — 包含集合视图中占位符相关信息的对象。
- [UIDataSourceTranslating](uidatasourcetranslating.md) — 用于管理数据源对象的高级接口。
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — 在集合视图上拖动或放置的条目的占位符。
