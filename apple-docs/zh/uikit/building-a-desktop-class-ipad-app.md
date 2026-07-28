---
title: 构建桌面级 iPad App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/building-a-desktop-class-ipad-app
source_url: 'https://developer.apple.com/documentation/uikit/building-a-desktop-class-ipad-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/building-a-desktop-class-ipad-app.json'
content_hash: 'sha256:031f848508f659f2'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 构建桌面级 iPad App

<sub>文章</sub>

针对使用台前调度进行多任务处理、文稿交互、文本编辑、搜索等场景采用桌面级增强功能，优化 iPad App 的用户体验。

## 概述

用户可以将 iPad 与妙控键盘和外接显示器搭配使用，获得桌面级生产力。构建 App 时，请充分利用能够帮助用户提高效率、自定义工作流程和更快完成任务的功能。创建桌面级 iPad App 后，可以使用 Mac Catalyst 直接将 App 移植到 Mac，几乎无需额外工作。若要将 App 带到 Apple Vision Pro，请参阅[让现有 App 与 visionOS 兼容](../visionos/making-your-app-compatible-with-visionos.md)中的详细信息。

![](../../../attachments/7f951373bc706766d41bd1db2e13acc0/media-4066536@2x.png)

<sub>一张 iPad 通过线缆连接妙控键盘和外接显示器的图像。内置屏幕和连接的屏幕都显示了使用台前调度进行多任务处理的体验。多个打开的 App 并排显示在屏幕中央，其他 App 则位于屏幕左侧，便于快速访问。</sub>

### 使用台前调度增强多任务处理体验

出色的 iPad App 会通过台前调度支持用户跨多个 App 快速执行复杂工作流程，从而提高生产力；用户可以借助台前调度快速切换到屏幕侧边其他已打开的 App 和窗口。用户还可以动态调整 App 窗口大小，在 iPad 或外接显示器上并排显示多个打开的窗口。

请按照以下步骤，通过台前调度提供出色的多任务处理体验：

- 使用场景构建 UI。场景（scene）包含用于呈现一个 UI 实例的窗口和视图控制器（view controller）。将场景作为 App 核心基础架构的一部分，并用它们在重要时刻调整 App 的行为，例如场景转入前台、更改方向或移到外接显示器时。请使用场景而不是 [UIScreen](uiscreen.md) 来确定哪个硬件显示器显示你的 UI。有关更多信息，请参阅[场景](scenes.md)。
- 使用多个 App 窗口支持各种工作流程。考虑让用户同时查看多个 App 窗口并与之交互，以支持同时查看多份文稿或将内容从 App 的一个部分快速拖放到另一部分等工作流程。使用场景支持多个 App 窗口。有关更多信息，请参阅[在 iPad 上支持多个窗口](supporting-multiple-windows-on-ipad.md)。
- 响应窗口大小调整。由于使用台前调度的用户可以动态调整 iPad App 窗口的大小，App UI 可能会在很大的尺寸范围内变化。请为灵活的布局配置设计 UI，并确保 App 能够快速、流畅地适应不同的窗口大小。使用 [UITraitCollection](uitraitcollection.md) 了解 App 的环境，并使用 Auto Layout 来适应该环境；也可以在视图控制器或视图中，使用 Swift 的 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 或 Objective-C 的 [UITraitChangeRegistration](uitraitchangeregistration.md) 注册特性（trait）变化通知。
- 考虑如何充分利用外接显示器提供的额外空间。通过角色为 [UIWindowSceneSessionRoleApplication](uiscenesession/role-swift.struct/windowapplication.md) 的场景支持可交互、可调整大小的窗口，或使用 [UIWindowSceneSessionRoleExternalDisplayNonInteractive](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) 场景呈现非交互式内容。有关更多信息，请参阅[在连接的显示器上呈现内容](presenting-content-on-a-connected-display.md)。
- 在不同设备和环境中测试 UI。考虑 UI 可能出现的各种配置和尺寸，并确保在这些条件下测试 App。例如，请在以下条件下进行测试：全屏、拆分视图、侧拉、画中画（PIP），以及将台前调度与外接显示器配合使用时在各个维度动态调整大小。

