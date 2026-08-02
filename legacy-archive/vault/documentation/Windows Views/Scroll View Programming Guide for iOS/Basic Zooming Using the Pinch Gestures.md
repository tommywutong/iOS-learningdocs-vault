---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/ZoomZoom/ZoomZoom.html
archived_at: '2026-07-18T02:22:55.459569Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Zooming%20by%20Tapping.md)[上一页](Scrolling%20the%20Scroll%20View%20Content.md)

# 使用捏合手势实现基本缩放

`UIScrollView` 让支持捏合手势缩放变得很容易。你的应用只需指定缩放系数（也就是内容能被放大或缩小到什么程度），再实现一个委托方法。做完这几步，你的 Scroll View 就能支持用捏合手势进行缩放了。

捏入和捏出缩放手势是 iOS 应用用户在放大和缩小时期望使用的标准手势。图 3-1 展示了捏合手势的示例。

__图 3-1__  标准的捏入和捏出手势

!

要支持缩放，你必须为 Scroll View 设置一个委托。委托对象必须遵循 `UIScrollViewDelegate` 协议。多数情况下，委托就是 Scroll View 所属的控制器类。该委托类必须实现 `viewForZoomingInScrollView:` 方法，并返回参与缩放的视图。下面这个委托方法的实现返回了控制器的 `imageView` 属性的值，它是一个 `UIImageView` 实例。这就指定了 `imageView` 属性会响应缩放手势以及所有代码触发的缩放而被缩放。

```objc
- (UIView *)viewForZoomingInScrollView:(UIScrollView *)scrollView
{
    return self.imageView;
}
```

要指定用户能缩放的幅度，你需要设置 `minimumZoomScale` 和 `maximumZoomScale` 属性的值，两者的初始值都是 `1.0`。这些属性的值可以在 Interface Builder 的 `UIScrollView` 检查器面板中设置，也可以用代码设置。清单 3-1 展示了在一个 UIViewController 子类中支持缩放所需的代码。它假定该控制器子类的实例就是委托，并且实现了上面展示的 `viewForZoomingInScrollView:` 委托方法。

__清单 3-1__  `UIViewController` 子类中支持缩放所需的最少方法的实现

```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    self.scrollView.minimumZoomScale=0.5;
    self.scrollView.maximumZoomScale=6.0;
    self.scrollView.contentSize=CGSizeMake(1280, 960);
    self.scrollView.delegate=self;
}
```

指定缩放系数，以及指定实现了 `viewForZoomingInScrollView:` 方法的委托对象，是支持捏合手势缩放的最低要求。

Scroll View 有时需要响应触摸事件（比如双击或其他点按手势）来缩放，或者响应捏合手势之外的其他用户操作来缩放。为此，`UIScrollView` 提供了两个方法的实现：`setZoomScale:animated:` 和 `zoomToRect:animated:`。

`setZoomScale:animated:` 把当前缩放比例设为指定值。该值必须落在 `minimumZoomScale` 和 `maximumZoomScale` 指定的范围之内。如果 animated 参数为 `YES`，缩放会以匀速动画进行直至完成；否则比例变化立即生效。你也可以直接设置 `zoomScale` 属性，这等价于调用 `setZoomScale:animated:` 并传入 `NO` 作为 animated 参数。使用这个方法缩放，或者直接改变该属性时，视图缩放的方式会保持视图中心不动。

`zoomToRect:animated:` 方法会缩放内容，使其填满指定的矩形。和 `setZoomScale:animated:` 一样，这个方法也有一个 animated 参数，用于决定位置和缩放的变化是否以动画方式呈现。

你的应用常常需要响应某个特定位置的点按来设置缩放比例和位置。由于 `setZoomScale:animated:` 是围绕可见内容的中心进行缩放的，你会需要一个函数，把一个特定位置和缩放系数转换成适合传给 `zoomToRect:animated:` 的矩形。清单 3-2 展示了这样一个工具方法，它接收一个 Scroll View、一个缩放比例，以及缩放矩形要以之为中心的点。

__清单 3-2__  把指定的比例和中心点转换成用于缩放的矩形的工具方法

```objc
- (CGRect)zoomRectForScrollView:(UIScrollView *)scrollView withScale:(float)scale withCenter:(CGPoint)center {

    CGRect zoomRect;

    // 缩放矩形使用内容视图的坐标系。
    // 当缩放比例为 1.0 时，它的大小就等于
    // imageScrollView 的 bounds。
    // 随着缩放比例减小，可见的内容变多，
    // 该矩形也随之变大。
    zoomRect.size.height = scrollView.frame.size.height / scale;
    zoomRect.size.width  = scrollView.frame.size.width  / scale;

    // 选取合适的原点，以得到正确的中心。
    zoomRect.origin.x = center.x - (zoomRect.size.width  / 2.0);
    zoomRect.origin.y = center.y - (zoomRect.size.height / 2.0);

    return zoomRect;
}
```

当你在支持双击手势的自定义子类中响应双击时，这个工具方法非常有用。使用时只需传入相关的 UIScrollView 实例、新的缩放比例（通常由现有的 `zoomScale` 加上或乘以某个缩放量得来），以及缩放要围绕的中心点。响应双击手势时，中心点通常就是点按的位置。该方法返回的矩形可以直接传给 `zoomToRect:animated:` 方法。

