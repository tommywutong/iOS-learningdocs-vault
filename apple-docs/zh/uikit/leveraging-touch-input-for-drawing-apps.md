---
title: 利用触控输入实现绘图 App
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, Xcode 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/leveraging-touch-input-for-drawing-apps
source_url: 'https://developer.apple.com/documentation/uikit/leveraging-touch-input-for-drawing-apps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/leveraging-touch-input-for-drawing-apps.json'
content_hash: 'sha256:ab6337f72aa31cff'
translated: true
---

> 导航： [技术](../technologies.md) · [UIKit](../uikit.md) · [触控、按压与手势](touches-presses-and-gestures.md)

# 利用触控输入实现绘图 App

<sub>示例代码</sub>

将触控捕获为一系列笔画，并在绘图画布上高效地渲染它们。

## 概述

此示例项目 Speed Sketch 演示了如何渲染用户通过手指或 Apple Pencil 在屏幕上移动所绘制的一系列笔画。该项目还演示了如何：

- 区分手指触控和 Apple Pencil 触控。
- 提升绘图性能。
- 针对 Apple Pencil 增强 App。

### 区分手指触控和 Apple Pencil 触控

在 Speed Sketch 中，用户可以通过手指或 Apple Pencil 在屏幕上移动来绘图，系统会将触控报告给 App。Speed Sketch 使用自定义手势识别器 `StrokeGestureRecognizer` 来捕获这些触控。

笔画手势识别器会接收每个触控事件，并将这些触控的数据追加到一个数据样本数组中。

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    if trackedTouch == nil {
        trackedTouch = touches.first
        initialTimestamp = trackedTouch?.timestamp
        collectForce = trackedTouch!.type == .pencil || view?.traitCollection.forceTouchCapability == .available
        if !isForPencil {
            // 为其他手势（例如平移和捏合）提供处理机会，
            // 方法是略微延迟 .began 状态。
            fingerStartTimer = Timer.scheduledTimer(
                withTimeInterval: cancellationTimeInterval,
                repeats: false,
                block: { [weak self] (timer) in
                    guard let strongSelf = self else { return }
                    if strongSelf.state == .possible {
                        strongSelf.state = .began
                    }
                }
            )
        }
    }
    if append(touches: touches, event: event) {
        if isForPencil {
            state = .began
        }
    }
}

override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        if state == .began {
            state = .changed
        }
    }
}

override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        stroke.state = .done
        state = .ended
    }
}

