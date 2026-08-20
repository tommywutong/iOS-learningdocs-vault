---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/AdvancedAnimationTricks/AdvancedAnimationTricks.html
archived_at: '2026-07-15T07:13:55.949204Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Changing%20a%20Layer%E2%80%99s%20Default%20Behavior.md)[上一页](Building%20a%20Layer%20Hierarchy.md)

# 高级动画技巧

配置基于属性的动画或关键帧动画的方式还有很多，可以让它们为你做更多的事情。需要同时或按顺序执行多个动画的应用，可以使用更高级的行为来同步这些动画的时间，或者把它们串联起来。你还可以使用其他类型的动画对象来创建视觉过渡效果和其他有趣的动画效果。

顾名思义，过渡（transition）动画对象会为图层创建一个带动画效果的视觉过渡。过渡对象最常见的用法，是协调一致地为一个图层的出现和另一个图层的消失添加动画。与基于属性的动画（只改变图层的某一个属性）不同，过渡动画操纵的是图层的缓存图像，可以创造出仅靠改变属性难以甚至无法实现的视觉效果。标准类型的过渡可以让你实现显露（reveal）、推入（push）、移动（move）或交叉淡化（crossfade）动画。在 OS X 上，你还可以使用 Core Image 滤镜来创建使用擦除、翻页、涟漪等其他效果类型的过渡，或者你自己设计的自定义效果。

