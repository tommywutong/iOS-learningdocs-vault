---
title: 使用键盘布局指南调整布局
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/adjusting-your-layout-with-keyboard-layout-guide
source_url: 'https://developer.apple.com/documentation/uikit/adjusting-your-layout-with-keyboard-layout-guide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adjusting-your-layout-with-keyboard-layout-guide.json'
content_hash: 'sha256:609098037ea1c30e'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [键盘与输入](keyboards-and-input.md)

# 使用键盘布局指南调整布局

<sub>示例代码</sub>

利用键盘布局指南（keyboard layout guide）的跟踪功能，动态响应键盘移动。

## 概述

当你的 App 显示键盘时，你会希望键盘与布局良好融合。此示例代码项目演示了如何在 `UIView` 的 [keyboardLayoutGuide](uiview/keyboardlayoutguide.md) 属性上将 [followsUndockedKeyboard](uikeyboardlayoutguide/followsundockedkeyboard.md) 设为 `true` 时配置约束，使布局能够适应屏幕上浮动键盘的移动。示例阐释了多项概念，例如处理键盘靠近屏幕顶部的情况，以及在其他视图没有与 `keyboardLayoutGuide` 直接相关的约束时调整布局。

使用 `keyboardLayoutGuide` 并将 `followsUndockedKeyboard` 保持为默认值 `false` 时，键盘停靠后，指南会与键盘相匹配。键盘不在屏幕上时，指南位于窗口底部，其高度等于当前 [safeAreaInsets](uiview/safeareainsets.md) 的底部 inset。默认情况下，键盘取消停靠时，指南的行为与关闭键盘或键盘不可见时相同。你可以像使用其他布局指南一样使用它。

```swift
view.keyboardLayoutGuide.topAnchor.constraint(
    equalToSystemSpacingBelow: textView.bottomAnchor, multiplier: 1.0).isActive = true
```

有关布局指南的更多信息，请参阅 [UILayoutGuide](uilayoutguide.md)。

### 跟随取消停靠的键盘

为了更精确地响应取消停靠键盘的布局变化，示例将 `followsUndockedKeyboard` 设为 `true`，然后创建跟踪约束，在键盘靠近或离开某条边缘时激活或停用这些约束。跟踪约束仅在 `followsUndockedKeyboard` 为 `true` 时适用。

```swift
// 必须进行此设置，才能让各种边缘约束生效。
view.keyboardLayoutGuide.followsUndockedKeyboard = true
```

### 启用跟踪约束

示例展示了 [UITrackingLayoutGuide](uitrackinglayoutguide.md) 如何在 `keyboardLayoutGuide` 靠近或离开某条边缘时激活或停用约束。示例代码将一组约束传给 `keyboardLayoutGuide`，并指出哪些边缘会触发变化。示例配置了一组在离开前缘和后缘时（`awayFrom`）激活的约束，因此键盘停靠或浮动键盘位于屏幕中部区域时，这些约束会被激活。相反，当浮动键盘靠近前缘或后缘时，这些约束会被停用。

> [!important] 重要
> 直接使用键盘布局指南锚点的约束不会自动激活和停用。为了获得完整的跟踪行为，示例使用 `UITrackingLayoutGuide` 的 [- setConstraints:activeWhenNearEdge:](<uitrackinglayoutguide/setconstraints(__activewhennearedge_).md>) 和 [- setConstraints:activeWhenAwayFromEdge:](<uitrackinglayoutguide/setconstraints(__activewhenawayfrom_).md>) 方法设置约束。

以下示例展示了如何在指南离开顶部边缘时（`awayFrom`），将视图固定到 `keyboardLayoutGuide` 顶部；以及在指南靠近顶部边缘时（`near`），将视图固定到其 [safeAreaLayoutGuide](uiview/safearealayoutguide.md) 的底部：

```swift
// 当键盘不靠近顶部时，将编辑视图连接到键盘布局指南
//（靠近顶部时停用）。
let editViewOnKeyboard = view.keyboardLayoutGuide.topAnchor.constraint(equalTo: editView.bottomAnchor)
editViewOnKeyboard.identifier = "editViewOnKeyboard"
view.keyboardLayoutGuide.setConstraints([editViewOnKeyboard], activeWhenAwayFrom: .top)

// 当键盘靠近顶部时，将编辑视图连接到 safeAreaLayoutGuide 的底部锚点，防止其移出屏幕。
let editViewOnBottom = view.safeAreaLayoutGuide.bottomAnchor.constraint(equalTo: editView.bottomAnchor)
editViewOnBottom.identifier = "editViewOnBottom"
view.keyboardLayoutGuide.setConstraints([editViewOnBottom], activeWhenNearEdge: .top)
```

