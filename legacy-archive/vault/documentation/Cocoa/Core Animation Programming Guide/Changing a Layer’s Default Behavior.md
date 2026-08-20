---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/ReactingtoLayerChanges/ReactingtoLayerChanges.html
archived_at: '2026-07-15T07:14:07.974591Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Improving%20Animation%20Performance.md)[上一页](Advanced%20Animation%20Tricks.md)

# 更改图层的默认行为

Core Animation 通过动作（action）对象来实现图层的隐式动画行为。动作对象是遵循 [CAAction](https://developer.apple.com/documentation/quartzcore/caaction) 协议的对象，它定义了要在图层上执行的某种相关行为。所有 `CAAnimation` 对象都实现了这个协议，通常正是这些对象被指定为在图层属性发生变化时执行。

为属性添加动画只是动作的一种类型，你几乎可以定义任意行为的动作。不过要做到这一点，你必须定义自己的动作对象，并把它们和你应用的图层对象关联起来。

要创建自己的动作对象，需要让某个类采纳 `CAAction` 协议，并实现 [runActionForKey:object:arguments:](https://developer.apple.com/documentation/quartzcore/caaction/1410806-run) 方法。在该方法中，利用可用的信息在图层上执行你想要的任何操作。你可以用这个方法给图层添加一个动画对象，也可以用它来执行其他任务。

定义动作对象时，你必须确定希望该动作以何种方式被触发。动作的触发条件决定了你之后用来注册该动作的键。动作对象可以由以下任意一种情况触发：

- 图层的某个属性值发生了变化。这可以是图层的任意属性，而不仅限于可动画的属性。（你也可以为自己给图层添加的自定义属性关联动作。）标识该动作的键就是属性的名称。
- 图层变为可见，或者被添加到图层层级结构中。标识该动作的键是 [kCAOnOrderIn](https://developer.apple.com/documentation/quartzcore/kcaonorderin)。
- 图层从图层层级结构中被移除。标识该动作的键是 [kCAOnOrderOut](https://developer.apple.com/documentation/quartzcore/kcaonorderout)。
- 图层即将参与一个过渡动画。标识该动作的键是 [kCATransition](https://developer.apple.com/documentation/quartzcore/kcatransition)。

在动作能够被执行之前，图层需要先找到与之对应、要执行的动作对象。与图层相关的动作所使用的键，要么是被修改属性的名称，要么是标识该动作的一个特殊字符串。当图层上发生了合适的事件时，图层会调用它的 [actionForKey:](https://developer.apple.com/documentation/quartzcore/calayer/1410844-action) 方法，来查找与该键关联的动作对象。你的应用可以在这个查找过程的几个环节中介入，为该键提供相应的动作对象。

Core Animation 会按照以下顺序查找动作对象：

1. 如果图层有委托，并且该委托实现了 [actionForLayer:forKey:](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097264-action) 方法，图层就会调用这个方法。委托必须执行以下操作之一：

   - 返回给定键对应的动作对象。
   - 如果不处理该动作，返回 `nil`，此时查找会继续进行。
   - 返回 [NSNull](https://developer.apple.com/documentation/foundation/nsnull) 对象，此时查找会立即结束。
2. 图层在自己的 [actions](https://developer.apple.com/documentation/quartzcore/calayer/1410789-actions) 字典中查找给定的键。
3. 图层在 [style](https://developer.apple.com/documentation/quartzcore/calayer/1410875-style) 字典中查找一个包含该键的 actions 字典。（换句话说，`style` 字典中包含一个 `actions` 键，其值也是一个字典，图层会在这个第二层字典中查找给定的键。）
4. 图层调用它的 [defaultActionForKey:](https://developer.apple.com/documentation/quartzcore/calayer/1410954-defaultactionforkey) 类方法。
5. 图层执行 Core Animation 定义的隐式动作（如果有的话）。

如果你在任何一个合适的查找环节提供了动作对象，图层就会停止查找，并执行返回的那个动作对象。图层找到动作对象后，会调用该对象的 [runActionForKey:object:arguments:](https://developer.apple.com/documentation/quartzcore/caaction/1410806-run) 方法来执行这个动作。如果你为某个键定义的动作本身就是 `CAAnimation` 类的实例，你可以使用该方法的默认实现来执行动画。如果你定义的是遵循 `CAAction` 协议的自定义对象，就必须使用你自己对象中实现的该方法，来执行合适的操作。

你把动作对象安装在哪里，取决于你打算如何修改图层。

- 对于只想在特定情况下应用的动作，或者已经在使用委托对象的图层，提供一个委托并实现它的 `actionForLayer:forKey:` 方法。
- 对于通常不使用委托的图层对象，把动作添加到图层的 `actions` 字典中。
- 对于与你在图层对象上定义的自定义属性相关的动作，把该动作放进图层的 `style` 字典中。
- 对于图层行为所固有的基础性动作，派生图层的子类并重写 [defaultActionForKey:](https://developer.apple.com/documentation/quartzcore/calayer/1410954-defaultactionforkey) 方法。

清单 6-1 展示了一个用于提供动作对象的委托方法实现。在这个例子中，委托会检测图层 [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) 属性的变化，并使用过渡动画把新内容替换进去。

__清单 6-1__  使用图层委托对象提供动作

```objc
- (id<CAAction>)actionForLayer:(CALayer *)theLayer
                        forKey:(NSString *)theKey {
    CATransition *theAnimation=nil;

    if ([theKey isEqualToString:@"contents"]) {

        theAnimation = [[CATransition alloc] init];
        theAnimation.duration = 1.0;
        theAnimation.timingFunction = [CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseIn];
        theAnimation.type = kCATransitionPush;
        theAnimation.subtype = kCATransitionFromRight;
    }
    return theAnimation;
}
```


你可以使用 [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction) 类临时禁用图层的动作。当你改变图层的属性时，Core Animation 通常会创建一个隐式事务对象来为这个改动添加动画。如果你不希望这个改动产生动画效果，可以创建一个显式事务，并把它的 [kCATransactionDisableActions](https://developer.apple.com/documentation/quartzcore/kcatransactiondisableactions) 属性设为 `true`，从而禁用隐式动画。清单 6-2 展示了一段代码，在把指定图层从图层树中移除时禁用了动画。

__清单 6-2__  临时禁用图层的动作

```objc
[CATransaction begin];
[CATransaction setValue:(id)kCFBooleanTrue
                 forKey:kCATransactionDisableActions];
[aLayer removeFromSuperlayer];
[CATransaction commit];
```

有关如何使用事务对象来管理动画行为的更多信息，请参阅[显式事务能让你更改动画参数](Advanced%20Animation%20Tricks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqobnknltg)。

[下一页](Improving%20Animation%20Performance.md)[上一页](Advanced%20Animation%20Tricks.md)

