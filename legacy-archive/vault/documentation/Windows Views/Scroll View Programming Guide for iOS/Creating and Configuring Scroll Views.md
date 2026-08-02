---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/CreatingBasicScrollViews/CreatingBasicScrollViews.html
archived_at: '2026-07-18T02:22:48.507946Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Scrolling%20the%20Scroll%20View%20Content.md)[上一页](About%20Scroll%20View%20Programming.md)

# 创建和配置 Scroll View

Scroll View 的创建方式和其他视图一样，既可以用代码创建，也可以在 Interface Builder 中创建。只需少量额外配置，就能获得基本的滚动能力。

Scroll View 像其他视图一样被创建并插入到控制器或视图层级中。要完成 Scroll View 的配置，只需再多做两步：

1. 你必须把 `contentSize` 属性设为可滚动内容的尺寸。它指定了可滚动区域的大小。
2. 你还必须添加一个或多个由 Scroll View 显示和滚动的视图。这些视图提供实际展示的内容。

此外，你还可以按应用需要配置各种视觉提示——垂直和水平滚动指示器、拖动回弹、缩放回弹，以及滚动方向的限制

要在 Interface Builder 中创建 Scroll View，请把 Library 面板中 __Library->Cocoa Touch->Data Views__ 一节里的 `UIScrollView` 图标拖到视图“窗口”中。然后把 [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) 子类的 view 输出口连接到该 Scroll View。图 1-1 展示了这个连接，其中假定 File's Owner 就是那个 `UIViewController` 子类（这是一种常见的设计模式）。

__图 1-1__  `UIViewController` 子类如何连接到 Scroll View

!

尽管 Interface Builder 中的 `UIScrollView` 检查器允许你设置 Scroll View 实例的许多属性，但你仍然需要在应用代码中设置 `contentSize` 属性，它定义了可滚动区域的大小。如果你把 Scroll View 连接到了某个控制器实例（通常是 File's Owner）的 `view` 属性，那么 [contentSize](https://developer.apple.com/documentation/uikit/uiscrollview/1619399-contentsize) 属性的初始化就应放在控制器的 [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) 方法中，如清单 1-1 所示。

__清单 1-1__  设置 Scroll View 的尺寸

```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    UIScrollView *tempScrollView=(UIScrollView *)self.view;
    tempScrollView.contentSize=CGSizeMake(1280,960);
}
```

配置好 Scroll View 的尺寸之后，你的应用就可以添加提供视图内容所需的子视图了——既可以用代码添加，也可以在 Interface Builder 中把它们插入到 Scroll View 里。

也可以完全用代码创建 Scroll View。这通常在控制器类中完成，具体来说是在 `loadView` 方法的实现里。清单 1-2 给出了一个示例实现。

__清单 1-2__  用代码创建 Scroll View

```objc
- (void)loadView {
    CGRect fullScreenRect=[[UIScreen mainScreen] applicationFrame];
    scrollView=[[UIScrollView alloc] initWithFrame:fullScreenRect];
    scrollView.contentSize=CGSizeMake(320,758);

    // 对 scroll view 做任何进一步的配置
    // 添加一个或多个视图作为 scroll view 的子视图。

    // 因为 self.view 已经保留了 scrollView，所以释放它
    self.view=scrollView;
    [scrollView release];
}
```

这段代码创建了一个与整屏等大（不含状态栏）的 Scroll View，把 `scrollView` 对象设为控制器的视图，并把 `contentSize` 属性设为 320 x 758 像素。这段代码创建的是一个可垂直滚动的 Scroll View。

这个方法的实现中通常还会有更多代码，例如插入一个或多个子视图并按需配置它们的代码。另外，这段代码假定控制器还没有设置过 `view`。如果已经设置过，你就需要在把 Scroll View 设为控制器的视图之前，先释放已有的视图。

创建并配置好 Scroll View 之后，你必须添加一个或多个子视图来显示内容。到底应该在 Scroll View 中直接使用单个子视图还是多个子视图，这是一个设计决策，通常取决于一个条件：你的 Scroll View 是否需要支持缩放？

如果你打算在 Scroll View 中支持缩放，最常见的做法是使用一个覆盖整个 `contentSize` 的单一子视图，然后把其他子视图添加到这个视图上。这样你就可以把这个“汇总性”的内容视图指定为参与缩放的视图，它的所有子视图都会随着它的状态一起缩放。

如果不需要缩放，那么 Scroll View 用单个子视图（无论它自己是否还有子视图）还是多个子视图，就是一个取决于具体应用的决策了。

`contentSize` 属性是你需要在 Scroll View 中显示的内容的尺寸。在“在 Interface Builder 中创建 Scroll View”一节里，它被设为宽 320、高 758 像素。图 1-2 中的插图展示了 Scroll View 的内容，并标出了 `contentSize` 的宽和高。

