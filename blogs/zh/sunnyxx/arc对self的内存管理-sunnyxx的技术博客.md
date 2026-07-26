---
title: ARC对self的内存管理 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/01/17/self-in-arc/'
original_language: zh
published: 2015-01-17
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:25b4eff4e18142db'
translated: n/a
---

> 原文：[ARC对self的内存管理 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/01/17/self-in-arc/)　·　sunnyxx (孙源)

# ARC对self的内存管理

2015年1月17日

记录下前两天的一次讨论，源于网络库**YTKNetwork**中[“YTKRequest.m”](https://github.com/yuantiku/YTKNetwork/blob/master/YTKNetwork/YTKRequest.m)的`- start`方法其中的几行代码：

```objc
- (void)start {
    // ......
    YTKRequest *strongSelf = self;
    [strongSelf.delegate requestFinished:strongSelf];
    if (strongSelf.successCompletionBlock) {
        strongSelf.successCompletionBlock(strongSelf);
    }
    [strongSelf clearCompletionBlock];
}
```

看起来比较有违常理，所以和猿题库的@晨钰Lancy，@唐巧以及网易的@老汉一起讨论了下这个问题。

---

具体的问题大概是这样：

1. 对象，将自己作为其delegate
2. 的

  方法发起网络请求
3. 中执行了
4. 中，

  方法在回调完

  后

  了

也就是说，`- start`方法还未返回时，self就被外部释放了。作者发现了这个潜在的问题，所以在方法局部增设了一个`strongSelf`的强引用来保证self的生命周期延续到方法结束。问题是解决了，但是更希望知道原因。

简化说明就是：

```objc
- (void)foo {
    // self被delegate持有
    [self.delegate callout]; // 外部释放了这个对象
    // 这里self野指针
}
```

---

现在想想还是比较不符合常理，入参的self居然不能保证这个函数执行完成。后来查阅了下文档，发现是ARC的(gao)机(de)制(gui)，clang的[《这篇ARC文档》](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#self)中有明确的解释，总结如下：

- 的，也就是说，入参的self被表示为：（init系列方法的self除外）

```objc
- (void)start {
   const __unsafe_unretained YTKRequest *self;
   // ...
}
```

- ，如果调用方没有保证，就会出现上面的crash
- ，objc中100%的方法（不是函数）调用第一个参数都是self，同时，99%的情况下，调用方都不会在方法执行时把这个对象释放，所以相比于在每个方法中插入对self的引用计数管理：

```objc
- (void)start {
    objc_retain(self);
    // 其中的代码self一定不会被释放
    objc_release(self);
}
```

优化了的性能还真是比较可观。  
而且，ARC也用了挺多方法来避免开发者进行额外的引用计数控制，比如方法的**命名约定**，通过判断方法是否以如`init`，`alloc`，`new`，`copy`等关键字开头来决定其内存管理方式。

---

**One more thing**

在写test时发现，下面两种调用方法会导致不同结果：

```objc
- (void)viewDidLoad {
    // 1
    [_request start]; // crash
    // 2
    [self.request start]; // 正常
}
```

因为`self.request`是一次方法调用，返回的结果被`objc_retainAutoreleasedReturnValue`方法在局部进行了一次强引用，关于这个方法可以看之前写过的关于Autorelease的[《这篇文章》](http://blog.sunnyxx.com/2014/10/15/behind-autorelease/)
