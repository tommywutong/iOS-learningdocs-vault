---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/ScrollingViewContent/ScrollingViewContent.html
archived_at: '2026-07-18T02:22:55.205252Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Basic%20Zooming%20Using%20the%20Pinch%20Gestures.md)[上一页](Creating%20and%20Configuring%20Scroll%20Views.md)

# 滚动 Scroll View 的内容

触发 Scroll View 滚动最常见的方式，是用户直接用手指触摸屏幕并拖动。内容随之响应这个动作而滚动。这个手势称为_拖动手势（drag gesture）_。

拖动手势有一种变体，叫作_轻扫手势（flick gesture）_。轻扫手势指的是用户手指先接触屏幕，朝着想要滚动的方向快速拖动，然后离开屏幕。这个手势不仅会引发滚动，还会根据用户拖动的速度赋予内容一个动量，使得手势结束后滚动仍会继续。随后滚动会在一段指定的时间内减速。轻扫手势让用户一次操作就能移动很长的距离。在减速过程中的任意时刻，用户都可以触摸屏幕让滚动就地停止。所有这些行为都内置于 [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) 之中，开发者无需自行实现。

但有时候应用需要用代码来滚动内容，例如显示文档中某个特定的部分。这种情况下，`UIScrollView` 提供了所需的方法。

