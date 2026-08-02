---
title: iOS View Controller 一览
apple_id: TP40011313
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-11-15'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewControllerCatalog/Chapters/PageViewControllers.html
archived_at: '2026-07-18T02:23:21.681992Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS View Controller 一览](About%20View%20Controllers.md)


[下一页](Split%20View%20Controllers.md)[上一页](Tab%20Bar%20Controllers.md)

# Page View Controller

你用 page view controller 以逐页翻阅的方式呈现内容。page view controller 管理着一套自包含的视图层级。该层级的父视图由 page view controller 管理，子视图则由你提供的内容 View Controller 管理。

page view controller 只有一个视图，用来承载你的内容。page view controller 提供的 UI 只在用户翻页时才可见。page view controller 会给它的 View Controller 的视图施加翻页卷曲效果，营造出书页正被翻动的视觉观感。

page view controller 提供的导航是一串线性的页面序列。它非常适合呈现以线性方式访问的内容（比如小说正文），也适合呈现存在天然分页的内容（比如日历）。对于用户需要以非线性方式访问的内容（比如工具书），导航逻辑和 UI 就要由你自己提供。

图 3-1 展示了某个示例应用实现的 page view 界面。最外层的棕色视图属于父 View Controller，而不是 page view controller 本身。page view controller 自己没有 UI；不过在用户翻页时，它确实会给自己的子视图加上翻页卷曲效果。自定义内容由 page view controller 的子 View Controller 提供。

__图 3-1__  page view 界面中的各个视图

!

一个 page view 界面由以下对象组成：

- 一个可选的委托
- 一个可选的数据源
- 一个存放当前各 View Controller 的数组
- 一个手势识别器数组

__图 3-2__  page view controller 及其关联对象

!

数据源按需提供 View Controller。

委托提供了一些方法，它们会在基于手势的导航发生时以及方向改变时被调用。

View Controller 数组包含当前正在显示的内容 View Controller。这个数组里的元素个数取决于传给 page view controller 的选项。

只有设置了数据源，手势识别器数组才会被填充。这些手势识别器让用户能够通过轻点、轻扫或拖拽来翻页。

page view controller 的视图可以调整尺寸，也可以嵌入到视图层级中。这意味着，与 navigation controller 或 tab bar controller 不同，page view controller 可以用在各种各样的场合，而不只是少数几种特定情形。

Xcode 的 Page-Based Application 模板会创建一个以 page view controller 作为初始场景的新工程。

要把 page view controller 添加到已有的 storyboard 中，执行以下步骤：

1. 从库中拖出一个 page view controller。把 page view controller 场景添加到你的 storyboard 中。
2. 在 Attributes 检查器中设置合适的选项。
3. （可选）通过连接对应的 outlet 来设置委托、数据源，或者两者都设置。
4. 在 Attributes 检查器中勾选 Is Initial View Controller 选项，把它作为第一个 View Controller 显示（或者用其他方式在你的用户界面中呈现该 View Controller）。

要以编程方式创建 page view controller：

1. 用 [initWithTransitionStyle:navigationOrientation:options:](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init) 方法分配并初始化一个 page view controller。关于初始化时的定制，参见[在初始化时定制行为](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnbnknlte)。
2. （可选）设置委托、数据源，或者两者都设置。
3. 设置初始的内容 View Controller。
4. 把 page view controller 的视图呈现到屏幕上。

无论你是在 Interface Builder 中创建 page view controller 还是以编程方式创建，都需要在把它显示到屏幕上之前设置好它的初始 View Controller。

要设置初始 View Controller，调用 [setViewControllers:direction:animated:completion:](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614087-setviewcontrollers) 方法，并传入一个包含适当数量 View Controller 的数组。

你可以向 [initWithTransitionStyle:navigationOrientation:options:](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614105-init) 方法传入参数值和选项，在初始化 page view controller 时对它进行定制。初始化之后，这些设置可以通过只读属性访问。你可以定制：

