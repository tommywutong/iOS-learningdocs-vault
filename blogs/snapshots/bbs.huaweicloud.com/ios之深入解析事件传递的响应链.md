---
title: iOS之深入解析事件传递的响应链
source_url: 'https://bbs.huaweicloud.com/blogs/331365'
source_domain: bbs.huaweicloud.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:a3b14c1bb0653c5f'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
container: '//div[contains(@class,''blog-content'')]'
container_source: map
---

> 原文：[iOS之深入解析事件传递的响应链](https://bbs.huaweicloud.com/blogs/331365)

# iOS之深入解析事件传递的响应链

举报

[![](https://res.hc-cdn.com/ecology/5.12.102/v2_resources/ydcomm/images/default_user.png)](https://bbs.huaweicloud.com/community/usersnew/id_1642161699862635) [Serendipity·y](https://bbs.huaweicloud.com/community/usersnew/id_1642161699862635)  发表于 2022/02/16 23:10:21 2022/02/16

【摘要】 一、UIResponder App 使用响应者对象接收和处理事件，只有继承 UIResponder 的类，才能处理事件。UIApplication、UIView、UIViewController 都是继...

#### 一、UIResponder

- App 使用响应者对象接收和处理事件，只有继承 UIResponder 的类，才能处理事件。
- UIApplication、UIView、UIViewController 都是继承自 UIResponder 类，可以响应和处理事件。CALayer 继承自 NSObject，不是 UIResponder 的子类，无法处理事件。
- 响应者接收到原始事件数据，必须处理事件或者转发到另一个响应者对象。当 App 接收到一个事件时，UIKit 自动引导事件到最合适的响应者对象，也叫做第一响应者。
- 有时候可能会通过 UIResponder 来查找控件的父视图。

```c
	/**
	 * 通过遍历 UIView 上的响应链来查找当前顶部 vc
	 */
	- (UIViewController *)firstVC {
	    for (UIView * next = self; next; next = next.superview) {
	        UIResponder * nextResponder = [next nextResponder];
	        if ([nextResponder isKindOfClass:[UIViewController class]]) {
	            return (UIViewController *)nextResponder;
	        }
	    }
	    return nil;
	}
	
	/**
	 * 通过遍历 button 上的响应链来查找 cell
	 */
	- (MyCell *)buttonTaped:(UIButton *)button {
	    UIResponder * responder = button.nextResponder;
	
	    while (responder) {
	        if ([responder isKindOfClass:[MyCell class]]) {
	            MyCell * cell = (MyCell *)responder;
	            break;
	        }
	        responder = responder.nextResponder;
	    }
	}
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
- 18
- 19
- 20
- 21
- 22
- 23
- 24
- 25
- 26
- 27

#### 二、事件的第一响应者

- 事件的每个类型，UIKit 指定一个第一响应者，然后最先发送事件到这个对象。第一响应者基于事件的类型而变化。
-   - Touch event 第一响应者是触摸事件产生的 view；
-   - Press event 第一响应者是焦点响应者；
-   - Shake-motion events,Remote-control events,Editing menu messages 第一响应者是你或者 UIKit 指定的对象。
- 注意：运动事件相关的加速度计、陀螺仪、磁强计都不属于响应者链，而是由 CoreMotion 传递事件给你指定的对象。
- 控件直接与它相关的 target 对象使用 action 消息通信。当用户与控件交互时，控件调用 target 对象的 action 方法。换句话说，控件发送 action 消息到目标对象。Action 消息不是事件，但是它仍然可以利用响应链。当控件的 target 对象为 nil，UIKit 从 target 对象和响应链走，直到找到一个对象实现了合适的 action 方法。
- 如果视图有添加手势识别器，手势识别器接收 touch 和 press 事件在视图接收事件之前。如果所有的视图的手势识别器都不能识别它们的手势，这些事件会传递到视图处理。如果视图不能处理它们，UIKit 传递事件到响应链。

#### 三、事件的分发和传递

- 当 iOS 程序中发生触摸事件后，系统会将事件加入到 UIApplication 管理的一个任务队列中；
- UIApplication 将处于任务队列最前端的事件向下分发，即 UIWindow。
- UIWindow 将事件向下分发，即 UIView。
- UIView首先看自己是否能处理事件，触摸点是否在自己身上。如果能，那么继续寻找子视图。
- 遍历子控件，重复以上两步。
- 如果没有找到，那么自己就是事件处理者。
- 如果自己不能处理，那么不做任何处理。

![在这里插入图片描述](https://res-hd.hc-cdn.cn/ecology/9.3.209/v2_resources/ydcomm/libs/images/loading.gif)

- 其中 UIView 不接受事件处理的情况主要有以下三种：
-   - alpha \< 0.01
-   - userInteractionEnabled = NO
-   - hidden ＝ YES
- 这个从父控件到子控件寻找处理事件最合适的 view 的过程，如果父视图不接受事件处理，那么子视图也不能接收事件。事件只要触摸了就会产生，关键在于是否有最合适的 view 来处理和接收事件，如果遍历到最后都没有最合适的 view 来接收事件，则该事件被废弃。

#### 四、hitTest:withEvent:

- UIKit 使用基于视图的 hit-testing 来确定 Touch 事件在哪里产生，UIKit 将 Touch 位置与视图层级中的视图对象的边界进行了比较。UIView 的 hitTest:withEvent: 方法在视图层级中执行，寻找最深的包含指定 Touch 的子视图，这个视图将成为 Touch 事件的第一响应者。

```c
	/**
	 * @return 本次点击事件需要的最佳 View
	 */
	- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event
```

- 1
- 2
- 3
- 4

- 注意：如果 Touch 位置超过视图边界，hitTest:withEvent 方法将忽略这个视图和它的所有子视图。结果就是，当视图的clipsToBounds 属性为 NO，子视图超过视图边界也不会返回，即使它们包含发生的 Touch。
- 当 touch 第一次产生时 UIKit 创建 UITouch 对象，在 touch 结束时释放这个 UITouch对象。当 touch 位置或者其他参数改变时，UIKit 更新 UITouch 对象新的信息。

![在这里插入图片描述](https://res-hd.hc-cdn.cn/ecology/9.3.209/v2_resources/ydcomm/libs/images/loading.gif)

- 把父视图的 userInteractionEnabled 设置为 NO，按钮 1 和按钮 2 都不会响应了。
- 如果点击按钮 2 视图，响应的是按钮 2，那么为什么点击按钮 2 和按钮 1 的交界处会是按钮 2 响应呢?
- 事件传递给窗口或控件的后，就调用 hitTest:withEvent: 方法寻找更合适的 view。如果子控件是合适的 view，则在子控件再调用 hitTest:withEvent: 查看子控件是不是合适的 view，一直遍历，直到找到最合适的 view 或者废弃事件。

```c
	- (UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event {
	   // ①、判断当前控件能否接收事件
	   if (self.userInteractionEnabled == NO || self.hidden == YES || self.alpha <= 0.01) return nil;
	
	   // ②、判断触摸点在不在当前控件内
	   if ([self pointInside:point withEvent:event] == NO) return nil;
	
	   // ②、倒序遍历自己的子控件
	   NSInteger count = self.subviews.count;
	   for (NSInteger i = count - 1; i >= 0; i--) {
	
	       UIView * childView = self.subviews[i];
	       // 把当前控件上的坐标系转换成子控件上的坐标系
	       CGPoint childP = [self convertPoint:point toView:childView];
	
	       UIView * fitView = [childView hitTest:childP withEvent:event];
	       if (fitView) { 
	           return fitView;  // 找到了最合适的 view
	       }
	   }
	   // 循环结束，表示没有比自己更合适的 view
	   return self;  
	}
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14
- 15
- 16
- 17
- 18
- 19
- 20
- 21
- 22
- 23

- 所有当父视图 userInteractionEnabled 关闭时，return nil，子视图无法继续寻找最合适的 view。
- 从后往前遍历子控件，图中按钮 2 在按钮 1 视图层级之上，所以按钮 2 是最合适的 view，还没有轮到按钮 1。

![在这里插入图片描述](https://res-hd.hc-cdn.cn/ecology/9.3.209/v2_resources/ydcomm/libs/images/loading.gif)

- 视图层级从后往前依次是 C-\>D-\>A、E-\>F-\>B-\>父视图，父视图的 subviews = @[ B, A ]。当点击界面发生触摸事件时，遍历父视图的子视图，倒序遍历，先遍历的 A 视图。
- 如果 A 视图 alpha \< 0.01 || userInteractionEnabled = YES || hidden ＝ NO，则 A 视图不是合适的View，返回 nil。开始遍历父视图的另一个子视图 B。
- 如果 A 视图 alpha \> 0.01 && userInteractionEnabled = YES && hidden ＝ NO，则 A 视图可以接收触摸事件，并且触摸点在 A 视图内，则 A 视图为一个合适的 View，但还要继续从后往前遍历 A 视图的子视图；如果 A 视图的所有子视图返回 nil，则 A 视图则为最终合适的 view。
- 如果 C 视图可以接收触摸事件且触摸点在 C 视图中，并且 C 视图的所有子视图返回 nil。
- 如果 C 视图调用 hitTest:withEvent: 处理返回 nil，则查看 B 视图满足条件。以此类推。

#### 五、pointInside:withEvent:

- 判断触摸点是否在视图内：

```c
	/**
	 * @brief  判断一个点是否落在范围内
	 */
	- (BOOL)pointInside:(CGPoint)point withEvent:(UIEvent *)event
```

- 1
- 2
- 3
- 4

- 如果现在要扩大按钮 2 的点击范围怎么办？如果要让按钮 1 只点击左右区域 40 像素有效，其他地方都不响应呢?

![在这里插入图片描述](https://res-hd.hc-cdn.cn/ecology/9.3.209/v2_resources/ydcomm/libs/images/loading.gif)

-   - 扩大响应范围：

```c
	- (BOOL)pointInside:(CGPoint)point withEvent:(UIEvent *)event {
	    /* Inset `rect' by `(dx, dy)' -- i.e., offset its origin by `(dx, dy)', and decrease its size by `(2*dx, 2*dy)'. 
	 
	       CGRectInset 效果为 origin.x/y + dx/dy，size.width/height - 2 * dx/dy，这里 dx = -10，dy = -10
	     */
	    bounds = CGRectInset(self.bounds, -10, -10);
	
	    return CGRectContainsPoint(bounds, point);
	}
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9

-   - 不规则的点击区域：

```c
	/**
	 * @brief  改变图片的点击范围
	 */
	- (BOOL)pointInside:(CGPoint)point withEvent:(UIEvent *)event {
	    // 控件范围宽度 +40，高度 +40
	    CGRect bounds = CGRectInset(self.bounds, -20, -20);
	    UIBezierPath * path1 = [UIBezierPath bezierPathWithRect:CGRectMake(-20, 0, 40, 120)];
	    UIBezierPath * path2 = [UIBezierPath bezierPathWithRect:CGRectMake(self.frame.size.width - 20, 0, 40, 120)];
	    if (([path1 containsPoint:point] || [path2 containsPoint:point])&& CGRectContainsPoint(bounds, point)){
	        
	        return YES;  // 如果在 path 区域内返回 YES
	    }
	    return NO;
	}
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13
- 14

- 可以看出：
-   - 在不规则区域内（红框）点击，[self pointInside:point withEvent:event] == YES，按钮 1 是最合适的 view，调用按钮 1 的点击事件。
-   - 不在不规则区域内点击，无法调用按钮 1 的点击事件，[self pointInside:point withEvent:event] == NO。
-   - 在按钮 1 和按钮 2 重合区域（绿框）内点击，调用按钮 2 的点击事件，因为按钮 2 图层在按钮 1 之上，遍历 subviews 时，从后往前遍历，先查看按钮 2，按钮 2 调用 -hitTest:withEvent: 返回是最合适的 view，调用按钮 2 的点击方法。

#### 六、响应者链

- 响应链是从最合适的 view 开始传递，处理事件传递给下一个响应者，响应者链的传递方法是事件传递的反方法，如果所有响应者都不处理事件，则事件被丢弃。我们通常用响应者链来获取上几级响应者，方法是 UIResponder 的 nextResponder。
- 在 App 中没有单一的响应链，UIKit 定义了默认的规则关于对象如何从一个响应者传递到另一个响应者，但是你可以重写响应者对象的方法来改变这些规则。
- 通过重写响应对象的 nextResponder 属性改变响应链。许多 UIKit 的类已经重写了这个属性然后返回了指定的对象。
-   - UIView 如果视图是 ViewController 的根视图，下一个响应者为 ViewController，否则是视图的父视图。
-   - UIViewController 如果视图控制器是 window 的根视图下一个响应者为 window 对象。如果视图控制器是由另一个视图控制器推出来，那么下一个响应者为正在推出的视图控制器。
-   - -UIWindow 下一个响应者为 UIApplication 对象。
-   - UIApplication 下一个响应者为 app delegate，但是代理应该是 UIResponder 的一个实例，而不是 UIView、UIViewController 或者 App 对象本身。

文章来源: blog.csdn.net，作者：Serendipity·y，版权归原作者所有，如需转载，请联系作者。

原文链接：blog.csdn.net/Forever_wj/article/details/120005168

推荐

![](https://res-hd.hc-cdn.cn/ecology/9.3.209/v2_resources\images\global\blog-dialog.png)

华为开发者空间发布

让每位开发者拥有一台云主机

【版权声明】本文为华为云社区用户转载文章，如果您发现本社区中有涉嫌抄袭的内容，欢迎发送邮件进行举报，并提供相关证据，一经查实，本社区将立刻删除涉嫌侵权内容，举报邮箱： [cloudbbs@huaweicloud.com](mailto:cloudbbs@huaweicloud.com)

[iOS](https://developer.huaweicloud.com/tags/200594/blog_1) [容器](https://developer.huaweicloud.com/tags/200455/blog_1)

- 点赞
- 收藏
- 关注作者
