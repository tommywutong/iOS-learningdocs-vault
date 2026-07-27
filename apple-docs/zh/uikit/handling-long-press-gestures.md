---
title: 处理长按手势
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-long-press-gestures
source_url: 'https://developer.apple.com/documentation/uikit/handling-long-press-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-long-press-gestures.json'
content_hash: 'sha256:5bcf6330b03b7613'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md) · [处理 UIKit 手势](handling-uikit-gestures.md)

# 处理长按手势

<sub>文章</sub>

检测屏幕上持续时间较长的点按操作，并利用它们来显示与上下文相关的内容。

## 概述

长按（也称为按住）手势用于检测一根或多根手指（或触控笔）在屏幕上持续触摸较长时间的情况。你可以配置识别这次按压所需的最短持续时间，以及手指必须触摸屏幕的次数。（该手势识别器只由触摸的持续时间触发，与触摸所产生的压力无关。）你可以使用长按手势，在被按压的对象上发起一个操作。例如，你可以用它来显示一个与上下文相关的菜单。

你可以通过以下方式之一附加手势识别器：

- 以编程方式。调用你视图的 [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) 方法。
- 在 Interface Builder 中。从库中拖拽相应的对象，并将其拖放到你的视图上。

![展示单指长按手势的示意图。](../../../attachments/5d9ad7f706eef9c5d1408527e29cb788/handling-long-press-gestures-1@2x.png)

长按手势是连续手势，这意味着随着状态的变化，你的操作方法可能会被多次调用。当用户的手指触摸屏幕达到最短所需时间后，长按手势识别器会进入 [UIGestureRecognizerStateBegan](uigesturerecognizer/state-swift.enum/began.md) 状态。如果手指移动，或触摸发生任何其他变化，手势识别器会转入 [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md) 状态。只要手指仍处于按下状态，手势识别器就会一直保持在 [UIGestureRecognizerStateChanged](uigesturerecognizer/state-swift.enum/changed.md) 状态，即使这些手指移动到了初始视图之外。当用户的手指离开屏幕时，手势识别器会进入 [UIGestureRecognizerStateEnded](uigesturerecognizer/state-swift.enum/ended.md) 状态。

以下代码展示了一个操作方法，用于在视图顶部显示一个上下文菜单。它会在手势开始时——也就是用户的手指仍在屏幕上时——显示该上下文菜单。实现此方法的视图控制器还会将自身设置为第一响应者，以便能够响应用户选择的菜单操作。

```swift
@IBAction func showResetMenu(_ gestureRecognizer: UILongPressGestureRecognizer) {
   if gestureRecognizer.state == .began {
      self.becomeFirstResponder()
      self.viewForReset = gestureRecognizer.view

      // Configure the menu item to display
      let menuItemTitle = NSLocalizedString("Reset", comment: "Reset menu item title")
      let action = #selector(ViewController.resetPiece(controller:))
      let resetMenuItem = UIMenuItem(title: menuItemTitle, action: action)

      // Configure the shared menu controller
      let menuController = UIMenuController.shared
      menuController.menuItems = [resetMenuItem]

      // Set the location of the menu in the view.
      let location = gestureRecognizer.location(in: gestureRecognizer.view)
      let menuLocation = CGRect(x: location.x, y: location.y, width: 0, height: 0)
      menuController.setTargetRect(menuLocation, in: gestureRecognizer.view!)

      // Show the menu.
      menuController.setMenuVisible(true, animated: true)
   }
}
```

如果你长按手势识别器的代码没有被调用，请检查以下条件是否成立，并按需进行修正：

- 视图的 [userInteractionEnabled](uiview/isuserinteractionenabled.md) 属性被设为 [true](../swift/true.md)。图像视图和标签默认将此属性设为 [false](../swift/false.md)。
- 点按持续时间大于 [minimumPressDuration](uilongpressgesturerecognizer/minimumpressduration.md) 属性中指定的时间。
- 点按次数等于 [numberOfTapsRequired](uilongpressgesturerecognizer/numberoftapsrequired.md) 属性中指定的次数。
- 手指数量等于 [numberOfTouchesRequired](uilongpressgesturerecognizer/numberoftouchesrequired.md) 属性中指定的数量。

## 另请参阅

### 手势

- [处理点按手势](handling-tap-gestures.md) — 使用屏幕上的短促点按操作，实现与你的内容之间类似按钮的交互。
- [处理平移手势](handling-pan-gestures.md) — 追踪手指在屏幕上的移动，并将该移动应用到你的内容上。
- [处理轻扫手势](handling-swipe-gestures.md) — 检测屏幕上的水平或垂直轻扫动作，并用它来触发对你内容的导览。
- [处理捏合手势](handling-pinch-gestures.md) — 追踪两根手指之间的距离，并利用该信息缩放你的内容。
- [处理旋转手势](handling-rotation-gestures.md) — 测量屏幕上两根手指的相对旋转角度，并利用该动作旋转你的内容。