__图 1-2__  标注了 `contentSize` 尺寸的内容

!

你可能想在 Scroll View 内容的边缘留出一些留白，通常是在顶部和底部，这样控制器和工具栏就不会遮挡内容。要添加留白，可以用 [contentInset](https://developer.apple.com/documentation/uikit/uiscrollview/1619406-contentinset) 属性指定 Scroll View 内容周围的缓冲区域。可以这样理解：它在不改变子视图尺寸、也不改变视图内容尺寸的前提下，把 Scroll View 的内容区域变大了。

`contentInset` 属性是一个 [UIEdgeInsets](https://developer.apple.com/documentation/uikit/uiedgeinsets) 结构体，包含 `top`、`bottom`、`left`、`right` 四个字段。图 1-3 展示了标出 `contentInset` 和 `contentSize` 的内容。

__图 1-3__  标出 `contentSize` 和 `contentInset` 的内容

!

如 [图 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnzzfvbuqmjqgewvgvzx) 所示，把 `contentInset` 属性指定为 `(64,44,0,0)`，会在内容顶部产生 64 像素（状态栏 20 像素加导航控制器 44 像素）、底部产生 44 像素（工具栏的高度）的额外缓冲区域。把 `contentInset` 设成这些值，既能在屏幕上显示导航控件和工具栏，又仍然可以通过滚动展示 Scroll View 的全部内容。

__清单 1-3__  设置 `contentInset` 属性

```objc
- (void)loadView {
    CGRect fullScreenRect=[[UIScreen mainScreen] applicationFrame];
    scrollView=[[UIScrollView alloc] initWithFrame:fullScreenRect];
    self.view=scrollView;
    scrollView.contentSize=CGSizeMake(320,758);
    scrollView.contentInset=UIEdgeInsetsMake(64.0,0.0,44.0,0.0);

    // 对 scroll view 做任何进一步的配置
    // 添加一个或多个视图作为 scroll view 的子视图。

    // 因为 self.view 已经保留了 scrollView，所以释放它
    self.view=scrollView;
    [scrollView release];
}
```

图 1-4 展示了把 [contentInset](https://developer.apple.com/documentation/uikit/uiscrollview/1619406-contentinset) 的 top 和 bottom 参数设为上述值之后的效果。滚动到顶部时（如左图所示），屏幕为导航栏和状态栏留出了空间。右图展示了内容滚动到底部时为工具栏留出的空间。两种情况下，滚动过程中你都能透过透明的导航栏和工具栏看到内容，而当内容完全滚动到顶部或底部时，所有内容都是可见的。

__图 1-4__  设置 `contentInset` 的 top 和 bottom 值之后的效果

!

不过，当 Scroll View 显示滚动指示器时，修改 `contentInset` 的值会带来一个意料之外的副作用。当用户把内容拖到屏幕顶部或底部时，滚动指示器会滚动到 `contentInset` 所定义区域内显示的内容之上，例如导航控件和工具栏上面。

要修正这个问题，你必须设置 [scrollIndicatorInsets](https://developer.apple.com/documentation/uikit/uiscrollview/1619427-scrollindicatorinsets) 属性。和 `contentInset` 属性一样，`scrollIndicatorInsets` 属性也定义为一个 `UIEdgeInsets` 结构体。设置垂直方向的内边距值可以限制垂直滚动指示器不超出该内边距显示，同时也会让水平滚动指示器显示在 `contentInset` 矩形区域之外。

只修改 `contentInset` 而不同时设置 `scrollIndicatorInsets` 属性，会导致滚动指示器画在导航控制器和工具栏上面，这不是我们想要的结果。而把 `scrollIndicatorInsets` 的值设成与 `contentInset` 相同，就能解决这个问题。

清单 1-4 给出了修正后的 `loadView` 实现，其中展示了通过添加 `scrollIndicatorInsets` 初始化来配置 Scroll View 所需的额外代码。

__清单 1-4__  设置 Scroll View 的 `contentInset` 和 `scrollIndicatorInsets` 属性

```objc
- (void)loadView {
    CGRect fullScreenRect=[[UIScreen mainScreen] applicationFrame];
    scrollView=[[UIScrollView alloc] initWithFrame:fullScreenRect];
    scrollView.contentSize=CGSizeMake(320,758);
    scrollView.contentInset=UIEdgeInsetsMake(64.0,0.0,44.0,0.0);
    scrollView.scrollIndicatorInsets=UIEdgeInsetsMake(64.0,0.0,44.0,0.0);

    // 对 scroll view 做任何进一步的配置
    // 添加一个或多个视图作为 scroll view 的子视图。

    // 因为 self.view 已经保留了 scrollView，所以释放它
    self.view=scrollView;
    [scrollView release];
}
```

[下一页](Scrolling%20the%20Scroll%20View%20Content.md)[上一页](About%20Scroll%20View%20Programming.md)

