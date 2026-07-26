---
title: '[iOS] CALayer与UIView（以及离屏渲染浅谈）'
source_url: 'https://www.jianshu.com/p/e6d44ca9c103'
source_domain: jianshu.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:d0f1114dc55aa78c'
plan_ref: 第六周：UIKit 渲染、UITableView 与性能 / Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02）
plan_week: 第六周：UIKit 渲染、UITableView 与性能
plan_day: Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02）
container: //article
container_source: map
---

> 原文：[[iOS] CALayer与UIView（以及离屏渲染浅谈）](https://www.jianshu.com/p/e6d44ca9c103)

写iOS的第一天可能大部分coder都会接触到UIView，然后慢慢地当我们需要加圆角、做动画、加渐变的时候我们就会接触到CALayer，那么这两个东西到底有啥区别呢，CALayer是什么呢？

- 先说一下区别吧：  
  **UIView可以接受用户点击事件，传递响应**  
  **CALayer只负责内容呈现**

#### 1. CALayer定义

> Layers provide infrastructure for your views. Specifically, layers make it easier and more efficient to draw and animate the contents of views and maintain high frame rates while doing so. However, there are many things that layers do not do. Layers do not handle events, draw content, participate in the responder chain, or do many other things

翻译一下就是：  
 layer给view提供了基础设施，使得绘制内容和呈现更高效动画更容易、更低耗；layer不参与view的事件处理、不参与响应链

CALayer

所以UIView的backgroundColor也是属于CALayer的属性，我们来测试一下：  
 给一个UIView设置一个背景颜色，然后在控制台打印以下内容

```
po self.view.layer.backgroundColor
<CGColor 0x600003b25ec0> [<CGColorSpace 0x600003b32700> (kCGColorSpaceICCBased; kCGColorSpaceModelRGB; sRGB IEC61966-2.1; extended range)] ( 0.278901 0.278908 0.278904 1 )

po self.view.backgroundColor
UIExtendedSRGBColorSpace 0.278901 0.278908 0.278904 1
```

可以看出虽然我没有给CALayer设置背景颜色，但是UIView的backgroundColor就是CALayer的backgroundColor，下面我们尝试一下改变CALayer的backgroundColor，看UIView会有什么变化：

```
self.view.layer.backgroundColor = [UIColor blueColor].CGColor;

输出：
po self.view.backgroundColor
UIExtendedSRGBColorSpace 0 0 1 1

po self.view.layer.backgroundColor
<CGColor 0x6000002d7c00> [<CGColorSpace 0x6000002c8720> (kCGColorSpaceICCBased; kCGColorSpaceModelRGB; sRGB IEC61966-2.1; extended range)] ( 0 0 1 1 )
```

表现上看就是UIView的背景颜色变了，打断点然后打印UIView的背景色也的确是和CALayer的背景色一致，**所以其实UIView的背景色就是CALayer的背景色。**

> **那么CALayer究竟是神马呢？**  
>  CALayer其实就是负责UIView的显示的，它借助bitmap的形式缓存view的显示，当我们做动画之类的时候，它只要通过transform矩阵对bitmap简单的进行变换就可以改变view的显示，避免了不断计算view每一个像素的位置并重新绘制的性能消耗，只要对bitmap操作就好了。

#### 2. CALayer和UIView的关系及区别

> 其实他俩的区别很简单，就是layer不能处理事件，如果你希望通过addSublayer实现不同的显示层分别接收点击事件，都用layer是不能实现的，可是通过addSubview是可以实现view的点击分别处理的。

举个例子，如果在已有view的layer上面加一个长得和button很像的小layer，你是无法单独区分button的点击还是view自身的点击的，只能通过拿到坐标然后计算，这样非常麻烦的。

view和layer的关系

UIView和CALayer的关系大概就是view是layer的容器，并且借助了layer的很多属性（就像上面举例的backgroundColor），view是持有layer的，然后layer的delegate是view，因为如果layer的一些属性变化以后view也需要跟着变化。

---

- 总结一下区别与联系：

1. UIView可以响应事件，CALayer不可以。  
   UIView继承自UIResponder类，CALayer直接继承 NSObject，并没有相应的处理事件的接口。
2. UIView是CALayer的delegate
3. UIView主要处理事件，CALayer负责绘制
4. 每个UIView内部都有一个CALayer在背后提供内容的绘制和显示，并且UIView的尺寸样式都由内部的Layer所提供。两者都有树状层级结构，layer内部有subLayers，View内部有subViews，但是Layer比View多了个AnchorPoint

---

- 一个小问题，我们addSubview的时候干了啥嘞？

```
testView = [[UIView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];
testView.backgroundColor = [UIColor blueColor];

UIView *redView = [[UIView alloc] initWithFrame:CGRectMake(50, 50, 100, 100)];
redView.backgroundColor = [UIColor redColor];
[testView addSubview:redView];

CALayer *yellowLayer = [[CALayer alloc] init];
yellowLayer.frame = CGRectMake(50, 50, 100, 100);
yellowLayer.backgroundColor = [UIColor yellowColor].CGColor;
[testView.layer addSublayer:yellowLayer];

输出：
po testView.layer.sublayers
<CALayerArray 0x282b29aa0>(
<CALayer:0x28254cc20; position = CGPoint (100 100); bounds = CGRect (0 0; 100 100); delegate = <UIView: 0x104d53f20; frame = (50 50; 100 100); layer = <CALayer: 0x28254cc20>>; allowsGroupOpacity = YES; backgroundColor = <CGColor 0x280168ea0> [<CGColorSpace 0x280161380> (kCGColorSpaceICCBased; kCGColorSpaceModelRGB; sRGB IEC61966-2.1; extended range)] ( 1 0 0 1 ); _uikit_viewPointer = <UIView: 0x104d53f20; frame = (50 50; 100 100); layer = <CALayer: 0x28254cc20>>>,
<CALayer:0x28254d460; position = CGPoint (100 100); bounds = CGRect (0 0; 100 100); allowsGroupOpacity = YES; backgroundColor = <CGColor 0x280168000> [<CGColorSpace 0x280161380> (kCGColorSpaceICCBased; kCGColorSpaceModelRGB; sRGB IEC61966-2.1; extended range)] ( 1 1 0 1 )>
)
```

当我们给view addSubview以后可以看到它的layer的sublayers就增加了，所以其实addSubview就是给view的layer addSublayer，如果你再手动给view的layer再次addSublayer，就会挡住之前的subview。

#### 3. CALayer如何负责内容绘制的

CALayer的子类

CALayer有很多子类供我们使用，可以添加各种各样的效果addSublayer给view的layer，比如我们常见的渐变以及贝塞尔曲线，都是作为layer存在的。

当需要展示layer的时候，会依次看下面的方法有没有实现，如果实现了任何一个，就不继续向下询问了：

1. CALayer的display
2. CALayer delegate的displayLayer:
3. CALayer的drawInContext:
4. CALayer delegate的drawLayer:inContext:;

第1和第2个方法是对应的，第3和第4个方法也是对应的，前面两个没有构建内容缓冲区(Backing Store),需要直接提供contents,一种方法就是直接赋值一个CAImageRef:  
 layer.contents = [UIImage imageNamed:@"xxx"].CGImage;

后两种方法，会给layer开辟一块内存用来存储绘制的内容，在这两个方法里，可以使用CoreGraphics的那套api来绘制需要的内容。

```
// 重新UIView的CALayerDelegate
- (void)displayLayer:(CALayer *)layer {
    layer.contents = CFBridgingRelease([UIImage imageNamed:@"li.jpg"].CGImage);
}

- (void)drawLayer:(CALayer *)layer inContext:(CGContextRef)ctx {
    [super drawLayer:layer inContext:ctx];

    //1.使用UIKit进行绘制，因为UIKit只会对当前上下文栈顶的context操作，所以要把形参中的context设置为当前上下文
    UIGraphicsPushContext(ctx);
    UIImage* image = [UIImage imageNamed:@"li.jpg"];

    //指定位置和大小绘制图片
    [image drawInRect:CGRectMake(0, 0, 100, 100)];
    UIGraphicsPopContext();
}
```

画出来丑丑的但是帅气的爱豆

上面两种方式都可以实现在UIView的layer中画一个图片哈，只是后面的是有缓存的，第一个方法是没有Backing Store的，其实两者还是有区别滴：

| displayLayer | drawLayer | drawRect |
|---|---|---|
| 实现+执行 | 实现+不执行 | 实现+不执行 |
| 不实现 | 实现+执行 | 实现+如果drawLayer调用了super则执行，不调用则不执行 |
| 不实现 | 不实现 | 实现+执行 |
| 实现+不执行 | 实现+不执行 | 不实现 |

- **另外说一个注意事项哦：**  
   如果是自己新建的layer，不是UIView默认自己的那个layer，最好不要把自己的layer的delegate设为已有的UIView，因为它已经是默认自带layer的delegate了，如果还将它设为我们新建layer的delegate，那么这个UIVew将作为多个layer的delegate，会变得很混乱，所以如果自定义了一个Layer，可以用下面的方式设置delegate：

```
LayerDelegate* delegate = [[LayerDelegate alloc]init];
CALayer* layer = [CALayer layer];
layer.anchorPoint = CGPointMake(0, 0);
layer.position = CGPointMake(100, 100);
layer.bounds = CGRectMake(0, 0, 200, 200);
layer.delegate = delegate;
```

P.S. UIView的绘制准备下次说啦~

#### 4. 动画

我们每次做CABasicAnimation动画都是给CALayer加的，它的特点就是其实我们改变的是layer的显示，并没有真正的改变view，这样的做的优点也是通过transform来给缓存好的bitmap做动画，而不用再次从0开始计算应该如何显示view再一点一点的显示。

当我们执行下面的代码给view做动画的时候：

```
testView = [[UIView alloc] initWithFrame:CGRectMake(0, 0, 200, 200)];
[self.view addSubview:testView];
testView.backgroundColor = [UIColor blueColor];

CABasicAnimation *translationXAnimation = [CABasicAnimation animationWithKeyPath:@"transform.translation.x"];
translationXAnimation.fromValue = @(0);
translationXAnimation.toValue = @(50);
translationXAnimation.timingFunction = [CAMediaTimingFunction functionWithControlPoints:0.28 :0.71 :0.44 :1.00];
translationXAnimation.duration = 0.4;
translationXAnimation.removedOnCompletion = NO;
translationXAnimation.fillMode = kCAFillModeForwards;
[testView.layer addAnimation:translationXAnimation forKey:@"animation.position.x"];
```

动画结束时状态.png

可以看到虽然界面显示的是坐标x值已经变为了50，但实际上通过Xcode debug看页面结构的时候，view是没有移动的，打印一下view的位置：

```
po testView.frame
(origin = (x = 0, y = 0), size = (width = 200, height = 200))

po testView.layer.frame
(origin = (x = 0, y = 0), size = (width = 200, height = 200))

po testView.layer.presentationLayer.frame.origin
(x = 50, y = 0)

po testView.layer.modelLayer.frame.origin
(x = 0, y = 0)
```

原来给layer做动画只有presentationLayer跟着动画不断改变，也就是我们看到的样子，那么presentationLayer是什么呢？

- Core Animation使用三种类型的layer tree对象来实现动画：

（1）Model Layer Tree（模型层树）  
 model tree保存了layer当前实际的状态，改变layer的position值就是改变modelLayer的位置，所以动画结束的时候，modelLayer的值仍旧是和layer一致的初始状态

（2）Presentation Tree（表示层树）  
 presentation tree包含了任何正在进行的动画的值，是当前值在屏幕上的映射。如果希望在动画过程中获取当前动画做到哪里了可以用这个

（3）Render Tree（渲染层树）  
 render tree是动画的真实执行者，但是它是私有的，开发者不能调用。  
 当改变layer的值的时候，layer tree的值会马上改变，通过render tree渲染，presentation tree以动画的形式展现layer的某个属性值的渐变过程。

> 所以如果做动画希望view真实位置改变，在做动画的代码之前可以将layer的属性设为动画结束状态的属性哦

- 用layer做动画有啥好处嘞？  
   不用不断的更新view的数据 + 不用不断的和图形硬件交互数据 + 如果有很多subview，不用重绘整个图层树

#### 5. 离屏渲染

layer的一大问题就是离屏渲染，什么是离屏渲染嘞？可以参考：[https://www.jianshu.com/p/748f9abafff8](https://www.jianshu.com/p/748f9abafff8)

产生的原因主要是以下几个对layer的处理：  
 （1）shouldRasterize（光栅化）  
 （2）masks（遮罩）  
 （3）shadows（阴影）  
 （4）edge antialiasing（抗锯齿）  
 （5）group opacity（组透明）  
 （6）cornerRadius+maskToBounds(圆角，iOS9以后imageview的cornerRadius不会触发离屏渲染了)  
 （7）高斯模糊

原因是这些操作都需要对现有图层做一些事情，然后再显示出来，举个例子：

高斯模糊过程

如果对一个view做高斯模糊，就得把view和高斯模糊效果叠加计算以后进行显示，也就是需要在屏幕外用一块缓冲区计算这两个混合的效果，即离屏渲染。

给Layer加mask以及radius其实也是，由于要先把mask和原图进行混合，这个过程就是找一块缓冲区计算，然后放到屏幕上。这样就会增加GPU的负荷，导致有可能没有及时显示view，形成掉帧卡顿。

这里插一句，其实不仅是layer，如下实验所示，view 1为0.5透明度的白色块，view 2为0.5透明度的绿色块，如果view1内加入view2，也会产生离屏渲染，但是如果不是包含关系的两个view，即使叠加展示也不会产生离屏渲染。

离屏渲染view叠加

如果在view1包含view2的基础上，将view1的透明度改为100%，那么也不会产生离屏渲染，即使view2的透明度是50%；然而如果view2的透明度改为100%，view1的透明度为50%就仍旧会产生离屏渲染。

通过Xcode可以看哪里有离屏渲染：（这里是真机调试哈，会把需要离屏渲染的图层高亮成黄色，这就意味着黄色图层可能存在性能问题）

离屏渲染查看

微信的离屏渲染检查

- 几个debug的优化路径：

（1）Color Blended Layers  
 勾选后，检查你的应用界面，blended layer会显示为红色，不透明的为绿色，红色越少越好，如果你的界面一片红海，那就是时候好好优化了。主要是要减少没必要的alpha混合。

（2）ColorHitsGreenandMissesRed  
 勾选后，如果在你使用了shouldRasterize的地方界面显示为绿色，则表示使用正确性能良好，如果为红色，则需要考虑优化了。(第一次加载时会显示红色，因为这时还没缓存成功，需要检测重用的过程中(比如tableview上下滚动)的变化)

（3）Color Offscreen-Rendered Yellow  
 如上所述，离屏渲染的地方都标记为黄色。并非所有的黄色区域都是需要优化的，比如UINavigationBar，因为需要做背景模糊效果，因此它需要离屏渲染。

---

**如果只是设置cornerRadius是不会产生离屏渲染的，但是如果设置了maskToBounds就有可能会了，这里顺带提一句其实UIView的clipsToBounds就是调用了layer的maskToBounds。**

如果调用以下方式设置圆角，是不会有离屏渲染的：

```
UIView *testView = [[UIView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];
testView.backgroundColor = [UIColor blueColor];
testView.layer.cornerRadius = 20;
```

cornerRadius无离屏渲染

甚至当我们再设置一下testView.layer.masksToBounds = YES以后，页面仍旧和上图一样，没有任何黄色的离屏渲染标志。

那离屏渲染是怎么触发的呢？当我们给现在的View里面增加一个subView并且不设置masksToBounds先来看一下：

```
UIView *testView = [[UIView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];
testView.backgroundColor = [UIColor blueColor];

UIView *redView = [[UIView alloc] initWithFrame:CGRectMake(0, 0, 100, 100)];
redView.backgroundColor = [UIColor redColor];
[testView addSubview:redView];

testView.layer.cornerRadius = 20;
```

只有cornerRadius及subview

可以看到如果只设置cornerRadius，即使有subview，subview超出view圆角的部分不会被裁剪，但是没有任何离屏渲染。

但是如果设置了testView.layer.masksToBounds并且有subview，就会是下面这样，无论subview是不是在testView的边缘需不需要被剪裁：

masksToBounds=YES&有subview

可以看到如果有subview还设置了masksToBounds就会产生离屏渲染。

然后我又尝试了一下addSublayer来代替addSubview看一下会不会产生离屏渲染：

```
UIView  *testView = [[UIView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];
testView.backgroundColor = [UIColor blueColor];

CALayer *redLayer = [[CALayer alloc] init];
redLayer.frame = CGRectMake(50, 50, 100, 100);
redLayer.backgroundColor = [UIColor redColor].CGColor;
[testView.layer addSublayer:redLayer];

testView.layer.cornerRadius = 20;
testView.clipsToBounds = YES;
```

最后的结果和上面的图是一样的，仍旧会有四个角角的黄色标识。

> 我猜测哈，其实只要有多个bitmap的叠加，以及对他们做些处理比如统一切掉圆角，就会产生离屏渲染。如果只是一个bitmap，完全可以直接绘制，在绘制的时候把mask部分显示出来就可以了，但是多个的时候就需要找一块缓冲先叠加再mask，感觉上重点是叠加。

---

那么要如何解决这个问题呢？

如果直接给imageView增加圆角就会是下图右边的样子，仍旧有离屏渲染：

```
// 直接设置cornerRadius及clipsToBounds
UIImageView *testView = [[UIImageView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];

testView.layer.cornerRadius = 20;
testView.clipsToBounds = YES;
```

如果我们只调用cornerRadius而不设置clipsToBounds显示的图片其实是没有圆角的哦，虽然也没有离屏渲染-。-

imageView圆角离屏渲染（左:优化后 右:优化前）

**优化的思路其实就是用画图的方式画圆角，因为Core Graphics是线程安全的可以把绘制抛出去。**

我们可以写个category来画圆角~

```
- (void)setRadius:(CGFloat)radius rectCornerType:(UIRectCorner)rectCornerType {
    CGSize size = self.bounds.size;
    CGFloat scale = [UIScreen mainScreen].scale;
    CGSize cornerRadii = CGSizeMake(radius, radius);
    
    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        UIGraphicsBeginImageContextWithOptions(size, YES, scale);
        if (nil == UIGraphicsGetCurrentContext()) {
            return;
        }
        UIBezierPath *cornerPath = [UIBezierPath bezierPathWithRoundedRect:self.bounds byRoundingCorners:rectCornerType cornerRadii:cornerRadii];
        [cornerPath addClip];
        [self.image drawInRect:self.bounds];
        id processedImageRef = (__bridge id _Nullable)(UIGraphicsGetImageFromCurrentImageContext().CGImage);
        UIGraphicsEndImageContext();
        
        dispatch_async(dispatch_get_main_queue(), ^{
            self.layer.contents = processedImageRef;
        });
    });
}

调用的时候：
UIImageView *testView.image = [UIImage imageNamed:@"li.jpg"];

testView = [[UIImageView alloc] initWithFrame:CGRectMake(100, 100, 200, 200)];
[self.view addSubview:testView];

testView.image = [UIImage imageNamed:@"li.jpg"];
[testView setRadius:20 rectCornerType:UIRectCornerAllCorners];
```

（这里代码其实有点问题哈：应该是不能通过其他线程操作UI的，所以其实不能从global queue里面取bound以及image的，正确的做法应该是在主线程复制一份UI的数据，再在global queue里面使用）

关于阴影、mask之类的离屏渲染解决方式在[https://www.jianshu.com/p/e3c118e56c9a](https://www.jianshu.com/p/e3c118e56c9a)里面都有提及，可以参考一下~ 总体而言就是用静态代替动态计算解决问题。

离屏渲染的解决和动画我之后都准备单独搞一篇滴，这次就水一下大概提一下啦~

> Reference:
> 
> 1. [https://www.jianshu.com/p/e3c118e56c9a](https://www.jianshu.com/p/e3c118e56c9a)
> 2. [https://www.jianshu.com/p/5750c8491a8d](https://www.jianshu.com/p/5750c8491a8d)
> 3. 关系：[https://www.jianshu.com/p/fd8cd2231541](https://www.jianshu.com/p/fd8cd2231541)
> 4. 高性能设置圆角：[https://cloud.tencent.com/developer/article/1198736](https://links.jianshu.com/go?to=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Farticle%2F1198736)
> 5. 离屏渲染：[https://www.jianshu.com/p/ca51c9d3575b](https://www.jianshu.com/p/ca51c9d3575b)
> 6. 圆角：[https://blog.csdn.net/poppin_category/article/details/50984738](https://links.jianshu.com/go?to=https%3A%2F%2Fblog.csdn.net%2Fpoppin_category%2Farticle%2Fdetails%2F50984738)