`UIScrollView` 的委托协议 [UIScrollViewDelegate](https://developer.apple.com/documentation/uikit/uiscrollviewdelegate) 提供了一些方法，让你的应用可以跟踪滚动进度，并按自身的具体需求做出相应的响应。

滚动 Scroll View 的内容并不总是由用户手指的拖动或轻扫引发的。有时候你的应用需要滚动到某个特定的内容偏移，以便露出某块特定的矩形区域，或者需要滚动到 Scroll View 的顶部。`UIScrollView` 为所有这些操作都提供了方法。

滚动到某个特定的左上角位置（即 `contentOffset` 属性）有两种方式。`setContentOffset:animated:` 方法把内容滚动到指定的内容偏移。如果 animated 参数为 `YES`，滚动会以匀速从当前位置动画过渡到指定位置。如果 animated 参数为 `NO`，滚动立即完成，不产生动画。两种情况下，委托都会收到 `scrollViewDidScroll:` 消息。如果禁用了动画，或者你直接设置 `contentOffset` 属性来改变内容偏移，委托只会收到一次 `scrollViewDidScroll:` 消息。如果启用了动画，委托会在动画进行过程中持续收到一系列 `scrollViewDidScroll:` 消息。动画结束时，委托会收到 `scrollViewDidEndScrollingAnimation:` 消息。

你也可以滚动内容，让某块矩形区域可见。当应用需要把当前处于可见区域之外的某个控件显示到可视范围内时，这一点尤其有用。`scrollRectToVisible:animated:` 方法会滚动指定的矩形，使其刚好在 Scroll View 内可见。如果 animated 参数为 `YES`，矩形会以匀速滚动进入可视范围。和 `setContentOffset:animated:` 一样，如果禁用动画，委托只收到一次 `scrollViewDidScroll:` 消息；如果启用动画，委托会随着动画推进收到一系列 `scrollViewDidScroll:` 消息。在 `scrollRectToVisible:animated:` 的情形下，Scroll View 的 tracking 和 dragging 属性也都是 `NO`。

如果为 `scrollRectToVisible:animated:` 启用了动画，委托会收到 `scrollViewDidEndScrollingAnimation:` 消息，用于通知 Scroll View 已到达指定位置且动画已完成。

如果状态栏可见，Scroll View 还可以响应用户点按状态栏而滚动到内容顶部。这种做法在以垂直方式呈现数据的应用中很常见。例如，“照片”应用就支持滚动到顶部，无论是在相簿选择的 Table View 中，还是在查看相簿内照片缩略图时；大多数 `UITableView`（`UIScrollView` 的子类）的实现也都支持滚动到顶部。

你的应用通过实现 Scroll View 的委托方法 `scrollViewShouldScrollToTop:` 并返回 `YES` 来启用这个行为。当屏幕上同时存在多个 Scroll View 时，这个委托方法通过返回要滚动的 Scroll View，让你可以精细地控制究竟哪个 Scroll View 会滚动到顶部。

滚动完成时，委托会收到 `scrollViewDidScrollToTop:` 消息，其中指明了对应的 Scroll View。

滚动发生时，Scroll View 会用 `tracking`、`dragging`、`decelerating` 和 `zooming` 这几个属性来跟踪状态。此外，`contentOffset` 属性定义了内容中显示在 Scroll View bounds 左上角的那个点。下表描述了各个状态属性：

| 状态属性 | 说明 |
| --- | --- |
| `tracking` | 如果用户的手指与设备屏幕保持接触，则为 `YES`。 |
| `dragging` | 如果用户的手指与设备屏幕保持接触并且发生了移动，则为 `YES`。 |
| `decelerating` | 如果 Scroll View 正因轻扫手势、或因拖动超出 Scroll View frame 后的回弹而减速，则为 `YES`。 |
| `zooming` | 如果 Scroll View 正在跟踪一个用于改变其 `zoomScale` 属性的捏合手势，则为 `YES`。 |
| `contentOffset` | 一个 `CGPoint` 值，定义 Scroll View bounds 的左上角。 |

你没有必要通过轮询这些属性来判断当前正在进行的操作，因为 Scroll View 会向委托发送一系列详细的消息，表明滚动动作的进展。这些方法让你的应用可以按需做出响应。委托方法内部可以查询这些状态属性，来判断收到该消息的原因，或者 Scroll View 当前处于什么位置。

如果你的应用只关心滚动过程的开始和结束，那么只需实现这些委托方法中的一小部分即可。

实现 `scrollViewWillBeginDragging:` 方法，即可收到拖动即将开始的通知。

要判断滚动何时完成，你必须实现两个委托方法：`scrollViewDidEndDragging:willDecelerate:` 和 `scrollViewDidEndDecelerating:`。滚动完成的标志是：委托收到 decelerate 参数为 `NO` 的 `scrollViewDidEndDragging:willDecelerate:` 消息，或者委托收到 `scrollViewDidEndDecelerating:` 方法。这两种情况都表示滚动已经结束。

当用户触摸屏幕时，跟踪序列就开始了。`tracking` 属性会立即被设为 `YES`，并且只要用户的手指还与屏幕接触，它就一直保持 `YES`，无论手指是否在移动。

如果用户的手指保持不动，而内容视图会响应触摸事件，那么内容视图应当处理这次触摸，序列到此结束。

但如果用户移动了手指，序列就会继续下去。

当用户开始移动手指以触发滚动时，Scroll View 首先会尝试（假定 Scroll View 使用默认值）取消任何正在进行的触摸处理——如果它正在尝试处理的话。

Scroll View 的 `dragging` 属性被设为 `YES`，其委托会收到 `scrollViewWillBeginDragging:` 消息。

随着用户拖动手指，`scrollViewDidScroll:` 消息会被发送给委托。只要滚动还在继续，这个消息就会持续发送。你在这个方法中的实现可以查询 Scroll View 的 `contentOffset` 属性，来确定 Scroll View bounds 左上角的位置。无论滚动是否正在进行，`contentOffset` 属性始终是滚动 bounds 左上角的当前位置。

如果用户做了一个轻扫手势，`tracking` 属性会被设为 `NO`，因为要完成轻扫手势，用户的手指必须在初始手势触发滚动之后离开屏幕。此时委托会收到 `scrollViewDidEndDragging:willDecelerate:` 消息。由于滚动正在减速，其中的 deceleration 参数会是 `YES`。减速速度由 `decelerationRate` 属性控制。该属性默认被设为 `UIScrollViewDecelerationRateNormal`，它允许滚动持续相当长的一段时间。你可以把速率设为 `UIScrollViewDecelerationFast`，让减速所需的时间大幅缩短，轻扫手势之后滚动的距离也会短得多。视图减速期间，Scroll View 的 `decelerating` 属性为 `YES`。

如果用户拖动、停止拖动、然后把手指从屏幕上抬起，委托会收到 `scrollViewDidEndDragging:willDecelerate:` 消息，但其中的 deceleration 参数为 `NO`。这是因为没有给 Scroll View 施加任何动量。由于用户的手指已不再接触屏幕，`tracking` 属性的值为 `NO`。

如果 `scrollViewDidEndDragging:willDecelerate:` 消息的 decelerate 参数是 `NO`，那么本次拖动动作中，Scroll View 的委托不会再收到任何委托消息。此时 Scroll View 的 decelerating 属性也会返回 `NO`。

还有另外一种情况会导致委托收到 `scrollViewDidEndDragging:willDecelerate:` 消息，即便用户抬起手指时手指是静止的。如果 Scroll View 被配置为在用户把内容拖过滚动区域边缘时提供回弹这一视觉提示，那么委托会收到 decelerate 参数为 `YES` 的 `scrollViewDidEndDragging:willDecelerate:` 消息。当 `bounces` 属性为 `YES`（默认状态）时，回弹是启用的。当 `bounces` 为 `NO` 时，`alwaysBounceVertical` 和 `alwaysBounceHorizontal` 属性不会影响 Scroll View 的行为。如果 `bounces` 为 `YES`，这两个属性能在 `contentSize` 属性值小于 Scroll View bounds 时依然允许回弹。

无论是什么情况导致 Scroll View 收到 `scrollViewDidEndDragging:willDecelerate:` 消息，只要 decelerate 参数为 `YES`，Scroll View 就会收到 `scrollViewWillBeginDecelerating:` 消息。减速期间，委托会持续收到 `scrollViewDidScroll:` 消息，尽管此时 `tracking` 和 `dragging` 的值都已是 `NO`。`decelerating` 属性则继续保持 `YES`。

最后，当 Scroll View 的减速完成时，委托会收到 `scrollViewDidEndDecelerating:` 消息，`decelerating` 属性的值变为 `NO`，整个滚动序列到此结束。

[下一页](Basic%20Zooming%20Using%20the%20Pinch%20Gestures.md)[上一页](Creating%20and%20Configuring%20Scroll%20Views.md)