override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        stroke.state = .cancelled
        state = .failed
    }
}
```

[- touchesBegan:withEvent:](<uigesturerecognizer/touchesbegan(__with_).md>) 方法会设置一个定时器，以便为其他手势识别器（例如平移和捏合）留出时间来处理用户用手指进行的触控。这种行为是 Speed Sketch 这类绘图 App 所特有的——它们在用户触摸屏幕的那一刻就开始捕获并绘制笔画。

为了分别追踪手指和 Apple Pencil 的触控，Speed Sketch 使用了两个 `StrokeGestureRecognizer` 实例：一个用于手指触控，另一个用于追踪来自 Apple Pencil 的触控。

```swift
self.fingerStrokeRecognizer = setupStrokeGestureRecognizer(isForPencil: false)
self.pencilStrokeRecognizer = setupStrokeGestureRecognizer(isForPencil: true)
```

为了简化代码，App 使用了一个辅助方法来创建手势识别器。

```swift
func setupStrokeGestureRecognizer(isForPencil: Bool) -> StrokeGestureRecognizer {
    let recognizer = StrokeGestureRecognizer(target: self, action: #selector(strokeUpdated(_:)))
    recognizer.delegate = self
    recognizer.cancelsTouchesInView = false
    scrollView.addGestureRecognizer(recognizer)
    recognizer.coordinateSpaceView = cgView
    recognizer.isForPencil = isForPencil
    return recognizer
}
```

手势识别器通过将 [allowedTouchTypes](uigesturerecognizer/allowedtouchtypes.md) 属性设置为 [UITouchTypePencil](uitouch/touchtype/pencil.md)（追踪 Apple Pencil 触控时）或 [UITouchTypeDirect](uitouch/touchtype/direct.md)（追踪手指触控时）来区分触控类型。

```swift
var isForPencil: Bool = false {
    didSet {
        if isForPencil {
            allowedTouchTypes = [UITouch.TouchType.pencil.rawValue as NSNumber]
        } else {
            allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
        }
    }
}
```

每当用户在屏幕上绘制笔画时，笔画手势识别器都会调用 `strokeUpdate(_:)` 方法。此方法会检查识别器是否用于 Apple Pencil，如果是，则将 App 切换至 Pencil 模式。当 App 处于 Pencil 模式时，用户可以用一根手指平移绘图画布。当 App 不处于 Pencil 模式时（即用户用手指绘图时），用户需要用两根手指来平移绘图画布。

```swift
var pencilMode = false {
    didSet {
        if pencilMode {
            scrollView.panGestureRecognizer.minimumNumberOfTouches = 1
            pencilButton.isHidden = false
            if let view = fingerStrokeRecognizer.view {
                view.removeGestureRecognizer(fingerStrokeRecognizer)
            }
        } else {
            scrollView.panGestureRecognizer.minimumNumberOfTouches = 2
            pencilButton.isHidden = true
            if fingerStrokeRecognizer.view == nil {
                scrollView.addGestureRecognizer(fingerStrokeRecognizer)
            }
        }
    }
}
```

### 提升绘图性能

笔画手势识别器从系统接收触控事件。对于大多数 App 来说，每次触控事件之间的时间间隔足以处理手势。然而，绘图 App 的用户期望更高的精度，这要求 App 收集自上次传递的触控事件以来系统报告的所有触控。

为了收集额外的触控，Speed Sketch 调用了 [- coalescedTouchesForTouch:](<uievent/coalescedtouches(for_).md>) 方法。此方法返回一个 [UITouch](uitouch.md) 对象数组，代表系统已接收到但未在上次事件中传递的触控。这些额外的触控允许 Speed Sketch 将合并的触控存储为笔画数据样本的一部分，从而提供更平滑的笔画渲染。

```swift
if collectsCoalescedTouches {
    if let event = event {
        let coalescedTouches = event.coalescedTouches(for: touchToAppend)!
        let lastIndex = coalescedTouches.count - 1
        for index in 0..<lastIndex {
            saveStrokeSample(stroke: stroke, touch: coalescedTouches[index], view: view, coalesced: true, predicted: false)
        }
        saveStrokeSample(stroke: stroke, touch: coalescedTouches[lastIndex], view: view, coalesced: false, predicted: false)
    }
} else {
    saveStrokeSample(stroke: stroke, touch: touchToAppend, view: view, coalesced: false, predicted: false)
}
```

除了合并的触控之外，Speed Sketch 还使用系统预测的触控数据来增强 App 绘图能力的感知精度。Speed Sketch 通过为事件调用 [- predictedTouchesForTouch:](<uievent/predictedtouches(for_).md>) 方法来获取预测的触控，然后将这些触控保存为笔画数据样本的一部分。

```swift
if usesPredictedSamples && stroke.state == .active {
    if let predictedTouches = event?.predictedTouches(for: touchToAppend) {
        for touch in predictedTouches {
            saveStrokeSample(stroke: stroke, touch: touch, view: view, coalesced: false, predicted: true)
        }
    }
}
```

当实际的触控可用时，App 会替换掉预测的触控。

```swift
override func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>) {
    for touch in touches {
        guard let index = touch.estimationUpdateIndex else {
            continue
        }
        if let (stroke, sampleIndex) = outstandingUpdateIndexes[Int(index.intValue)] {
            var sample = stroke.samples[sampleIndex]
            let expectedUpdates = sample.estimatedPropertiesExpectingUpdates
            if expectedUpdates.contains(.force) {
                sample.force = touch.force
                if !touch.estimatedProperties.contains(.force) {
                    // 仅当新值也不是估计值时，才移除估计标记。
                    sample.estimatedProperties.remove(.force)
                }
            }
            sample.estimatedPropertiesExpectingUpdates = touch.estimatedPropertiesExpectingUpdates
            if touch.estimatedPropertiesExpectingUpdates == [] {
                outstandingUpdateIndexes.removeValue(forKey: sampleIndex)
            }
            stroke.update(sample: sample, at: sampleIndex)
        }
    }
}
```

### 针对 Apple Pencil 增强

Apple Pencil 可以感知倾斜角度（altitude）、力度（pressure）和方位角（azimuth），绘图 App 可以利用这些数据来影响笔画的外观。例如，Speed Sketch 在使用 App 的书法（Calligraphy）绘图工具时，会利用方位角来增强笔画效果。

```swift
func drawCalligraphy(in context: CGContext,
                     toSample: StrokeSample,
                     fromSample: StrokeSample,
                     forceAccessBlock: (_ sample: StrokeSample) -> CGFloat) {

    var fromAzimuthUnitVector = Stroke.calligraphyFallbackAzimuthUnitVector
    var toAzimuthUnitVector = Stroke.calligraphyFallbackAzimuthUnitVector

    if fromSample.azimuth != nil {

        if lockedAzimuthUnitVector == nil {
            lockedAzimuthUnitVector = fromSample.azimuthUnitVector
        }
        fromAzimuthUnitVector = fromSample.azimuthUnitVector
        toAzimuthUnitVector = toSample.azimuthUnitVector
        if fromSample.altitude! > azimuthLockAltitudeThreshold {
            fromAzimuthUnitVector = lockedAzimuthUnitVector!
        }
        if toSample.altitude! > azimuthLockAltitudeThreshold {
            toAzimuthUnitVector = lockedAzimuthUnitVector!
        } else {
            lockedAzimuthUnitVector = toAzimuthUnitVector
        }

    }
    // 旋转 90 度
    let calligraphyTransform = CGAffineTransform(rotationAngle: CGFloat.pi / 2.0)
    fromAzimuthUnitVector = fromAzimuthUnitVector.applying(calligraphyTransform)
    toAzimuthUnitVector = toAzimuthUnitVector.applying(calligraphyTransform)

    let fromUnitVector = fromAzimuthUnitVector * forceAccessBlock(fromSample)
    let toUnitVector = toAzimuthUnitVector * forceAccessBlock(toSample)

    context.beginPath()
    context.addLines(between: [
        fromSample.location + fromUnitVector,
        toSample.location + toUnitVector,
        toSample.location - toUnitVector,
        fromSample.location - fromUnitVector
        ])
    context.closePath()

    context.drawPath(using: .fillStroke)

}
```

当用户选择调试（Debug）绘图工具时，Speed Sketch 还会将倾斜角度和方位角数据显示为笔画的一部分。

```swift
func drawDebugMarkings(in context: CGContext, fromSample: StrokeSample) {

    let isEstimated = fromSample.estimatedProperties.contains(.azimuth)
    guard displayOptions == .debug,
        fromSample.predicted == false,
        fromSample.azimuth != nil,
        (!fromSample.coalesced || isEstimated) else {
            return
    }

    let length = CGFloat(20.0)
    let azimuthUnitVector = fromSample.azimuthUnitVector
    let azimuthTarget = fromSample.location + azimuthUnitVector * length
    let altitudeStart = azimuthTarget + (azimuthUnitVector * (length / -2.0))
    let transformToApply = CGAffineTransform(rotationAngle: fromSample.altitude!)
    let altitudeTarget = altitudeStart + (azimuthUnitVector * (length / 2.0)).applying(transformToApply)

    // 将倾斜角度绘制为从方位角中心引出的黑色线条。
    altitudeSettings(in: context)
    context.beginPath()
    context.move(to: altitudeStart)
    context.addLine(to: altitudeTarget)
    context.strokePath()

    // 将方位角绘制为蓝色线条（若为估计值则为橙色）。
    azimuthSettings(in: context)
    if isEstimated {
        context.setStrokeColor(UIColor.orange.cgColor)
    }
    context.beginPath()
    context.move(to: fromSample.location)
    context.addLine(to: azimuthTarget)
    context.strokePath()

}
```

从第二代 Apple Pencil 开始，用户可以通过在 Apple Pencil 上双击来请求 App 执行操作（有关更多信息，请参阅 [Apple Pencil 交互](apple-pencil-interactions.md)）。在可能的情况下，App 应遵循系统针对 Apple Pencil 双击操作的设置，其中包括：

- 切换到橡皮擦或上次使用的工具
- 显示调色板
- 忽略双击

Speed Sketch 没有橡皮擦工具或调色板，但它有不同的绘图工具：书法（Calligraphy）、墨迹（Ink）和调试（Debug）。当用户首选的双击操作是 [UIPencilPreferredActionSwitchPrevious](uipencilpreferredaction/switchprevious.md) 并且用户在 Apple Pencil 上双击时，Speed Sketch 会切换到用户上次使用的工具。此示例 App 会忽略其他首选操作。

```swift
func pencilInteractionDidTap(_ interaction: UIPencilInteraction) {
    if UIPencilInteraction.preferredTapAction == .switchPrevious {
        leftRingControl.switchToPreviousTool()
    }
}
```

为了让 Speed Sketch 接收双击事件，它向画布视图添加了一个 [UIPencilInteraction](uipencilinteraction.md) 对象。

```swift
let pencilInteraction = UIPencilInteraction()
pencilInteraction.delegate = self
view.addInteraction(pencilInteraction)
```

有关在绘图 App 中支持触控输入和 Apple Pencil 的更多信息，请观看 WWDC 2016 会议视频 [Leveraging Touch Input on iOS](https://developer.apple.com/videos/play/wwdc2016/220) 和 Tech Talks 会议视频 [Designing for iPad Pro and Apple Pencil](https://developer.apple.com/videos/play/tech-talks/804/)。

## 另请参阅

### 触控

- [在你的视图中处理触控](handling-touches-in-your-view.md) — 当触控处理与视图内容紧密相关时，直接在视图子类上使用触控事件。
- [处理来自 Apple Pencil 的输入](handling-input-from-apple-pencil.md) — 了解如何检测和响应来自 Apple Pencil 的触控。
- [追踪 3D Touch 事件的力度](tracking-the-force-of-3d-touch-events.md) — 根据触控力度操纵你的内容。
- [图示触控输入的力度、倾斜角度和方位角属性](illustrating-the-force-altitude-and-azimuth-properties-of-touch-input.md) — 在视图中捕获 Apple Pencil 和触控输入。
- [UITouch](uitouch.md) — 一个代表屏幕上触控的位置、大小、移动和力度的对象。

## 下载

- [LeveragingTouchInputForDrawingApps.zip](https://docs-assets.developer.apple.com/published/72f431f71f59/LeveragingTouchInputForDrawingApps.zip)