示例表明，视图不必固定到 `keyboardLayoutGuide`，也能在键盘靠近某条边缘时影响其约束。指南可以接收布局中的任意约束数组，并在必要时激活和停用它们。例如，以下代码展示了一个本身与 `keyboardLayoutGuide` 没有约束关系的 `imageView`。当键盘四处移动时，图像会移到屏幕上键盘的另一侧，以保持可见：

```swift
let centeredImage = imageView.centerXAnchor.constraint(equalTo: view.centerXAnchor)
centeredImage.identifier = "centeredImage"
view.keyboardLayoutGuide.setConstraints([centeredImage], activeWhenAwayFrom: [.leading, .trailing])

let imageViewToLeading = imageView.leadingAnchor.constraint(
    equalToSystemSpacingAfter: view.safeAreaLayoutGuide.leadingAnchor, multiplier: 1.0)
imageViewToLeading.identifier = "imageViewToLeading"

let nearTrailingConstraints = [ editViewToUndockedKeyboardTrailing, imageViewToLeading ]
view.keyboardLayoutGuide.setConstraints(nearTrailingConstraints, activeWhenNearEdge: .trailing)

let imageViewToTrailing = view.safeAreaLayoutGuide.trailingAnchor.constraint(
    equalToSystemSpacingAfter: imageView.trailingAnchor, multiplier: 1.0)
imageViewToTrailing.identifier = "imageViewToTrailing"

let nearLeadingConstraints = [ editViewToKeyboardLeading, imageViewToTrailing ]
view.keyboardLayoutGuide.setConstraints(nearLeadingConstraints, activeWhenNearEdge: .leading)
```

### 考虑不同的键盘类型

以下列表说明了不同类型的键盘处于活跃状态时，系统会报告 `keyboardLayoutGuide` 靠近（`near`）或离开（`awayFrom`）哪些边缘：

- 停靠键盘：

    - 始终离开前缘、后缘和顶部边缘
    - 始终靠近底部边缘
- 拆分和取消停靠的键盘：

    - 始终离开前缘、后缘和底部边缘
    - 可以靠近顶部边缘
- 浮动键盘：

    - 可以离开所有边缘
    - 可以靠近任意一条边缘或任意两条相邻边缘
- 快捷栏（连接外接键盘时可用）：

    - 始终离开顶部边缘并靠近底部边缘
    - 折叠时可以靠近前缘或后缘

> [!note] 注意
> 虽然浮动键盘可以同时靠近两条相邻边缘，但键盘不支持靠近两条以上边缘的情形，而且通常只靠近一条边缘。不过，它可以离开任意边缘组合。如果浮动键盘可用但没有覆盖 App，`keyboardLayoutGuide` 的行为就如同键盘已关闭。

当 App 处于三分之一分屏浏览模式时，`keyboardLayoutGuide` 会离开前缘和后缘；键盘停靠时靠近底部边缘，浮动或取消停靠时则可以靠近顶部边缘。

### 处理边缘组合

示例展示了靠近或离开多条边缘时生效的约束。仅当键盘位置满足所有边缘要求时，系统才会激活或停用约束。由于停靠键盘会离开前缘和后缘，但靠近底部边缘，因此下例中的约束仅在键盘取消停靠并离开前缘和后缘时激活。取消停靠的全尺寸或拆分键盘，以及位于屏幕水平中部的浮动键盘都会出现这种情况。

```swift
let editCenterXToKeyboard = view.keyboardLayoutGuide.centerXAnchor.constraint(equalTo: editView.centerXAnchor)
editCenterXToKeyboard.identifier = "editCenterXToKeyboard"

view.keyboardLayoutGuide.setConstraints([editCenterXToKeyboard], activeWhenAwayFrom: [.leading, .trailing, .bottom])
```

## 另请参阅

### 键盘布局

- [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md) — 表示键盘在 App 布局中所占空间的布局指南。
- [UITrackingLayoutGuide](uitrackinglayoutguide.md) — 根据自身与边缘的接近程度自动激活和停用布局约束的布局指南。

## 下载

- [AdjustingYourLayoutWithKeyboardLayoutGuide.zip](https://docs-assets.developer.apple.com/published/51351f27fd2e/AdjustingYourLayoutWithKeyboardLayoutGuide.zip)
