---
title: 动画类型与时间控制编程指南
apple_id: TP40006166
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2010-05-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Animation_Types_Timing/Articles/TransitionAnimations.html
archived_at: '2026-07-15T05:25:28.394796Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [动画类型与时间控制编程指南](Introduction%20to%20Animation%20Types%20and%20Timing%20Programming%20Guide.md)


[下一页](Document%20Revision%20History.md)[上一页](Property-Based%20Animations.md)

# 过渡动画

当无法在数学上对改变图层（layer）属性值所产生的效果、或者图层在图层树中的状态变化进行插值（interpolation）时，就要用到过渡（transition）动画。

本章讨论 Core Animation 提供的过渡动画功能。

`CATransition` 类为 Core Animation 提供过渡功能。它是 `CAAnimation` 的直接子类，因为它影响的是整个图层，而不是图层的某个特定属性。

`CATransition` 的新实例通过继承来的类方法 `animation` 创建。这会创建一个过渡动画，其默认值如表 1 所示：

__表 1__  `CATransition` 属性的默认值

| 过渡属性 | 取值 |
| --- | --- |
| `type` | 使用淡入淡出过渡。取值为 [kCATransitionFade](https://developer.apple.com/documentation/quartzcore/kcatransitionfade)。 |
| `subType` | 不适用。 |
| `duration` | 使用当前事务的时长；若事务未设置时长，则使用 0.25 秒。取值为 0.0 |
| `timingFunction` | 使用线性节奏。取值为 `nil`。 |
| `startProgress` | 0.0 |
| `endProgress` | 1.0 |

创建之后，你可以用某种预定义的过渡类型来配置这个过渡动画；在 OS X 上，你也可以用 Core Image 滤镜创建自定义过渡。

要使用预定义的过渡，把 `type` 属性设为表 2 中的某个常量即可。

__表 2__  常见的过渡类型

| 过渡类型 | 说明 |
| --- | --- |
| [kCATransitionFade](https://developer.apple.com/documentation/quartzcore/kcatransitionfade) | 图层在变为可见或隐藏时淡入淡出。 |
| [kCATransitionMoveIn](https://developer.apple.com/documentation/quartzcore/catransitiontype/1412487-movein) | 图层滑入到位，覆盖在任何已有内容之上。 |
| [kCATransitionPush](https://developer.apple.com/documentation/quartzcore/catransitiontype/1412528-push) | 图层在滑入到位的同时把任何已有内容推走 |
| [kCATransitionReveal](https://developer.apple.com/documentation/quartzcore/catransitiontype/1412489-reveal) | 图层按过渡子类型指定的方向逐渐显露出来。 |

除 `kCATransitionFade` 之外，这些预定义的过渡类型还允许你通过把 `subType` 属性设为表 3 中的某个常量来指定过渡的方向。

__表 3__  常见的过渡子类型

| 过渡子类型常量 | 说明 |
| --- | --- |
| [kCATransitionFromRight](https://developer.apple.com/documentation/quartzcore/kcatransitionfromright) | 过渡从图层的右侧开始。 |
| [kCATransitionFromLeft](https://developer.apple.com/documentation/quartzcore/catransitionsubtype/1412459-fromleft) | 过渡从图层的左侧开始。 |
| [kCATransitionFromTop](https://developer.apple.com/documentation/quartzcore/kcatransitionfromtop) | 过渡从图层的顶部开始。 |
| [kCATransitionFromBottom](https://developer.apple.com/documentation/quartzcore/kcatransitionfrombottom) | 过渡从图层的底部开始。 |

`startProgress` 属性允许你通过设置一个表示整段动画进度比例的值来改变过渡的起点。例如，若要让过渡从其进度的一半处开始，就把 `startProgress` 设为 0.5。同样，你也可以为过渡指定 `endProgress` 值。`endProgress` 表示过渡应当在整段过渡的哪个进度比例处停止。这两个属性的默认值分别是 0.0 和 1.0。

如果预定义的过渡无法提供你想要的视觉效果，而你的应用程序面向的是 OS X 而非 iOS，那么你可以指定一个自定义的 Core Image 滤镜对象来显示该过渡。自定义滤镜必须同时支持 `kCIInputImageKey` 和 `kCIInputTargetImageKey` 这两个输入键，以及 `kCIOutputImageKey` 输出键。该滤镜还可以选择性地支持 `kCIInputExtentKey` 输入键，该键被设为一个矩形，用于描述过渡应在其中运行的区域。

[下一页](Document%20Revision%20History.md)[上一页](Property-Based%20Animations.md)