当用户完成缩放捏合手势，或者 Scroll View 的代码缩放完成时，`UIScrollView` 的委托会收到 `scrollViewDidEndZooming:withView:atScale:` 消息，从而得到通知。

这个方法的参数包括 Scroll View 实例、被滚动的 Scroll View 子视图，以及缩放结束时的比例系数。收到这个委托消息后，你的应用就可以采取相应的动作。

Scroll View 的内容被缩放时，缩放视图的内容只是随着缩放系数的变化被简单地做了比例变换。这样内容虽然变大或变小了，却不会触发重绘。结果就是显示出来的内容不够清晰。如果被缩放的内容是一张图片，而且你的应用不需要像“地图”应用那样显示更详细的新内容，这可能并不是问题。

如果你的应用确实需要在缩放时显示更精细的位图图像，可以研究一下 _[ScrollViewSuite](../../../samplecode/ScrollViewSuite/ScrollViewSuite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojqgq)_ 示例代码中的 Tiling 例子。它采用的技术是把缩放后的内容预先渲染成小块，然后在 Scroll View 中用一个个独立的视图来显示这些小块。

不过，如果你的缩放内容是实时绘制的，并且需要在缩放时保持清晰，那么应用中负责绘制缩放视图的类就需要用到 Core Animation。这个类需要把 `UIView` 类所用的 Core Animation 图层类改为 `CATiledLayer`，并使用 Core Animation 的 `drawLayer:inContext:` 方法进行绘制。

[清单 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnzzfvbuqmjqgiwvgvzu) 给出了一个子类的完整实现，它会绘制一个十字并支持缩放。整个缩放过程中图像都保持清晰。`Zoomable` 视图是一个 `UIView` 子类，被添加为某个内容尺寸为 (460,320) 的 Scroll View 的子视图，并由 Scroll View 的委托方法 `viewForZoomingInScrollView:` 返回。缩放发生时，开发者无需做任何事情就能让 `Zoomable` 视图重绘。

__清单 3-3__  在缩放过程中清晰绘制自身内容的 UIView 子类的实现

```objc
#import "ZoomableView.h"
#import <QuartzCore/QuartzCore.h>

@implementation ZoomableView


// 把 UIView 的图层设为 CATiledLayer
+(Class)layerClass
{
    return [CATiledLayer class];
}


// 初始化该图层，设置
// 分块图层的 levelsOfDetailBias
// 和 levelsOfDetail
-(id)initWithFrame:(CGRect)r
{
    self = [super initWithFrame:r];
    if(self) {
        CATiledLayer *tempTiledLayer = (CATiledLayer*)self.layer;
        tempTiledLayer.levelsOfDetail = 5;
        tempTiledLayer.levelsOfDetailBias = 2;
        self.opaque=YES;
    }
    return self;
}

// 实现 -drawRect: 以保证 UIView 类正常工作
// 真正的绘制工作在 -drawLayer:inContext 中完成
-(void)drawRect:(CGRect)r
{
}

-(void)drawLayer:(CALayer*)layer inContext:(CGContextRef)context
{
    // 该上下文已经过恰当的缩放和平移，因此你可以像在整个图层上绘制那样
    // 向这个上下文绘制，最终会渲染出正确的内容。
    // 我们假定当前的 CTM 是一个未经旋转的均匀缩放

   // 仿射变换，这意味着
    // a == d 且 b == c == 0
    // CGFloat scale = CGContextGetCTM(context).a;
    // 这里虽然没有用到，但在其他场景下可能有用。

    // 裁剪包围盒表示上下文中当前被请求渲染的区域。
    // 这里虽然没有用到，
    // 但在其他场景下你的应用可能需要它
    // 来做缩放。
    // CGRect rect = CGContextGetClipBoundingBox(context);

    // 设置并绘制整个图层的背景色
    // 另一种做法是把图层设为 opaque=NO；
    // 删掉下面两行代码
    // 并设置 scroll view 的背景色
    CGContextSetRGBFillColor(context, 1.0,1.0,1.0,1.0);
    CGContextFillRect(context,self.bounds);

    // 画一个简单的加号
    CGContextSetRGBStrokeColor(context, 0.0, 0.0, 1.0, 1.0);
    CGContextBeginPath(context);
    CGContextMoveToPoint(context,35,255);
    CGContextAddLineToPoint(context,35,205);
    CGContextAddLineToPoint(context,135,205);
    CGContextAddLineToPoint(context,135,105);
    CGContextAddLineToPoint(context,185,105);
    CGContextAddLineToPoint(context,185,205);
    CGContextAddLineToPoint(context,285,205);
    CGContextAddLineToPoint(context,285,255);
    CGContextAddLineToPoint(context,185,255);
    CGContextAddLineToPoint(context,185,355);
    CGContextAddLineToPoint(context,135,355);
    CGContextAddLineToPoint(context,135,255);
    CGContextAddLineToPoint(context,35,255);
    CGContextClosePath(context);

    // 描边这个简单图形
    CGContextStrokePath(context);


}
```

[下一页](Zooming%20by%20Tapping.md)[上一页](Scrolling%20the%20Scroll%20View%20Content.md)

