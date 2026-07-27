---
title: 允许同时识别多个手势
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/allowing-the-simultaneous-recognition-of-multiple-gestures
source_url: 'https://developer.apple.com/documentation/uikit/allowing-the-simultaneous-recognition-of-multiple-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/allowing-the-simultaneous-recognition-of-multiple-gestures.json'
content_hash: 'sha256:7761022bb1674ade'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)

# 允许同时识别多个手势

<sub>文章</sub>

了解如何使用委托对象来同时检测多个手势。

## 概述

在某些情况下，允许同时识别多个手势是合理的。下图展示了一个 App，用户可以在屏幕上拖动、缩放和旋转三个视图。每个视图都维护自己的一组平移、捏合和旋转手势识别器，并且一个视图的三个手势识别器可以同时执行操作。

![](../../../attachments/8559fcb4402d0499f4e131301b8d0e58/media-2880130@2x.png)

<sub>一个 App 的屏幕截图，展示用户如何同时使用旋转、捏合和平移手势来控制粉色方块的外观。</sub>

要允许手势识别器与其他手势同时运行，请为其指定一个实现 [- gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrecognizesimultaneouslywith_).md>) 方法的委托对象。UIKit 会针对附加到同一视图的手势识别器对调用此方法。返回 `true` 会允许两个手势同时处理事件。

以下代码展示了上图 App 中的 [- gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrecognizesimultaneouslywith_).md>) 方法。当手势识别器附加到同一视图时，此方法返回 `true`。如果手势识别器附加到不同视图，或者其中一个对象是长按手势识别器，此方法会返回 `false`。

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer,
       shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer)
        -> Bool {
   // 如果手势识别器的视图不是这些方块之一，则不允许
   // 同时识别。
   if gestureRecognizer.view != self.yellowView &&
            gestureRecognizer.view != self.cyanView &&
            gestureRecognizer.view != self.magentaView {
      return false
   }
   // 如果手势识别器位于不同视图上，则不允许
   // 同时识别。
   if gestureRecognizer.view != otherGestureRecognizer.view {
      return false
   }
   // 如果任一手势识别器为长按，则不允许
   // 同时识别。
   if gestureRecognizer is UILongPressGestureRecognizer ||
          otherGestureRecognizer is UILongPressGestureRecognizer {
      return false
   }

   return true
}
```

## 另请参阅

### 同时识别手势

- [使一个手势优先于另一个手势](preferring-one-gesture-over-another.md) — 使用手势识别器委托对象来确定视图中手势的识别顺序。
- [将手势识别器附加到 UIKit 控件](attaching-gesture-recognizers-to-uikit-controls.md) — 了解手势识别器如何与按钮、开关和滑块等 UIKit 控件交互。
