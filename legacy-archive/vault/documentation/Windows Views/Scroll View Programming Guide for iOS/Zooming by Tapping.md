---
title: iOS Scroll View 编程指南
apple_id: TP40008179
resource_type: Guide
platform: iOS
topic: User Experience
technology: UIKit
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/UIScrollView_pg/ZoomingByTouch/ZoomingByTouch.html
archived_at: '2026-07-18T02:22:57.184587Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS Scroll View 编程指南](About%20Scroll%20View%20Programming.md)


[下一页](Scrolling%20Using%20Paging%20Mode.md)[上一页](Basic%20Zooming%20Using%20the%20Pinch%20Gestures.md)

# 通过点按实现缩放

基本的 `UIScrollView` 类只需极少量代码就能支持捏入和捏出手势，但要通过点按检测来支持更丰富的缩放体验，你的应用就得做更多工作了。

_iOS Human Interface Guidelines_ 定义了用双击来放大和缩小。不过这里有一些特定的前提：视图只有一个缩放层级（比如“照片”应用），或者连续双击会一直放大到最大倍数，到达之后再次双击就缩回全屏视图。但有些应用在处理点按缩放功能时需要更灵活的行为，“地图”应用就是一个例子。“地图”支持双击放大，继续双击会进一步放大。要分级缩小，“地图”使用两根靠得很近的手指触摸屏幕，逐级缩小。虽然 _iOS Human Interface Guidelines_ 中没有定义这个手势，但应用在需要该功能时，可以选择采用它来模仿“地图”应用。

要让你的应用支持点按缩放功能，你不需要给 `UIScrollView` 类派生子类。相反，你应该在 `UIScrollView` 的委托方法 `viewForZoomingInScrollView:` 所返回的那个类中实现所需的触摸处理。该类负责跟踪屏幕上的手指数量和点按次数。当它检测到单次点按、双击或双指触摸时，就做出相应的响应。在双击和双指触摸的情况下，它应该用代码按合适的系数缩放 Scroll View。

要在 `UIView`（或其后代）子类的触摸代码中支持点按、双击和双指点按，需要实现三个方法：`touchesBegan:withEvent:`、`touchesEnded:withEvent:` 和 `touchesCanceled:withEvent:`。此外，可能还需要初始化交互开关、多点触摸开关和跟踪用的变量。下面的代码片段取自 _[ScrollViewSuite](../../../samplecode/ScrollViewSuite/ScrollViewSuite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojqgq)_ 示例代码工程中的 _TapToZoom_ 例子，位于 `TapDetectingImageView` 类中，它是 `UIImageView` 的一个子类。

点按缩放实现所需的这些手势，要求视图启用用户交互和多点触摸，启用这些功能的方法在 `initWithImage:` 方法中调用。这个方法还初始化了两个实例变量，用于在触摸方法中跟踪状态。`twoFingerTapIsPossible` 属性是一个布尔值，除非有超过两根手指接触设备屏幕，否则它都是 `YES`。`multipleTouches` 属性的值为 `NO`，除非检测到多于一个的触摸事件。第三个属性 `tapLocation` 是一个 CGPoint，用于跟踪双击的位置，或者检测到双指触摸时两根手指之间的中点。随后这个点会被用作放大或缩小的中心点，具体做法参见[以编程方式缩放](Basic%20Zooming%20Using%20the%20Pinch%20Gestures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnzzfvbuqmjqgiwvgvzx)中描述的编程缩放方法。

```objc
- (id)initWithImage:(UIImage *)image {
    self = [super initWithImage:image];
    if (self) {
        [self setUserInteractionEnabled:YES];
        [self setMultipleTouchEnabled:YES];
        twoFingerTapIsPossible = YES;
        multipleTouches = NO;
    }
    return self;
}
```

初始化完成之后，这个类就做好了接收触摸事件的准备。

`touchesBegan:withEvent:` 方法首先取消所有尚未执行的单指点按处理请求，也就是 `handleSingleTap` 消息。之所以取消这个消息，是因为如果它已经被安排发送，那么由于现在又来了一个额外的触摸事件，它就失效了——这排除了单次点按的可能。如果因为这是第一次触摸而尚未安排该消息，那么取消操作会被忽略。

接着，这个方法会更新跟踪变量的状态。如果收到了多于一个的触摸事件，`multipleTouches` 属性就被设为 `YES`，因为这可能是一个双指触摸。如果发生了超过两个触摸事件，`twoFingerTapIsPossible` 属性就被设为 `NO`，一次用超过两根手指的触摸属于会被忽略的手势。

