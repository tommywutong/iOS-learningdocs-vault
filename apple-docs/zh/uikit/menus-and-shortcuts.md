---
title: 菜单和快捷方式
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/menus-and-shortcuts
source_url: 'https://developer.apple.com/documentation/uikit/menus-and-shortcuts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/menus-and-shortcuts.json'
content_hash: 'sha256:1dc15b08c0d24e48'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 菜单和快捷方式

<sub>API 集合</sub>

使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键，简化与 App 的交互。

## 主题

### 菜单元素和键盘快捷键

- [为菜单栏和用户界面添加菜单和快捷方式](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — 通过为使用 Mac Catalyst 构建的 Mac App 添加菜单和键盘快捷键，提供对有用操作的快速访问。
- [在你的用户界面中采用菜单和 UIAction](adopting-menus-and-uiactions-in-your-user-interface.md) — 向你的用户界面添加菜单（内置按钮支持和栏按钮项），并创建自定菜单体验。
- [UIMenuElement](uimenuelement.md) — 表示菜单、操作或命令的对象。
- [UIAction](uiaction.md) — 在闭包中执行其操作的菜单元素。
- [UICommand](uicommand.md) — 在选择器中执行其操作的菜单元素。
- [UIKeyCommand](uikeycommand.md) — 指定在硬件键盘上按下的按键及相应操作的对象。
- [UIDeferredMenuElement](uideferredmenuelement.md) — 一个占位菜单元素，系统会用 block 的完成处理程序的结果替换它。
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — 决定菜单元素样式的属性。
- [State](uimenuelement/state.md) — 指示基于操作或命令的菜单元素状态的常量。
- [UIMenuLeaf](uimenuleaf.md) — 用于表示没有子元素的菜单元素的接口。

### 编辑菜单

- [UIEditMenuInteraction](uieditmenuinteraction.md) — 使用菜单提供编辑操作的交互。
- [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) — 用于自定交互所显示菜单的方法。
- [UIEditMenuConfiguration](uieditmenuconfiguration.md) — 包含你的 App 响应编辑菜单交互而呈现的菜单的配置详细信息的对象。
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — App 可采用以支持编辑的一组标准方法。

### App 菜单

- [UIMenu](uimenu.md) — 用于在 App 菜单或上下文菜单中分组相关菜单元素的容器。
- [UIMenuBuilder](uimenubuilder.md) — 用于从菜单系统中添加和移除菜单的接口。
- [UIMenuSystem](uimenusystem.md) — 表示主菜单系统或上下文菜单系统的对象。
- [UIMainMenuSystem](uimainmenusystem.md) — 主菜单系统。

### 上下文菜单

- [UIContextMenuSystem](uicontextmenusystem.md) — 上下文菜单系统。
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — 你用来为你的内容显示相关操作的交互对象。
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — 用于提供可在你的内容上执行的操作集，以及自定该内容预览的方法。
- [UITargetedPreview](uitargetedpreview.md) — 描述预览相关动画期间所用视图的对象。
- [UIPreviewTarget](uipreviewtarget.md) — 指定动画所用容器视图的对象。
- [UIPreviewParameters](uipreviewparameters.md) — 动画化预览界面时使用的附加参数。

### 查找和替换

- [UIFindInteraction](uifindinteraction.md) — 使用系统查找面板提供文本查找和替换操作的交互。
- [UIFindInteractionDelegate](uifindinteractiondelegate.md) — 一个委托（delegate）对象，提供用于管理查找交互搜索状态的会话对象，并接收搜索会话生命周期的通知。
- [UIFindSession](uifindsession.md) — 一个抽象基类，管理由查找交互发起的搜索的状态、呈现和行为。
- [UITextSearchingFindSession](uitextsearchingfindsession.md) — 一个查找会话对象，包装实现了文本搜索协议的可搜索对象。
- [UITextSearching](uitextsearching-3wkjv.md) — 你在查找会话的可搜索对象上使用这些方法来执行搜索操作并修饰找到的文本结果。
- [UITextSearchOptions](uitextsearchoptions.md) — 包含文本搜索的可配置选项的对象。
- [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) — 描述查找会话用于修饰文本的样式的常量。
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — 描述在文本中搜索与字符串匹配的单词时所用方法的常量。
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — 描述查找面板 UI 包含的结果摘要样式的常量。

### 主屏幕快速操作

- [添加主屏幕快速操作](add-home-screen-quick-actions.md) — 通过静态或动态的 3D Touch 主屏幕快速操作，暴露常用功能。
- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — 一个应用快捷项，也称为主屏幕动态快速操作，它为你的 App 指定一个由用户发起的操作。
- [UIApplicationShortcutIcon](uiapplicationshortcuticon.md) — 你可以选择与主屏幕快速操作关联的图像，以改善其外观和可用性。
- [UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md) — 一个可变的主屏幕动态快速操作，它是一个为你的 App 指定可配置的用户发起操作的项。

## 另请参阅

### 用户交互

- [触摸、按压与手势](touches-presses-and-gestures.md) — 将 App 的事件处理逻辑封装在手势识别器中，以便在整个 App 中复用这些代码。
- [拖放](drag-and-drop.md) — 通过在视图中使用交互 API，为 App 添加拖放功能。
- [指针交互](pointer-interactions.md) — 在自定控制和视图中支持指针交互。
- [Apple Pencil 交互](apple-pencil-interactions.md) — 处理用户在 Apple Pencil 上的双击和捏合等交互。
- [基于焦点的导览](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘在 UIKit App 界面中导览。
- [UIKit 的辅助功能](accessibility-for-uikit.md) — 让使用 iOS 和 tvOS 的每个人都能顺畅使用你的 UIKit App。
