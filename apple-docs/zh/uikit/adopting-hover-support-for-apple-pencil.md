---
title: 采用 Apple Pencil 悬停支持
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, Xcode 14.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-hover-support-for-apple-pencil
source_url: 'https://developer.apple.com/documentation/uikit/adopting-hover-support-for-apple-pencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-hover-support-for-apple-pencil.json'
content_hash: 'sha256:7e18caabdd70e509'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md)

# 采用 Apple Pencil 悬停支持

<sub>示例代码</sub>

通过 Apple Pencil 输入的悬停预览，增强 iPadOS App 的用户反馈。

## 概述

此示例展示如何添加对 Apple Pencil 悬停手势的支持。这个 App 是一个简单的绘图工具，用户可以在空白画布上绘制笔画。当用户将 Apple Pencil 悬停在绘图画布上方不远处时，App 会使用悬停手势渲染视觉预览，显示 Apple Pencil 将在画布上的哪个位置落笔绘制。

### 配置示例代码项目

虽然示例 App 的基本功能可在模拟器中使用，但建议在实体设备上运行项目，以展示硬件的全部能力。请使用以下设备运行此项目：

- 运行 iPadOS 16.1 或更高版本的 11 英寸 iPad Pro（第 4 代）或 12.9 英寸 iPad Pro（第 6 代）
- Apple Pencil（第 2 代）

要运行示例代码项目：

