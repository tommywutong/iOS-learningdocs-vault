---
title: 自动引用计数
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f0a17dee8c28f205'
translated: true
---

> 原文：[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/)

[git add](https://belkadan.com/blog/2011/06/git-add/) »

« [Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/?tag=cocoa)

« [Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=objective-c)

[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c) »

[Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/?tag=llvm) »

[弱链接](https://belkadan.com/blog/2011/07/Weak-Linking/?tag=compilers) »

## [自动引用计数](#)

在 Cocoa 的世界里，这次 WWDC 最大的新闻就是自动引用计数(Automatic Reference Counting)，也就是 ARC 的到来。目前关于这套机制唯一像样的文档,是 Clang 网站上一个没有链接入口的[参考页面](http://clang.llvm.org/docs/AutomaticReferenceCounting.html),不过既然 Clang 是开源的,而且这个实现已经进了最新的构建版本,那也算得上是公开信息了。

Cocoa 框架长期以来都用的是基于引用计数的体系,不过从 Mac OS X v10.5 起,苹果加入了可选的垃圾回收。和大多数 GC 系统一样,你可以把某些引用标记为 `__weak`(当目标对象被回收时,这类引用会自动变成 `nil`),而对象的实际回收时机是不确定的,也就是说不应该把清理代码放进 `finalize` 方法里。(实际上,`finalize` 方法里能安全做的事情非常少。)但你基本上可以把代码里所有的 `retain`、`release`、`autorelease` 消息都去掉,再也不用为内存泄漏操心。

问题在于?iOS 上没有垃圾回收,大概是因为每个 App 多一条后台线程、再加上内存释放的延迟,在 iOS App 运行所在的、资源有限的平台上代价太高了。在现代电脑上可以忽略不计的开销,到了移动设备上就变得明显起来。

我们都以为苹果会继续优化垃圾回收器,或者等 iOS 硬件早晚强大到不再在意那点性能损耗。结果呢,苹果拿出的是 ARC,你基本可以把它理解成在必要的地方自动插入 `retain`、`release`、`autorelease`。垃圾回收的所有好处,却没有运行时的开销。跟变魔术一样!

好吧,我自己用引用计数从来没遇到过什么问题,所以问题或许不是"为什么要用 ARC",而是"怎么这么久才来"。我所知道最接近的类比是 Boost 的 `shared_ptr`,现在已经被吸收进了 C++11。(`shared_ptr` 同样用的是引用计数,通过 [RAII](https://belkadan.com/blog/2011/06/Sandwich-Code) 实现。)但当然,自动引用计数的问题在于[循环引用](http://www.catb.org/jargon/html/koans.html#id3141202):如果两个对象互相引用对方,它们就永远不会被释放。

那为什么循环引用在_手动_引用计数里不是问题呢?因为你只需要区分两类引用:一类意味着拥有关系(子视图、字符串和日期这类值对象),一类不意味着(委托、动作目标)。这只是个小小的麻烦,在某个框架里写上几周代码之后,通常很快就能上手。

现在,想想苹果(还有 NeXT)在 Cocoa 过去十年里做的这些事:

- 简单的[所有权规则](http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html),基于命名约定。
- 供你在确实需要打破这条约定时使用的[特性](http://clang-analyzer.llvm.org/annotations.html#cocoa_mem)。
- 用来强制执行所有权规则的[静态分析](http://clang-analyzer.llvm.org/xcode.html)。
- 一种指定[存取方法所有权语义](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAccessorMethods.html#//apple_ref/doc/uid/TP40003539-SW1)的方式,以及一种自动生成这些存取方法的手段。
- 一套[弱引用](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmObjectOwnership.html#//apple_ref/doc/uid/20000043-1044135-BCICCFAE)的约定,(直到现在为止)一直比较松散。
- [Autorelease](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmObjectOwnership.html#//apple_ref/doc/uid/20000043-SW5)。

事后回过头看,几乎显得苹果一直以来都在朝这个方向努力。我们已经被训练得会遵循命名约定,会给代码打注解来声明想要的语义。我们几乎从不会弄错,因为规则总体上是清楚的。而如果我们想在 Cocoa 类型上获得 RAII 那样的语义,[也是能做到的](http://kickingbear.com/blog/archives/13)。

```
// See http://kickingbear.com/blog/archives/13 to see how it works
{
    NSObject *myObject KBScopeReleased = [[NSObject alloc] init];
    NSLog( @"%@", myObject );
} // myObject is sent a release message here.
```

但如果规则是清楚的,那么一个对源代码有良好理解的程序,就能替我们把该加的 `retain` 加上去。^[1](#fn:automatic)

这就是 ARC。

而且它在判断该在何时 `retain`、`release` 这件事上,能做得比你还好。([`objc_autoreleaseReturnValue`](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#runtime.objc_autoreleaseReturnValue) 这类函数的存在就说明,它甚至可能把方法调用结束时释放所有权的那次 `autorelease` 直接优化掉。)

我目前还没完全弄懂 ARC 的全部细节;我没加入 iOS 开发者计划,所以我能接触到的只有 Clang 以及它的[这些](http://llvm.org/svn/llvm-project/cfe/trunk/test/ARCMT)[测试用例](http://llvm.org/svn/llvm-project/cfe/trunk/test/SemaObjC)。尤其是在受管理对象指针和不受管理的 C 指针(包括 CoreFoundation 对象)之间转换这件事,看起来变得混乱了不少。希望苹果正式发布这套机制的时候,能拿出一份像样的文档。

不过你猜怎么着?我在最近的一个 App 上试了试 GC,结果发现:不用操心 `retain` 和 `release` 真的很爽!所以,我是支持 ARC 的,也准备好把它整合进我的 Cocoa 开发流程里了。

有意思的是,这下苹果在 Mac 上就有了_两套_受管理内存模型:ARC 和 GC。GC 依然更强大一些,因为你完全不用担心循环引用的问题。(GC 里的 `__weak` 只用来应对你预期某个对象会先于你消失的情况。)但 ARC 几乎不需要运行时支持,而且在 iOS 上它是除了手动引用计数之外唯一的选择。我猜苹果会把宝押在 ARC 上,任由 GC 慢慢边缘化。

另一方面,关于苹果从 GCC 转向 LLVM/Clang 的讨论,现在总算有了一个实打实的证据。据我所知,GCC 没有 ARC 的实现,我也怀疑它以后会有。苹果现在手握的这条编译器链条,不仅不是 GPL 协议,而且基本上完全由他们自己掌控。(LLVM 社区里的不少领军人物,包括项目创始人 Chris Lattner,都在苹果工作。第二大贡献者是谷歌。)这正是大家一直以来所猜测的、苹果一直在图谋的东西。

附言:[Autorelease pool 现在看起来样子有点怪](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#autoreleasepool)。

```
@autoreleasepool {
    NSString *fileName = [input lastPathComponent];
    NSString *baseName = [fileName stringByDeletingPathExtension];
    NSString *extension = [fileName pathExtension];
    return [NSString stringWithFormat:@"Base: %@\nExtension: %@",
                                      baseName, extension];
}
```

1. 如果你不喜欢编译器在背地里帮你摆弄东西,可以这么想:几乎在任何情况下,你都是想在使用对象期间保留它,用完再释放。所以与其用 `retain`/`release` 来标记所有权,你本该只需要对 `__weak` 引用这个特例做标注就够了。 [↩︎](#fnref:automatic)

本文发布于 [2011](https://belkadan.com/blog/2011) 年 [6](https://belkadan.com/blog/2011/06) 月 20 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Cocoa](https://belkadan.com/blog/tags/cocoa)、[Objective-C](https://belkadan.com/blog/tags/objective-c)、[LLVM](https://belkadan.com/blog/tags/llvm)、[编译器](https://belkadan.com/blog/tags/compilers)
</content>
