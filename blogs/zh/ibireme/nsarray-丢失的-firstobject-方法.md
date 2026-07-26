---
title: NSArray 丢失的 firstObject 方法
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2013/08/07/nsarray-firstobject/'
original_language: zh
published: 2013-08-07
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ccfb3b0407523583'
translated: n/a
---

> 原文：[NSArray 丢失的 firstObject 方法](https://blog.ibireme.com/2013/08/07/nsarray-firstobject/)　·　ibireme (郭曜源)

NSArray有一个 lastObject方法用于取到最后一个元素，但是翻翻看头文件，并没有firstObject方法。

如果强制发送firstObject，并且无视xcode警告的话，代码是不会出错的。。用下面方法测试返一下，返回的是YES。

```
[[NSArray array] respondsToSelector:@selector(firstObject)];
```

很明显苹果有实现这个方法（查资料说是iOS4起就已经有实现了），只是没有放到头文件来。

写一个Category来实现它吧~

```
@interface NSArray (FirstObject)
- (id)firstObject;
@end

@implementation NSArray (FirstObject)
- (id)firstObject {
    if (self.count)
        return self[0];
    return nil;
}
@end
```

由于本身苹果有这个实现，那implementation部分不写也OK。  
 然后。。NSMutableArray有个removeLastObject，如果是强迫症想要平衡的话，写个removeFirstObject也行。。

嗯。。问题是。。苹果为什么这么做呢？  
   
 [stackoverflow](http://stackoverflow.com/questions/13064610/why-nsarray-does-not-have-a-firstobject-method)上有一些讨论，[这篇博客](http://troybrant.net/blog/2010/02/adding-firstobject-to-nsarray/)上也有一堆讨论。  
 最常见的理由是：firstObject和 array[0]差不多，所以无需多此一举。很明显这种说法对空数组是不成立的。  
 不管怎么样，在[iOS 7.0 API Diffs](https://developer.apple.com/library/prerelease/ios/releasenotes/General/iOS70APIDiffs/index.html#//apple_ref/doc/uid/TP40013203)中，苹果终于把这个方法暴露出来了。这说明开发者的确是有这个需求的，只是苹果之前没有注意。

然后的问题是，苹果本身有实现，随后又用Category重写一次，这会有什么影响吗？

苹果网站上有一个[mail list](http://lists.apple.com/archives/objc-language/2009/Nov/msg00074.html)讨论了这个问题：一个有实现但没公布的API，想要用这个功能怎么搞？

1.把这个方法声明出来，但实现还是用苹果默认的实现，就像一般调用Private API那样。

嗯。。这个方式对于AppStore审查来说是比较危险的，苹果也说不准哪天改掉了。。好处就是能确保执行的结果。

2.写个Category，然后自己模仿着实现这个功能。

这个方法看着比较稳妥，默认Category的方法会在运行时覆盖掉原来的实现。

只是。。Category调试不易，多个Category实现同一个方法时，无法确定最后起作用的是哪一个。

如果原来private的方法实现有变化，现有Category实现和原先的方法不一致，那有可能会影响到系统的功能。

3.用[swizzle](http://cocoadev.com/MethodSwizzling)替换一下：自己实现一个myFirstObject，然后尝试和系统的firstObject的实现交换一下。

这里可以进行一些判断，比如如果系统有实现，那就直接调用；没有这个实现那就用自己写的逻辑处理。

这么做有些危险。。嗯。。环境复杂一些的话我也不知道会怎么样。。

比较上面的几种方法，看起来Category相对来对比较靠谱，也经是过AppStore验证的，那就这么做好了。

PS：整理我的工具包[YYKit](https://github.com/ibireme/YYKit)的时候，对这个firstObject方法很是不解，所以才一顿查资料。。
