---
title: 拖放
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/drag-and-drop
source_url: 'https://developer.apple.com/documentation/swiftui/drag-and-drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/drag-and-drop.json'
content_hash: 'sha256:980093a79ceae346'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# 拖放

<sub>API 集合</sub>

让人们通过把项目从一个位置拖到另一个位置来移动或复制项目。

## 概述

拖放为人们提供了一种便捷方式：用直观的拖拽手势，把内容从 App 的一部分移到另一部分、从一个 App 移到另一个 App，或者重新排列内容的顺序。在 App 界面内潜在的源视图和目标视图上添加视图修饰符，即可在你的 App 中支持这项功能。

![](../../../attachments/389cb904528e698574c83a1ccfbb85d9/drag-and-drop-hero@2x.png)

在修饰符中，提供或接受遵循 [Transferable](../coretransferable/transferable.md) 协议的类型，或遵循 [NSItemProviderReading](../foundation/nsitemproviderreading.md) 和/或 [NSItemProviderWriting](../foundation/nsitemproviderwriting.md) 的类型。在 Swift 中，优先使用可转移（transferable）的项目。

如需设计指导，参见《人机界面指南》中的[拖放](../design/human-interface-guidelines/drag-and-drop.md)。

## 主题

### 基础

- [使用 SwiftUI 采用拖放](adopting-drag-and-drop-using-swiftui.md) — 在列表、表格和自定视图中启用拖放交互。
- [把视图变成拖拽源](making-a-view-into-a-drag-source.md) — 采用 draggable API 为拖放操作提供项目。
- [在列表、叠放、网格和自定布局中重新排列项目](reordering-items-in-lists-stacks-grids-and-custom-layouts.md) — 使用重排修饰符为 SwiftUI 布局添加拖拽重排交互。

### 配置拖放行为

- [dragConfiguration(_:)](<view/dragconfiguration(__).md>) — 配置一个拖拽会话。
- [DragConfiguration](dragconfiguration.md) — 由拖拽源提出的拖拽行为。一个描述拖拽源所支持的拖拽操作的值。
- [dropConfiguration(_:)](<view/dropconfiguration(__).md>) — 配置一个放置会话。
- [DropConfiguration](dropconfiguration.md) — 描述放置的行为。
- [dragContainer(for:in:_:)](<view/dragcontainer(for_in___).md>) — 一个包含可拖拽视图的容器，其拖拽载荷基于被拖拽项目的多个标识符。
- [dragContainer(for:itemID:in:_:)](<view/dragcontainer(for_itemid_in___).md>) — 一个包含可拖拽视图的容器。
- [dragContainerSelection(_:containerNamespace:)](<view/dragcontainerselection(__containernamespace_).md>) — 为拖拽容器提供多项目选择支持。

### 移动项目

- [DragSession](dragsession.md) — 描述进行中的拖拽会话。
- [DropSession](dropsession.md)

### 移动可转移项目

- [draggable(_:)](<view/draggable(__).md>) — 将此视图激活为拖放操作的源。
- [draggable(_:preview:)](<view/draggable(__preview_).md>) — 将此视图激活为拖放操作的源。
- [draggable(_:containerNamespace:_:)](<view/draggable(__containernamespace___).md>) — 将此视图激活为拖放操作的源，允许提供可选的可标识载荷，并指定此视图所属拖拽容器的命名空间。
- [draggable(_:id:containerNamespace:_:)](<view/draggable(__id_containernamespace___).md>) — 将此视图激活为拖放操作的源，允许提供可选的载荷，并指定此视图所属拖拽容器的命名空间。
- [draggable(_:id:item:containerNamespace:)](<view/draggable(__id_item_containernamespace_).md>) — 将此视图激活为拖放操作的源，允许提供可选的载荷，并指定此视图所属拖拽容器的命名空间。
- [draggable(_:item:containerNamespace:)](<view/draggable(__item_containernamespace_).md>) — 将此视图激活为拖放操作的源，允许提供可选的可标识载荷，并指定此视图所属拖拽容器的命名空间。
- [draggable(containerItemID:containerNamespace:)](<view/draggable(containeritemid_containernamespace_).md>) — 在拖拽容器内，将此视图激活为拖放操作的源。支持惰性拖拽容器。

