---
title: 在 SwiftUI 中通过拖放和重排制作卡牌游戏
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [macOS 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui
source_url: 'https://developer.apple.com/documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/making-a-card-game-with-drag-drop-and-reordering-in-swiftui.json'
content_hash: 'sha256:c47f59abc3669d4f'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [拖放](drag-and-drop.md)

# 在 SwiftUI 中通过拖放和重排制作卡牌游戏

<sub>示例代码</sub>

在卡牌游戏中使用拖放和重排修饰符在各个位置之间移动卡牌。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC26 场次 271：[Code-along: Build powerful drag and drop in SwiftUI](http://developer.apple.com/videos/play/wwdc2026/271/)。

## 另请参阅

### 重排条目

- [reorderable()](<dynamicviewcontent/reorderable().md>) — 在可重排容器修饰符的作用域内，允许对来自此内容的视图进行重排。 _(beta)_
- [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>) — 在可重排容器修饰符的作用域内，允许在分区内和分区之间对来自此内容的视图进行重排。 _(beta)_
- [ReorderableSingleCollectionIdentifier](reorderablesinglecollectionidentifier.md) — 一种不透明的空类型，用于标识只有一个集合的可重排容器和修饰符。 _(beta)_
- [reorderContainer(for:isEnabled:move:)](<view/reordercontainer(for_isenabled_move_).md>) — 定义一个可重排视图的容器。 _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<view/reordercontainer(for_in_isenabled_move_).md>) — 定义一个可重排视图的容器，使用你指定的类型来标识分区。 _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<view/reordercontainer(for_itemid_isenabled_move_).md>) — 定义一个可重排视图的容器，使用你指定的类型和键路径来标识条目。 _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<view/reordercontainer(for_itemid_in_isenabled_move_).md>) — 定义一个可重排视图的容器，使用你指定的类型和键路径来标识条目，并使用一个类型来标识集合。 _(beta)_
- [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) — 提供与此放置目的地修饰符关联的容器中发生的重排操作的目的地值。 _(beta)_
- [reorderDestination(for:itemID:in:)](<dropsession/reorderdestination(for_itemid_in_).md>) — 提供与此放置目的地修饰符关联的容器中发生的重排操作的目的地值。 _(beta)_
- [ReorderDifference](reorderdifference.md) — 重排操作所产生的差异。 _(beta)_

## 下载

- [MakingACardGameWithDragDropAndReorderingInSwiftUI.zip](https://docs-assets.developer.apple.com/published/97ac6f9aaef0/MakingACardGameWithDragDropAndReorderingInSwiftUI.zip)