- 导航发生的方向：水平或垂直
- 书脊的位置：位于任一边缘，或者位于中央
- 过渡样式：翻页卷曲或滚动

例如，清单 3-1 初始化了一个水平导航、书脊居中、采用翻页卷曲过渡的 page view controller：

__清单 3-1__  定制 page view controller

```objc
NSDictionary * options = [NSDictionary dictionaryWithObject:
            [NSNumber numberWithInt:UIPageViewControllerSpineLocationMid]
    forKey:UIPageViewControllerOptionSpineLocationKey];

UIPageViewController *pageViewController = [[UIPageViewController alloc]
    initWithTransitionStyle:UIPageViewControllerTransitionStylePageCurl
      navigationOrientation:UIPageViewControllerNavigationOrientationHorizontal
                    options:options];
```


page view controller 的委托实现 [UIPageViewControllerDelegate](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdelegate) 协议。它可以在设备方向改变时以及用户导航到新页面时执行操作，也可以在界面方向发生变化时更新书脊位置。

提供数据源就能启用手势驱动的导航。如果没有数据源，你就必须自己提供导航用的 UI，并按[通过设置当前 View Controller 来提供内容](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmjtfvbuqnbnknltc)中所述的方式提供内容。你提供的数据源必须实现 [UIPageViewControllerDataSource](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource) 协议。

数据源的方法在被调用时会收到当前显示的 View Controller，并返回排在它之前或之后的那个 View Controller。为了简化查找上一个或下一个 View Controller 的过程，你可以在自己的 View Controller 中存储额外的信息，比如页码。

如果提供了数据源，page view controller 会给自己的视图关联一组手势识别器。这些手势识别器让用户能够通过轻点、轻扫和拖拽来翻页；它们可以通过 [gestureRecognizers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614107-gesturerecognizers) 属性访问。

要把这些手势识别器移到另一个视图上，把 [gestureRecognizers](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614107-gesturerecognizers) 属性的值传给目标视图的 [addGestureRecognizer:](https://developer.apple.com/documentation/uikit/uiview/1622496-addgesturerecognizer) 方法。如果你把 page view controller 嵌入到一个更大的视图层级中，把手势识别器移到别的视图上就特别有用。

例如，如果 page view controller 没有填满整个屏幕范围，把手势识别器放到更大的父视图上，能让用户更容易发起翻页。移动手势识别器之后，用户可以在父视图范围内的任意位置开始手势，而不必局限在 page view controller 视图的范围之内。

要直接控制显示什么内容，调用 [setViewControllers:direction:animated:completion:](https://developer.apple.com/documentation/uikit/uipageviewcontroller/1614087-setviewcontrollers) 方法，传入一个要显示的内容 View Controller 数组。需要传入的 View Controller 数量视情况而定；具体细节参见该方法的参考文档。

想让用户跳转到内容中的特定位置（比如第一页或概览页），用的就是这种方式：响应用户与 UI 的交互，直接设置 View Controller。

如果你不提供数据源，就需要自己提供在页面之间移动的 UI，比如前进和后退按钮。只有在你提供了数据源时，手势驱动的导航才可用。

page view controller 把位于左侧和上方的内容理解为当前页之前的内容，把位于右侧和下方的内容理解为当前页之后的内容。这与从左到右、从上到下的内容习惯是一致的。

要用 page view controller 从数据源显示从右到左或从下到上的内容，只需把两个方法的行为反过来：

- 在你的数据源中，实现 [pageViewController:viewControllerBeforeViewController:](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614086-pageviewcontroller)，返回给定 View Controller _之后_ 的那个 View Controller。
- 在你的数据源中，实现 [pageViewController:viewControllerAfterViewController:](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/1614118-pageviewcontroller)，返回给定 View Controller _之前_ 的那个 View Controller。

对于从右到左或从上到下的内容，你通常需要把书脊位置设为 [UIPageViewControllerSpineLocationMax](https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation/max)。

[下一页](Split%20View%20Controllers.md)[上一页](Tab%20Bar%20Controllers.md)

