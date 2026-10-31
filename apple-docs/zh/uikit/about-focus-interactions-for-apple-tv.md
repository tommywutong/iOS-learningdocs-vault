---
title: 关于 Apple TV 的焦点交互
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/about-focus-interactions-for-apple-tv
source_url: 'https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/about-focus-interactions-for-apple-tv.json'
content_hash: 'sha256:5596df729a77616b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Focus-based navigation](focus-based-navigation.md)

# 关于 Apple TV 的焦点交互

<sub>文章</sub>

为菜单和交互式用户界面布局设计并实现直观的控制方案。

## 概述

在 iOS 设备上，用户直接与触控屏交互。在 Apple TV 上，则使用遥控器或其他输入设备间接控制界面。焦点（focus）指的是来自输入设备的外部间接用户输入在屏幕上产生的效果。当用户在界面中导览时，用户导览方向上的下一个可聚焦项目会获得焦点，从而触发焦点更新。如果获得焦点的项目是可选择的，用户可以用遥控器选择它。某些项目（例如标签页栏）会在短暂延迟后自动被选中。

UIKit 框架仅支持基于焦点的界面，并且在大多数情况下会自动提供此行为。对于具有自定用户界面组件的 App，你需要实现自定焦点行为。

### 理解焦点引擎

[UIKit](../uikit.md) 中控制焦点和焦点移动的系统称为焦点引擎（focus engine）。焦点引擎会监听你的 App 中传入的焦点移动事件。当事件到来时，焦点引擎会自动确定下一个可聚焦项目并通知你的 App。这在各个 App 之间创造一致的用户体验，为当前和未来的所有输入方法提供自动支持，并帮助开发者专注于实现其 App 的独特行为，而不是定义或重新发明基本导览。

只有焦点引擎可以显式更新焦点，这意味着没有用于直接设置获得焦点的项目或向特定方向移动焦点的 API。焦点引擎仅在用户发送移动事件，或系统或 App 请求更新时才更新焦点。在创建布局设计时请记住以下焦点行为：

**并非所有项目都可聚焦。** 如果某个项目不可聚焦，在确定焦点时会忽略它。使用 [canBecomeFocused](uifocusitem/canbecomefocused.md) 属性来判断某个项目是否可聚焦。

**在任意给定时刻，只能有一个项目获得焦点。**

**用户通过在遥控器上选择一个方向来更改焦点。** 然后 UIKit 会尝试将该方向上的新用户界面元素设为焦点。如果系统在该方向找到另一个可以接受焦点的项目，该找到的项目就会获得焦点。如果在该方向找不到元素，当前获得焦点的项目保持焦点，并广播 [UIFocusMovementDidFailNotification](uifocussystem/movementdidfailnotification.md) 通知。

**只有用户可以按方向更改焦点。** 你的 App 无法以编程方式在给定方向搜索新元素。虽然你可以以编程方式更改焦点，但对焦点如何更改存在限制。焦点几乎应始终由用户控制。例如，如果表格视图的内容发生了变化且原来的焦点元素不再存在，让你的 App 以编程方式选择一个新项目获得焦点是合理的。

**焦点由焦点环境管理。** 当焦点环境获得焦点时，它可以保留焦点，或把焦点交给其某个子焦点环境。它选择的焦点环境是其首选焦点环境。如果选择了子焦点环境，该子焦点环境也可以选择保留焦点或将其传递给其某个子焦点环境。此过程会向下钻取，直到某个焦点环境为自己接受焦点。窗口的根视图控制器也会参与焦点过程。根视图控制器的 [preferredFocusEnvironments](uifocusguide/preferredfocusenvironments.md) 属性是第一个被选中以获得焦点的焦点环境。

## 另请参阅

### 焦点交互

- [使用键盘导览 App 的用户界面](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 以及使用 Mac Catalyst 构建的 App 中，使用键盘和可聚焦的 UI 元素在用户界面元素之间导览。
- [向 tvOS App 添加用户可聚焦元素](adding-user-focusable-elements-to-a-tvos-app.md) — 为你的 tvOS App 创建直观且易于操控的用户交互控制。
- [UIFocusEnvironment](uifocusenvironment.md) — 一组定义视图层级某一分支焦点行为的方法。
- [UIFocusSystem](uifocussystem.md) — 查询并重新评估当前获得焦点的项目。
- [UIFocusUpdateContext](uifocusupdatecontext.md) — 提供与从某个视图到另一个视图的特定焦点更新相关信息的对象。
- [UIFocusItem](uifocusitem.md) — 可以获得焦点的对象。
- [UIFocusMovementHint](uifocusmovementhint.md) — 为获得焦点的项目提供移动提示信息。
- [UIFocusItemContainer](uifocusitemcontainer.md) — 负责为给定焦点环境中的焦点项目提供几何上下文的容器。
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — 一种支持可聚焦内容自动滚动的焦点项目容器类型。
- [UIFocusGroupPriority](uifocusgrouppriority.md) — 焦点组内某个项目的重要性，供焦点系统用于确定该组的主要项目。