### 使用项目提供器移动项目

- [itemProvider(_:)](<view/itemprovider(__).md>) — 提供一个闭包，为特定的数据元素生成要使用的拖拽表示。
- [onDrag(_:preview:)](<view/ondrag(__preview_).md>) — 将此视图激活为拖放操作的源。
- [onDrag(_:)](<view/ondrag(__).md>) — 将此视图激活为拖放操作的源。
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — 定义拖放操作的目标，使用你指定的闭包处理放置的内容。
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_).md>) — 使用由你提供的代理控制的行为，定义拖放操作的目标。
- [DropDelegate](dropdelegate.md) — 你可以实现的一个接口，用于与被修饰为接受放置的视图中的放置操作交互。
- [DropProposal](dropproposal.md) — 一次放置的行为。
- [DropOperation](dropoperation.md) — 决定用户放下拖拽项目时拖放会话如何解析的操作类型。
- [DropInfo](dropinfo.md) — 一次放置的当前状态。

### 重新排列项目

- [在 SwiftUI 中用拖放和重排制作卡牌游戏](making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md) — 在卡牌游戏中使用拖放和重排修饰符在各个位置之间移动卡牌。
- [reorderable()](<dynamicviewcontent/reorderable().md>) — 在可重排容器修饰符的作用范围内，启用来自此内容的视图的重排。 _(beta)_
- [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>) — 在可重排容器修饰符的作用范围内，启用来自此内容的视图在分节之内和之间的重排。 _(beta)_
- [ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md) — 一种不透明的空类型，用于标识只有单个集合的可重排容器和修饰符。 _(beta)_
- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — 定义一个可重排视图的容器。 _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — 定义一个可重排视图的容器，并使用你指定的类型来标识分节。 _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — 定义一个可重排视图的容器，并使用你指定的类型和键路径来标识项目。 _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — 定义一个可重排视图的容器，使用你指定的类型和键路径来标识项目，并用一个类型来标识集合。 _(beta)_
- [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) — 提供与此放置目标修饰符关联的容器中发生的重排操作的目标值。 _(beta)_
- [reorderDestination(for:itemID:in:)](<dropsession/reorderdestination(for_itemid_in_).md>) — 提供与此放置目标修饰符关联的容器中发生的重排操作的目标值。 _(beta)_
- [ReorderDifference](reorderdifference.md) — 重排操作所产生的差异。 _(beta)_

### 描述预览排布

- [dragPreviewsFormation(_:)](<view/dragpreviewsformation(__).md>) — 描述被拖拽预览的视觉组合方式。
- [dropPreviewsFormation(_:)](<view/droppreviewsformation(__).md>) — 描述放置预览的组合方式。
- [DragDropPreviewsFormation](dragdroppreviewsformation.md) — 在 macOS 上，描述被拖拽预览的视觉组合方式。拖拽源和放置目标都可以指定各自期望的预览排布。

### 配置弹簧加载

- [springLoadingBehavior(_:)](<view/springloadingbehavior(__).md>) — 设置此视图的弹簧加载行为。
- [springLoadingBehavior](environmentvalues/springloadingbehavior.md) — 与此环境关联的视图的弹簧加载交互行为。
- [SpringLoadingBehavior](springloadingbehavior.md) — 控制视图弹簧加载行为的选项。

## 另请参阅

### 事件处理

- [Gestures](gestures.md) — 定义从轻点、点按、轻扫到精细手势的各种交互。
- [Input events](input-events.md) — 响应来自硬件设备的输入，例如键盘或 Touch Bar。
- [Clipboard](clipboard.md) — 让人们通过发出“拷贝”和“粘贴”命令来移动或复制项目。
- [Focus](focus.md) — 识别并控制哪个可见对象响应用户交互。
- [System events](system-events.md) — 对系统事件作出响应，例如打开 URL。