> [!note] WWDC22 相关场次
> Session 10068：[UIKit 新变化](https://developer.apple.com/wwdc22/10068)

### 支持强大的文稿编辑工作流程

基于导览的 App 支持一种专用编辑器样式，它会将重要的文稿编辑功能置于显眼位置，并支持用户自定义。基于导览的 App 还可以使用标题菜单来显示文稿管理操作、共享功能和自定义操作。

请按照以下步骤，在 iPad 上支持增强的文稿编辑功能：

- 为文稿编辑 App 切换到编辑器样式的导览。基于导览的界面可以使用 [UINavigationItemStyleEditor](uinavigationitem/itemstyle/editor.md) 样式，将 Mac 工具栏的内容密度和灵活性带到 iPad。此样式会将标题移到前缘侧，为重要控制（control）腾出更多空间，让你可以通过一次轻点快速访问常用操作。使用 [centerItemGroups](uinavigationitem/centeritemgroups.md) 指定重要控制，并使用 [customizationIdentifier](uinavigationitem/customizationidentifier.md) 让用户能够自定义这些控制的布局。
- 通过标题菜单支持文稿交互。当用户轻点文稿标题时，使用 [titleMenuProvider](uinavigationitem/titlemenuprovider.md) 显示菜单。包含移动、复制和导出等标准操作，或实现自定义操作。使用 [documentProperties](uinavigationitem/documentproperties.md) 添加菜单页眉，其中包含文稿信息和共享功能，例如共享与拖放（drag and drop）。
- 支持快速重命名文稿。实现 [renameDelegate](uinavigationitem/renamedelegate-o32h.md)，在标题菜单中显示 Rename；并在用户轻点文稿标题后，显示用于重命名文稿的内联系统 UI。

> [!note] WWDC22 相关场次
> Session 10069：[认识桌面级 iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 110343：[iPad 上的 SwiftUI：添加工具栏、标题等](https://developer.apple.com/wwdc22/110343)

### 简化文本编辑过程

用户将 iPad 与外接键盘搭配使用时，会期望 App 完整支持键盘输入，包括熟悉的键盘快捷键和交互。流畅的文本编辑体验会充分利用标准系统功能，并根据触摸或键盘输入进行调整。若要提供高效的文本编辑体验，请利用系统对文本编辑菜单以及“查找与替换”的增强功能。

请按照以下步骤，在 iPad 上提供出色的文本编辑体验：

- 为当前输入方式创建文本编辑菜单。若要创建可根据触摸或间接输入调整呈现样式、以提供最佳用户体验的编辑菜单，请参阅 [UIEditMenuInteraction](uieditmenuinteraction.md)。
- 将系统“查找与替换”体验集成到文本视图中。对于 [UITextView](uitextview.md) 或 [WKWebView](../webkit/wkwebview.md) 等标准系统文本输入视图，请将 [findInteractionEnabled](uitextview/isfindinteractionenabled.md) 设置为 [true](../swift/true.md)，让用户可以使用系统 Find 面板查找和替换文本。对于自定义文本视图实现，请参阅 [UIFindInteraction](uifindinteraction.md)。

> [!note] WWDC22 相关场次
> Session 10071：[采用桌面级编辑交互](https://developer.apple.com/wwdc22/10071)

### 支持带建议的内联搜索

iPadOS 包含内联搜索 UI，可以为周围内容腾出更多空间。利用 iPad App 中的搜索功能并提供搜索建议来改进内容发现，帮助用户更快地导览内容。

请按照以下步骤，在 iPad 上提供出色的搜索体验：

- 选择最适合 UI 的搜索体验。利用导航栏中的内联搜索位置，为内容腾出更多空间。若要明确控制搜索位置，请设置 [preferredSearchBarPlacement](uinavigationitem/preferredsearchbarplacement.md)，在内联搜索体验和传统叠放式搜索体验之间进行选择。
- 提供有用的搜索建议。在导览项目的搜索控制器上指定 [searchSuggestions](uisearchcontroller/searchsuggestions.md)，帮助用户快速缩小搜索范围。随着用户输入更新搜索建议。如果你使用独立于搜索控制器的搜索栏，请使用 [searchSuggestions](uisearchtextfield/searchsuggestions.md) 提供搜索建议。

### 提供直观的多选体验

将 iPad 与妙控键盘搭配使用的用户会期望使用触控板在 App 中执行不同类型的选择和操作。利用多选提供直观的交互，并突出最相关的上下文操作。

请按照以下步骤，在 iPad 上提供出色的多选体验：

- 使用间接输入启用轻量级多选。允许使用键盘或触控板等间接输入方式的用户在不将集合视图（collection view）置于编辑模式的情况下选择多个项目。将 [allowsMultipleSelection](uicollectionview/allowsmultipleselection.md)、[allowsFocus](uicollectionview/allowsfocus.md) 和 [selectionFollowsFocus](uicollectionview/selectionfollowsfocus.md) 设置为 [true](../swift/true.md)，以选择采用此行为。
- 区分选择与主要操作。主要操作让你能够区分一项独立的用户操作与选择变化。用户在不扩展现有选择的情况下选择单个单元格时，会发生主要操作。实现 [- collectionView:performPrimaryActionForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__performprimaryactionforitemat_).md>)，以执行导览或显示另一个拆分视图分栏等操作。
- 根据所选项目数量定制上下文菜单选项。自定义上下文菜单，使其根据选择包含零个、一个还是多个项目显示不同功能。实现 [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemsat_point_).md>)，以支持集合视图多选的上下文菜单。如果直接使用 [UIContextMenuInteraction](uicontextmenuinteraction.md)，请实现 [secondaryItemIdentifiers](uicontextmenuconfiguration/secondaryitemidentifiers.md) 以及 [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) 的预览动画方法。

> [!note] WWDC22 相关场次
> Session 10070：[构建桌面级 iPad App](https://developer.apple.com/wwdc22/10070)
>
> Session 10058：[iPad 上的 SwiftUI：组织界面](https://developer.apple.com/wwdc22/10058)

### 使用 Mac Catalyst 将 iPad App 带到 Mac

如果 iPad App 已支持桌面级体验，你可以使用 Mac Catalyst 将 App 带到 Mac。使用 Mac Catalyst 构建 iPadOS App 时，系统会将某些交互和 UI 元素桥接到 macOS 中的对应元素。

请按照以下步骤，加快使用 Mac Catalyst 将 iPad App 带到 Mac 的过程：

- 将导航栏自定义内容带到 Mac 工具栏。默认情况下，当导航栏的行为样式为 [UIBehavioralStyleMac](uibehavioralstyle/mac.md) 时，[NSToolbar](../appkit/nstoolbar.md) 会自动承载导航栏的内容。使用 [behavioralStyle](uinavigationbar/behavioralstyle.md) 检查导航栏的行为样式，并使用 [currentNSToolbarSection](uinavigationbar/currentnstoolbarsection.md) 检查工具栏在何处承载导航栏。将 [preferredBehavioralStyle](uinavigationbar/preferredbehavioralstyle.md) 设置为 [UIBehavioralStylePad](uibehavioralstyle/pad.md)，可以选择不让 [NSToolbar](../appkit/nstoolbar.md) 承载导航栏。
- 直接在 Mac 工具栏中承载自定义视图。如果你构建自己的 [NSToolbar](../appkit/nstoolbar.md)，而不使用 [UINavigationBar](uinavigationbar.md)，请创建 [NSUIViewToolbarItem](nsuiviewtoolbaritem.md)，在工具栏中承载自定义 UIKit 视图。在自定义视图中，使用 [toolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md) 特性，根据工具栏的显示模式以合适的尺寸渲染内容。

有关使用 Mac Catalyst 构建 App 的更多信息，请参阅[使用 Mac Catalyst 将 iPad App 带到 Mac](../tutorials/mac-catalyst.md)。

> [!note] WWDC22 相关场次
> Session 10076：[将 iOS App 带到 Mac](https://developer.apple.com/wwdc22/10076)

## 另请参阅

### iPad、Mac 与 Apple Vision Pro

- [使用标签页栏和边栏提升 iPad App](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md) — 提供紧凑、符合人体工程学的标签页栏，以快速访问 App 的关键部分，并提供用于深入导览的边栏。
- [在 iPad App 中支持桌面级功能](supporting-desktop-class-features-in-your-ipad-app.md) — 添加桌面级功能和文稿支持，增强 iPad App。
- [在 iPad、Mac 和 Apple Vision Pro 上进行多任务处理](multitasking-on-ipad-mac-and-apple-vision-pro.md) — 实现多任务处理 API，让 App 与 iPadOS、macOS 和 visionOS 无缝集成。
