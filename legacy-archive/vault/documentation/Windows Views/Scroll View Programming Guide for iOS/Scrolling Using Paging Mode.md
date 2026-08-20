---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/ScrollViewPagingMode/ScrollViewPagingMode.html
archived_at: '2026-07-18T02:22:54.293549Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Nesting%20Scroll%20Views.md)[上一页](Zooming%20by%20Tapping.md)

# 使用分页模式滚动

`UIScrollView` 类支持一种分页模式，它把用户发起的滚动动作限制为每次只滚动一屏内容。这种模式适用于展示连续性的内容，比如电子书或一系列操作说明。

要把 Scroll View 配置为支持分页模式，需要在 Scroll View 所属的控制器类中编写代码。

除了[创建和配置 Scroll View](Creating%20and%20Configuring%20Scroll%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnzzfvbuqmjqgewvgvzr)中描述的标准 Scroll View 初始化之外，你还必须把 `pagingMode` 属性设为 `YES`。

分页 Scroll View 的 `contentSize` 属性应设置为：高度填满整个屏幕，宽度为设备屏幕宽度乘以要显示的页数。

此外，滚动指示器应当禁用，因为用户触摸屏幕时的相对位置并不重要；或者改用 [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) 来展示位置。

图 5-1 展示了一个配置为分页模式的 Scroll View 示例。图中所示应用的实现可以在 _[PageControl: Using a Paginated UIScrollView](../../../samplecode/PageControl-%20Using%20a%20Paginated%20UIScrollView/PageControl-%20Using%20a%20Paginated%20UIScrollView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzzgu)_ 示例代码中找到。

__图 5-1__  处于分页模式的 Scroll View 以及滚动操作的结果

!

分页 Scroll View 的子视图可以用两种方式来配置。如果内容不多，你可以一次性把全部内容绘制到一个与 Scroll View 的 `contentSize` 等大的视图里。这种方式实现起来最简单，但在处理很大的内容区域，或者页面内容绘制耗时较长时，效率就不高了。

当你的应用需要显示大量页面，或者绘制页面内容比较耗时时，就应该用多个视图来显示内容，每页对应一个视图。这种方式更复杂，但能大幅提升性能，让应用能支持大得多的展示集合。_[PageControl: Using a Paginated UIScrollView](../../../samplecode/PageControl-%20Using%20a%20Paginated%20UIScrollView/PageControl-%20Using%20a%20Paginated%20UIScrollView.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzzgu)_ 这个例子就使用了多视图技术。通过研究它的示例代码，你可以清楚地看到这一技术的具体实现方式。

在分页 Scroll View 中支持大量页面，只需三个视图实例即可实现，每个视图都和设备屏幕一样大：一个显示当前页，一个显示上一页，还有一个显示下一页。当用户翻页时，这些视图会被复用。

Scroll View 的控制器初始化时，这三个视图会全部被创建和初始化。这些视图通常是 UIView 的自定义子类，不过在合适的场景下应用也可以使用 `UIImageView` 实例。随后这些视图会相对彼此定位好，这样当用户滚动时，下一页或上一页始终已就位，内容随时可供显示。控制器负责记录当前页是哪一页。

要判断何时需要因用户滚动内容而重新配置这些页面，Scroll View 需要一个实现了 `scrollViewDidScroll:` 方法的委托。这个方法的实现应当跟踪 Scroll View 的 `contentOffset`，当它越过当前视图宽度的中点时，就应该重新配置这些视图，把已经不在屏幕上可见的那个视图移到代表下一页或上一页的位置（取决于用户滚动的方向）。然后委托应当通知该视图，让它绘制与新位置相对应的内容。

采用这种技术，你就能用最少的资源显示大量内容。

如果绘制页面内容很耗时，你的应用可以往视图池中再添加一些视图，随着滚动的进行把它们放在下一页和上一页两侧的页面位置上，然后在当前内容滚动时绘制这些额外页面的内容。

[下一页](Nesting%20Scroll%20Views.md)[上一页](Zooming%20by%20Tapping.md)