- 按照[将 Apple Pencil 与 iPad 连接](https://support.apple.com/en-us/HT205236)中的说明，将 Apple Pencil 与 iPad Pro 连接。
- 使用硬件线缆将 iPad Pro 连接到 Mac。
- 在 Xcode 中打开示例代码项目。
- 在 Scheme 菜单中选择已连接的 iPad Pro。
- 运行 App，并使用 Apple Pencil 与 App 交互。

### 创建用于绘图的手势识别器

示例项目使用_长按手势识别器（long-press gesture recognizer）_通过 Apple Pencil 绘制笔画；当用户按住触摸达到最短时长时，该识别器就会作出响应。

App 实现了 `DrawGestureRecognizer` 子类，该子类扩展其超类 [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) 的能力，以跟踪 `currentTouch` 和 `currentEvent`。这些附加属性提供了实现高保真绘图所需的信息。

```swift
class DrawGestureRecognizer: UILongPressGestureRecognizer {

    weak var currentTouch: UITouch?
    weak var currentEvent: UIEvent?

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent) {
        super.touchesBegan(touches, with: event)
        currentTouch = touches.first
        currentEvent = event
    }

    override func reset() {
        super.reset()
        currentTouch = nil
        currentEvent = nil
    }
}
```

绘图实现在 `drawGesture(_:)` 方法中。在绘图手势的 [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md) 状态期间，此方法会尝试通过 [- coalescedTouchesForTouch:](<uievent/coalescedtouches(for_).md>) 获取与主要触摸 `currentTouch` 关联的其他触摸。这些额外的触摸数据可以减少延迟、提高精度，营造更流畅的绘图体验。

```swift
case .changed:
    if let drawGR = drawGestureRecognizer,
       let currentTouch = drawGR.currentTouch,
       let currentEvent = drawGR.currentEvent,
       let touches = currentEvent.coalescedTouches(for: currentTouch) {
        for touch in touches {
            let point = touch.preciseLocation(in: self)
            updatePath(point: point)
        }
    } else {
        updatePath(point: point)
    }
```

为了在画布上渲染笔画，示例会调用 `updatePath(point: CGPoint)`，该方法更新与当前笔画关联的贝塞尔路径，并将视觉输出渲染到 [`CAShapeLayer`](../quartzcore/cashapelayer.md)。

### 创建用于悬停预览的手势识别器

示例项目使用悬停手势识别器，在 Apple Pencil 落到 iPad 屏幕上之前生成笔画的视觉预览。_悬停手势识别器_会在 Apple Pencil 等指点设备的指针移动到用户界面元素上方时作出响应。当用户将 Apple Pencil 悬停在 iPad 屏幕上方不远处时，App 会生成预览。

示例项目创建 [UIHoverGestureRecognizer](uihovergesturerecognizer.md) 实例来处理悬停手势。

```swift
let hoverGesture = UIHoverGestureRecognizer(target: self, action: #selector(hoverGesture(_:)))
```

悬停预览实现在 `hoverGesture(_:)` 方法中。此方法会等待绘图手势结束后再开始渲染悬停预览。这种延迟可确保绘图和预览不会同时发生，避免在 UI 中产生重叠的视觉效果。

```swift
guard !isDrawing else { return }
```

### 更新悬停预览

示例会根据 Apple Pencil 悬停在 iPad 屏幕上方的距离，改变悬停预览效果的不透明度（即 _alpha_）。Apple Pencil 离屏幕较远时，预览 alpha 较低，视觉效果更加含蓄。Apple Pencil 更靠近屏幕时，预览 alpha 较高，视觉效果更加醒目。

示例使用以下值，在 `hoverGesture(_:)` 方法中计算预览 alpha：

- [zOffset](uihovergesturerecognizer/zoffset.md) — [UIHoverGestureRecognizer](uihovergesturerecognizer.md) 的属性，报告 Apple Pencil 与 iPad 屏幕之间当前经过归一化的距离。
- `maxPreviewZOffset` — 表示 Apple Pencil 与 iPad 屏幕之间最大距离的常量。由于 `zOffset` 已归一化，示例使用最大距离 `1.0`。
- `fadeZOffset` — 表示阈值距离的常量；预览 alpha 会在此距离切换为完全不透明或部分不透明，使视觉预览效果开始淡出。

```swift
previewAlpha = 1.0 - max(zOffset - fadeZOffset, 0.0) / (maxPreviewZOffset - fadeZOffset)
```

这行代码会计算预览 alpha。当 Apple Pencil 与屏幕的距离小于 `fadeZOffset` 时，预览 alpha 为 `1.0`，视觉效果完全不透明。当 Apple Pencil 移到比 `fadeZOffset` 更远的位置时，alpha 开始降低并最终达到 `0.0`，使视觉预览淡出并消失。

### 为不同输入类型配置不同行为

默认情况下，悬停手势不仅适用于 Apple Pencil，也适用于触控板等指点设备。例如，在连接了触控板的 iPad 上运行示例代码项目时，如果指针经过绘图画布上方，就会渲染悬停预览。不过，此示例为 Apple Pencil 和触控板提供不同的悬停体验，因此默认行为可能不适合触控板输入。

要将悬停预览限制为仅适用于 Apple Pencil 输入，并对触控板停用该功能，请取消以下代码行的注释，然后再次运行 App：

```swift
// hoverGesture.allowedTouchTypes = [ UITouch.TouchType.pencil.rawValue as NSNumber ]
```

## 另请参阅

### 标准手势

- [处理 UIKit 手势](handling-uikit-gestures.md) — 使用手势识别器简化触摸处理，并创建一致的用户体验。
- [协调多个手势识别器](coordinating-multiple-gesture-recognizers.md) — 了解如何在同一视图上使用多个手势识别器。
- [在 App 中支持手势交互](supporting-gesture-interaction-in-your-apps.md) — 通过支持标准和自定义手势交互，丰富 App 的用户体验。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 解释视图上方指针移动的连续手势识别器。
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — 解释长按手势的连续手势识别器。
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — 解释平移手势的连续手势识别器。
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — 解释涉及两个触摸点的捏合手势的连续手势识别器。
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — 解释涉及两个触摸点的旋转手势的连续手势识别器。
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — 解释从屏幕边缘附近开始的平移手势的连续手势识别器。
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — 解释一个或多个方向轻扫手势的离散手势识别器。
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — 解释单次或多次轻点的离散手势识别器。

## 下载

- [AdoptingHoverSupportForApplePencil.zip](https://docs-assets.developer.apple.com/published/adc8da922f3a/AdoptingHoverSupportForApplePencil.zip)
