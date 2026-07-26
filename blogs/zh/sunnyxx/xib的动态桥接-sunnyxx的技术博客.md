---
title: xib的动态桥接 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/07/01/ios_ib_bridge/'
original_language: zh
published: 2014-07-01
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5dfc256fa14d2c32'
translated: n/a
---

> 原文：[xib的动态桥接 · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/07/01/ios_ib_bridge/)　·　sunnyxx (孙源)

# xib的动态桥接

2014年7月1日

# [#我是前言](#我是前言)我是前言

个人很主张使用`Interface Builder`(以下都简称`IB`)来构建程序UI，包括`storyboard`和`xib`，相比代码更可视和易于修改，尤其在使用AutoLayout的时候，一目了然。  
但用了这么久IB之后发现一个很大的槽点，就是IB间很难`嵌套混用`，比如一个xib中的view是另一个xib的子view，或者一个storyboard中两个vc都用到了一个xib构建的view等。解决方法一般是代码手动拼接，这就造成了比较混乱的情况。

**本文将尝试解决这个问题，实现xib的`动态桥接`，并提供一个支持`cocoapods`的开源工具类供方便使用。**

## [#一张图顶十句话：](#一张图顶十句话：)一张图顶十句话：

![](http://ww2.sinaimg.cn/large/51530583gw1ehzgklik42j20m80go0ua.jpg)

## [#实现效果：](#实现效果：)实现效果：

![](http://ww3.sinaimg.cn/large/51530583gw1ehzgoiqfkfj20hs0qo75u.jpg)

---

# [#黑魔法方法](#黑魔法方法)黑魔法方法

实现这个功能的关键在于：在ib加载的某个时刻将`placeholder`的view动态替换成从xib加载的view，下面的方法就可以做到：

```objc
- (id)awakeAfterUsingCoder:(NSCoder *)aDecoder NS_REPLACES_RECEIVER;
```

这个方法很少用到，在`NSObject (NSCoderMethods)`中定义，由`NSCoder`在decode过程中调用（于`-initWithCoder:`之后），所以说就算从文件里decode出来的对象也会走这个方法。  
方法后面有`NS_REPLACES_RECEIVER`这个宏：

```objc
#define NS_REPLACES_RECEIVER __attribute__((ns_consumes_self)) NS_RETURNS_RETAINED
```

在clang的文档中可以找到对这个[编译器属性的介绍](http://clang-analyzer.llvm.org/annotations.html#attr_ns_consumes_self)

> One use of this attribute is declare your own init-like methods that do not follow the standard Cocoa naming conventions.

所以这个宏主要为了给编译器标识出这个方法可以像`self = [super init]`一样使用，并作出合理的内存管理。  
So，这个方法提供了一个机会，**可以将decode出来的对象替换成另一个对象**

**动态桥接流程**

```objc
- (id)awakeAfterUsingCoder:(NSCoder *)aDecoder {
    self = [super awakeAfterUsingCoder:aDecoder];

    // 0. 判断是否要进行替换
    // 1. 根据self.class从xib创建真正的view
    // 2. 将placeholder的属性、autolayout等替换到真正的view上
    // 3. return 真正的view
}
```

流程不难理解，就是有2个小难点：

- ，如何判断
- 迁移`AutoLayoutConstrains`

### [#解决递归问题](#解决递归问题)解决递归问题

这个topic全网可能就[《这篇文章》](http://blog.yangmeyer.de/blog/2012/07/09/an-update-on-nested-nib-loading)有写，本文也是从它发起的，但是发现它的方法并不能解决所有问题（尤其是用storyboard加载xib时），所以换了个思路，采取了设置标志位的方式避免递归调用：

```objc
- (id)awakeAfterUsingCoder:(NSCoder *)aDecoder {
    self = [super awakeAfterUsingCoder:aDecoder];
    if (这个类的Loading标志位 -> NO)
    {
        Loading标志位 -> YES
        从xib加载真实的View (这里会递归调用这个函数)
        return 真实View
    }
    Loading标志位 -> NO
    return self
}
```

方法有点土，但是有效了，源代码文章后面会给地址。

### [#迁移AutoLayoutConstrains](#迁移AutoLayoutConstrains)迁移AutoLayoutConstrains

由于IB在加载AutoLayoutConstrains时的顺序是**先加载子View内部的约束，后加载父View上的约束**，而我们替换placeholder的时机是：

1. placehodler view被创建（只带width，height的自身约束）
2. 真正的view被从xib动态加载（带其子view的所有约束）
3. **_placeholder被替换成真的view_**
4. placeholder view在其父View（一直到父父父…View）的约束被创建

所以说，迁移AutoLayout时，`只需要把placeholder view的自身约束copy到真实View上就好了`（停顿10s感受下）  
代码如下：

```objc
- (void)replaceAutolayoutConstrainsFromView:(UIView *)placeholderView toView:(UIView *)realView
{
    for (NSLayoutConstraint *constraint in placeholderView.constraints) {
        NSLayoutConstraint* newConstraint  = [NSLayoutConstraint constraintWithItem:realView
                                                     attribute:constraint.firstAttribute
                                                     relatedBy:constraint.relation
                                                        toItem:nil // Only first item
                                                     attribute:constraint.secondAttribute
                                                    multiplier:constraint.multiplier
                                                      constant:constraint.constant];
        newConstraint.shouldBeArchived = constraint.shouldBeArchived;
        newConstraint.priority = constraint.priority;
        [realView addConstraint:newConstraint];
    }
}
```

One more thing，保证AutoLayout生效还要加上下面这句话：

```objc
realView.translatesAutoresizingMaskIntoConstraints = NO;
```

---

# [#开源项目XXNibBridge](#开源项目XXNibBridge)开源项目XXNibBridge

光说方案不给源码还是不地道的，demo放到了[我的github上面的XXNibBridge项目](https://github.com/sunnyxx/XXNibBridge)，回顾一下上面的关系图：

![](http://ww2.sinaimg.cn/large/51530583gw1ehzgklik42j20m80go0ua.jpg)

不得不提到`IB命名约定`的最佳实践方案：

**将类名作为Cell或者VC的Reusable Identifier**  
设`ReuseIdentifier`一直比较蛋疼，我一般将Cell的`类名`作为`ReuseIdentifier`（当然，大多数情况我们都会子类化Cell的），写法如：

```objc
[self.tableView registerClass:[XXSarkCell class] forCellReuseIdentifier:NSStringFromClass([XXSarkCell class])];
```

在`dequeueCell`的时候同理，这样的好处在于省去了起名的恶心、通过ReuseId可以直接找到Cell类、同时重构Cell类名时ReuseId也不用去再改。

**View的xib与View的类名同名** 同理

实现了桥接Xib的功能的同时，也简单实现了这个命名约定：

```objc
// XXNibBridge.h
+ (NSString *)xx_nibID; // 类名
+ (UINib *)xx_nib; // 返回类名对应nib
+ (id)xx_loadFromNib; // 对应nib的类对象
+ (id/*UIViewController*/)xx_loadFromStoryboardNamed:(NSString *)name; // 返回类名对应的vc
```

所以之后的代码可以这么写:

```objc
[tableView registerNib:[XXSarkView xx_nib] forCellReuseIdentifier:[XXSarkView xx_nibID]];
```

# [#XXNibBridge的使用](#XXNibBridge的使用)XXNibBridge的使用

**Cocoapods安装**

```
pod 'XXNibBridge', :git => 'https://github.com/sunnyxx/XXNibBridge.git'
```

对于要支持Bridge的类，重载下面的方法：

```objc
#import "XXNibBridge.h"
@implementation XXDogeView
+ (BOOL)xx_shouldApplyNibBridging
{
    return YES;
}
@end
```

在父的Xib或Storyboard中拖个UIView进来作为Placeholder，设置为真实Nib的类

![](http://ww1.sinaimg.cn/large/51530583gw1ei03b0vuzmj20z40a6q4e.jpg)

保证真实Nib的类名和Nib名相同，记得在Nib中设好Class  
![](http://ww3.sinaimg.cn/large/51530583gw1ei03dn8rq8j206g036q2z.jpg)

**Done.**  
![](http://ww4.sinaimg.cn/large/51530583gw1ei03g01mmej20ga07sjrt.jpg)

---

# [#References](#References)References

[http://blog.yangmeyer.de/blog/2012/07/09/an-update-on-nested-nib-loading](http://blog.yangmeyer.de/blog/2012/07/09/an-update-on-nested-nib-loading)  
[http://stackoverflow.com/questions/19816703/replacing-nsview-while-keeping-autolayout-constraints](http://stackoverflow.com/questions/19816703/replacing-nsview-while-keeping-autolayout-constraints)  
[http://clang-analyzer.llvm.org/annotations.html#attr_ns_consumes_self](http://clang-analyzer.llvm.org/annotations.html#attr_ns_consumes_self)
