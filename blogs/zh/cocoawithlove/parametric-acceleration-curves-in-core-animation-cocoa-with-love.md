---
title: 'Core Animation 中的参数化加速曲线 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/09/parametric-acceleration-curves-in-core.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c5750a6bcf16cf9c'
translated: true
---

> 原文：[Parametric acceleration curves in Core Animation | Cocoa with Love](https://www.cocoawithlove.com/2008/09/parametric-acceleration-curves-in-core.html)　·　Cocoa with Love (Matt Gallagher)

CAMediaTimerFunction 用于控制 Core Animation 中沿路径的基本加速，但其功能非常有限。在这篇文章中，我将探讨 CAMediaTimerFunction 背后的数学原理，并展示一个示例应用，它通过使用参数化的 CAKeyframeAnimation 值来模拟 CAMediaTimerFunction 无法实现的一些函数。

## 引言

如果你在 [Core Animation](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html) 中沿直线让某个对象动起来，你可以让该对象以恒定速度沿整条路径移动，也可以指定对象在开始时加速到目标速度，在结束时减速停止（ease-in/ease-out）。[CAMediaTimerFunction](http://developer.apple.com/documentation/Cocoa/Reference/CAMediaTimingFunction_class/Introduction/Introduction.html) 类就用于指定这种行为。

如果你想要一些完全不同的效果，比如沿路径的[指数衰减](http://en.wikipedia.org/wiki/Exponential_decay)，那么遗憾的是，CAMediaTimerFunction 做不到。此外，你无法通过派生子类（subclass）CAMediaTimerFunction 来修改其行为。我们仍然可以在 Core Animation 中实现指数衰减，但需要换一种方式。

![](https://www.cocoawithlove.com/assets/objc-era/mediatimercapabilities.png)

这些截图来自 [「AnimationAcceleration」示例应用](https://www.cocoawithlove.com/assets/objc-era/AnimationAcceleration.zip)（下文会介绍）。它可以处理所有这些加速类型。

## ease-in/ease-out 动画的数学原理

在 Core Animation 中，派生自 [CAAnimation](http://developer.apple.com/documentation/GraphicsImaging/Reference/CAAnimation_class/Introduction/Introduction.html) 的动画类允许你设置 timingFunction（一个 CAMediaTimerFunction 对象）。这个属性（property）的主要用途是让你控制动画在端点处的「平滑度」（线性速度或 ease-in/ease-out）。

CAMediaTimerFunction 使用一个[三次贝塞尔](http://en.wikipedia.org/wiki/Bézier_curve)曲线将输入时间值转换为输出时间值。文档并未明确说明贝塞尔曲线是如何用于映射时间值的。因此，我们先来探讨这一点。

三次贝塞尔曲线由以下参数方程描述：

```objc
F(t) = (1 - t)<sup>3</sup>P<sub>0</sub> + 3t(1 - t)<sup>2</sup>P<sub>1</sub> + 3t<sup>2</sup>(1 - t)P<sub>2</sub> + t<sup>3</sup>P<sub>3</sub>
```

其中，贝塞尔曲线由四个控制点（control point）P~0、P~1、P~2 和 P~3 指定（每个点都是一对坐标——X 坐标和 Y 坐标），参数 "t" 从 P~0 处的零移动到 P~3 处的一（即 t ∈ [0, 1]）。整个函数为每个 t 值产生一个输出点 F（其中 F 包含一个 X 坐标和一个 Y 坐标，与每个 P 值一样）。

CAMediaTimerFunction *不*将输入时间用作该方程中的 "t" 值。相反，输入时间被用作 F 的 X 值，而输出时间则通过求解相同 "t" 点处的 F 的 Y 值来获得。这比直接使用 "t" 作为输入值更灵活，但计算上更复杂，因为你必须求解三次方程。

## CAMediaTimerFunction 无法做到的事情

由于它使用三次贝塞尔曲线，CAMediaTimerFunction 只能提供可由三阶多项式描述的时间映射。

这意味着以下映射是可以实现的：

- 恒定斜率映射
- 二次映射（抛物线）
- 三次映射（包括简单的 "s" 形曲线）

但以下映射无法实现：

- 指数
- 正弦波
- 高于三阶的多项式

## 解决方案：CAKeyframeAnimation

[CAKeyframeAnimation](http://developer.apple.com/documentation/GraphicsImaging/Reference/CAKeyframeAnimation_class/Introduction/Introduction.html) 类允许我们指定动画路径上的每一个点。如果我们生成足够多的关键帧（keyframe），就可以模拟任何我们想要的方程。这样，我们就可以克服 CAMediaTimerFunction 的限制——我们使用线性的匀速时间，但通过分布关键帧来实现相同的效果。

为了解决这个问题，我们需要重新创建 CAMediaTimerFunction 的参数化映射特性，但使用任意我们选择的映射函数。

## 示例应用：AnimationAcceleration

下载 [「AnimationAcceleration」示例应用](https://www.cocoawithlove.com/assets/objc-era/AnimationAcceleration.zip)。它是一个 XCode 3.1 项目，但应该能在 XCode 3.0 或更高版本中正确加载。

该示例应用展示了如何使用参数化函数生成关键帧，以便红点以不同的加速度比率沿其线性路径（屏幕左侧的垂直轴）移动。底部的灰点以恒定速度移动，标志着时间。

![](https://www.cocoawithlove.com/assets/objc-era/animationaccelerationscreenshot.png)

所使用的加速曲线包括：

- _线性_

- _Ease-in/Ease-out_

- _二次_

- _指数衰减_

- _二阶响应曲线_

在程序中，每条曲线都由一个实现了 `evaluateAt:` 方法的 `NSObject<Evaluate>` 对象进行参数化描述。CAKeyframeAnimation 的子类（subclass）AccelerationAnimation 随后实现了以下方法，使用该方法的结果来生成所有关键帧值。

```objc
- (void)calculateKeyFramesWithEvaluationObject:(NSObject<Evaluate> *)evaluationObject
    startValue:(double)startValue
    endValue:(double)endValue
    interstitialSteps:(NSUInteger)steps
{
    NSUInteger count = steps + 2;
    
    NSMutableArray *valueArray = [NSMutableArray arrayWithCapacity:count];

    double progress = 0.0;
    double increment = 1.0 / (double)(count - 1);
    NSUInteger i;
    for (i = 0; i < count; i++)
    {
        double value =
            startValue +
            [evaluationObject evaluateAt:progress] * (endValue - startValue);
        [valueArray addObject:[NSNumber numberWithDouble:value]];
        
        progress += increment;
    }
    
    [self setValues:valueArray];
}
```

此方法生成的关键帧值适用于单属性（property）动画（在本例中，是红点的 `"position.y"` 坐标）。如果你想在二维中进行动画（例如，使用 `"position"` 而不是 `"position.y"`），你可以实现一个类似的方法，该方法接受 `startValue` 和 `endValue` 作为 `NSPoint`，并对 X 和 Y 坐标执行类似的参数化插值。

该动画被应用于 acceleratedDot（红点）图层（layer），如下所示：

```objc
[CATransaction begin];
[CATransaction
    setValue:[NSNumber numberWithFloat:2.5]
    forKey:kCATransactionAnimationDuration];
AccelerationAnimation *animation =
    [AccelerationAnimation
        animationWithKeyPath:@"position.y"
        startValue:[self originPoint].y
        endValue:[self maxYPoint].y
        evaluationObject:[currentConfiguration objectForKey:@"evaluator"]
        interstitialSteps:INTERSTITIAL_STEPS];
[animation setDelegate:self];
[[acceleratedDot layer]
    setValue:[NSNumber numberWithDouble:[self maxYPoint].y]
    forKeyPath:@"position.y"];
[[acceleratedDot layer] addAnimation:animation forKey:@"position"];
[CATransaction commit];
```

其中，`originPoint` 和 `maxYPoint` 方法返回红点路径的两个端点。目标点通过 `setValue:forKeyPath:` 应用，以便在 AccelerationAnimation 完成后，对象将保持在目标位置。

## 结论

Core Animation 主要面向简单的点对点过渡（transition）的[隐式](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreAnimation_guide/Articles/AnimatingLayers.html#//apple_ref/doc/uid/TP40006085-SW7)动画——这并非坏事，因为这是绝大多数常见情况。

沿复杂路径（在本例中，是沿时间维度的复杂路径）的显式动画需要编写更多的代码。你还必须决定需要多少个关键帧才能实现平滑的路径。然而，使用 CAKeyframeAnimation 的参数化动画为你打开了任何想要的加速曲线的大门，并且你仍然能获得 Core Animation 其余部分的优势（CALayer、单独的动画线程（thread）、NSView 集成等）。
