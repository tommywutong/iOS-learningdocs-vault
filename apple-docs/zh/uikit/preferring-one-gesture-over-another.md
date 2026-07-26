---
title: 优先选用某个手势而非另一个
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/preferring-one-gesture-over-another
source_url: 'https://developer.apple.com/documentation/uikit/preferring-one-gesture-over-another'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/preferring-one-gesture-over-another.json'
content_hash: 'sha256:8037e967d953af07'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Touches, presses, and gestures](touches-presses-and-gestures.md) · [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)

# 优先选用某个手势而非另一个

<sub>文章</sub>

使用手势识别器委托对象，来决定视图中各手势被识别的顺序。

## 概述

对于任何两个可能发生冲突的手势识别器，只需要其中一个拥有关联的委托对象，且该对象必须遵循 [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) 协议。在你的委托中，实现你所需要的方法以获得恰当的解决方案。了解如何使用这些方法的最佳方式是看几个示例。

下面的代码展示了如何在同一个视图中识别点按和双击手势。这个示例中的视图有两个 [UITapGestureRecognizer](uitapgesturerecognizer.md) 对象，其中一个被配置为要求两次点按。正常情况下，单击手势总是会先于双击手势被识别，但你可以使用 [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>) 方法来反转这种行为。这个方法的实现会阻止单击手势被识别，直到双击手势识别器明确进入失败状态——当触摸序列中只包含一次点按时，就会发生这种情况。

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldRequireFailureOf otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   // Don't recognize a single tap until a double-tap fails.
   if gestureRecognizer == self.tapGesture && 
          otherGestureRecognizer == self.doubleTapGesture {
      return true
   }
   return false
}
```

下面的代码展示了如何让轻扫手势先于平移手势被识别。在这个例子中，委托对象被附加到了轻扫手势识别器上，并实现了 [- gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldberequiredtofailby_).md>) 方法。这个方法的逻辑会阻止平移手势被识别，直到轻扫手势失败为止。

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   // Do not begin the pan until the swipe fails. 
   if gestureRecognizer == self.swipeGesture && 
          otherGestureRecognizer == self.panGesture {
      return true
   }
   return false
}
```

下面的代码展示了配置轻扫手势与平移手势之间依赖关系的另一种方式。这个示例没有把委托对象附加到轻扫手势上，而是把委托附加到了平移手势上。由于这一变化，该委托现在必须实现 [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>) 方法，并要求轻扫手势失败。最终结果与上一个示例相同。

```swift
func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
         shouldRequireFailureOf otherGestureRecognizer: UIGestureRecognizer) -> Bool {
   if gestureRecognizer == self.panGesture && 
          otherGestureRecognizer == self.swipeGesture {
      return true
   }
   return false
}
```

能够把委托附加到任何手势识别器上，让你可以在各个手势之间创建复杂的依赖链。有关调控手势识别的更多信息，请参阅 [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)。

## 另请参阅

### Simultaneous gestures

- [Allowing the simultaneous recognition of multiple gestures](allowing-the-simultaneous-recognition-of-multiple-gestures.md) — 了解如何使用委托对象，允许同时检测多个手势。
- [Attaching gesture recognizers to UIKit controls](attaching-gesture-recognizers-to-uikit-controls.md) — 了解手势识别器如何与按钮、切换和滑块等 UIKit 控制交互。
