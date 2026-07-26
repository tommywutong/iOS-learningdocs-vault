---
title: '深入理解"weak-strong dance"'
source_url: 'https://luohs.github.io/2017/05/31/20170531/'
source_domain: luohs.github.io
source_group: single-site
original_language: zh
published: 2017-05-31
archived_at: 2026-07-27
content_hash: 'sha256:c99259a81fea8862'
plan_ref: 第二周：weak、属性关键字与 Block / Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）
container: '//*[contains(@class,''post-body'')]'
container_source: guess
---

> 原文：[深入理解"weak-strong dance"](https://luohs.github.io/2017/05/31/20170531/)

使用block时利用”weak-strong dance”解决循环引用大家都知道，但这里有三点值得注意：  
1、当self指向的对象已经被废弃的情况下，持有block成员变量也不存在了，这个时候block对象应该已经没有被变量所持有了，它的引用计数应该已经为0了，它应该被废弃了啊，为什么它还能继续存在并执行。  
如以下代码，在 block 执行前退出这个页面的话，该 Controller 实例会被废弃，但 Block 还是会执行，会打印“self is (null)”。

```plain
- (void)viewDidLoad {
    [super viewDidLoad];

    __weak typeof(self) weakSelf = self;
    self.handler = ^{
        __strong typeof(weakSelf) strongSelf = weakSelf;
        NSLog(@"self is %@", strongSelf);
    };

    NSTimeInterval interval = 6.0;
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(interval * NSEC_PER_SEC)), dispatch_get_main_queue(), weakSelf.handler);
}
```

理解这个问题需要了解block原理，简单一点的说，block有三种类型：  
NSConcreteStackBlock（栈）  
NSConcreteGlobalBlock（全局）  
NSConcreteMallocBlock（堆）

如何实现这三种类型的block：

![](https://luohs.github.io/images/20170531/block_objc.png)

使用`clang -rewrite-objc $filePath`将OC代码转化为C++代码实现。[如何安装编译clang](https://luohs.github.io/2017/05/30/20170530/)

![](https://luohs.github.io/images/20170531/clang_rewrite.png)

![](https://luohs.github.io/images/20170531/block_clang.png)

如果 block 在记述全局变量的地方被设置或者 block 没有捕获外部变量，那就生成一个 NSConcreteGlobalBlock 实例。其它情况都会生成一个 NSConcreteStackBlock 实例，也就是说，它是在栈上的，所以一旦它所属的变量超出了变量作用域，该 block 就被废弃了。而当发生以下任一情况时：  
a、手动调用 block 的实例方法copy。  
b、block 作为函数返回值返回。  
c、将 block 赋值给附有__strong修饰符的成员变量。  
d、在方法名中含有usingBlock的 Cocoa 框架方法或 GCD 的 API 中传递 block。  
所以NSConcreteMallocBlock 类型的 block 通常不会在源码中直接出现。  
[看一下Block_copy()实现](http://www.galloway.me.uk/2013/05/a-look-inside-blocks-episode-3-block-copy/)：

```plain
static void *_Block_copy_internal(const void *arg, const int flags) {
    struct Block_layout *aBlock;
    const bool wantsOne = (WANTS_ONE & flags) == WANTS_ONE;

    // 1
    if (!arg) return NULL;

    // 2
    aBlock = (struct Block_layout *)arg;

    // 3
    if (aBlock->flags & BLOCK_NEEDS_FREE) {
        // latches on high
        latching_incr_int(&aBlock->flags);
        return aBlock;
    }

    // 4
    else if (aBlock->flags & BLOCK_IS_GLOBAL) {
        return aBlock;
    }

    // 5
    struct Block_layout *result = malloc(aBlock->descriptor->size);
    if (!result) return (void *)0;

    // 6
    memmove(result, aBlock, aBlock->descriptor->size); // bitcopy first

    // 7
    result->flags &= ~(BLOCK_REFCOUNT_MASK);    // XXX not needed
    result->flags |= BLOCK_NEEDS_FREE | 1;

    // 8
    result->isa = _NSConcreteMallocBlock;

    // 9
    if (result->flags & BLOCK_HAS_COPY_DISPOSE) {
        (*aBlock->descriptor->copy)(result, aBlock); // do fixup
    }

    return result;
}
```

综上所述，已经可以解答问题1。把 block 赋值给self.handler的时候，在栈上生成的 block 被复制了一份放到堆上。而之后如果你把这个 block 当作 GCD 参数使用，GCD 函数内部会把该 block 再 copy 一遍，而此时 block 已经在堆上，则该 block 的引用计数加1。所以此时 block 的引用计数是大于1的，即使self对象被废弃 block 会被 release 一次，但它的引用计数仍然大于0，故而不会被废弃。  
Tips:  
其实在 ARC 开启的情况下，将只会有 NSConcreteGlobalBlock 和 NSConcreteMallocBlock 类型的 block。  
![](https://luohs.github.io/images/20170531/block_work_in_ARC.png)  
更多请查看[苹果官方文档](https://developer.apple.com/library/content/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html)

2、在 block 内部使用weakSelf就是为了让 block 对象不持有self指向的对象，那在 block 内部又把weakSelf赋给strongSelf不就又持有self对象了么？又循环引用了？  
理解这个问题就需要了解block捕获对象变量。  
使用**weak修饰的变量时**weak是不会持有对象，它用一张 weak 表来管理对象和变量。赋值的时候它会以赋值对象的地址作为 key，变量的地址为 value，注册到 weak 表中。一旦该对象被废弃，就通过对象地址在 weak 表中找到变量的地址，赋值为 nil，然后将该条记录从 weak 表中删除。  
那使用 “weak-strong dance” 的时候是怎么个情况呢？

```plain
struct __block_impl {
    void *isa;
    int Flags;
    int Reserved;
    void *FuncPtr;
};

struct __xx_block_impl_y {
    struct __block_impl impl;
    __weak OCClass *occlass;
    // ...
};

static void __xx_block_func_y(struct __xx_block_impl_y *__cself) {
    OCClass *occlass = __cself -> occlass;
    // ...
}
```

每次使用**weak变量的时候，都会取出该变量指向的对象并 retain，然后将该对象注册到 autoreleasepool 中。通过上述代码我们可以发现，在**xx_block_func_y中，局部变量occlass会持有捕获的对象，然后对象会被注册到 autoreleasepool。这是延长对象生命周期的关键（保证在执行 Block 期间对象不会被废弃），但这不会造成循环引用，当函数执行结束，变量occlass超出作用域，过一会儿（一般一次 RunLoop 之后），对象就被释放了。所以 weak-strong dance 的行为非常符合预期：延长捕获对象的生命周期，一旦 Block 执行完，对象被释放，而 Block 也会被释放（如果被 GCD 之类的 API copy 过一次增加了引用计数，那最终也会被 GCD 释放）。

3、使用”weak-strong dance”一定安全吗？  
其实通过问题2就可以理解，”weak-strong dance”并不是安全的，”weak-strong dance”只实用与block已经捕获到对象的情况，”weak-strong dance”并不能保证 block 所引用对象的释放时机在执行之后， 更安全的做法应该是在 block 内部使用 strongSelf 时进行 nil检测，这样可以避免上述情况。

参考：  
[https://developer.apple.com/library/content/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html](https://developer.apple.com/library/content/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html)  
[http://www.galloway.me.uk/2013/05/a-look-inside-blocks-episode-3-block-copy/](http://www.galloway.me.uk/2013/05/a-look-inside-blocks-episode-3-block-copy/)  
[http://blog.devtang.com/2013/07/28/a-look-inside-blocks/](http://blog.devtang.com/2013/07/28/a-look-inside-blocks/)  
[http://albertodebortoli.com/blog/2013/08/03/objective-c-blocks-caveat/](http://albertodebortoli.com/blog/2013/08/03/objective-c-blocks-caveat/)  
[http://www.jianshu.com/p/737999a30544](http://www.jianshu.com/p/737999a30544)
