---
title: iOS：重识Transform和frame
source_url: 'https://www.jianshu.com/p/e1fec2f92c63'
source_domain: jianshu.com
source_group: platform
original_language: zh
published: 2017-12-21
archived_at: 2026-07-27
content_hash: 'sha256:bb58ecb8a6563ef8'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08）
container: //article
container_source: map
---

> 原文：[iOS：重识Transform和frame](https://www.jianshu.com/p/e1fec2f92c63)

### 关于frame

- frame是一个复合属性，由center、bounds和transform共同计算而来。
- transform改变，frame会受到影响，但是center和bounds不会受到影响。也就是你使用transform来缩放，bounds是不会变的。那么由center和bounds计算得到的frame是永远保持transform为`identity`时的状态。这也是为什么把transform设为`identity`后，view会回归到最初状态。

### 关于transform的计算

当你使用`view.transform = xxx`时候，它到底是怎么起作用的？首先，它是一个矩阵，使用矩阵乘法，对view的frame进行变换，得到新的变换，那么这个逻辑是怎样的？

- 它是针对父视图坐标的。
- 它是针对view的初始中心为坐标的：“初始”是指transform值为`identity`时的状态，即没有任何的缩放、平移或旋转；“中心”默认是view方块的中心，但实际是`anchorPoint`。

**那么`viewA.transform = myTransform`这么一段代码就等价于：**

1. 把父视图坐标系的原点移动到view的中心，计算中心坐标系的frame,得到frame1:

```
CGRect frame1 = CGRectMake(
-originalFrame2.size.width/2.0,
-originalFrame2.size.height/2.0, 
originalFrame2.size.width, 
originalFrame2.size.height);
```

1. 以坐标系改变后的frame(即centerFrame)计算，使用矩阵乘法应用transform,得到frame2：`CGRect frame2 = CGRectApplyAffineTransform(frame2, myTransform)`
2. 再把结果转回原父视图坐标系,得到frame3：

```
CGRect frame3 = CGRectMake(
frame2.origin.x + CGRectGetMidX(originalFrame), 
frame2.origin.y + CGRectGetMidY(originalFrame),
frame2.size.width, 
frame2.size.height);
```

这么做的好处便是在缩放的时候，是针对view当前位置的，这样view的原点不会改变，也就是缩放只会产生缩放的效果，而不会产生平移。假设使用父视图原点，frame为{10,20,100,100},缩放后变成{5,10,50,50},那么frame不仅变小了，也和原点更近了。

### 怎么计算两个frame之间的transform

给你一个view和一个目标frame，求一个transform，使得把这个transform给view后，view的frame等于目标frame。

在处理动画的时候会用到。

因为缩放会影响平移，而平移却不会影响缩放，所以先平移到中心和目标frame一致，然后缩放。

平移的距离就是两个center的差值，缩放比例的就是两个frame的边长之比。

即：

```
-(CGAffineTransform)transformFromRect:(CGRect)fromRect toRect:(CGRect)toRect{
     CGAffineTransform moveTrans = CGAffineTransformMakeTranslation(CGRectGetMidX(toRect) - CGRectGetMidX(fromRect), CGRectGetMidY(toRect) - CGRectGetMidY(fromRect));
   
     CGAffineTransform scaleTrans = CGAffineTransformMakeScale(toRect.size.width / fromRect.size.width, toRect.size.height / fromRect.size.height);
   
     //右边先执行
     return CGAffineTransformConcat(scaleTrans, moveTrans);
}
```

### 为什么使用transform动画而不是设置frame?

如果transform里包含了旋转，那么计算出来的frame就没有意义了，因为frame总是描述一个“摆正的”方块，而旋转后的方块是没法描述的。

但对于只有平移和缩放，用上述逻辑是可以计算的。我在做一个过场动画的时候用到了这个，动画是类似系统相册那样从一个小图逐渐放大到全屏，所以你拥有的信息是一个起始的frame，以这个为开始动画。

我尝试了通过直接设置frame来执行动画，但发现效果糟糕，**因为动画虽然有一个过程，但其实从动画一开始，frame就已经修改了。如果直接设置frame，那么开始的时候，子视图就会按变化后的frame来重新布局，而不是跟随父视图一起慢慢变化**。

动画是渲染呈现上的样子，而实际的数值却是另一种样子，在core animation里有_模型树_和_呈现树_的区别。

举个例子：

设置frame的动画

设置transform的动画

测试view是灰色，它有一个子视图是红色：

```
-(void)layoutSubviews{
    innerView.frame = CGRectMake(10, 10, self.frame.size.width-20, self.frame.size.height-20);
}
```

内部的view保持和父视图10的边距。所以看第一个动画，在刚开始的时候，红色的view就变成了动画结束时的大小，而第二个动画使用transform变换，其实`layoutSubviews`并没有调用，但是却得到了想要的效果。貌似transform只是影响了view的渲染，而且是影响了整个的子视图数，就像把这个view当做一张图片一样缩小了，而内部却不需要重新布局。

使用transform效果更好，那么就要从一个初始frame计算得到transform，使得赋值给view后，它就是到初始frame的位置。所以就有了上面的transform计算。
