---
title: 处理 UIKit 手势
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-uikit-gestures
source_url: 'https://developer.apple.com/documentation/uikit/handling-uikit-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-uikit-gestures.json'
content_hash: 'sha256:37569dbae67a13d2'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md)

# 处理 UIKit 手势

使用手势识别器（gesture recognizer）简化触摸处理，并创建一致的用户体验。

## 概述

手势识别器是在你的视图中处理触摸或按压事件的最简单方式。你可以把一个或多个手势识别器附加到任何视图。手势识别器封装了为该视图处理和解释传入事件、并将其与已知模式匹配所需的全部逻辑。当检测到匹配时，手势识别器会通知它所指定的目标对象——可以是视图控制器、视图本身，或你的 App 中的任何其他对象。

手势识别器使用目标-动作（target-action）设计模式来发送通知。当 [UITapGestureRecognizer](uitapgesturerecognizer.md) 对象在视图中检测到单指轻点时，它会调用视图的视图控制器的某个操作方法，由你提供响应。

![演示手势识别器如何把用户交互与你的视图控制器操作方法关联起来的示意图。](../../../attachments/e0f3c0b200ea9d469efc115be5be3dd8/handling-uikit-gestures-1@2x.png)

手势识别器分为两类：离散（discrete）与连续（continuous）。_离散手势识别器_在手势被识别后恰好调用一次你的操作方法。_连续手势识别器_在满足初始识别条件之后，会多次调用你的操作方法，每当手势事件中的信息变化时都会通知你。例如，[UIPanGestureRecognizer](uipangesturerecognizer.md) 对象会在触摸位置每次变化时调用你的操作方法。

Interface Builder 为每个标准 UIKit 手势识别器都提供了对象。它还包含一个自定义手势识别器对象，可用于表示你自定义的 [UIGestureRecognizer](uigesturerecognizer.md) 子类。

### 配置手势识别器

配置手势识别器的步骤：

1. 在你的 storyboard 中，把手势识别器拖到你的视图上。
2. 实现一个在手势被识别时要调用的操作方法；参见下面的代码。
3. 把你的操作方法连接到手势识别器。

你可以在 Interface Builder 中建立这种连接：右点手势识别器，把它的 Sent Action 选择器连接到界面中合适的对象。你也可以用编程方式，使用手势识别器的 [- addTarget:action:](<uigesturerecognizer/addtarget(__action_).md>) 方法配置操作方法。

下面的代码展示了手势识别器的操作方法的一般形式。如果你愿意，可以把参数类型改成与某个具体的手势识别器子类匹配。

**Swift**

```swift
@IBAction func myActionMethod(_ sender: UIGestureRecognizer)
```

**Objective-C**

```objc
- (IBAction)myActionMethod:(UIGestureRecognizer*)sender
```

### 响应手势

与手势识别器关联的操作方法提供了你的 App 对该手势的响应。对离散手势，你的操作方法与按钮的操作方法类似。操作方法一旦被调用，你就执行适合该手势的任何任务。对连续手势，你的操作方法既可以响应手势的识别，也可以在手势被识别之前追踪事件。追踪事件让你得以创建交互性更强的体验。例如，你可以利用 [UIPanGestureRecognizer](uipangesturerecognizer.md) 对象的更新来重新定位你的 App 中的内容。

手势识别器的 [state](uigesturerecognizer/state-swift.property.md) 属性传达该对象当前的识别状态。对连续手势，手势识别器会把该属性的值从 [UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md) 更新到 [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md)，再到 [UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md)，或更新为 [UIGestureRecognizerStateCancelled](uigesturerecognizer/state-swift.enum/cancelled.md)。你的操作方法用这个属性来决定合适的行动方案。例如，你可以用 began 和 changed 状态对内容做临时更改，用 ended 状态使这些更改永久生效，用 cancelled 状态丢弃更改。在执行任何操作之前，务必检查手势识别器的 [state](uigesturerecognizer/state-swift.property.md) 属性的值。

有关如何处理特定类型手势的示例，参见以下内容：

- [处理轻点手势](handling-tap-gestures.md)
- [处理长按手势](handling-long-press-gestures.md)
- [处理拖移手势](handling-pan-gestures.md)
- [处理轻扫手势](handling-swipe-gestures.md)
- [处理捏合手势](handling-pinch-gestures.md)
- [处理旋转手势](handling-rotation-gestures.md)

关于手势识别器状态及其如何影响你的代码的更多信息，参见[实现自定义手势识别器](implementing-a-custom-gesture-recognizer.md)。

## 主题

### 手势

- [处理轻点手势](handling-tap-gestures.md) — 利用屏幕上的短暂轻点，为你的内容实现类似按钮的交互。
- [处理长按手势](handling-long-press-gestures.md) — 检测屏幕上持续时间较长的按压，并用它们呈现与上下文相关的内容。
- [处理拖移手势](handling-pan-gestures.md) — 追踪手指在屏幕上的移动，并把该移动应用到你的内容上。
- [处理轻扫手势](handling-swipe-gestures.md) — 检测屏幕上的水平或垂直轻扫动作，并用它触发内容间的导览。
- [处理捏合手势](handling-pinch-gestures.md) — 追踪两根手指之间的距离，并用该信息缩放你的内容。
- [处理旋转手势](handling-rotation-gestures.md) — 测量两根手指在屏幕上的相对旋转，并用该动作旋转你的内容。

## 另请参阅

### 标准手势

- [协调多个手势识别器](coordinating-multiple-gesture-recognizers.md) — 了解如何在同一个视图上使用多个手势识别器。
- [为 Apple Pencil 采用悬停支持](adopting-hover-support-for-apple-pencil.md) — 通过 Apple Pencil 输入的悬停预览，增强你的 iPadOS App 的用户反馈。
- [在你的 App 中支持手势交互](supporting-gesture-interaction-in-your-apps.md) — 通过支持标准与自定义手势交互，丰富你的 App 的用户体验。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 解释视图之上指针移动的连续手势识别器。
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — 解释长按手势的连续手势识别器。
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — 解释拖移手势的连续手势识别器。
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — 解释涉及两次触摸的捏合手势的连续手势识别器。
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — 解释涉及两次触摸的旋转手势的连续手势识别器。
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — 解释从屏幕边缘附近开始的拖移手势的连续手势识别器。
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — 解释一个或多个方向轻扫手势的离散手势识别器。
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — 解释单次或多次轻点的离散手势识别器。
