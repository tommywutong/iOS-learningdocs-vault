---
title: 在你的 App 中支持手势交互
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-gesture-interaction-in-your-apps
source_url: 'https://developer.apple.com/documentation/uikit/supporting-gesture-interaction-in-your-apps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-gesture-interaction-in-your-apps.json'
content_hash: 'sha256:7e035f8267eac981'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md)

# 在你的 App 中支持手势交互

<sub>示例代码</sub>

通过支持标准和自定手势交互，丰富你 App 的用户体验。

## 概述

手势交互是 iOS 上最直观的用户体验之一，手势识别器（gesture recognizer）为 App 提供了一种简单的实现方式。iOS 定义了一些[标准手势](https://developer.apple.com/design/human-interface-guidelines/ios/user-interaction/gestures/)，App 可以使用系统提供的识别器来支持这些标准手势，也可以为非标准手势创建自定识别器。此示例演示了如何通过为三个彩色视图（示例称之为 _pieces_）添加平移、捏合和旋转支持来使用标准手势识别器，以及如何实现自定识别器，将这些视图还原到初始状态。

### 设置手势识别器

要在视图上支持手势交互，请创建适当的手势识别器，并调用 [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) 方法将其与视图关联，如下所示。

```swift
let resetGestureRecognizer = ResetGestureRecognizer(target: self, action: #selector(resetPieces(_:)))
view.addGestureRecognizer(resetGestureRecognizer)
```

Xcode 的 Objects 库包含 UIKit 的标准手势识别器，开发者可以在 Storyboard 中使用它们。要在 Storyboard 中将识别器与视图关联：

1. 在 Xcode 中选择 Storyboard，以打开 Storyboard 视图。
2. 在 Xcode 的 Objects 库中找到手势识别器。
3. 按住 Control 键，将识别器拖到视图上。

完成这些步骤后，Xcode 会自动将识别器添加到 Storyboard 并与视图关联。然后，开发者可以像对其他 UI 元素一样为识别器添加操作。

### 处理平移、捏合和旋转手势

此示例使用平移、捏合和旋转手势来移动、缩放和旋转视图。当用户平移视图时，UIKit 会触发关联的操作方法（此示例中为 `panPiece(_:)`），并传入携带平移量的 [UIPanGestureRecognizer](uipangesturerecognizer.md) 实例。该方法随后计算新位置并将视图移到那里，然后通过将平移量设为 `.zero` 来清除它，使其下次仍表示相对于当前位置的增量。

```swift
let translation = panGestureRecognizer.translation(in: piece.superview)
piece.center = CGPoint(x: piece.center.x + translation.x, y: piece.center.y + translation.y)
panGestureRecognizer.setTranslation(.zero, in: piece.superview)
```

同样，当用户捏合和旋转视图时，此示例使用 `UIPinchGestureRecognizer` 和 `UIRotationGestureRecognizer` 的 [scale](uipinchgesturerecognizer/scale.md) 和 [rotation](uirotationgesturerecognizer/rotation.md) 属性来计算并应用新的 [transform](uiview/transform.md)，然后清除这些属性。

```swift
let scale = pinchGestureRecognizer.scale
piece.transform = piece.transform.scaledBy(x: scale, y: scale)
pinchGestureRecognizer.scale = 1 // 清除缩放比例，使其下次表示正确的增量。
```

```swift
piece.transform = piece.transform.rotated(by: rotationGestureRecognizer.rotation)
rotationGestureRecognizer.rotation = 0 // 清除旋转量，使其下次表示正确的增量。
```

`scale` 和 `rotation` 属性以视图 [layer](uiview/layer.md) 的 [`anchorPoint`](../quartzcore/calayer/anchorpoint.md) 属性为基准。为了让视图缩放或旋转起来更直观，此示例会将锚点移动到手势所在位置，该位置通常是参与手势的各个触摸点的质心。

```swift
let locationInPiece = gestureRecognizer.location(in: piece)
let locationInSuperview = gestureRecognizer.location(in: piece.superview)
let anchorX = locationInPiece.x / piece.bounds.size.width
let anchorY = locationInPiece.y / piece.bounds.size.height
piece.layer.anchorPoint = CGPoint(x: anchorX, y: anchorY)
piece.center = locationInSuperview
```

### 允许同时识别多个手势

用户有时会直观地期望多个手势同时生效，例如同时捏合和旋转视图。此示例通过实现以下 [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) 方法来允许这样做。该方法返回 `true`，让此示例中的所有手势识别器都可以协同工作。

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer,
                       shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool {
    return true
}
```

为使委托（delegate）方法生效，此示例将手势识别器的 [delegate](uigesturerecognizer/delegate.md) 属性设为 `self`，也就是实现该方法的视图控制器。

```swift
resetGestureRecognizer.delegate = self
```

对于 Storyboard 中的手势识别器，此示例会按住 Control 键，将手势识别器拖到视图控制器上并选择 `delegate`，从而设置其 `delegate` 属性。

`UIGestureRecognizerDelegate` 还提供可供 App 控制手势识别顺序的方法。有关手势识别顺序的更多信息，请参阅[让一种手势优先于另一种手势](preferring-one-gesture-over-another.md)。

### 创建自定手势识别器

此示例创建了一个自定手势识别器 `ResetGestureRecognizer`，用于识别至少包含三次水平方向转折的手势。用户可以通过该手势轻松将视图还原到初始状态。为此，请先将视图移离初始位置，然后将一根手指放在彩色视图未覆盖的区域，依次向右、左、右、左移动（或反向移动），就像在屏幕上晃动手指一样。

为识别该手势，此示例在 [- touchesBegan:withEvent:](<uigesturerecognizer/touchesbegan(__with_).md>) 中获取一个有效触摸，并在 [- touchesMoved:withEvent:](<uigesturerecognizer/touchesmoved(__with_).md>) 中收集触摸位置。当用户抬起手指并触发 [- touchesEnded:withEvent:](<uigesturerecognizer/touchesended(__with_).md>) 时，此示例会计算触摸路径中的水平方向转折次数；如果路径包含两次以上转折，就将 `state` 属性设为 `.ended` 以识别该手势。

```swift
let count = countHorizontalTurning(touchedPoints: touchedPoints)
state = count > 2 ? .ended : .failed
```

请注意，此示例没有进一步消除位置噪声，也没有通过检查各线段的距离来验证线段。实际 App 可以考虑这样做，以提高手势识别准确率，并避免误识别手势。

有关自定手势识别器的更多详细信息，请参阅[实现自定手势识别器](implementing-a-custom-gesture-recognizer.md)。

## 另请参阅

### 标准手势

- [处理 UIKit 手势](handling-uikit-gestures.md) — 使用手势识别器简化触摸处理并创建一致的用户体验。
- [协调多个手势识别器](coordinating-multiple-gesture-recognizers.md) — 了解如何在同一视图上使用多个手势识别器。
- [采用 Apple Pencil 悬停支持](adopting-hover-support-for-apple-pencil.md) — 通过 Apple Pencil 输入的悬停预览，增强 iPadOS App 的用户反馈。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 解读指针在视图上方移动的连续手势识别器。
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md) — 解读长按手势的连续手势识别器。
- [UIPanGestureRecognizer](uipangesturerecognizer.md) — 解读平移手势的连续手势识别器。
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md) — 解读涉及两个触摸点的捏合手势的连续手势识别器。
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) — 解读涉及两个触摸点的旋转手势的连续手势识别器。
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) — 解读从屏幕边缘附近开始的平移手势的连续手势识别器。
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) — 解读一个或多个方向上轻扫手势的离散手势识别器。
- [UITapGestureRecognizer](uitapgesturerecognizer.md) — 解读单次或多次轻点的离散手势识别器。

## 下载

- [SupportingGestureInteractionInYourApps.zip](https://docs-assets.developer.apple.com/published/a82148190f9c/SupportingGestureInteractionInYourApps.zip)
