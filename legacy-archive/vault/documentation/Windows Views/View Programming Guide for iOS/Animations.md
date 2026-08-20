---
title: iOS 视图编程指南
apple_id: TP40009503
resource_type: Guide
platform: tvOS|iOS
topic: User Experience
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/AnimatingViews/AnimatingViews.html
archived_at: '2026-07-18T02:24:09.524113Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [iOS 视图编程指南](About%20Windows%20and%20Views.md)


[下一页](Document%20Revision%20History.md)[上一页](Views.md)

# 动画

动画（animation）能在用户界面的不同状态之间提供流畅的视觉过渡。在 iOS 中，动画被广泛用于重新定位视图、改变视图大小、把视图从视图层级中移除以及隐藏视图。你可以用动画向用户传达反馈，也可以用它实现有趣的视觉效果。

在 iOS 中，创建复杂的动画并不需要你编写任何绘制代码。本章介绍的所有动画技术都使用 Core Animation 提供的内建支持。你要做的只是触发动画，然后让 Core Animation 负责渲染每一帧。这使得只用几行代码就能轻松创建复杂的动画。

UIKit 和 Core Animation 都提供了动画支持，但两者提供的支持程度不同。在 UIKit 中，动画通过 [UIView](https://developer.apple.com/documentation/uikit/uiview) 对象来完成。视图支持一组基本动画，可以覆盖许多常见任务。例如，你可以为视图属性的变化添加动画，或者用过渡（transition）动画把一组视图替换成另一组。

表 4-1 列出了 `UIView` 类的_可动画_属性（animatable property）——即内建了动画支持的那些属性。可动画并不意味着动画会自动发生。改变这些属性的值通常只是立即更新属性（以及视图），并不会产生动画。要让这样的改变带上动画，你必须在动画 block 内部修改属性的值，具体做法参见[为视图的属性变化添加动画](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltg)。

__表 4-1__  可动画的 `UIView` 属性

| 属性 | 你可以做的改变 |
| --- | --- |
| [frame](https://developer.apple.com/documentation/uikit/uiview/1622621-frame) | 修改该属性可以改变视图相对于其父视图坐标系的大小和位置。（如果 `transform` 属性中不是恒等变换，请改为修改 `bounds` 或 `center` 属性。） |
| [bounds](https://developer.apple.com/documentation/uikit/uiview/1622580-bounds) | 修改该属性可以改变视图的大小。 |
| [center](https://developer.apple.com/documentation/uikit/uiview/1622627-center) | 修改该属性可以改变视图相对于其父视图坐标系的位置。 |
| [transform](https://developer.apple.com/documentation/uikit/uiview/1622459-transform) | 修改该属性可以相对于视图的中心点对视图做缩放、旋转或平移。使用该属性的变换始终在 2D 空间中进行。（要执行 3D 变换，必须用 Core Animation 为视图的图层对象添加动画。） |
| [alpha](https://developer.apple.com/documentation/uikit/uiview/1622417-alpha) | 修改该属性可以逐渐改变视图的透明度。 |
| [backgroundColor](https://developer.apple.com/documentation/uikit/uiview/1622591-backgroundcolor) | 修改该属性可以改变视图的背景色。 |
| [contentStretch](https://developer.apple.com/documentation/uikit/uiview/1622511-contentstretch) | 修改该属性可以改变视图内容拉伸以填满可用空间的方式。 |

带动画的视图过渡让你能对视图层级做出超出 View Controller 所能提供范围的改变。虽然你应当使用 View Controller 来管理精简的视图层级，但有时你可能想替换整个或部分视图层级。在这些情况下，你可以用基于视图的过渡为视图的添加和移除加上动画。

如果你想执行更复杂的动画，或者 `UIView` 类不支持的动画，可以使用 Core Animation 和视图底层的图层来创建动画。由于视图对象和图层对象紧密关联在一起，对视图图层的改变会影响视图本身。使用 Core Animation，你可以为视图的图层实现以下类型变化的动画：

- 图层的大小和位置
- 执行变换时使用的中心点
- 图层或其子图层在 3D 空间中的变换
- 向图层层级中添加图层或从中移除图层
- 图层相对于其他同级图层的 Z 轴顺序
- 图层的阴影
- 图层的边框（包括图层的圆角）
- 图层在缩放操作期间被拉伸的部分
- 图层的不透明度
- 超出图层 bounds 之外的子图层的裁剪行为
- 图层的当前内容
- 图层的栅格化行为

本章虽然涉及了少量 Core Animation 的行为，但只是围绕如何从视图代码中启动它们来讲的。关于如何用 Core Animation 为图层添加动画的更完整信息，请参阅 _[Core Animation 编程指南](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_ 和 _[Core Animation 实用手册](../../Graphics%20Imaging/Core%20Animation%20Cookbook/Core%20Animation%20Cookbook.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timbw)_。

要为 [UIView](https://developer.apple.com/documentation/uikit/uiview) 类某个属性的变化添加动画，你必须把这些变化包裹在动画 block 中。术语_动画 block_ 是泛指的说法，指代任何声明可动画变化的代码。在 iOS 4 及更高版本中，你使用 [block 对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3)来创建动画 block。在更早的 iOS 版本中，你使用 `UIView` 类的专用类方法来标记动画 block 的开始和结束。两种技术支持相同的配置选项，对动画执行的控制程度也相同。不过，只要条件允许，都应优先使用基于 block 的方法。

以下各节聚焦于为视图属性变化添加动画所需的代码。关于如何在成组的视图之间创建带动画的过渡，请参阅[在视图之间创建带动画的过渡](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknlts)。

在 iOS 4 及更高版本中，你使用基于 [block](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) 的类方法来启动动画。有若干个基于 block 的方法，它们为动画 block 提供了不同程度的可配置性。这些方法是：

- [animateWithDuration:animations:](https://developer.apple.com/documentation/uikit/uiview/1622418-animate)
- [animateWithDuration:animations:completion:](https://developer.apple.com/documentation/uikit/uiview/1622515-animatewithduration)
- [animateWithDuration:delay:options:animations:completion:](https://developer.apple.com/documentation/uikit/uiview/1622451-animatewithduration)

由于它们都是[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)，用它们创建的动画 block 并不绑定到某一个视图上。因此，你可以用这些方法创建一个涉及多个视图变化的单一动画。例如，清单 4-1 展示了在一秒时间内让一个视图淡入、同时让另一个视图淡出所需的代码。这段代码执行时，指定的动画会立即在另一个线程上启动，以免阻塞当前线程或应用的主线程。

__清单 4-1__  执行一个简单的基于 block 的动画

```objc
[UIView animateWithDuration:1.0 animations:^{
        firstView.alpha = 0.0;
        secondView.alpha = 1.0;
}];
```

上例中的动画只运行一次，使用的是先加速后减速（ease-in、ease-out）的动画曲线。如果你想改变默认的动画参数，就必须用 `animateWithDuration:delay:options:animations:completion:` 方法来执行动画。该方法允许你自定义以下动画参数：

- 启动动画前使用的延迟
- 动画期间使用的时间曲线类型
- 动画应重复的次数
- 动画到达终点时是否应自动反向播放
- 动画进行期间触摸事件是否投递给视图
- 动画是应中断任何正在进行的动画，还是等这些动画完成后再开始

`animateWithDuration:animations:completion:` 和 `animateWithDuration:delay:options:animations:completion:` 这两个方法还都支持指定一个完成回调 block。你可以用完成回调来通知应用某个特定动画已经结束。完成回调也是把多个独立动画串联起来的手段。

清单 4-2 展示了一个动画 block 的例子，它用完成回调在第一个动画结束后启动新动画。第一次调用 `animateWithDuration:delay:options:animations:completion:` 设置了一个淡出动画，并为它配置了一些自定义选项。该动画完成时，它的完成回调会运行，并设置动画的后半部分，也就是在延迟之后把视图重新淡入。

使用完成回调是串联多个动画的主要方式。

__清单 4-2__  创建带自定义选项的动画 block

```objc
- (IBAction)showHideView:(id)sender
{
    // 立即把视图淡出
    [UIView animateWithDuration:1.0
        delay: 0.0
        options: UIViewAnimationOptionCurveEaseIn
        animations:^{
             thirdView.alpha = 0.0;
        }
        completion:^(BOOL finished){
            // 等待一秒，然后把视图淡入
            [UIView animateWithDuration:1.0
                 delay: 1.0
                 options:UIViewAnimationOptionCurveEaseOut
                 animations:^{
                    thirdView.alpha = 1.0;
                 }
                 completion:nil];
        }];
}
```


如果你的应用要在 iOS 3.2 及更早版本上运行，就必须使用 `UIView` 的 [beginAnimations:context:](https://developer.apple.com/documentation/uikit/uiview/1622463-beginanimations) 和 [commitAnimations](https://developer.apple.com/documentation/uikit/uiview/1622664-commitanimations) [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)来定义动画 block。这两个方法标记出动画 block 的开始和结束。你在这两个方法之间修改的任何可动画属性，都会在你调用 `commitAnimations` 方法之后以动画方式过渡到新值。动画在辅助线程上执行，以免阻塞当前线程或应用的主线程。

清单 4-3 展示了实现与[清单 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltcmy)相同行为所需的代码，但使用的是 begin/commit 方法。和清单 4-1 一样，这段代码在一秒时间内让一个视图淡出、另一个视图淡入。不过在这个例子中，你必须通过单独的方法调用来设置动画的时长。

__清单 4-3__  执行一个简单的 begin/commit 动画

```objc
    [UIView beginAnimations:@"ToggleViews" context:nil];
    [UIView setAnimationDuration:1.0];

    // 做出可动画的改变。
    firstView.alpha = 0.0;
    secondView.alpha = 1.0;

    // 提交这些改变并执行动画。
    [UIView commitAnimations];
```

默认情况下，动画 block 内所有可动画属性的改变都会带上动画。如果你想让一部分改变带动画、另一部分不带，可以用 [setAnimationsEnabled:](https://developer.apple.com/documentation/uikit/uiview/1622420-setanimationsenabled) 方法临时禁用动画，做出那些不希望带动画的改变，然后再次调用 `setAnimationsEnabled:` 重新启用动画。你可以调用 [areAnimationsEnabled](https://developer.apple.com/documentation/uikit/uiview/1622571-areanimationsenabled) 类方法来判断动画当前是否处于启用状态。

要为 begin/commit 动画 block 配置动画参数，你可以使用若干个 `UIView` [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)。表 4-2 列出了这些方法，并说明了如何用它们来配置动画。其中大多数方法只应在 begin/commit 动画 block 内部调用，但有些也可以配合基于 block 的动画使用。如果你没有在动画 block 中调用某个方法，对应特性就会采用默认值。关于每个方法所关联的默认值的更多信息，请参阅 _[UIView 类参考](https://developer.apple.com/documentation/uikit/uiview)_ 中的方法说明。

__表 4-2__  用于配置动画 block 的方法

| 方法 | 用途 |
| --- | --- |
| [setAnimationStartDate:](https://developer.apple.com/documentation/uikit/uiview/1622466-setanimationstart)  [setAnimationDelay:](https://developer.apple.com/documentation/uikit/uiview/1622472-setanimationdelay) | 用这两个方法中的任意一个来指定动画何时开始执行。如果指定的开始日期已经过去（或者延迟为 0），动画会尽快开始。 |
| [setAnimationDuration:](https://developer.apple.com/documentation/uikit/uiview/1622617-setanimationduration) | 用这个方法设置执行动画所经历的时间长度。 |
| [setAnimationCurve:](https://developer.apple.com/documentation/uikit/uiview/1622588-setanimationcurve) | 用这个方法设置动画的时间曲线。它控制动画是线性执行，还是在某些时刻改变速度。 |
| [setAnimationRepeatCount:](https://developer.apple.com/documentation/uikit/uiview/1622419-setanimationrepeatcount)  [setAnimationRepeatAutoreverses:](https://developer.apple.com/documentation/uikit/uiview/1622501-setanimationrepeatautoreverses) | 用这些方法设置动画重复的次数，以及动画在每个完整周期结束时是否反向播放。关于如何使用这些方法的更多信息，请参阅[实现自动反向播放的动画](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltcni)。 |
| [setAnimationDelegate:](https://developer.apple.com/documentation/uikit/uiview/1622509-setanimationdelegate)  [setAnimationWillStartSelector:](https://developer.apple.com/documentation/uikit/uiview/1622649-setanimationwillstart)  [setAnimationDidStopSelector:](https://developer.apple.com/documentation/uikit/uiview/1622539-setanimationdidstopselector) | 用这些方法在动画开始前或结束后立即执行代码。关于使用委托的更多信息，请参阅[配置动画委托](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltq)。 |
| [setAnimationBeginsFromCurrentState:](https://developer.apple.com/documentation/uikit/uiview/1622446-setanimationbeginsfromcurrentsta) | 用这个方法立即停止所有先前的动画，并从停止点开始新动画。如果你给这个方法传入 `NO` 而不是 `YES`，新动画要等到先前的动画停止后才会开始执行。 |

清单 4-4 展示了实现与[清单 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltm)中代码相同行为所需的代码，但使用的是 begin/commit 方法。和之前一样，这段代码先把一个视图淡出，等待一秒，然后再把它淡入。为了实现动画的第二部分，代码设置了一个动画委托，并实现了一个 did-stop 处理方法。该处理方法随后设置动画的后半部分并运行它们。

__清单 4-4__  使用 begin/commit 方法配置动画参数

```objc
// 这个方法开始第一段动画。
- (IBAction)showHideView:(id)sender
{
    [UIView beginAnimations:@"ShowHideView" context:nil];
    [UIView setAnimationCurve:UIViewAnimationCurveEaseIn];
    [UIView setAnimationDuration:1.0];
    [UIView setAnimationDelegate:self];
    [UIView setAnimationDidStopSelector:@selector(showHideDidStop:finished:context:)];

    // 做出可动画的改变。
    thirdView.alpha = 0.0;

    // 提交这些改变并执行动画。
    [UIView commitAnimations];
}

// 在前一段动画结束时被调用。
- (void)showHideDidStop:(NSString *)animationID finished:(NSNumber *)finished context:(void *)context
{
    [UIView beginAnimations:@"ShowHideView2" context:nil];
    [UIView setAnimationCurve:UIViewAnimationCurveEaseOut];
    [UIView setAnimationDuration:1.0];
    [UIView setAnimationDelay:1.0];

    thirdView.alpha = 1.0;

    [UIView commitAnimations];
}
```


如果你想在动画开始前或结束后立即执行代码，就必须为 begin/commit 动画 block 关联一个[委托对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)以及一个开始或停止选择器。你用 `UIView` 的 [setAnimationDelegate:](https://developer.apple.com/documentation/uikit/uiview/1622509-setanimationdelegate) [类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8)来设置委托对象，用 [setAnimationWillStartSelector:](https://developer.apple.com/documentation/uikit/uiview/1622649-setanimationwillstart) 和 [setAnimationDidStopSelector:](https://developer.apple.com/documentation/uikit/uiview/1622539-setanimationdidstopselector) 类方法来设置开始和停止选择器。在动画期间，动画系统会在适当的时机调用你的委托方法，让你有机会执行自己的代码。

你的动画委托方法的签名需要与下面类似：

```objc
- (void)animationWillStart:(NSString *)animationID context:(void *)context;
- (void)animationDidStop:(NSString *)animationID finished:(NSNumber *)finished context:(void *)context;
```

这两个方法的 _animationID_ 和 _context_ 参数，就是你在动画 block 开始处传给 `beginAnimations:context:` 方法的那两个参数：

- _animationID_——由应用提供的字符串，用于标识该动画。
- _context_——由应用提供的对象，你可以用它向委托传递额外信息。

`setAnimationDidStopSelector:` 指定的选择器方法还有一个额外参数——一个布尔值，如果动画完整运行到结束则为 `YES`。如果该参数的值为 `NO`，说明动画要么被取消，要么被另一个动画提前中止。

通过嵌套额外的动画 block，你可以给一个动画 block 中的不同部分指定不同的时间和配置选项。顾名思义，嵌套动画 block 就是在已有动画 block 内部创建的新动画 block。嵌套动画与父动画同时开始，但（大体上）按照各自的配置选项运行。默认情况下，嵌套动画确实会继承父动画的时长和动画曲线，不过这些选项也可以按需覆盖。

清单 4-5 展示了如何用嵌套动画来改变整组动画中某些动画的时间、时长和行为。在这个例子中，两个视图都被淡化到完全透明，但 `anotherView` 对象的透明度在最终隐藏之前来回变化了好几次。嵌套动画 block 中使用的 [UIViewAnimationOptionOverrideInheritedCurve](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionoverrideinheritedcurve) 和 [UIViewAnimationOptionOverrideInheritedDuration](https://developer.apple.com/documentation/uikit/uiview/animationoptions/1622434-overrideinheritedduration) 键使得第二个动画可以修改来自第一个动画的曲线和时长值。如果没有这些键，就会改用外层动画 block 的时长和曲线。

__清单 4-5__  嵌套配置各不相同的动画

```objc
[UIView animateWithDuration:1.0
        delay: 1.0
        options:UIViewAnimationOptionCurveEaseOut
        animations:^{
            aView.alpha = 0.0;

            // 创建一个嵌套动画，它有不同的
            // 时长、时间曲线和配置。
            [UIView animateWithDuration:0.2
                 delay:0.0
                 options: UIViewAnimationOptionOverrideInheritedCurve |
                          UIViewAnimationOptionCurveLinear |
                          UIViewAnimationOptionOverrideInheritedDuration |
                          UIViewAnimationOptionRepeat |
                          UIViewAnimationOptionAutoreverse
                 animations:^{
                      [UIView setAnimationRepeatCount:2.5];
                      anotherView.alpha = 0.0;
                 }
                 completion:nil];

        }
        completion:nil];
```

如果你使用 begin/commit 方法创建动画，嵌套的工作方式与基于 block 的方法大致相同。在一个已打开的动画 block 内每次再调用 `beginAnimations:context:`，都会创建一个新的嵌套动画 block，你可以按需对它进行配置。你做出的任何配置改动都作用于最近打开的那个动画 block。所有动画 block 都必须通过调用 [commitAnimations](https://developer.apple.com/documentation/uikit/uiview/1622664-commitanimations) 关闭，动画才会被提交并执行。

在创建带重复次数的可反向动画时，可以考虑把重复次数指定为非整数值。对于自动反向的动画，每个完整周期都包含从原值动画到新值再动画回来的过程。如果你希望动画停在新值上，把重复次数加上 `0.5`，动画就会多完成半个周期，从而结束在新值上。如果不加这半步，你的动画会先动画回原值，然后猛地跳到新值，这可能并不是你想要的视觉效果。

视图过渡可以帮你掩盖在视图层级中添加、移除、隐藏或显示视图时产生的突兀变化。你可以用视图过渡来实现以下类型的改变：

- __改变现有视图中可见的子视图。__ 当你想对现有视图做相对较小的改动时，通常选择这一种。
- __用另一个视图替换视图层级中的某个视图。__ 当你想替换占据整个或大部分屏幕的视图层级时，通常选择这一种。

改变一个视图的子视图，可以让你对该视图做出中等程度的改动。例如，你可以添加或移除子视图，让父视图在两种不同状态之间切换。动画结束时，显示的仍是同一个视图，但它的内容已经不同了。

在 iOS 4 及更高版本中，你使用 [transitionWithView:duration:options:animations:completion:](https://developer.apple.com/documentation/uikit/uiview/1622574-transition) 方法为视图启动过渡动画。在传给该方法的 animations block 中，通常只有与显示、隐藏、添加或移除子视图相关的改变才会带上动画。把动画限制在这个范围内，视图就可以为变化前后的两个版本各生成一张快照图像，然后在两张图像之间做动画，这样效率更高。不过，如果你需要为其他改变添加动画，可以在调用该方法时加上 [UIViewAnimationOptionAllowAnimatedContent](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionallowanimatedcontent) 选项。加上这个选项后，视图就不会创建快照，而是直接为所有改变添加动画。

清单 4-6 举例说明了如何用过渡动画营造出“新增了一个文本输入页”的效果。在这个例子中，主视图内嵌了两个文本视图。这两个文本视图配置完全相同，但始终一个可见、另一个隐藏。当用户点按按钮创建新页面时，这个方法会切换两个视图的可见性，于是就出现了一个新的空白页面，里面有一个可以接受输入的空文本视图。过渡完成后，视图用一个私有方法保存旧页面上的文本，并重置那个现已隐藏的文本视图，以便之后重复使用。接着视图会调整自己的指针，这样如果用户再次请求新页面，它就能做同样的事情。

__清单 4-6__  用一个空文本视图替换现有的文本视图

```objc
- (IBAction)displayNewPage:(id)sender
{
    [UIView transitionWithView:self.view
        duration:1.0
        options:UIViewAnimationOptionTransitionCurlUp
        animations:^{
            currentTextView.hidden = YES;
            swapTextView.hidden = NO;
        }
        completion:^(BOOL finished){
            // 保存旧文本，然后交换两个视图。
            [self saveNotes:temp];

            UIView*    temp = currentTextView;
            currentTextView = swapTextView;
            swapTextView = temp;
        }];
}
```

如果你需要在 iOS 3.2 及更早版本中执行视图过渡，可以用 [setAnimationTransition:forView:cache:](https://developer.apple.com/documentation/uikit/uiview/1622528-setanimationtransition) 方法来指定过渡的参数。传给该方法的视图，与你作为第一个参数传给 `transitionWithView:duration:options:animations:completion:` 方法的视图是同一个。清单 4-7 展示了你需要创建的动画 block 的基本结构。注意，要实现[清单 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltcoi)中的完成回调 block，你需要按[配置动画委托](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltq)中描述的那样，配置一个带 did-stop 处理方法的动画委托。

__清单 4-7__  使用 begin/commit 方法改变子视图

```objc
    [UIView beginAnimations:@"ToggleSiblings" context:nil];
    [UIView setAnimationTransition:UIViewAnimationTransitionCurlUp forView:self.view cache:YES];
    [UIView setAnimationDuration:1.0];

    // 在此做出你的改变

    [UIView commitAnimations];
```


当你希望界面发生显著变化时，就会用到替换视图。由于这项技术只交换视图（而不交换 View Controller），你需要自行妥善设计应用的控制器对象。这项技术只是一种利用若干标准过渡快速呈现新视图的方式。

在 iOS 4 及更高版本中，你使用 [transitionFromView:toView:duration:options:completion:](https://developer.apple.com/documentation/uikit/uiview/1622562-transitionfromview) 方法在两个视图之间做过渡。该方法实际上会把第一个视图从层级中移除，并插入另一个视图，所以如果你想保留第一个视图，务必确保自己持有它的引用。如果你想隐藏视图而不是把它们从视图层级中移除，可以把 [UIViewAnimationOptionShowHideTransitionViews](https://developer.apple.com/documentation/uikit/uiviewanimationoptions/uiviewanimationoptionshowhidetransitionviews) 键作为选项之一传入。

清单 4-8 展示了在同一个 View Controller 管理的两个主视图之间切换所需的代码。在这个例子中，View Controller 的根视图始终显示两个子视图（`primaryView` 或 `secondaryView`）中的一个。两个视图呈现相同的内容，但呈现方式不同。View Controller 用 `displayingPrimary` 成员变量（一个布尔值）来跟踪当前显示的是哪个视图。翻转方向会根据当前显示的视图而改变。

__清单 4-8__  在 View Controller 中切换两个视图

```objc
- (IBAction)toggleMainViews:(id)sender {
    [UIView transitionFromView:(displayingPrimary ? primaryView : secondaryView)
        toView:(displayingPrimary ? secondaryView : primaryView)
        duration:1.0
        options:(displayingPrimary ? UIViewAnimationOptionTransitionFlipFromRight :
                    UIViewAnimationOptionTransitionFlipFromLeft)
        completion:^(BOOL finished) {
            if (finished) {
                displayingPrimary = !displayingPrimary;
            }
    }];
}
```


[UIView](https://developer.apple.com/documentation/uikit/uiview) 动画接口支持把多个独立的动画 block 串联起来，使它们依次执行而不是同时执行。串联动画 block 的做法取决于你使用的是基于 block 的动画方法还是 begin/commit 方法：

- 对于基于 block 的动画，使用 [animateWithDuration:animations:completion:](https://developer.apple.com/documentation/uikit/uiview/1622515-animatewithduration) 和 [animateWithDuration:delay:options:animations:completion:](https://developer.apple.com/documentation/uikit/uiview/1622451-animatewithduration) 方法所支持的完成回调来执行后续动画。
- 对于 begin/commit 动画，为动画关联一个委托对象和一个 did-stop 选择器。关于如何为动画关联委托，请参阅[配置动画委托](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltq)。

串联动画之外的另一种做法，是使用带不同延迟因子的嵌套动画，从而让各个动画在不同时刻开始。关于如何嵌套动画的更多信息，请参阅[嵌套动画 block](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltcmi)。

应用可以按需自由混用基于视图和基于图层的动画代码，但配置动画参数的方式取决于图层归谁所有。修改视图自有的图层等同于修改视图本身，你施加在该图层属性上的任何动画都会遵循当前基于视图的动画 block 的动画参数。而对你自己创建的图层则不然。自定义图层对象会忽略基于视图的动画 block 参数，转而使用 Core Animation 的默认参数。

如果你想为自己创建的图层自定义动画参数，就必须直接使用 Core Animation。通常，用 Core Animation 为图层添加动画的做法是创建一个 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，或者 [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation) 的其他某个具体子类的对象，然后把该动画添加到对应的图层上。你可以在基于视图的动画 block 内部或外部施加这个动画。

清单 4-9 展示了一个同时修改视图和自定义图层的动画。这个例子中的视图在其 bounds 中心包含一个自定义 [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) 对象。该动画让视图逆时针旋转，同时让图层顺时针旋转。由于两者旋转方向相反，图层相对于屏幕保持了原有朝向，看起来并没有明显转动。而图层下面的视图则旋转了 360 度并回到原来的朝向。这个例子主要是为了演示如何混用视图动画和图层动画。在需要精确时间控制的场合，不应使用这类混合方式。

__清单 4-9__  混用视图动画和图层动画

```objc
[UIView animateWithDuration:1.0
    delay:0.0
    options: UIViewAnimationOptionCurveLinear
    animations:^{
        // 为视图旋转的前半程做动画。
        CGAffineTransform  xform = CGAffineTransformMakeRotation(DEGREES_TO_RADIANS(-180));
        backingView.transform = xform;

        // 让内嵌的 CALayer 朝相反方向旋转。
        CABasicAnimation*    layerAnimation = [CABasicAnimation animationWithKeyPath:@"transform"];
        layerAnimation.duration = 2.0;
        layerAnimation.beginTime = 0; //CACurrentMediaTime() + 1;
        layerAnimation.valueFunction = [CAValueFunction functionWithName:kCAValueFunctionRotateZ];
        layerAnimation.timingFunction = [CAMediaTimingFunction
                        functionWithName:kCAMediaTimingFunctionLinear];
        layerAnimation.fromValue = [NSNumber numberWithFloat:0.0];
        layerAnimation.toValue = [NSNumber numberWithFloat:DEGREES_TO_RADIANS(360.0)];
        layerAnimation.byValue = [NSNumber numberWithFloat:DEGREES_TO_RADIANS(180.0)];
        [manLayer addAnimation:layerAnimation forKey:@"layerAnimation"];
    }
    completion:^(BOOL finished){
        // 现在执行视图旋转的后半程。
        [UIView animateWithDuration:1.0
             delay: 0.0
             options: UIViewAnimationOptionCurveLinear
             animations:^{
                 CGAffineTransform  xform = CGAffineTransformMakeRotation(DEGREES_TO_RADIANS(-359));
                 backingView.transform = xform;
             }
             completion:^(BOOL finished){
                 backingView.transform = CGAffineTransformIdentity;
         }];
}];
```

如果你需要视图动画和图层动画之间保持精确的时间同步，建议全部改用 Core Animation 来创建动画。你可能会发现，有些动画本来用 Core Animation 就更容易实现。例如，[清单 4-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbtfvbuqnrnknltcoa) 中基于视图的旋转，超过 180 度就必须分成多个步骤，而 Core Animation 那部分则使用了一个旋转值函数，可以经由一个中间值从起点一路旋转到终点。

关于如何用 Core Animation 创建和配置动画的更多信息，请参阅 _[Core Animation 编程指南](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_ 和 _[Core Animation 实用手册](../../Graphics%20Imaging/Core%20Animation%20Cookbook/Core%20Animation%20Cookbook.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timbw)_。

[下一页](Document%20Revision%20History.md)[上一页](Views.md)

