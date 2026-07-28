---
title: 指针交互
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/pointer-interactions
source_url: 'https://developer.apple.com/documentation/uikit/pointer-interactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/pointer-interactions.json'
content_hash: 'sha256:5d6b80d66b6cb591'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 指针交互

<sub>API 集合</sub>

在你自定的控制和视图中支持指针交互。

## 概述

iPadOS 13.4 引入了动态指针效果和行为，提升了在 iPad 上使用触控板或鼠标等外接输入设备的体验。当用户使用输入设备时，iPadOS 会自动让指针适配当前情境，提供丰富的视觉反馈，以及恰到好处的精度，从而提升工作效率、简化常见任务。

如果你使用的是 [UIButton](uibutton.md)、[UIBarButtonItem](uibarbuttonitem.md) 或 [UISegmentedControl](uisegmentedcontrol.md)，[UIKit](../uikit.md) 会自动处理指针交互。如果你使用自定视图来显示内容，就必须自己定义指针效果和样式。

更多信息，请参阅《[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/inputs/pointing-devices/)》。

### 指定自定的指针样式

要为某个视图添加自定的指针样式效果：

1. 创建一个 [UIPointerInteraction](uipointerinteraction.md) 实例。
2. 指定该指针交互的委托（一个遵循 [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) 协议的对象）。
3. 把该交互添加到视图的 [interactions](uiview/interactions.md) 属性中。
4. 添加 [- pointerInteraction:styleForRegion:](<uipointerinteractiondelegate/pointerinteraction(__stylefor_).md>) 委托方法。
5. 从该委托方法中返回 [UIPointerStyle](uipointerstyle.md)。

下面这个示例使用了一个自定的辅助方法，你通常会在视图控制器的 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法中调用它：

```swift
func customPointerInteraction(on view: UIView, pointerInteractionDelegate: UIPointerInteractionDelegate) {
    let pointerInteraction = UIPointerInteraction(delegate: pointerInteractionDelegate)
    view.addInteraction(pointerInteraction)
}
```

当指针进入视图的区域时，会调用 [- pointerInteraction:styleForRegion:](<uipointerinteractiondelegate/pointerinteraction(__stylefor_).md>) 委托方法。下面的示例展示了一个通过返回 [UIPointerStyle](uipointerstyle.md) 对象来应用 [UIPointerLiftEffect](uipointerlifteffect.md) 效果的交互：

```swift
func pointerInteraction(_ interaction: UIPointerInteraction, styleFor region: UIPointerRegion) -> UIPointerStyle? {
    var pointerStyle: UIPointerStyle? = nil

    if let interactionView = interaction.view {
        let targetedPreview = UITargetedPreview(view: interactionView)
        pointerStyle = UIPointerStyle(effect: UIPointerEffect.lift(targetedPreview))
    }
    return pointerStyle
}
```

### 添加交互动画

在指针交互中加入动画会很有帮助，尤其是当视图中包含会干扰指针效果的元素时。例如，当指针进入 [UISegmentedControl](uisegmentedcontrol.md) 控制时隐藏其中的分隔条，可以让活动分段的效果在视觉上显得更简洁。

下面的示例执行了一个简单的动画，在指针进入和退出该区域时改变视图的 alpha 值：

```swift
func pointerInteraction(_ interaction: UIPointerInteraction, willEnter region: UIPointerRegion, animator: UIPointerInteractionAnimating) {
    if let interactionView = interaction.view {
        animator.addAnimations {
            interactionView.alpha = 0.5
        }
    }
}

func pointerInteraction(_ interaction: UIPointerInteraction, willExit region: UIPointerRegion, animator: UIPointerInteractionAnimating) {
    if let interactionView = interaction.view {
        animator.addAnimations {
            interactionView.alpha = 1.0
        }
    }
}
```

### 区分指针设备的输入事件

如果你想区分来自指针设备的触摸事件与来自其他来源（比如用户的手指或 Apple Pencil）的触摸事件，可以在 `Info.plist` 文件中启用 [UIApplicationSupportsIndirectInputEvents](../bundleresources/information-property-list/uiapplicationsupportsindirectinputevents.md) 键。启用该键后，你的 App 就可以响应针对 [UITouchTypeIndirectPointer](uitouch/touchtype/indirectpointer.md) 类型触摸的特定手势。

更多信息，请参阅 [UIApplicationSupportsIndirectInputEvents](../bundleresources/information-property-list/uiapplicationsupportsindirectinputevents.md)。

## 主题

### 基础

- [UIPointerInteraction](uipointerinteraction.md) — 一种交互，可为视图启用效果支持，或自定 App 某个区域内指针的外观。
- [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) — 一个用于处理交互所在视图内指针移动的接口。
- [Integrating pointer interactions into your iPad app](integrating-pointer-interactions-into-your-ipad-app.md) — 通过为你的视图添加指针交互，让你的 iPad App 支持触摸交互。
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md) — 通过融入指针内容效果和形状自定，为使用指针设备的用户提供出色的体验。

### Interaction animations

- [UIPointerInteractionAnimating](uipointerinteractionanimating.md) — 一个用于在指针效果动画的配合下修改交互动画的接口。

### Pointer styles

- [UIPointerStyle](uipointerstyle.md) — 一个定义指针形状和效果的对象。
- [UIPointerShape](uipointershape-swift.enum.md) — 一个定义自定指针形状的对象。
- [UIPointerEffect](uipointereffect-swift.enum.md) — 一种在指针进入当前区域时改变视图外观的效果。
- [UIPointerAccessory](uipointeraccessory.md) — 描述与主指针一同显示的附件的常量。

### Pointer region

- [UIPointerRegion](uipointerregion.md) — 一个与指针移动交互的矩形区域。
- [UIPointerRegionRequest](uipointerregionrequest.md) — 一个用于描述指针在交互所在视图中位置的对象。

### Lock state

- [UIPointerLockState](uipointerlockstate.md) — 一个包含某个场景指针锁定状态信息的对象。

### Band selection

- [UIBandSelectionInteraction](uibandselectioninteraction.md) — 一个使用基于指针的输入来跟踪多项目选择的对象。
- [State](uibandselectioninteraction/state-swift.enum.md) — 表示某个框选交互对象处于非活动状态还是正在跟踪某项交互的常量。

## 另请参阅

### 用户交互

- [Touches, presses, and gestures](touches-presses-and-gestures.md) — 把你 App 的事件处理逻辑封装到手势识别器中，以便在你的 App 中复用这些代码。
- [Menus and shortcuts](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键，简化与你 App 的交互。
- [Drag and drop](drag-and-drop.md) — 通过在你的视图中使用交互 API，为你的 App 带来拖放功能。
- [Apple Pencil interactions](apple-pencil-interactions.md) — 处理用户在 Apple Pencil 上的双击和捏握等交互。
- [Focus-based navigation](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘浏览你 UIKit App 的界面。
- [Accessibility for UIKit](accessibility-for-uikit.md) — 让使用 iOS 和 tvOS 的每一个人都能顺畅使用你的 UIKit App。
