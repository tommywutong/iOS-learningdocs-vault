---
title: 处理轻扫手势
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-swipe-gestures
source_url: 'https://developer.apple.com/documentation/uikit/handling-swipe-gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-swipe-gestures.json'
content_hash: 'sha256:1a05766ce60bf118'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md) · [处理 UIKit 手势](handling-uikit-gestures.md)

# 处理轻扫手势

<sub>文章</sub>

检测屏幕上的水平或垂直轻扫动作，并用它来触发对你内容的导览。

## 概述

当用户在屏幕上沿特定的水平或垂直方向移动一根或多根手指时，就会发生轻扫手势。使用 [UISwipeGestureRecognizer](uiswipegesturerecognizer.md) 类来检测轻扫手势。

你可以通过以下方式之一附加手势识别器：

- 以编程方式。调用你视图的 [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>) 方法。
- 在 Interface Builder 中。从库中拖拽相应的对象，并将其拖放到你的视图上。

![演示单指水平轻扫手势的示意图。](../../../attachments/0430610b5b6b3330af7208abf27117e0/handling-swipe-gestures@2x.png)

[UISwipeGestureRecognizer](uiswipegesturerecognizer.md) 对象会追踪用户手指在屏幕上水平或垂直方向的移动。轻扫要求用户的手指朝某个特定方向移动，且不能明显偏离主要移动方向。（手势所需的方向和手指数量都是可配置的。）轻扫手势是离散的，因此只有在手势成功结束后，你的操作方法才会被调用。因此，当你只关心手势的结果、而不关心追踪用户手指移动过程时，轻扫最为适用。

> [!note] 注意
> 由于轻扫是离散的，请仅将其用于轻拂或快速平移手势，且所触发的操作要能被用户理解。轻扫不适用于交互式手势，例如交互式过渡效果。有关设计指导，请参阅[《人机界面指南》](https://developer.apple.com/design/human-interface-guidelines/inputs/touchscreen-gestures/)。

以下代码展示了一个轻扫手势识别器操作方法的基本框架。当手势被识别时，你可以使用类似这样的方法来执行某项任务。由于该手势是离散的，手势识别器不会进入开始或变化状态。

```swift
@IBAction func swipeHandler(_ gestureRecognizer : UISwipeGestureRecognizer) {
    if gestureRecognizer.state == .ended {
        // Perform action.
    }
}
```

如果你轻扫手势识别器的代码没有被调用，请检查以下条件是否成立，并按需进行修正：

- 视图的 [userInteractionEnabled](uiview/isuserinteractionenabled.md) 属性被设为 [true](../swift/true.md)。图像视图和标签默认将此属性设为 [false](../swift/false.md)。
- 触摸的数量等于 [numberOfTouchesRequired](uiswipegesturerecognizer/numberoftouchesrequired.md) 属性中指定的值。
- 轻扫的方向与 [direction](uiswipegesturerecognizer/direction-swift.property.md) 属性中的值一致。

## 另请参阅

### 手势

- [处理点按手势](handling-tap-gestures.md) — 使用屏幕上的短促点按操作，实现与你的内容之间类似按钮的交互。
- [处理长按手势](handling-long-press-gestures.md) — 检测屏幕上持续时间较长的点按操作，并利用它们来显示与上下文相关的内容。
- [处理平移手势](handling-pan-gestures.md) — 追踪手指在屏幕上的移动，并将该移动应用到你的内容上。
- [处理捏合手势](handling-pinch-gestures.md) — 追踪两根手指之间的距离，并利用该信息缩放你的内容。
- [处理旋转手势](handling-rotation-gestures.md) — 测量屏幕上两根手指的相对旋转角度，并利用该动作旋转你的内容。
