---
title: 在 App 中实现合并触摸支持
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/implementing-coalesced-touch-support-in-an-app
source_url: 'https://developer.apple.com/documentation/uikit/implementing-coalesced-touch-support-in-an-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/implementing-coalesced-touch-support-in-an-app.json'
content_hash: 'sha256:e40c9bc888c2f649'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Handling touches in your view](handling-touches-in-your-view.md) · [Getting high-fidelity input with coalesced touches](getting-high-fidelity-input-with-coalesced-touches.md)

# 在 App 中实现合并触摸支持

<sub>文章</sub>

了解如何创建一个处理合并触摸的简单 App。

## 概述

下图展示了一个简单的绘图 App，它捕获触摸并在屏幕上渲染生成的路径。该 App 会跟踪 UIKit 报告的所有触摸，包括合并触摸。App 通过在一个触摸点到下一个触摸点之间绘制线段来构建路径。

![一个使用合并触摸实现高精度绘图的 App 的屏幕截图。](../../../attachments/0d0f7d0937372b87523f55052d4c2ade/implementing-coalesced-touch-support-in-an-app-1@2x.png)

### 为触摸提供存储

App 的主视图使用传入的触摸事件来构建一组 `Stroke` 对象。下图展示了 `Stroke` 类及相关的 `StrokeSample` 类的定义，它们存储了每个触摸事件的信息。

```swift
class Stroke {
    var samples = [StrokeSample]()
    func add(sample: StrokeSample) {
        samples.append(sample)
    }
}
 
struct StrokeSample {
    let location: CGPoint
    let coalescedSample: Bool
    init(point: CGPoint, coalesced : Bool = false) {
        location = point
        coalescedSample = coalesced
    }
}

```

主视图维护一个由 `StrokeCollection` 类创建的 `Stroke` 对象集合，其实现如下面的代码所示。这个类的 `strokes` 属性存储已完成的笔画，`activeStroke` 属性则包含当前正在被修改的笔画对象。调用 `acceptActiveStroke` 方法会将活动笔画移入已完成笔画的集合中。

```swift
class StrokeCollection {
    var strokes = [Stroke]()
    var activeStroke: Stroke? = nil
 
    func acceptActiveStroke() {
        if let stroke = activeStroke {
            strokes.append(stroke)
            activeStroke = nil
        }
    }
}
```

### 获取合并触摸

以下代码展示了主绘图视图中创建新 `Stroke` 对象的部分。该视图不支持多点触控，因此只需要跟踪第一个触摸事件。[- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>) 方法创建一个新的笔画对象，并将其标记为活动笔画。新的触摸数据会被添加到活动笔画中，直到调用 [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) 方法，此时该笔画会被接受进入笔画集合。如果触摸序列因任何原因被中断，[- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) 方法会放弃当前活动的笔画。

```swift
class DrawingView : UIView {
   var strokeCollection: StrokeCollection? {
      didSet {
         // If the strokes change, redraw the view's content.
         if oldValue !== strokeCollection {
            setNeedsDisplay()
         }
      }
   }
 
   // Initialization methods...
 
   // Touch Handling methods
   override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
      // Create a new stroke and make it the active stroke.
      let newStroke = Stroke()
      strokeCollection?.activeStroke = newStroke
 
      // The view does not support multitouch, so get the samples
      //  for only the first touch in the event.
      if let coalesced = event?.coalescedTouches(for: touches.first!) {
         addSamples(for: coalesced)
      }
   }
 
   override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
      if let coalesced = event?.coalescedTouches(for: touches.first!) {
         addSamples(for: coalesced)
      }
   }
 
   override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
      // Accept the current stroke and add it to the stroke collection.
      if let coalesced = event?.coalescedTouches(for: touches.first!) {
         addSamples(for: coalesced)
      }
      // Accept the active stroke.
      strokeCollection?.acceptActiveStroke()
   }
 
   override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
      // Clear the last stroke.
      strokeCollection?.activeStroke = nil
   }
 
   // More methods...
}
```

`DrawingView` 的触摸输入方法使用 `addSamples` 方法（如下面的代码所示）将新触摸纳入活动笔画。这个方法为每个触摸点创建一个新的 `StrokeSample`，并将该样本添加到活动笔画中。这个示例在内部标记了合并触摸，但这些触摸与系统报告的常规触摸并无不同。

```swift
func addSamples(for touches: [UITouch]) {
   if let stroke = strokeCollection?.activeStroke {
      // Add all of the touches to the active stroke.
      for touch in touches {
         if touch == touches.last {
            let sample = StrokeSample(point: touch.preciseLocation(in: self))
            stroke.add(sample: sample)
         } else {
            // If the touch is not the last one in the array,
            //  it was a coalesced touch. 
            let sample = StrokeSample(point: touch.preciseLocation(in: self), 
                                  coalesced: true)
            stroke.add(sample: sample)
         }
      } 
      // Update the view.
      self.setNeedsDisplay()
   }
}
```

> [!note] 注意
> 在从 Apple Pencil 捕获绘图输入时，你可以使用 [- preciseLocationInView:](<uitouch/preciselocation(in_).md>) 方法而不是 [- locationInView:](<uitouch/location(in_)-8rd36.md>) 方法来获得更精确的触摸信息。只在捕获与绘图相关的输入时使用 [- preciseLocationInView:](<uitouch/preciselocation(in_).md>) 方法。对于与你界面的一般交互，请继续使用 [- locationInView:](<uitouch/location(in_)-8rd36.md>) 方法获取触摸位置。

`DrawingView` 类的其余方法负责将触摸样本转换为渲染输出。App 的「清除」按钮会释放该视图当前的 `StrokeCollection` 对象并创建一个新对象。
</content>
