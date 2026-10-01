---
title: 关于 Apple TV 上的焦点交互
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [基于焦点的导览](focus-based-navigation.md)

# 关于 Apple TV 上的焦点交互

<sub>文章</sub>

为菜单和交互式用户界面布局设计并实现直观的控制方案。

## 概述

在 iOS 设备上，用户直接与触摸屏交互。在 Apple TV 上，则通过遥控器或其他输入设备间接控制界面。焦点（focus）指的是来自输入设备的外部、间接的用户输入在屏幕上产生的效果。当用户在界面中导览时，用户导览方向上的下一个可聚焦项会获得焦点，从而触发焦点更新。如果获得焦点的项目是可选中的，用户就用遥控器选中它。某些项目（例如标签页栏）会在短暂的延迟后自动选中。

UIKit 框架仅支持基于焦点的界面，而且大多数情况下，这一行为是自动提供的。对于带有自定用户界面组件的 App，你需要实现自定的焦点行为。

### 了解焦点引擎

[UIKit](../uikit.md) 中负责控制焦点和焦点移动的系统称为焦点引擎（focus engine）。焦点引擎会监听你的 App 中传入的焦点移动事件。事件传入时，焦点引擎会自动确定下一个可聚焦项，并通知你的 App。这带来了跨 App 一致的用户体验，为当前和未来的所有输入方式提供自动支持，并帮助开发者专注于实现 App 的独特行为，而不必定义或重新发明基础导览。

只有焦点引擎能够显式更新焦点，也就是说，不存在直接设置焦点项或沿特定方向移动焦点的 API。只有当用户发送移动事件，或者系统或 App 请求更新时，焦点引擎才会更新焦点。创建布局设计时，请牢记以下焦点行为：

**并非所有项目都可聚焦。** 如果某个项目不可聚焦，那么在确定焦点时它会被忽略。使用 [canBecomeFocused](uifocusitem/canbecomefocused.md) 属性来判断某个项目是否可聚焦。

**在任一时刻，只能有一个项目拥有焦点。**

**用户通过在遥控器上选择方向来改变焦点。** 随后 UIKit 会尝试把焦点移到该方向上的一个新的用户界面元素。如果系统在该方向上找到另一个可接受焦点的项目，被找到的项目就会获得焦点。如果在该方向上没有找到元素，则当前获得焦点的项目保持焦点，并广播一条 [UIFocusMovementDidFailNotification](uifocussystem/movementdidfailnotification.md) 通知。

**只有用户才能按方向改变焦点。** 你的 App 无法以编程方式在给定方向上搜索新的元素。虽然你可以以编程方式改变焦点，但焦点的改变方式存在限制。焦点几乎始终应由用户掌控。例如，如果表格视图（table view）的内容发生了变化，原先的焦点元素已不复存在，那么让你的 App 以编程方式选择一个新项目来获得焦点就是合理的。

**焦点由焦点环境（focus environment）管理。** 当一个焦点环境获得焦点时，它可以自己保留焦点，也可以把焦点交给它自己的某个子焦点环境。它选中的那个焦点环境就是它的偏好焦点环境（preferred focus environment）。如果选中的是某个子焦点环境，该子焦点环境同样可以选择是保留焦点，还是把焦点传给它的某个子焦点环境。这个过程不断向下深入，直到某个焦点环境自己接受焦点为止。窗口的根视图控制器也会参与焦点过程。根视图控制器的 [preferredFocusEnvironments](uifocusguide/preferredfocusenvironments.md) 属性是被选中获得焦点的第一个焦点环境。

## 另请参阅

### 焦点交互

- [使用键盘在 App 的用户界面中导览](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和以 Mac Catalyst 构建的 App 中，使用键盘和可聚焦的 UI 元素在用户界面元素之间导览。
- [向 tvOS App 添加用户可聚焦元素](adding-user-focusable-elements-to-a-tvos-app.md) — 为你的 tvOS App 创建直观且易于操作的用户交互控制。
- [UIFocusEnvironment](uifocusenvironment.md) — 定义视图层级结构中某个分支的焦点行为的一组方法。
- [UIFocusSystem](uifocussystem.md) — 查询并重新评估当前获得焦点的项目。
- [UIFocusUpdateContext](uifocusupdatecontext.md) — 提供从一个视图到另一个视图的某次特定焦点更新相关信息的对象。
- [UIFocusItem](uifocusitem.md) — 可以获得焦点的对象。
- [UIFocusMovementHint](uifocusmovementhint.md) — 为获得焦点的项目提供移动提示信息。
- [UIFocusItemContainer](uifocusitemcontainer.md) — 负责为给定焦点环境内的焦点项提供几何上下文的容器。
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — 一种焦点项容器，支持对可聚焦内容进行自动滚动。
- [UIFocusGroupPriority](uifocusgrouppriority.md) — 某个项目在焦点组内的重要性，焦点系统用它来确定该组的主要项目。
