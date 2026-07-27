---
title: 向 tvOS App 添加用户可聚焦元素
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-user-focusable-elements-to-a-tvos-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-user-focusable-elements-to-a-tvos-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-user-focusable-elements-to-a-tvos-app.json'
content_hash: 'sha256:d8889b4f899f70d1'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Focus-based navigation](focus-based-navigation.md)

# 向 tvOS App 添加用户可聚焦元素

<sub>文章</sub>

为你的 tvOS App 创建直观、易于操作的用户交互控制。

## 概述

在 Apple TV 上，用户使用遥控器或游戏控制器在电影海报、App 或按钮等界面元素之间导览，每当移动到某个项目时都会将其高亮显示。被高亮的项目被称为「获得焦点」或「处于焦点中」。它会显得凸起，或以其他方式区别于其他项目。当用户高亮了某个项目但尚未选择它时，该项目就被视为处于焦点中。用户通过在不同的 UI 项目之间导览来移动焦点，这会触发一次焦点更新。

### 向视图添加可聚焦项目

在 Xcode 中，在资源库面板中搜索你想添加到 App 中的项目，并将其拖到 App 的故事板中。多个 UIKit 元素默认就是可聚焦的，包括按钮（[UIButton](uibutton.md)）、文本栏（[UITextField](uitextfield.md)）和表格单元格（[UITableViewCell](uitableviewcell.md)）。App 启动时，左上角的项目处于焦点中。（在从右到左书写的语言中，最初处于焦点中的是右上角的项目。）对于默认可聚焦的 UIKit 元素，你无需做任何事。不过，你可以将 SceneKit 和 SpriteKit 节点添加为可聚焦元素。要让 SceneKit 或 SpriteKit 节点变为可聚焦，将该节点的 [focusBehavior](../spritekit/sknode/focusbehavior.md) 属性设置为 `focusable`，如下所示。

```swift
node.focusBehavior = .focusable
```

### 以网格模式设计你的布局

确保焦点能够在各个可聚焦项目之间移动的最简单方法，是以网格模式排列这些项目。在遥控器上滑动会触发焦点引擎——即控制焦点和移动的系统——在滑动方向上查找所有可聚焦的项目。找到的第一个项目随即成为新的焦点项目。下图展示了用户向右滑动时焦点引擎找到的项目，以及最终获得焦点的项目。

![展示在遥控器上向右滑动结果的图像。](../../../attachments/40e8a8d70b354eaae5c29913389c254f/media-2923202@2x.png)

下图展示了用户向下滑动时焦点引擎找到的项目，以及最终获得焦点的项目。

![展示在遥控器上向下滑动结果的图像。](../../../attachments/42b84cff9a5af577e38c4344dbe5e95c/media-2923200@2x.png)

当焦点引擎在滑动方向上没有找到任何项目时，默认情况下焦点项目不会改变，如下图所示。

![展示在没有可聚焦项目的情况下向下滑动结果的图像。](../../../attachments/dd1cf54e395780106979fafdd2d05f2f/media-2923201@2x.png)

在必要时，你可以使用 [UIFocusGuide](uifocusguide.md) 将焦点重定向到用户界面中的其他可聚焦项目，从而改变默认行为。

## 另请参阅

### Focus interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和使用 Mac Catalyst 构建的 App 中，使用键盘和可获得焦点的 UI 元素在用户界面元素之间导览。
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — 为菜单和交互式用户界面布局设计并实现直观的控制方案。
- [UIFocusEnvironment](uifocusenvironment.md) — 一组用于定义视图层级结构中某个分支的焦点行为的方法。
- [UIFocusSystem](uifocussystem.md) — 查询并重新评估当前获得焦点的项目。
- [UIFocusUpdateContext](uifocusupdatecontext.md) — 一个对象，提供与从一个视图到另一个视图的特定焦点更新相关的信息。
- [UIFocusItem](uifocusitem.md) — 一个可以获得焦点的对象。
- [UIFocusMovementHint](uifocusmovementhint.md) — 为获得焦点的项目提供移动提示信息。
- [UIFocusItemContainer](uifocusitemcontainer.md) — 负责为给定焦点环境中的焦点项目提供几何上下文的容器。
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — 一种支持对可聚焦内容进行自动滚动的焦点项目容器。
- [UIFocusGroupPriority](uifocusgrouppriority.md) — 某个项目在焦点组内的重要程度，供焦点系统用来确定该组的主要项目。
</content>
