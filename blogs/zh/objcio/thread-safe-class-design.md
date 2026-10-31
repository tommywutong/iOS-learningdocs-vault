---
title: 线程安全的类设计
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/2-concurrency/thread-safe-class-design'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1876be6fd8c1e0d9'
translated: true
---

> 原文：[Thread-Safe Class Design](https://www.objc.io/issues/2-concurrency/thread-safe-class-design)　·　objc.io

本文将聚焦于编写线程安全的类以及使用 Grand Central Dispatch（GCD）方面的_实用_技巧、设计模式与反模式。

## 线程安全

### Apple 的框架

首先，我们来看看 Apple 的框架。总体而言，除非另有声明，大多数类默认并非线程安全。对某些类来说这在意料之中；对另一些则相当有意思。

即使是经验丰富的 iOS/Mac 开发者，最常见的错误之一也是在后台线程上访问 UIKit/AppKit 的部分内容。很容易犯下从后台线程设置诸如 `image` 这类属性的错误，因为它们的内容本来就会在后台从网络请求。Apple 的代码为性能做了优化，不会在你从不同线程更改属性时发出警告。

就图片而言，常见症状是你的更改会延迟生效。但若两个线程同时设置图片，应用很可能会直接崩溃，因为当前设置的图片可能被释放两次。由于这取决于时序，通常会在客户使用时崩溃，而不是在开发期间。

没有_官方_工具来发现此类错误，但有一些技巧可以很好地完成这项工作。[UIKit Main Thread Guard](https://gist.github.com/steipete/5664345) 是一个小源文件，会拦截对 UIView 的 `setNeedsLayout` 与 `setNeedsDisplay` 的任何调用，在转发调用前检查是否在主线程上执行。由于 UIKit 的许多 setter（包括 image）都会调用这两个方法，这能捕获许多与线程相关的错误。虽然这一技巧不使用私有 API，我们也不建议在生产应用中使用——但在开发期间非常有用。

UIKit 不做成线程安全，是 Apple 有意为之的设计决策。使之线程安全在性能方面不会带来多少收益；实际上会使许多事情变慢。而 UIKit 绑定到主线程这一事实，反而让编写并发程序并使用 UIKit 变得非常容易。你只需确保对 UIKit 的调用始终在主线程上进行。

#### 为何 UIKit 不是线程安全的？

确保像 UIKit 这样的大型框架线程安全将是一项重大工程，代价高昂。把非 atomic 属性改成 atomic 只是所需改动的一小部分。通常你希望一次更改多个属性，然后才看到更改后的结果。为此，Apple 将不得不暴露类似 Core Data 的 `performBlock:` 与 `performBlockAndWait:` 这样的方法来同步更改。而若考虑到对 UIKit 类的大多数调用都是关于_配置_的，使它们线程安全就更加没有意义。

然而，即便不是关于配置的调用，也会共享内部状态，因而也不是线程安全的。若你在 iOS 3.2 及更早的黑暗年代就已写过应用，一定经历过在准备后台图片时使用 NSString 的 `drawInRect:withFont:` 导致的随机崩溃。幸运的是，自 iOS 4 起，[Apple 使大多数绘图方法以及像 `UIColor` 和 `UIFont` 这样的类可在后台线程上使用](http://developer.apple.com/library/ios/#releasenotes/General/WhatsNewIniOS/)。

不幸的是，Apple 在线程安全方面的文档不足。他们建议仅在主线程上访问，即便对绘图方法也未明确保证线程安全——因此同时阅读 [iOS Release Notes](http://developer.apple.com/library/ios/#releasenotes/General/WhatsNewIniOS/Articles/iPhoneOS4.html) 始终是个好主意。

就大部分而言，UIKit 类应仅从应用程序的主线程使用。对于派生自 UIResponder 的类，或任何以任何方式操纵应用用户界面的类，尤其如此。

#### 释放问题

在后台使用 UIKit 对象时的另一危险称为「释放问题」（The Deallocation Problem）。Apple 在 [TN2109](http://developer.apple.com/library/ios/#technotes/tn2109/_index.html) 中概述了该问题并提出了各种解决方案。问题在于 UI 对象应在主线程上释放，因为其中一些可能在 `dealloc` 中对视图层次结构进行更改。我们知道，这类对 UIKit 的调用需要发生在主线程上。

由于次要线程、operation 或 block 保留调用者的情况很常见，这一点很容易做错，且相当难以发现/修复。这也曾是 [AFNetworking 中一个长期存在的 bug](https://github.com/AFNetworking/AFNetworking/issues/56)，只是因为知道此问题的人不多——而且一如既往，它表现为罕见、难以复现的崩溃。一致地使用 __weak，并且不在异步 block/operation 中访问 ivar，会有帮助。

#### 集合类

Apple 有一份针对 [iOS 与 Mac](https://developer.apple.com/library/ios/#documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html#//apple_ref/doc/uid/10000057i-CH12-SW1) 的良好概览文档，列出了最常见 Foundation 类的线程安全性。总体而言，像 `NSArray` 这样的不可变类是线程安全的，而其可变变体如 `NSMutableArray` 则不是。实际上，从不同线程使用它们是可以的，只要访问在队列内被串行化。请记住：方法可能返回集合对象的可变变体，即便它们声明的返回类型是不可变的。写成类似 `return [array copy]` 以确保返回对象确实不可变，是良好实践。

与 [Java](http://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ConcurrentHashMap.html) 等语言不同，Foundation 框架并未开箱即用地提供线程安全的集合类。这其实非常合理，因为多数情况下你希望把锁应用在更高层，以避免过多的加锁操作。一个值得注意的例外是缓存：可变字典可能持有不可变数据——Apple 在 iOS 4 中加入了 `NSCache`，它不仅对访问加锁，还会在低内存情况下清除其内容。

即便如此，你的应用中可能仍有线程安全的可变字典派得上用场的合理场景。得益于类簇方法，[编写一个并不难](https://gist.github.com/steipete/5928916)。

### Atomic 属性

有没有想过 Apple 如何处理属性的 atomic 设置/获取？到现在你大概已听说过自旋锁、信号量、锁、@synchronized——那么 Apple 用的是什么？幸运的是，[Objective-C 运行时是公开的](http://www.opensource.apple.com/source/objc4/)，我们可以一窥幕后。

一个 nonatomic 属性的 setter 可能如下所示：

```
- (void)setUserName:(NSString *)userName {
      if (userName != _userName) {
          [userName retain];
          [_userName release];
          _userName = userName;
      }
}
```

这是手动 retain/release 的变体；不过 ARC 生成的代码看起来类似。看这段代码就能明白，为何在并发调用 `setUserName:` 时会出问题。我们最终可能释放 `_userName` 两次，这会损坏内存并导致难以发现的 bug。

对于任何未手动实现的属性，编译器内部会生成对 [`objc_setProperty_non_gc(id self, SEL _cmd, ptrdiff_t offset, id newValue, BOOL atomic, signed char shouldCopy)`](https://github.com/opensource-apple/objc4/blob/master/runtime/Accessors.subproj/objc-accessors.mm#L127) 的调用。在我们的例子中，调用参数会如下所示：

```
objc_setProperty_non_gc(self, _cmd, 
  (ptrdiff_t)(&_userName) - (ptrdiff_t)(self), userName, NO, NO);`
```

`ptrdiff_t` 可能看起来怪异，但归根结底只是简单的指针算术，因为 Objective-C 类不过是另一种 C 结构体。

`objc_setProperty` 会下沉到下面的方法：

```
static inline void reallySetProperty(id self, SEL _cmd, id newValue, 
  ptrdiff_t offset, bool atomic, bool copy, bool mutableCopy) 
{
    id oldValue;
    id *slot = (id*) ((char*)self + offset);

    if (copy) {
        newValue = [newValue copyWithZone:NULL];
    } else if (mutableCopy) {
        newValue = [newValue mutableCopyWithZone:NULL];
    } else {
        if (*slot == newValue) return;
        newValue = objc_retain(newValue);
    }

    if (!atomic) {
        oldValue = *slot;
        *slot = newValue;
    } else {
        spin_lock_t *slotlock = &PropertyLocks[GOODHASH(slot)];
        _spin_lock(slotlock);
        oldValue = *slot;
        *slot = newValue;        
        _spin_unlock(slotlock);
    }

    objc_release(oldValue);
}
```

抛开相当有趣的名字不谈，这个方法其实相当直观，并使用了 `PropertyLocks` 中 128 个可用自旋锁之一。这是一种务实且快速的方法——最坏情况是某个 setter 可能因哈希碰撞而不得不等待一个无关的 setter 完成。

虽然这些方法未在任何公共头文件中声明，但可以手动调用它们。我并不是说这是个好主意，但知道这一点很有意思，若你既想要 atomic 属性_又_同时实现 setter，可能会相当有用。

```
// Manually declare runtime methods.
extern void objc_setProperty(id self, SEL _cmd, ptrdiff_t offset, 
  id newValue, BOOL atomic, BOOL shouldCopy);
extern id objc_getProperty(id self, SEL _cmd, ptrdiff_t offset, 
  BOOL atomic);

#define PSTAtomicRetainedSet(dest, src) objc_setProperty(self, _cmd, 
  (ptrdiff_t)(&dest) - (ptrdiff_t)(self), src, YES, NO) 
#define PSTAtomicAutoreleasedGet(src) objc_getProperty(self, _cmd, 
  (ptrdiff_t)(&src) - (ptrdiff_t)(self), YES)
```

[参见此 gist](https://gist.github.com/steipete/5928690) 获取包含处理结构体代码的完整片段。但请记住，我们不建议使用它。

#### 那么 @synchronized 呢？

你可能好奇 Apple 为何不使用已有的运行时特性 `@synchronized(self)` 来做属性加锁。一旦你[查看源码](https://github.com/opensource-apple/objc4/blob/master/runtime/objc-sync.mm#L291)，就会发现其中发生的事情要多得多。Apple 使用了[多达三次加锁/解锁序列](http://googlemac.blogspot.co.at/2006/10/synchronized-swimming.html)，部分原因是他们还加入了[异常展开](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/Multithreading/ThreadSafety/ThreadSafety.html#//apple_ref/doc/uid/10000057i-CH8-SW3)。与快得多的自旋锁方法相比，这会造成减速。由于设置属性通常相当快，自旋锁非常适合这项工作。当你需要确保可以抛出异常而不使代码死锁时，`@synchonized(self)` 是不错的选择。

### 你自己的类

仅使用 atomic 属性并不会使你的类线程安全。它只会保护你免受 setter 中的[竞态条件](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#shared_resources)，但不会保护你的应用逻辑。考虑下面的片段：

```
if (self.contents) {
    CFAttributedStringRef stringRef = CFAttributedStringCreate(NULL, 
      (__bridge CFStringRef)self.contents, NULL);
    // draw string
}
```

我很早就在 [PSPDFKit](http://pspdfkit.com) 中犯过这个错误。时不时地，当 `contents` 属性在检查之后被设为 nil 时，应用会以 EXC_BAD_ACCESS 崩溃。对此问题的简单修复是捕获该变量：

```
NSString *contents = self.contents;
if (contents) {
    CFAttributedStringRef stringRef = CFAttributedStringCreate(NULL, 
      (__bridge CFStringRef)contents, NULL);
    // draw string
}
```

这会解决这里的问题，但多数情况下没那么简单。想象我们也有一个 `textColor` 属性，并在一个线程上更改这两个属性。那么我们的渲染线程可能最终使用新内容搭配旧颜色值，从而得到怪异的组合。这是 Core Data 将模型对象绑定到一个线程或队列的原因之一。

对此问题没有放之四海而皆准的解决方案。使用[不可变模型](http://www.cocoawithlove.com/2008/04/value-of-immutable-values.html)是一种方案，但它也有自己的问题。另一种方式是将现有对象的更改限制在主线程或特定队列上，并在工作线程上使用它们之前生成副本。我推荐 Jonathan Sterling 关于 [Objective-C 中的轻量不可变性](http://www.jonmsterling.com/posts/2012-12-27-a-pattern-for-immutability.html)的文章，以获得解决此问题的更多想法。

简单的解决方案是使用 @synchronize。其他任何做法都极有可能让你陷入麻烦。比这聪明得多的人也一再失败。

#### 实用的线程安全设计

在尝试使某物线程安全之前，先认真想想是否有必要。确保这不是过早优化。若它像配置类之类的东西，就没必要考虑线程安全。更好的做法是加入一些断言以确保正确使用：

```
void PSPDFAssertIfNotMainThread(void) {
    NSAssert(NSThread.isMainThread, 
      @"Error: Method needs to be called on the main thread. %@", 
      [NSThread callStackSymbols]);
}
```

不过确实有些代码应当是线程安全的；缓存类就是一个好例子。一个好方法是使用并发的 dispatch_queue 作为读写锁以最大化性能，并尽量只锁定真正必要的区域。一旦开始使用多个队列来锁定不同部分，事情很快就会变得棘手。

有时你也可以重写代码，使特殊锁变得不必要。考虑这个多播委托形式的片段。（许多情况下，使用 NSNotifications 会更好，但也有[多播委托的合理用例。](https://code.google.com/r/riky-adsfasfasf/source/browse/Utilities/GCDMulticastDelegate.h)）

```
// header
@property (nonatomic, strong) NSMutableSet *delegates;

// in init
_delegateQueue = dispatch_queue_create("com.PSPDFKit.cacheDelegateQueue", 
  DISPATCH_QUEUE_CONCURRENT);

- (void)addDelegate:(id<PSPDFCacheDelegate>)delegate {
    dispatch_barrier_async(_delegateQueue, ^{
        [self.delegates addObject:delegate];
    });
}

- (void)removeAllDelegates {
    dispatch_barrier_async(_delegateQueue, ^{
        self.delegates removeAllObjects];
    });
}

- (void)callDelegateForX {
    dispatch_sync(_delegateQueue, ^{
        [self.delegates enumerateObjectsUsingBlock:^(id<PSPDFCacheDelegate> delegate, NSUInteger idx, BOOL *stop) {
            // Call delegate
        }];
    });
}
```

除非每秒调用 `addDelegate:` 或 `removeDelegate:` 上千次，否则更简单、更干净的方法如下：

```
// header
@property (atomic, copy) NSSet *delegates;

- (void)addDelegate:(id<PSPDFCacheDelegate>)delegate {
    @synchronized(self) {
        self.delegates = [self.delegates setByAddingObject:delegate];
    }
}

- (void)removeAllDelegates {
    @synchronized(self) {
        self.delegates = nil;
    }
}

- (void)callDelegateForX {
    [self.delegates enumerateObjectsUsingBlock:^(id<PSPDFCacheDelegate> delegate, NSUInteger idx, BOOL *stop) {
        // Call delegate
    }];
}
```

诚然，这个例子有些刻意，也可以干脆把更改限制在主线程上。但对许多数据结构而言，在修改方法中创建不可变副本可能是值得的，这样一般应用逻辑就不必处理过度的加锁。

## GCD 的陷阱

对于你的大多数加锁需求，GCD 都很完美。它简单、快速，其基于 block 的 API 使意外造成不平衡的锁变得困难得多。然而，仍有不少陷阱，我们将在此探讨其中一些。

### 将 GCD 用作递归锁

GCD 是用于串行化对共享资源访问的队列。这可用于加锁，但与 `@synchronized` 相当不同。GCD 队列不可重入——那会破坏队列特性。许多人试图用 `dispatch_get_current_queue()` 绕过这一点，这是[一个坏主意](https://gist.github.com/steipete/3713233)，Apple 在 iOS 6 中弃用该方法是有理由的。

```
// This is a bad idea.
inline void pst_dispatch_sync_reentrant(dispatch_queue_t queue, 
  dispatch_block_t block) 
{
    dispatch_get_current_queue() == queue ? block() 
                                          : dispatch_sync(queue, block);
}
```

检测当前队列对简单方案可能管用，但一旦代码变得更复杂，且可能同时锁定多个队列，就会失败。到了那一步，你几乎肯定会遇到[死锁](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#dead_locks)。当然，可以使用 `dispatch_get_specific()`，它会遍历整个队列层次结构来测试特定队列。为此你得编写自定义队列构造器来应用这些元数据。别走那条路。在某些用例中，`NSRecursiveLock` 是更好的解决方案。

### 用 dispatch_async 修复时序问题

UIKit 中有些时序问题？多数时候，这会是完美的「修复」：

```
dispatch_async(dispatch_get_main_queue(), ^{
    // Some UIKit call that had timing issues but works fine 
    // in the next runloop.
    [self updatePopoverSize];
});
```

别这样做，相信我。随着应用变大，这会回来纠缠你。它极难调试，很快当你因「时序问题」需要越来越多地派发时，事情就会分崩离析。仔细检查你的代码，找到调用的正确位置（例如 viewWillAppear 而非 viewDidLoad）。我的代码库中仍有一些此类技巧，但大多数都有妥善文档，并已提交 issue。

请记住，这并非真正特定于 GCD，而是一种常见的反模式，只是用 GCD 很容易这样做。你可以将同样的智慧应用于 `performSelector:afterDelay:`，其中 delay 为 0.f 以进入下一个 runloop。

### 在性能关键代码中混用 dispatch_sync 与 dispatch_async

弄清这一点花了我一段时间。在 [PSPDFKit](http://pspdfkit.com) 中有一个缓存类，使用 LRU 列表跟踪图片访问。滚动页面时，这会被调用_很多次_。最初的实现用 dispatch_sync 做可用性访问，用 dispatch_async 更新 LRU 位置。这导致帧率远达不到 60 FPS 的目标。

当你的应用中运行的其他代码阻塞了 GCD 的线程时，派发管理器可能要花一段时间才能找到线程来执行 dispatch_async 代码——在那之前，你的 sync 调用会被阻塞。即便像本例中 async 情况的执行顺序并不重要，也没有简单方法告诉 GCD。读写锁在这里帮不了你，因为 async 过程肯定需要进行 barrier 写入，而在此期间所有读者都会被锁定。教训：`dispatch_async` 若被误用可能很昂贵。将其用于加锁时要小心。

### 用 dispatch_async 派发内存密集型操作

我们已经谈了很多关于 NSOperation，以及通常最好使用更高层 API。若你处理的是做内存密集型操作的工作块，尤其如此。

在旧版 PSPDFKit 中，我用 GCD 队列派发将缓存的 JPG 图片写入磁盘。当视网膜 iPad 问世后，这开始造成麻烦。分辨率翻倍，编码图片数据所需时间远超渲染时间。结果，操作在队列中堆积，系统繁忙时可能因内存耗尽而崩溃。

没有办法查看有多少操作在排队（除非你手动添加代码来跟踪），也没有内置方式在低内存通知时取消操作。切换到 NSOperation 使代码可调试性高得多，并允许在不编写手动管理代码的情况下实现这一切。

当然也有一些注意事项；例如你无法在 `NSOperationQueue` 上设置目标队列（如用于节流 I/O 的 `DISPATCH_QUEUE_PRIORITY_BACKGROUND`）。但相对于可调试性而言这是小代价，而且也能防止你陷入像[优先级反转](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/#priority_inversion)这样的问题。我甚至建议不要用漂亮的 `NSBlockOperation` API，而建议真正的 NSOperation 子类，包括实现 description。工作更多，但之后能打印所有正在运行/挂起的操作会极其有用。

---
