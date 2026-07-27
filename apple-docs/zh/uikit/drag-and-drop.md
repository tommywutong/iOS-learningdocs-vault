---
title: 拖放
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/drag-and-drop
source_url: 'https://developer.apple.com/documentation/uikit/drag-and-drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/drag-and-drop.json'
content_hash: 'sha256:f326c28ac5fa3dca'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# 拖放

<sub>API 集合</sub>

通过在视图中使用交互 API，为 App 添加拖放（drag and drop）功能。

## 概述

借助 iOS 中的拖放功能，用户可以使用连续手势将项目从屏幕上的一个位置拖到另一个位置。拖放活动可以在单个 App 中进行，也可以在一个 App 中开始并在另一个 App 中结束。

[演示将图像拖入“信息”App 的视频。](https://docs-assets.developer.apple.com/published/ac27ec1cd25a9b72fb934693e5e3599a/drag-and-drop-1.mp4)

> [!note] 注意
> 在 iOS 15 之前，iPhone 上的拖放活动可以在单个 App 中进行，但不能在两个 App 之间进行。

项目被拖出的 App 是_源 App_，项目被放入的 App 是_目的地 App_。对于单个 App 内的拖放，该 App 会同时扮演这两个角色。从开始到结束、使用系统协调手势完成的整个用户操作称为_拖动活动_。相比之下，_拖动会话_是由系统管理的对象，负责管理用户正在拖动的项目。

拖动进行时，源 App 和目的地 App 会继续正常运行并支持用户交互。用户可以调出 Dock、返回主屏幕、在拆分视图（Split View）中打开第二个 App，甚至开始另一个拖动活动。

与 macOS 不同，iOS 拖放支持多个同时进行的拖动活动——数量取决于用户的手指所能处理的范围。你可以将 App 设计为允许用户依次向正在进行的拖动会话添加拖动项目，而目的地 App 可以接受多个同时进行的放置操作。

文本视图和文本栏（text field）自动支持拖放。集合视图（collection view）和表格视图（table view）提供专用的视图特有方法与属性，文本视图则提供用于自定其拖放行为的 API。你可以配置任何自定视图以支持拖放。

> [!note] 注意
> 系统会处理 iOS 中 App 间拖放的所有安全性方面。你不需要执行其他配置，例如设置特殊的 entitlement 或 `Info.plist` 键。

## 主题

### 基础

- [将拖动项目理解为承诺](understanding-a-drag-item-as-a-promise.md) — 使用拖动项目在源 App 和目的地 App 之间传递数据表示承诺。
- [使视图成为拖动源](making-a-view-into-a-drag-source.md) — 采用拖动交互 API 来提供可拖动的项目。
- [使视图成为放置目的地](making-a-view-into-a-drop-destination.md) — 采用放置交互 API，有选择地使用所拖内容。
- [在自定视图中采用拖放](adopting-drag-and-drop-in-a-custom-view.md) — 演示如何为 `UIImageView` 实例启用拖放。
- [在表格视图中采用拖放](adopting-drag-and-drop-in-a-table-view.md) — 演示如何为表格视图启用并实现拖放。

### 拖放交互

- [UIDragInteractionDelegate](uidraginteractiondelegate.md) — 用于配置和控制拖动交互的接口。
- [UIDropInteractionDelegate](uidropinteractiondelegate.md) — 用于配置和控制放置交互的接口。
- [UIDragInteraction](uidraginteraction.md) — 支持从视图拖动项目的交互，它使用委托（delegate）来提供拖动项目并响应拖动会话的调用。
- [UIDropInteraction](uidropinteraction.md) — 支持将项目放到视图上的交互，它使用委托来实例化对象并响应放置会话的调用。

### 弹簧加载交互

- [UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md) — 用于指定弹簧加载交互行为的接口。
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md) — 用于确定对象是否支持拖放活动弹簧加载交互的接口。
- [UISpringLoadedInteraction](uispringloadedinteraction.md) — 用于在拖动活动期间配置和控制由用户驱动的弹簧加载导览的交互对象。
- [UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md) — 对象为提供弹簧加载交互相关信息而实现的接口。
- [UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md) — 用于根据交互状态提供弹簧加载交互视觉样式的接口。

### 拖动源

- [UIDragItem](uidragitem.md) — 用户将底层数据项目从一个位置拖到另一个位置时，该数据项目的表示。
- [UIDragDropSession](uidragdropsession.md) — 用于查询拖动会话和放置会话状态的通用接口。
- [UIDragSession](uidragsession.md) — 用于配置拖动会话的接口。
- [UIDragAnimating](uidraganimating.md) — 用于与系统的抬起、放置和取消动画配合提供自定动画的接口。

### 放置目的地

- [UIDropSession](uidropsession.md) — 用于查询放置会话状态及其关联拖动项目的接口。
- [UIDropProposal](uidropproposal.md) — 放置交互行为的配置；如果视图接受放置活动，则需要提供此配置。
- [UIDropOperation](uidropoperation.md) — 决定用户放下拖动项目时拖放活动如何完成的操作类型。
- [UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md) — 数据从源移动到目的地时，放置会话所用的放置进度指示器样式。

### 项目提供器

- [通过拖放交付数据](data-delivery-with-drag-and-drop.md) — 使用项目提供器，在拖放操作期间于 iPad App 之间共享数据。
- [NSItemProvider](../foundation/nsitemprovider.md) — 在进程之间进行拖放或复制粘贴活动时，或者从宿主 App 向 App 扩展传递数据或文件的项目提供器。
- [NSItemProviderReading](../foundation/nsitemproviderreading.md) — 用于实现一个类，使项目提供器能够创建该类实例的协议。
- [NSItemProviderWriting](../foundation/nsitemproviderwriting.md) — 用于实现一个类，使项目提供器能够从该类的实例中检索数据的协议。
- [UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)
- [UIItemProviderReadingAugmentationDesignating](uiitemproviderreadingaugmentationdesignating.md)
- [UIItemProviderReadingAugmentationProviding](uiitemproviderreadingaugmentationproviding.md)

### 粘贴板支持

- [UIPasteConfiguration](uipasteconfiguration.md) — 对象为声明其能够接受用于粘贴和拖放活动的特定数据类型而实现的接口。
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — 用于确定响应器对象是否支持粘贴配置的接口。

### 自定拖动项目预览

- [UIDragPreviewParameters](uidragpreviewparameters.md) — 用于调整拖动项目预览或定向拖动项目预览外观的一组参数。
- [UIDragPreview](uidragpreview.md) — 单个拖动项目的图形预览，由系统在拖动开始后且没有相关动画运行时使用。
- [UIDragPreviewTarget](uidragpreviewtarget.md) — 拖动项目预览源或目的地的几何规范，由系统在用户放置项目或取消拖动活动时使用。
- [UITargetedDragPreview](uitargeteddragpreview.md) — 系统在抬起、放置或取消动画期间使用的拖动项目预览。

## 另请参阅

### 用户交互

- [触摸、按压和手势](touches-presses-and-gestures.md) — 将 App 的事件处理逻辑封装在手势识别器中，以便在整个 App 中复用这些代码。
- [菜单和快捷方式](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键简化与 App 的交互。
- [指针交互](pointer-interactions.md) — 在自定控制和视图中支持指针交互。
- [Apple Pencil 交互](apple-pencil-interactions.md) — 处理用户在 Apple Pencil 上的双击和捏合等交互。
- [基于焦点的导览](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘在 UIKit App 界面中导览。
- [UIKit 的辅助功能](accessibility-for-uikit.md) — 让使用 iOS 和 tvOS 的每个人都能顺畅使用你的 UIKit App。
