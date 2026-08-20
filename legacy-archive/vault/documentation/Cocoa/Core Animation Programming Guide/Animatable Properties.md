---
title: Core Animation 编程指南
apple_id: TP40004514
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/AnimatableProperties/AnimatableProperties.html
archived_at: '2026-07-15T07:13:55.960457Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Core Animation 编程指南](About%20Core%20Animation.md)


[下一页](Key-Value%20Coding%20Extensions.md)[上一页](Layer%20Style%20Property%20Animations.md)

# 可动画属性

`CALayer` 和 `CIFilter` 中的许多属性都可以进行动画处理。本附录列出了这些属性，以及默认情况下使用的动画。

表 B-1 列出了 `CALayer` 类中你可能会考虑进行动画处理的属性。对于每个属性，该表还列出了为执行隐式动画而创建的默认动画对象的类型。

__表 B-1__  图层属性及其默认动画

| Property | Default animation |
| --- | --- |
| [anchorPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410817-anchorpoint) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [backgroundColor](https://developer.apple.com/documentation/quartzcore/calayer/1410966-backgroundcolor) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [backgroundFilters](https://developer.apple.com/documentation/quartzcore/calayer/1410827-backgroundfilters) | 使用默认隐式 [CATransition](https://developer.apple.com/documentation/quartzcore/catransition) 对象，具体说明参见[表 B-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomy)。滤镜的子属性使用默认隐式 `CABasicAnimation` 对象进行动画处理，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [borderColor](https://developer.apple.com/documentation/quartzcore/calayer/1410903-bordercolor) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [borderWidth](https://developer.apple.com/documentation/quartzcore/calayer/1410917-borderwidth) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [bounds](https://developer.apple.com/documentation/quartzcore/calayer/1410915-bounds) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter) | 使用默认隐式 [CATransition](https://developer.apple.com/documentation/quartzcore/catransition) 对象，具体说明参见[表 B-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomy)。滤镜的子属性使用默认隐式 `CABasicAnimation` 对象进行动画处理，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [contentsRect](https://developer.apple.com/documentation/quartzcore/calayer/1410866-contentsrect) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [cornerRadius](https://developer.apple.com/documentation/quartzcore/calayer/1410818-cornerradius) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [doubleSided](https://developer.apple.com/documentation/quartzcore/calayer/1410924-isdoublesided) | 没有默认的隐式动画。 |
| [filters](https://developer.apple.com/documentation/quartzcore/calayer/1410901-filters) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。滤镜的子属性使用默认隐式 `CABasicAnimation` 对象进行动画处理，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [frame](https://developer.apple.com/documentation/quartzcore/calayer/1410779-frame) | 该属性不可动画化。你可以通过对 [bounds](https://developer.apple.com/documentation/quartzcore/calayer/1410915-bounds) 和 [position](https://developer.apple.com/documentation/quartzcore/calayer/1410791-position) 属性进行动画处理来达到同样的效果。 |
| [hidden](https://developer.apple.com/documentation/quartzcore/calayer/1410838-ishidden) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [mask](https://developer.apple.com/documentation/quartzcore/calayer/1410861-mask) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [masksToBounds](https://developer.apple.com/documentation/quartzcore/calayer/1410896-maskstobounds) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [opacity](https://developer.apple.com/documentation/quartzcore/calayer/1410933-opacity) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [position](https://developer.apple.com/documentation/quartzcore/calayer/1410791-position) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [shadowColor](https://developer.apple.com/documentation/quartzcore/calayer/1410829-shadowcolor) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [shadowOffset](https://developer.apple.com/documentation/quartzcore/calayer/1410970-shadowoffset) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [shadowOpacity](https://developer.apple.com/documentation/quartzcore/calayer/1410751-shadowopacity) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [shadowPath](https://developer.apple.com/documentation/quartzcore/calayer/1410771-shadowpath) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [shadowRadius](https://developer.apple.com/documentation/quartzcore/calayer/1410819-shadowradius) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [sublayers](https://developer.apple.com/documentation/quartzcore/calayer/1410802-sublayers) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [sublayerTransform](https://developer.apple.com/documentation/quartzcore/calayer/1410888-sublayertransform) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [transform](https://developer.apple.com/documentation/quartzcore/calayer/1410836-transform) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |
| [zPosition](https://developer.apple.com/documentation/quartzcore/calayer/1410884-zposition) | 使用默认隐式 [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) 对象，具体说明参见[表 B-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjufvbuqmjrfvjvomq)。 |

表 B-2 列出了默认的基于属性动画的动画属性。

__表 B-2__  默认隐式基本动画

| Description | Value |
| --- | --- |
| Class | [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation) |
| Duration | 0.25 秒，或当前事务的持续时间 |
| Key path | 设置为图层的属性名称。 |

表 B-3 列出了默认的基于过渡动画的动画对象配置。

__表 B-3__  默认隐式过渡

| Description | Value |
| --- | --- |
| Class | [CATransition](https://developer.apple.com/documentation/quartzcore/catransition) |
| Duration | 0.25 秒，或当前事务的持续时间 |
| Type | 淡入淡出（`kCATransitionFade`） |
| Start progress | `0.0` |
| End progress | `1.0` |

Core Animation 为 Core Image 的 [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter) 类添加了以下可动画属性。这些属性仅在 OS X 上可用。

- [name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)
- [enabled](https://developer.apple.com/documentation/coreimage/cifilter/1438276-enabled)

关于这些新增内容的更多信息，请参阅 _CIFilter Core Animation Additions_。

[下一页](Key-Value%20Coding%20Extensions.md)[上一页](Layer%20Style%20Property%20Animations.md)

