---
title: 实现一个 Multi-Touch App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/implementing-a-multi-touch-app
source_url: 'https://developer.apple.com/documentation/uikit/implementing-a-multi-touch-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/implementing-a-multi-touch-app.json'
content_hash: 'sha256:758f4b1f0b8dac23'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Handling touches in your view](handling-touches-in-your-view.md)

# 实现一个 Multi-Touch App

<sub>文章</sub>

了解如何创建一个处理多点触控输入的简单 App。

## 概述

请看下图所示的 App，其中一个主视图会在每个触摸位置绘制一个灰色圆圈。触摸结束时，圆圈消失。当用户的手指移动时，底层的圆圈会随之移动。

![一个 App 的屏幕截图，该 App 会在屏幕上多个触摸点同时绘制灰色圆圈。](../../../attachments/89a7d6067ec9aaf5fca8d5ed42735fa6/implementing-a-multi-touch-app-1@2x.png)

这个 App 的创建从 Xcode 中的 Single View App 模板开始。这种类型的 App 有一个视图控制器，其视图——在本例中是一个名为 `TouchableView` 的 [UIView](uiview.md) 自定子类——铺满整个屏幕。该视图最初只包含一个标签，但 App 随后会以编程方式添加子视图。下图展示了该视图控制器的 storyboard。

![](../../../attachments/b4c436d090bae28fe81887c93d048f43/implementing-a-multi-touch-app-2@2x.png)

<sub>Interface Builder 中一个 storyboard 的屏幕截图，展示了单个视图控制器，其视图属于自定类型 TouchableView。</sub>

### 实现 TouchableView 类

`TouchableView` 类重写了继承的 [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>)、[- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>)、[- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) 和 [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) 方法。这些方法处理在每个触摸位置绘制灰色圆圈的子视图的创建和管理。具体来说，这些方法会执行以下操作：

- [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>) 方法在每个触摸事件的位置创建一个新的子视图。
- [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>) 方法更新与每个触摸关联的子视图的位置。
- [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) 和 [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) 方法移除与每个结束的触摸关联的子视图。

以下代码展示了 `TouchableView` 类及其触摸处理方法的主要实现。每个方法都会遍历触摸并执行所需的操作。`touchViews` 字典使用 [UITouch](uitouch.md) 对象作为键，来检索用户正在屏幕上操作的子视图。

```swift
class TouchableView: UIView {
   var touchViews = [UITouch:TouchSpotView]() 
 
   override init(frame: CGRect) {
      super.init(frame: frame)
      isMultipleTouchEnabled = true
   }
 
   required init?(coder aDecoder: NSCoder) {
      super.init(coder: aDecoder)
      isMultipleTouchEnabled = true
   }
 
   override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
      for touch in touches {
         createViewForTouch(touch: touch)
      }
   }
 
   override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
      for touch in touches {
         let view = viewForTouch(touch: touch) 
         // Move the view to the new location.
         let newLocation = touch.location(in: self)
         view?.center = newLocation
      }
   }
 
   override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
      for touch in touches {
         removeViewForTouch(touch: touch)
      }
   }
 
   override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
      for touch in touches {
         removeViewForTouch(touch: touch)
      }
   }
  
   // Other methods... 
}
```

几个辅助方法负责子视图的创建、管理和释放，如下面的代码所示。`createViewForTouch` 方法创建一个新的 `TouchSpotView` 对象，并将其添加到 `TouchableView` 对象中，同时以动画方式将该视图放大到完整尺寸。`removeViewForTouch` 方法移除对应的子视图，并更新类的数据结构。`viewForTouch` 方法是一个便捷方法，用于检索与给定触摸事件关联的视图。

```swift
func createViewForTouch( touch : UITouch ) {
   let newView = TouchSpotView()
   newView.bounds = CGRect(x: 0, y: 0, width: 1, height: 1)
   newView.center = touch.location(in: self)
 
   // Add the view and animate it to a new size.
   addSubview(newView)
   UIView.animate(withDuration: 0.2) {
      newView.bounds.size = CGSize(width: 100, height: 100)
   }
 
   // Save the views internally.
   touchViews[touch] = newView
}
 
func viewForTouch (touch : UITouch) -> TouchSpotView? {
   return touchViews[touch]
}
 
func removeViewForTouch (touch : UITouch ) {
   if let view = touchViews[touch] {
      view.removeFromSuperview()
      touchViews.removeValue(forKey: touch)
   }
}
```

### 实现 TouchSpotView 类

`TouchSpotView` 类（如下面的代码所示）表示在屏幕上绘制灰色圆圈的自定子视图。`TouchSpotView` 通过在每次其 [bounds](uiview/bounds.md) 属性发生变化时设置图层的 [cornerRadius](../quartzcore/calayer/cornerradius.md) 属性，来保持其圆形外观。

```swift
class TouchSpotView : UIView {
   override init(frame: CGRect) {
      super.init(frame: frame)
      backgroundColor = UIColor.lightGray
   }
 
   // Update the corner radius when the bounds change.
   override var bounds: CGRect {
      get { return super.bounds }
      set(newBounds) {
         super.bounds = newBounds
         layer.cornerRadius = newBounds.size.width / 2.0
      }
   }
}
```

## 另请参阅

### 高级触摸处理

- [使用合并触摸获得高保真度输入](getting-high-fidelity-input-with-coalesced-touches.md) — 了解如何在你的 App 中支持高精度触摸。
- [使用预测触摸最小化延迟](minimizing-latency-with-predicted-touches.md) — 使用 UIKit 对触摸位置的预测，创建流畅且响应灵敏的绘图体验。
</content>
