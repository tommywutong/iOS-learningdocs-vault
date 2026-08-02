---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/ImprovingAnimationPerformance/ImprovingAnimationPerformance.html
archived_at: '2026-07-15T07:14:02.860526Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Layer%20Style%20Property%20Animations.md)[上一页](Changing%20a%20Layer%E2%80%99s%20Default%20Behavior.md)

# 提升动画性能

Core Animation 是提升 app 动画帧率的绝佳方式，但使用它并不能保证性能一定会提升。尤其是在 OS X 中，你仍然需要就如何最有效地使用 Core Animation 的各项行为做出选择。而且，与所有性能相关的问题一样，你应当使用 Instruments 持续测量并跟踪 app 的性能，以确保性能在不断改善而不是出现退步。

[NSView](https://developer.apple.com/documentation/appkit/nsview) 类的默认重绘策略即使在该视图是 layer-backed 的情况下，也会保留该类原本的绘制行为。如果你的 app 中使用了 layer-backed 视图，就应该检查各种重绘策略的选择，并挑选出能为你的 app 带来最佳性能的那一种。在大多数情况下，默认策略并不是最可能带来最佳性能的选项。相反，[NSViewLayerContentsRedrawOnSetNeedsDisplay](https://developer.apple.com/documentation/appkit/nsviewlayercontentsredrawpolicy/nsviewlayercontentsredrawonsetneedsdisplay) 策略更有可能减少 app 所做的绘制工作量，从而提升性能。对于特定类型的视图，其他策略也可能带来更好的性能。

关于视图重绘策略的更多信息，请参阅 [OS X 视图的图层重绘策略会影响性能](Setting%20Up%20Layer%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvomrs)。

在 OS X v10.8 及更高版本中，视图有两种方式来更新底层图层的内容。在 OS X v10.7 及更早版本中更新 layer-backed 视图时，图层会把视图 `drawRect:` 方法中的绘制指令捕获到背后的位图图像中。缓存绘制指令是有效的，但并不是在所有情况下都是最高效的选择。如果你知道如何在不实际渲染的情况下直接提供图层的内容，就可以使用 [updateLayer](https://developer.apple.com/documentation/appkit/nsview/1483580-updatelayer) 方法来实现。

关于不同渲染路径的信息（包括涉及 `updateLayer` 方法的路径），请参阅 [使用委托提供图层的内容](Setting%20Up%20Layer%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjtfvjvomju)。

有几种方法可以让你的图层实现变得更高效。不过，与所有此类优化一样，你应当先测量代码当前的性能，然后再尝试优化。这样你才能得到一个基准，用来判断优化是否真正起到了作用。

把图层的 [opaque](https://developer.apple.com/documentation/quartzcore/calayer/1410763-isopaque) 属性设置为 `YES`，可以让 Core Animation 知道它不需要为该图层维护 alpha 通道。没有 alpha 通道意味着合成器不需要将图层的内容与其背景内容进行混合，从而在渲染时节省时间。不过，这个属性主要适用于属于 layer-backed 视图一部分的图层，或者由 Core Animation 创建底层图层位图的情况。如果你直接把一张图像赋值给图层的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性，那么无论 `opaque` 属性的值是什么，该图像的 alpha 通道都会被保留。

[CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer) 类会在合成时，把你提供的路径渲染到一张位图图像中来生成其内容。这样做的优点是，图层总能以最佳可能的分辨率绘制该路径，但这个优点也伴随着额外渲染时间的代价。如果你提供的路径很复杂，栅格化该路径的开销可能会变得过高。而且，如果图层的尺寸频繁变化（因而必须频繁重绘），绘制所花费的时间累积起来可能会成为性能瓶颈。

减少形状图层绘制时间的一种方法，是把复杂的形状拆分成更简单的形状。使用更简单的路径，并在合成器中把多个 `CAShapeLayer` 对象层层叠加，可能会比绘制一个巨大而复杂的路径快得多。这是因为绘制操作发生在 CPU 上，而合成操作发生在 GPU 上。不过，与所有这类简化手段一样，潜在的性能收益取决于你的具体内容。因此，在优化之前先测量代码的性能就显得尤为重要，这样你才有一个可供比较的基准。

如果你在多个图层对象中使用同一张图像，就应该自己加载这张图像，并将其直接赋值给这些图层对象的 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性。把图像赋值给 `contents` 属性可以避免图层为后备存储分配内存。图层会转而使用你提供的图像作为它的后备存储。当多个图层使用同一张图像时，这意味着这些图层共享同一块内存，而不是各自分配一份图像的副本。

为了获得最佳效果，始终将图层对象的宽度和高度设置为整数值。尽管你是用浮点数来指定图层 bounds 的宽度和高度，但图层的 bounds 最终会被用来创建一张位图图像。为宽度和高度指定整数值，可以简化 Core Animation 创建和管理后备存储及其他图层信息所需完成的工作。

你在委托的 [drawLayer:inContext:](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097262-drawlayer) 方法或视图的 `drawRect:` 方法中所做的任何绘制，通常都是在 app 的主线程上同步执行的。不过，在某些情况下，同步绘制内容未必能带来最佳性能。如果你发现动画的表现不佳，可以尝试启用图层的 [drawsAsynchronously](https://developer.apple.com/documentation/quartzcore/calayer/1410974-drawsasynchronously) 属性，把这些操作转移到后台线程执行。这样做时，请确保你的绘制代码是线程安全的。而且一如既往，在把异步绘制方案投入生产代码之前，你应当先测量它的性能表现。

让 Core Animation 自行判断阴影的形状可能开销很大，并影响 app 的性能。与其让 Core Animation 判断阴影的形状，不如使用 `CALayer` 的 [shadowPath](https://developer.apple.com/documentation/quartzcore/calayer/1410771-shadowpath) 属性显式指定阴影的形状。当你为这个属性指定一个路径对象后，Core Animation 会使用该形状来绘制并缓存阴影效果。对于形状从不改变或很少改变的图层，这种做法能够减少 Core Animation 所需完成的渲染量，从而大幅提升性能。

[下一页](Layer%20Style%20Property%20Animations.md)[上一页](Changing%20a%20Layer%E2%80%99s%20Default%20Behavior.md)