要执行一个过渡动画，需要创建一个 [CATransition](https://developer.apple.com/documentation/quartzcore/catransition) 对象，并把它添加到参与过渡的图层上。你可以用这个过渡对象指定要执行的过渡类型，以及过渡动画的起点和终点。你也不必使用整段过渡动画：过渡对象允许你指定动画时使用的起始和结束进度值，这些值可以让你实现诸如从动画中点开始或结束等效果。

清单 5-1 展示了在两个视图之间创建带动画效果的推入（push）过渡所用的代码。在这个示例中，`myView1` 和 `myView2` 位于同一个父视图的相同位置，但目前只有 `myView1` 可见。这个推入过渡会让 `myView1` 向左滑出并逐渐消失直至隐藏，同时 `myView2` 从右侧滑入并变为可见。更新两个视图的 hidden 属性，可以确保动画结束时两个视图的可见性都是正确的。

__清单 5-1__  在 iOS 中为两个视图间的过渡添加动画

```objc
CATransition* transition = [CATransition animation];
transition.startProgress = 0;
transition.endProgress = 1.0;
transition.type = kCATransitionPush;
transition.subtype = kCATransitionFromRight;
transition.duration = 1.0;

// 将过渡动画添加到两个图层
[myView1.layer addAnimation:transition forKey:@"transition"];
[myView2.layer addAnimation:transition forKey:@"transition"];

// 最后，改变图层的可见性。
myView1.hidden = YES;
myView2.hidden = NO;
```

当两个图层参与同一个过渡时，你可以对两者使用同一个过渡对象，这样也能简化你需要编写的代码。不过，你也可以使用不同的过渡对象，而如果各图层的过渡参数不同，你就必须这样做。

清单 5-2 展示了如何在 OS X 上使用 Core Image 滤镜来实现过渡效果。用你想要的参数配置好滤镜之后，把它赋值给过渡对象的 [filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter) 属性即可。之后应用该动画的过程就和其他类型的动画对象相同了。

__清单 5-2__  在 OS X 上使用 Core Image 滤镜为过渡添加动画

```objc
// 创建 Core Image 滤镜，设置几个关键参数。
CIFilter* aFilter = [CIFilter filterWithName:@"CIBarsSwipeTransition"];
[aFilter setValue:[NSNumber numberWithFloat:3.14] forKey:@"inputAngle"];
[aFilter setValue:[NSNumber numberWithFloat:30.0] forKey:@"inputWidth"];
[aFilter setValue:[NSNumber numberWithFloat:10.0] forKey:@"inputBarOffset"];

// 创建过渡对象
CATransition* transition = [CATransition animation];
transition.startProgress = 0;
transition.endProgress = 1.0;
transition.filter = aFilter;
transition.duration = 1.0;

[self.imageView2 setHidden:NO];
[self.imageView.layer addAnimation:transition forKey:@"transition"];
[self.imageView2.layer addAnimation:transition forKey:@"transition"];
[self.imageView setHidden:YES];
```


时间是动画中很重要的一部分，使用 Core Animation 时，你可以通过 [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming) 协议的方法和属性，为动画指定精确的时间信息。有两个 Core Animation 类采纳了这个协议：`CAAnimation` 类采纳它，是为了让你能在动画对象中指定时间信息；`CALayer` 也采纳了它，是为了让你能为隐式动画配置一些与时间相关的特性，不过包装这些动画的隐式事务对象通常会提供默认的时间信息，并且优先生效。

在考虑时间和动画时，理解图层对象是如何处理时间的很重要。每个图层都有自己的本地时间，用来管理动画的时间。通常情况下，两个不同图层的本地时间足够接近，即使你为它们指定相同的时间值，用户也不会察觉到什么差异。然而，图层的本地时间可能会被它的父图层或者它自身的时间参数所改变。例如，改变图层的 [speed](https://developer.apple.com/documentation/quartzcore/camediatiming/1427647-speed) 属性，会使该图层（及其子图层）上动画的持续时间按比例发生变化。

为了帮助你确保时间值适用于某个特定图层，`CALayer` 类定义了 [convertTime:fromLayer:](https://developer.apple.com/documentation/quartzcore/calayer/1410821-converttime) 和 [convertTime:toLayer:](https://developer.apple.com/documentation/quartzcore/calayer/1410823-converttime) 方法。你可以使用这些方法把一个固定的时间值转换为某个图层的本地时间，或者把时间值从一个图层转换到另一个图层。这些方法会考虑到可能影响图层本地时间的媒体时间属性，并返回一个可以用于另一个图层的值。清单 5-3 展示了一个示例，你应该经常使用它来获取图层当前的本地时间。[CACurrentMediaTime](https://developer.apple.com/documentation/quartzcore/1395996-cacurrentmediatime) 函数是一个便捷函数，返回计算机当前的时钟时间，该方法会将其转换为图层的本地时间。

__清单 5-3__  获取图层当前的本地时间

```objc
CFTimeInterval localLayerTime = [myLayer convertTime:CACurrentMediaTime() fromLayer:nil];
```

一旦你得到了图层本地时间下的时间值，就可以用它来更新动画对象或图层中与时间相关的属性。借助这些时间属性，你可以实现一些有趣的动画行为，包括：

- 使用 [beginTime](https://developer.apple.com/documentation/quartzcore/camediatiming/1427654-begintime) 属性来设置动画的开始时间。通常情况下，动画会在下一个更新周期开始。你可以使用 `beginTime` 参数把动画的开始时间延后几秒。把两个动画串联起来的方法，就是把一个动画的开始时间设为和另一个动画的结束时间相同。

  如果你延迟了动画的开始时间，可能还需要把 [fillMode](https://developer.apple.com/documentation/quartzcore/camediatiming/1427656-fillmode) 属性设为 [kCAFillModeBackwards](https://developer.apple.com/documentation/quartzcore/camediatimingfillmode/1427660-backwards)。这种填充模式会让图层显示动画的起始值，即使图层树中的图层对象包含的是另一个值。如果不使用这种填充模式，你会在动画开始执行之前看到画面跳变到最终值。此外还有其他填充模式可用。
- [autoreverses](https://developer.apple.com/documentation/quartzcore/camediatiming/1427645-autoreverses) 属性会让动画按指定的持续时间执行一次，然后再返回到动画的起始值。你可以把这个属性和 [repeatCount](https://developer.apple.com/documentation/quartzcore/camediatiming/1427666-repeatcount) 属性结合起来，让动画在起始值和结束值之间来回运动。对于一个自动反转（autoreversing）的动画，把重复次数设为一个整数（比如 1.0）会让动画停在起始值上；再多加半步（比如把重复次数设为 1.5）则会让动画停在结束值上。
- 在动画组中使用 [timeOffset](https://developer.apple.com/documentation/quartzcore/camediatiming/1427650-timeoffset) 属性，可以让某些动画比其他动画更晚开始。

要暂停一个动画，你可以利用图层采纳了 [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming) 协议这一点，把图层动画的速度设为 `0.0`。把速度设为零会暂停动画，直到你把该值改回一个非零值为止。清单 5-4 展示了一个简单的示例，说明之后如何暂停和恢复动画。

__清单 5-4__  暂停和恢复图层的动画

```objc
-(void)pauseLayer:(CALayer*)layer {
   CFTimeInterval pausedTime = [layer convertTime:CACurrentMediaTime() fromLayer:nil];
   layer.speed = 0.0;
   layer.timeOffset = pausedTime;
}

-(void)resumeLayer:(CALayer*)layer {
   CFTimeInterval pausedTime = [layer timeOffset];
   layer.speed = 1.0;
   layer.timeOffset = 0.0;
   layer.beginTime = 0.0;
   CFTimeInterval timeSincePause = [layer convertTime:CACurrentMediaTime() fromLayer:nil] - pausedTime;
   layer.beginTime = timeSincePause;
}
```


你对图层所做的每一次改动，都必须是某个事务（transaction）的一部分。[CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction) 类负责管理动画的创建、分组，以及在合适的时间执行它们。在大多数情况下，你不需要自己创建事务：只要你向某个图层添加显式或隐式动画，Core Animation 就会自动创建一个隐式事务。不过，你也可以创建显式事务，来更精确地管理这些动画。

你可以使用 `CATransaction` 类的方法来创建和管理事务。调用 [begin](https://developer.apple.com/documentation/quartzcore/catransaction/1448282-begin) 类方法可以开始（并隐式创建）一个新事务；调用 [commit](https://developer.apple.com/documentation/quartzcore/catransaction/1448255-commit) 类方法可以结束该事务。这两次调用之间就是你希望成为该事务一部分的改动。例如，要改变图层的两个属性，你可以使用清单 5-5 中的代码。

__清单 5-5__  创建一个显式事务

```objc
[CATransaction begin];
theLayer.zPosition=200.0;
theLayer.opacity=0.0;
[CATransaction commit];
```

使用事务的一个主要原因是，在一个显式事务的范围内，你可以改变持续时间、时间函数以及其他参数。你还可以为整个事务指定一个完成 block，这样应用就能在这组动画执行完毕时得到通知。要改变动画参数，需要使用 [setValue:forKey:](https://developer.apple.com/documentation/quartzcore/catransaction/1448278-setvalue) 方法修改事务字典中相应的键。例如，要把默认持续时间改为 10 秒，你需要修改 [kCATransactionAnimationDuration](https://developer.apple.com/documentation/quartzcore/kcatransactionanimationduration) 键，如清单 5-6 所示。

__清单 5-6__  改变动画的默认持续时间

```objc
[CATransaction begin];
[CATransaction setValue:[NSNumber numberWithFloat:10.0f]
                 forKey:kCATransactionAnimationDuration];
// 执行动画
[CATransaction commit];
```

在需要为不同的动画组提供不同默认值的情况下，你可以嵌套事务。要在一个事务内部嵌套另一个事务，只需再次调用 `begin` 类方法。每一次 `begin` 调用都必须有对应的 `commit` 方法调用与之匹配。只有当最外层事务的改动被提交之后，Core Animation 才会开始执行相关的动画。

清单 5-7 展示了一个事务嵌套在另一个事务内部的示例。在这个示例中，内层事务改变了和外层事务相同的动画参数，但使用了不同的值。

__清单 5-7__  嵌套显式事务

```objc
[CATransaction begin]; // 外层事务

// 将动画持续时间改为两秒
[CATransaction setValue:[NSNumber numberWithFloat:2.0f]
                forKey:kCATransactionAnimationDuration];
// 将图层移动到新位置
theLayer.position = CGPointMake(0.0,0.0);

[CATransaction begin]; // 内层事务
// 将动画持续时间改为五秒
[CATransaction setValue:[NSNumber numberWithFloat:5.0f]
                 forKey:kCATransactionAnimationDuration];

// 改变 zPosition 和 opacity
theLayer.zPosition=200.0;
theLayer.opacity=0.0;

[CATransaction commit]; // 内层事务

[CATransaction commit]; // 外层事务
```


应用可以在三维空间中操纵图层，但为简单起见，Core Animation 使用平行投影来显示图层，这实际上会把场景压平成一个二维平面。这种默认行为会导致尺寸相同但 [zPosition](https://developer.apple.com/documentation/quartzcore/calayer/1410884-zposition) 值不同的图层显示为相同大小，即使它们在 z 轴上相距很远。你在三维空间中观察这样一个场景时通常会有的透视效果也随之消失了。不过，你可以通过修改图层的变换矩阵、加入透视信息来改变这种行为。

要修改一个场景的透视效果，你需要修改包含所查看图层的父图层（superlayer）的 [sublayerTransform](https://developer.apple.com/documentation/quartzcore/calayer/1410888-sublayertransform) 矩阵。修改父图层可以把相同的透视信息应用到所有子图层上，从而简化你需要编写的代码；这样做还能确保透视效果正确应用到彼此在不同平面上重叠的同级子图层上。

清单 5-8 展示了如何为一个父图层创建简单的透视变换。这里自定义的 `eyePosition` 变量指定了观察图层时沿 z 轴的相对距离。通常你会为 `eyePosition` 指定一个正值，以让图层保持预期的朝向。数值越大，场景看起来越平坦；数值越小，图层之间的视觉差异就越明显。

__清单 5-8__  为父图层添加透视变换

```objc
CATransform3D perspective = CATransform3DIdentity;
perspective.m34 = -1.0/eyePosition;

// 将变换应用到父图层。
myParentLayer.sublayerTransform = perspective;
```

配置好父图层之后，你可以改变任意子图层的 `zPosition` 属性，观察它们的大小如何随着与观察点（eye position）相对距离的变化而变化。

[下一页](Changing%20a%20Layer%E2%80%99s%20Default%20Behavior.md)[上一页](Building%20a%20Layer%20Hierarchy.md)

