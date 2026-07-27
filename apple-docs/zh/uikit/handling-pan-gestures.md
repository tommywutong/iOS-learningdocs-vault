---
title: 处理平移手势
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-pan-gestures
source_url: 'https://developer.apple.com/documentation/uikit/handling-pan-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-pan-gestures.json'
content_hash: 'sha256:92ed4ac217e1a3a7'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md) · [处理 UIKit 手势](handling-uikit-gestures.md)

# 处理平移手势

<sub>文章</sub>

追踪手指在屏幕上的移动，并将该移动应用到你的内容上。

## 概述

只要用户在屏幕上移动一根或多根手指，就会发生平移手势。屏幕边缘平移手势是一种特殊的平移手势，起始于屏幕边缘。使用 [UIPanGestureRecognizer](uipangesturerecognizer.md) 类处理平移手势，使用 [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) 类处理屏幕边缘平移手势。

你可以通过以下方式之一附加手势识别器：

- 以编程方式。调用你视图的 [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) 方法。
- 在 Interface Builder 中。从库中拖拽相应的对象，并将其拖放到你的视图上。

![演示单指平移手势的示意图。](../../../attachments/a55542b478cf749779ee3eecda67ba90/handling-pan-gestures-1@2x.png)

对于需要追踪用户手指在屏幕上移动的任务，使用平移手势识别器。你可以使用平移手势识别器在你的界面中拖动对象，或根据用户手指的位置更新对象的外观。平移手势是连续的，因此只要触摸信息发生变化，你的操作方法就会被调用，让你有机会更新你的内容。

一旦达到所需的初始移动量，平移手势识别器就会进入 [UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md) 状态。在这次初始变化之后，后续的变化会使手势识别器进入 [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md) 状态。当用户的手指离开屏幕时，手势识别器会进入 [UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md) 状态。

为了简化追踪过程，使用平移手势识别器的 [- translationInView:](<uipangesturerecognizer/translation(in_).md>) 方法来获取用户手指相对于初始触摸位置移动的距离。手势开始时，平移手势识别器会存储用户手指的初始接触点。（如果手势涉及多根手指，手势识别器会使用这组触摸的中心点。）每次手指移动时，[- translationInView:](<uipangesturerecognizer/translation(in_).md>) 方法都会报告相对于初始位置的距离。

以下代码展示了一个用于在屏幕上拖动视图的操作方法。手势开始时，该方法会保存视图的初始位置。随后，它会根据用户手指的移动来更新视图的位置。

```swift
var initialCenter = CGPoint()  // The initial center point of the view.
@IBAction func panPiece(_ gestureRecognizer: UIPanGestureRecognizer) {   
   guard gestureRecognizer.view != nil else { return }
   let piece = gestureRecognizer.view!
   // Get the changes in the X and Y directions relative to
   // the superview's coordinate space.
   let translation = gestureRecognizer.translation(in: piece.superview)
   if gestureRecognizer.state == .began {
      // Save the view's original position. 
      self.initialCenter = piece.center
   }
      // Update the position for the .began, .changed, and .ended states
   if gestureRecognizer.state != .cancelled {
      // Add the X and Y translation to the view's original position.
      let newCenter = CGPoint(x: initialCenter.x + translation.x, y: initialCenter.y + translation.y)
      piece.center = newCenter
   }
   else {
      // On cancellation, return the piece to its original location.
      piece.center = initialCenter
   }
}

```

如果你平移手势识别器的代码没有被调用，请检查以下条件是否成立，并按需进行修正：

- 视图的 [userInteractionEnabled](uiview/isuserinteractionenabled.md) 属性被设为 [true](../swift/true.md)。图像视图和标签默认将此属性设为 [false](../swift/false.md)。
- 触摸的数量介于 [minimumNumberOfTouches](uipangesturerecognizer/minimumnumberoftouches.md) 和 [maximumNumberOfTouches](uipangesturerecognizer/maximumnumberoftouches.md) 属性中指定的值之间。
- 对于 [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md) 对象，[edges](uiscreenedgepangesturerecognizer/edges.md) 属性已配置，且触摸从相应的边缘开始。

## 另请参阅

### 手势

- [处理点按手势](handling-tap-gestures.md) — 使用屏幕上的短促点按操作，实现与你的内容之间类似按钮的交互。
- [处理长按手势](handling-long-press-gestures.md) — 检测屏幕上持续时间较长的点按操作，并利用它们来显示与上下文相关的内容。
- [处理轻扫手势](handling-swipe-gestures.md) — 检测屏幕上的水平或垂直轻扫动作，并用它来触发对你内容的导览。
- [处理捏合手势](handling-pinch-gestures.md) — 追踪两根手指之间的距离，并利用该信息缩放你的内容。
- [处理旋转手势](handling-rotation-gestures.md) — 测量屏幕上两根手指的相对旋转角度，并利用该动作旋转你的内容。