这个方法的代码如下：

```objc
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    // 取消所有待处理的 handleSingleTap 消息。
    [NSObject cancelPreviousPerformRequestsWithTarget:self
                                             selector:@selector(handleSingleTap)
                                               object:nil];

    // 更新触摸状态。
    if ([[event touchesForView:self] count] > 1)
        multipleTouches = YES;
    if ([[event touchesForView:self] count] > 2)
        twoFingerTapIsPossible = NO;

}
```


这个方法是点按处理的主力，也稍微有些复杂。不过代码注释很完善，所以下面直接给出。`midPointBetweenPoints` 函数用于确定调用 `handleTwoFingerTap` 方法时双指触摸所围绕的中心点，该方法会让视图缩小一级。

```objc
- (void)touchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
    BOOL allTouchesEnded = ([touches count] == [[event touchesForView:self] count]);

    // 首先检查单纯的单击/双击，只有在没有出现多点触摸时才可能
    if (!multipleTouches) {
        UITouch *touch = [touches anyObject];
        tapLocation = [touch locationInView:self];

        if ([touch tapCount] == 1) {
            [self performSelector:@selector(handleSingleTap)
                       withObject:nil
                       afterDelay:DOUBLE_TAP_DELAY];
        } else if([touch tapCount] == 2) {
            [self handleDoubleTap];
        }
    }

    // 如果出现了多点触摸，并且该情形尚未被排除，
    // 则检查是否为双指点按
    else if (multipleTouches && twoFingerTapIsPossible) {

        // 情况 1：两次触摸同时结束
        if ([touches count] == 2 && allTouchesEnded) {
            int i = 0;
            int tapCounts[2];
            CGPoint tapLocations[2];
            for (UITouch *touch in touches) {
                tapCounts[i] = [touch tapCount];
                tapLocations[i] = [touch locationInView:self];
                i++;
            }
            if (tapCounts[0] == 1 && tapCounts[1] == 1) {
                // 如果两者都是单次点按，那就是双指点按
                tapLocation = midpointBetweenPoints(tapLocations[0],
                                                    tapLocations[1]);
                [self handleTwoFingerTap];
            }
        }

        // 情况 2：其中一次触摸结束了，另一次还没结束
        else if ([touches count] == 1 && !allTouchesEnded) {
            UITouch *touch = [touches anyObject];
            if ([touch tapCount] == 1) {
                // 如果这次触摸是单次点按，就保存它的位置
                // 以便之后与第二次触摸的位置取平均
                tapLocation = [touch locationInView:self];
            } else {
                twoFingerTapIsPossible = NO;
            }
        }

        // 情况 3：两次触摸中的第二次结束了
        else if ([touches count] == 1 && allTouchesEnded) {
            UITouch *touch = [touches anyObject];
            if ([touch tapCount] == 1) {
                // 如果最后抬起的这次是单次点按，那么这就是一次双指点按
                tapLocation = midpointBetweenPoints(tapLocation,
                                                    [touch locationInView:self]);
                [self handleTwoFingerTap];
            }
        }
    }

    // 如果所有手指都已抬起，重置触摸监测状态
    if (allTouchesEnded) {
        twoFingerTapIsPossible = YES;
        multipleTouches = NO;
    }
}
```


如果 Scroll View 检测到手指已经移动、从而将要开始滚动，导致点按处理不再相关，视图就会收到 `touchesCancelled:withEvent:` 消息。这个方法只是简单地重置状态变量。

```objc
- (void)touchesCancelled:(NSSet *)touches withEvent:(UIEvent *)event {
    twoFingerTapIsPossible = YES;
    multipleTouches = NO;
}
```


_[ScrollViewSuite](../../../samplecode/ScrollViewSuite/ScrollViewSuite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojqgq)_ 示例代码工程中有很好的用点按手势实现缩放的例子。该套件中的 `TapToZoom` 例子实现了一个 `UIImageView` 子类，支持像“地图”应用那样通过点按行为进行缩放。它的实现足够通用——通过使用一个委托（通常是管理该 Scroll View 的控制器）来实际处理点按、双击或双指触摸的响应——因此你应该能轻松地把这段代码和设计移植到自己的视图上。

`TapDetectingImageView` 类是实现触摸处理的 `UIImageView` 子类，它使用 `RootViewController` 类作为委托来实际处理点按和触摸的响应，该控制器同时也负责最初对 `UIScrollView` 的配置。

[下一页](Scrolling%20Using%20Paging%20Mode.md)[上一页](Basic%20Zooming%20Using%20the%20Pinch%20Gestures.md)

