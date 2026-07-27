---
title: 在自定义文本视图中采用系统选择 UI
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-system-selection-ui-in-custom-text-views
source_url: 'https://developer.apple.com/documentation/uikit/adopting-system-selection-ui-in-custom-text-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-system-selection-ui-in-custom-text-views.json'
content_hash: 'sha256:c678c341381bfb38'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Keyboards and input](keyboards-and-input.md)

# 在自定义文本视图中采用系统选择 UI

<sub>文章</sub>

将系统文本选择体验整合到 UIKit 的自定义文本 UI 中。

## 概述

用户可以通过多种方式向你的 App 输入文本，例如键入、拷贝粘贴或听写。iOS 17 对用于插入和选择文本的系统 UI 进行了更改，以提供更流畅的文本体验。

如果你的 App 通过 [UITextView](uitextview.md) 或 [UITextField](uitextfield.md) 等标准 UIKit 视图处理文本输入，就会自动使用用于插入和选择文本的系统 UI。此系统选择 UI 包括以下元素：

- 表示文本插入点的文本光标
- 位于所选文本后方的高亮
- 用于选择文本范围的选择手柄
- 用于在大段文本中放置文本光标的放大镜

如果你使用高度自定义的 UI 显示文本，可以在 UIKit App 中采用此系统选择 UI。在大多数涉及文本选择显示和交互的情况下，请使用 [UITextInteraction](uitextinteraction.md)。它包含系统选择 UI 和标准手势识别器，让用户可以在自定义文本视图中修改选择状态。如果你想自行实现选择手势，但仍希望使用标准系统 UI 表示文本选择，请改用 [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)。本文介绍采用 [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) 的步骤。

### 向自定义文本视图添加系统选择 UI

如果你的 App 通过基于 [UITextInput](uitextinput.md) 构建的自定义文本视图处理文本输入，可以手动显示系统选择 UI。创建 [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) 交互，并将其添加到采用 [UITextInput](uitextinput.md) 的自定义文本视图。

```swift
// 设置交互。
let selectionDisplayInteraction = UITextSelectionDisplayInteraction(textInput: documentView,
                                                     delegate: self)
documentView.addInteraction(selectionDisplayInteraction)
```

当自定义文本视图变为活跃状态或成为第一响应者时，激活该交互。

```swift
// 在文本视图变为活跃状态时激活交互。
func didBecomeActive() {
    selectionDisplayInteraction.isActivated = true
}
```

### 更新文本选择

当用户与自定义文本视图中的文本交互时，请在文本选择状态发生变化时通知该交互。

```swift
// 在文本选择发生变化时通知交互。
func didChangeSelection() {
    selectionDisplayInteraction.setNeedsSelectionUpdate()
}
```

调用 [- setNeedsSelectionUpdate](<uitextselectiondisplayinteraction/setneedsselectionupdate().md>) 后，交互会从 [textInput](uitextselectiondisplayinteraction/textinput.md) 获取当前文本选择的最新信息，以便重新绘制选择 UI。

### 自定义系统选择 UI 元素

你可能希望进一步自定义系统选择 UI，使其与自定义文本视图的样式和行为相匹配。你可以自定义 [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) 的多种属性。

- [cursorView](uitextselectiondisplayinteraction/cursorview.md) 属性表示文本光标。你可以自定义文本光标闪烁动画的状态。
- [highlightView](uitextselectiondisplayinteraction/highlightview.md) 属性表示所选文本后方的高亮。你可以自定义选择区域的形状，以绘制自定义高亮。
- [handleViews](uitextselectiondisplayinteraction/handleviews.md) 属性表示用于选择文本范围的选择手柄。你可以通过定义自定义形状或指定手柄方向来自定义其外观。

### 使用文本放大镜增强文本光标放置体验

你的自定义文本视图还可以显示放大镜的系统 UI，用户可借此在大段文本中放置文本光标。当用户以你希望显示放大镜的方式与自定义文本视图交互（例如执行平移手势）时，请在 [UITextLoupeSession](uitextloupesession.md) 对象上调用 [+ beginLoupeSessionAtPoint:fromSelectionWidgetView:inView:](<uitextloupesession/begin(at_fromselectionwidgetview_in_).md>)。系统会根据你提供的起点，为放大镜的呈现和放置添加动画。当用户移动文本光标时，调用 [- moveToPoint:withCaretRect:trackingCaret:](<uitextloupesession/move(to_withcaretrect_trackingcaret_).md>) 跟踪放大镜的移动；调用 [- invalidate](<uitextloupesession/invalidate().md>) 隐藏放大镜并结束会话。

以下代码展示如何使用平移手势识别器显示放大镜。

```swift
// 使用平移手势显示放大镜。
var loupeSession: UITextLoupeSession?

func didRecognizePanGesture(_ gesture: UIPanGestureRecognizer) {
    let location = gesture.location(in: view)
    let cursorView = selectionDisplayInteraction.cursorView
    switch gesture.state {
    case .began:
        loupeSession = UITextLoupeSession.begin(at: location,
                                                fromSelectionWidgetView: cursorView,
                                                in: view)
    case .changed:
        loupeSession?.move(to: location, withCaretRect: cursorView.frame,
                           trackingCaret: true)
    case .ended, .cancelled, .failed:
        loupeSession?.invalidate()
        loupeSession = nil
    default:
        break
    }
}
```

### 隐藏系统选择 UI

当自定义文本视图变为非活跃状态或放弃第一响应者状态时，请务必停用该交互。

```swift
// 在文本视图变为非活跃状态时停用交互。
func didBecomeInactive() {
    selectionDisplayInteraction.isActivated = false
}
```

如果你在 AppKit App 中实现自定义文本 UI，请参阅[在自定义文本视图中采用系统文本光标](../appkit/adopting-the-system-text-cursor-in-custom-text-views.md)。

> [!note] WWDC23 相关场次
> 第 10058 场：[What’s new with text and text interactions](https://developer.apple.com/videos/play/wwdc2023/10058/)

## 另请参阅

### 自定义文本选择

- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — 提供用于显示文本选择的系统 UI 的对象。
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — 用于在所选文本后方提供自定义高亮 UI 的接口。
- [UITextSelectionHandleView](uitextselectionhandleview.md) — 用于为文本范围绘制自定义选择手柄的接口。
- [UITextCursorView](uitextcursorview.md) — 用于在一段文本中绘制插入点的接口。
- [UIStandardTextCursorView](uistandardtextcursorview.md) — 在一段文本中绘制标准系统插入点的视图。
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [UITextLoupeSession](uitextloupesession.md) — 管理系统放大镜在你指定位置呈现的对象。
