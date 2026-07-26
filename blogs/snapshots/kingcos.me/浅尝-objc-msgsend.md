---
title: 浅尝 objc_msgSend
source_url: 'https://kingcos.me/posts/2019/objc_msgsend/'
source_domain: kingcos.me
source_group: single-site
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:dda5467c8181744c'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
container: '//div[contains(@class,''markdown'')]'
container_source: guess
---

> 原文：[浅尝 objc_msgSend](https://kingcos.me/posts/2019/objc_msgsend/)

| Date | Notes | Refers. |
|---|---|---|
| 2019-07-20 | 首次提交 | [objc4-750.1](https://opensource.apple.com/tarballs/objc4/) |
| 2019-09-07 | 完成「缓存、动态方法解析」等部分 | [Obj-C 中的对象 - kingcos](https://kingcos.me/posts/2019/objects_in_obj-c/) |
| 2019-10-21 | 补充《Effective Objective-C 2.0》相关内容 | 《[〈编写高质量 iOS 与 OS X 代码的 52 个有效方法〉阅读笔记 - kingcos](https://kingcos.me/posts/2019/effective_obj-c_2.0_notes/)》 |

![0](https://kingcos.me/img/2019/objc_msgsend/0.png)

## Preface

Obj-C 中方法调用的本质是消息发送机制，即 `[foo bar]` 是向 `foo` 对象发送一条 `bar` 的消息，而消息发送就是通过 `objc_msgSend` 所进行的。那么这次本文就简单窥探一下 `objc_msgSend` 吧。

## Why

在开始之前，先思考以下为什么 Obj-C 中方法调用的本质是 `objc_msgSend` 呢？

我们创建一个使用 Obj-C 的 iOS 项目，如下在 `ViewController` 中添加一个按钮，并在按钮的点击事件中创建一个 Obj-C 对象，再调用其方法：

```objectivec
#import "ViewController.h"

@interface Foo : NSObject
- (void)bar;
@end

@implementation Foo
- (void)bar {}
@end

@interface ViewController ()
@end

@implementation ViewController

- (IBAction)clickOnButton:(UIButton *)sender {
    Foo *foo = [[Foo alloc] init];

    [foo bar]; // Breakpoint 🔴
}

@end
```

我们将断点打在 `[foo bar];` 一行，启动程序并点击按钮。在 Xcode 的控制台多次输入 `si`（Step Into）即可最终跳转到 `objc_msgSend`：

![3](https://kingcos.me/img/2019/objc_msgsend/3.png)

或者我们也可以使用 `xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc ViewController.m -o foo.cpp` 将 Obj-C 代码翻译为 C/C++：

```objectivec
static void _I_ViewController_clickOnButton_(ViewController * self, SEL _cmd, UIButton *sender) {
    Foo *foo = ((Foo *(*)(id, SEL))(void *)objc_msgSend)((id)((Foo *(*)(id, SEL))(void *)objc_msgSend)((id)objc_getClass("Foo"), sel_registerName("alloc")), sel_registerName("init"));

    // objc_msgSend(foo, sel_registerName("bar"))
    ((void (*)(id, SEL))(void *)objc_msgSend)((id)foo, sel_registerName("bar"));
}
```

综上，我们可以说 Obj-C 中方法调用的本质即是 `objc_msgSend`。

## Steps

`objc_msgSend` 总共分为消息发送、动态方法解析、以及消息转发三大部分，下面我们就依次来研究一下。

### 消息发送

`objc_msgSend` 中的第一个部分是消息发送，即对消息接收者发送一条方法消息，当接收者可以处理消息时将执行相应的方法，无法处理时则进入下一步骤。

#### Where & Why

在 Apple 开源的 objc4 源码中，我们似乎只能在「message.h」中找到 `objc_msgSend` 的声明，其将消息接收者（即对象）作为第一个参数，将消息（即方法选择器）作为第二个参数，并将方法的参数追加在参数列表的最后：

```c
// message.h

/**
 * Sends a message with a simple return value to an instance of a class.
 * 发送一个带有简易返回值的消息到一个类的实例。
 *
 * @param self A pointer to the instance of the class that is to receive the message.
 *             指向接收消息者实例的指针。
 * @param op The selector of the method that handles the message.
 *           处理消息的选择器。
 * @param ...
 *   A variable argument list containing the arguments to the method.
 *   包含方法参数的可变参数列表。
 *
 * @return The return value of the method.
 *         方法的返回值。
 *
 * @note When it encounters a method call, the compiler generates a call to one of the
 *  functions \c objc_msgSend, \c objc_msgSend_stret, \c objc_msgSendSuper, or \c objc_msgSendSuper_stret.
 *  Messages sent to an object’s superclass (using the \c super keyword) are sent using \c objc_msgSendSuper;
 *  other messages are sent using \c objc_msgSend. Methods that have data structures as return values
 *  are sent using \c objc_msgSendSuper_stret and \c objc_msgSend_stret.
 * 注意：当遇到方法调用时，编译器会生成对 objc_msgSend、objc_msgSend_stret、objc_msgSendSuper、objc_msgSendSuper_stret 四个函数之一的调用。
 * 到达对象父类（使用 super 关键字）的消息通过 objc_msgSendSuper 发送；其它消息则通过 objc_msgSend 发送。
 * 返回值为结构体的消息通过 objc_msgSendSuper_stret 或 objc_msgSend_stret 发送。
 *
 */
OBJC_EXPORT id _Nullable
objc_msgSend(id _Nullable self, SEL _Nonnull op, ...)
    OBJC_AVAILABLE(10.0, 2.0, 9.0, 1.0, 2.0);
```

![1](https://kingcos.me/img/2019/objc_msgsend/1.png)

而 `objc_msgSend` 的具体实现是由汇编语言编写的，原因有两点：

1. 对性能的极致追求，因为每一条汇编指令都对应一条机器指令，使用汇编可便于针对不同架构的 CPU 优化每一条指令的速度；
2. C 语言无法实现一个保存未知参数且支持跳转到任一函数指针处的函数，对于 C 来说没有必要的特性来表示（引自 [Dissecting objc_msgSend on ARM64 - Mike Ash](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)）。

由于 `objc_msgSend` 整个流程比较复杂，下面我将尝试把流程分解为多个用例，逐个分析。

#### 当接收者为 `nil` 时

当接收者为 `nil` 时，即 `[foo bar]` 中的 `foo` 为 `nil`：

```objectivec
- (IBAction)clickOnButton:(UIButton *)sender {
    Foo *foo = [[Foo alloc] init];

    // 将接收者置为 nil
    foo = nil;
    [foo bar];
}

// LLDB:
// 进入 objc_msgSend 后可以尝试使用 LLDB 命令读取 x0 寄存器中存储的值
// (lldb) register read x0
//       x0 = 0x0000000000000000
```

我们从 `ENTRY _objc_msgSend` 的第一条语句 `cmp p0, #0` 开始：

![4](https://kingcos.me/img/2019/objc_msgsend/4.png)

在 Xcode 中 `si` 执行即可看到具体的汇编代码跳转，也与上图的源码分析一致：

```asm
libobjc.A.dylib`objc_msgSend:
    0x192bd8180 <+0>:   cmp    x0, #0x0                  ; =0x0
    0x192bd8184 <+4>:   b.le   0x192bd81f8               ; <+120>
    ; ...
    0x192bd81f8 <+120>: b.eq   0x192bd8230               ; <+176>
    ; ...
    0x192bd8230 <+176>: mov    x1, #0x0
    0x192bd8234 <+180>: movi   d0, #0000000000000000
    0x192bd8238 <+184>: movi   d1, #0000000000000000
    0x192bd823c <+188>: movi   d2, #0000000000000000
    0x192bd8240 <+192>: movi   d3, #0000000000000000
    0x192bd8244 <+196>: ret
```

#### 方法缓存

```cpp
struct objc_class : objc_object {
    // Class ISA;
    Class superclass;
    // ⬇️ 方法缓存
    cache_t cache;             // formerly cache pointer and vtable
    class_data_bits_t bits;    // class_rw_t * plus custom rr/alloc flags
};
```

在 [Obj-C 中的对象](https://kingcos.me/posts/2019/objects_in_obj-c/)一文中，我们简单了解了 Obj-C 中类和元类对象的结构，其中的 `cache_t cache;` 是方法缓存。那么为什么需要缓存呢？

Obj-C 的消息发送本质属于**动态绑定（Dynamic Binding）**，而非 C 语言常用的静态绑定（Static Binding）。动态绑定意味着只有在运行时才能确定真正被调用的函数；而静态绑定在编译时即可确定（不考虑内联函数的前提下），编译器会直接生成调用函数的指令，函数地址就被硬编码在指令当中。

> **Tips - 内联（Inline）函数**
> 
> 建议编译器对函数进行内联扩展，即建议编译器将指定的函数体直接插入到每一处调用该函数的地方（注：「建议」指具体是否进行内联需要看编译器本身）。

因此对于动态绑定的语言来说，其方法查找的速度一定是慢于静态绑定的。为了提高效率，Obj-C 会将方法查找的结果缓存在 `cache_t cache;` 中，当后续发送同样的消息时即可得到更快得执行。

```cpp
// _uint32_t.h

typedef unsigned int uint32_t;

// _uintptr_t.h

typedef unsigned long           uintptr_t;

// objc-ptrauth.h

using MethodCacheIMP = IMP;

// objc-runtime-new.h

#if __LP64__
typedef uint32_t mask_t;  // x86_64 & arm64 asm are less efficient with 16-bits
#else
typedef uint16_t mask_t;
#endif
typedef uintptr_t cache_key_t;

struct bucket_t {
private:
    // IMP-first is better for arm64e ptrauth and no worse for arm64.
    // SEL-first is better for armv7* and i386 and x86_64.
#if __arm64__
    MethodCacheIMP _imp;
    cache_key_t _key;
#else
    cache_key_t _key;
    MethodCacheIMP _imp;
#endif

    // ...
};

struct cache_t {
    struct bucket_t *_buckets;
    mask_t _mask;
    mask_t _occupied;

    // ...
};
```

`cache_t` 结构体中存储了指向 `bucket_t` 结构体（数组）的指针、`_mask`（表示散列表容量 - 1，详见下文源码）、以及 `_occupied`（表示已缓存方法的数量）。`bucket_t` 即缓存方法的散列表，方法名将作为键，`IMP` 即方法的内存地址将作为值。

#### 当未命中缓存时

方法的首次调用或遇到缓存扩容后无法命中缓存，将进入 C 函数中搜索，并在找到方法后缓存在调用者本身的缓存中。因此我们仍从 `cmp p0, #0` 开始，但这次接收者并非 `nil` 所以不会跳入判空分支：

![5](https://kingcos.me/img/2019/objc_msgsend/5.png)

到达 `bl __class_lookupMethodAndLoadCache3` 后将跳入 C 函数 `_class_lookupMethodAndLoadCache3` 中：

```cpp
// objc-runtime-new.mm

/***********************************************************************
* _class_lookupMethodAndLoadCache.
* Method lookup for dispatchers ONLY. OTHER CODE SHOULD USE lookUpImp().
* 仅供调度程序所使用的方法查找。其它代码应当使用 lookUpImp()。
* This lookup avoids optimistic cache scan because the dispatcher
* already tried that.
* 此查找可避免乐观缓存扫描，因为调度程序已经尝试了此操作。
**********************************************************************/
IMP _class_lookupMethodAndLoadCache3(id obj, SEL sel, Class cls)
{
    // ⬇️ 查找 IMP 或转发
    return lookUpImpOrForward(cls, sel, obj,
                              YES/*initialize*/, NO/*cache*/, YES/*resolver*/);
}

/***********************************************************************
* lookUpImpOrForward.
* The standard IMP lookup.
* 标准 IMP 查找。
* initialize==NO tries to avoid +initialize (but sometimes fails)
* initialize==NO 尝试避免调用 +initialize（但有时会失败）
* cache==NO skips optimistic unlocked lookup (but uses cache elsewhere)
* cache==NO 跳过乐观解锁查找（但在其它地方使用缓存）
* Most callers should use initialize==YES and cache==YES.
* 大多数调用者应当使用 initialize==YES 和 cache==YES。
* inst is an instance of cls or a subclass thereof, or nil if none is known.
* inst 是 cls 或其子类的实例，若未知则为 nil。
*   If cls is an un-initialized metaclass then a non-nil inst is faster.
*   如果 cls 是未初始化的元类，那么非空 inst 将更快。
* May return _objc_msgForward_impcache. IMPs destined for external use
*   must be converted to _objc_msgForward or _objc_msgForward_stret.
* 可能会返回 _objc_msgForward_impcache。被指定外部使用的 IMP 必须转换为 _objc_msgForward 或 _objc_msgForward_stret。
*   If you don't want forwarding at all, use lookUpImpOrNil() instead.
*   如果不你需要任何转发，使用 lookUpImpOrNil() 代替。
**********************************************************************/
IMP lookUpImpOrForward(Class cls, SEL sel, id inst,
                       bool initialize, bool cache, bool resolver)
{
    IMP imp = nil;
    bool triedResolver = NO;

    runtimeLock.assertUnlocked();

    // Optimistic cache lookup
    // cache 为 NO，跳过
    if (cache) {
        imp = cache_getImp(cls, sel);
        if (imp) return imp;
    }

    // runtimeLock is held during isRealized and isInitialized checking
    // to prevent races against concurrent realization.

    // runtimeLock is held during method search to make
    // method-lookup + cache-fill atomic with respect to method addition.
    // Otherwise, a category could be added but ignored indefinitely because
    // the cache was re-filled with the old value after the cache flush on
    // behalf of the category.

    runtimeLock.lock();
    checkIsKnownClass(cls);

    // 若类未实化，则进行实化
    if (!cls->isRealized()) {
        realizeClass(cls);
    }

    if (initialize  &&  !cls->isInitialized()) {
        runtimeLock.unlock();
        _class_initialize (_class_getNonMetaClass(cls, inst));
        runtimeLock.lock();
        // If sel == initialize, _class_initialize will send +initialize and
        // then the messenger will send +initialize again after this
        // procedure finishes. Of course, if this is not being called
        // from the messenger then it won't happen. 2778172
    }

 retry:
    runtimeLock.assertLocked();

    // Try this class's cache.

    // ⬇️ 再次尝试从缓存中取 IMP（汇编）
    imp = cache_getImp(cls, sel);
    // 取到了则结束
    if (imp) goto done;

    // Try this class's method lists.
    {
        // ⬇️ 根据 SEL 获取本类的方法
        Method meth = getMethodNoSuper_nolock(cls, sel);
        if (meth) {
            // ⬇️ 如果获取到方法了，则填充缓存，并返回 IMP
            log_and_fill_cache(cls, meth->imp, sel, inst, cls);
            imp = meth->imp;
            goto done;
        }
    }

    // Try superclass caches and method lists.
    {
        unsigned attempts = unreasonableClassCount();
        // 如果本类找不到，则去父类（父类的父类）中查找
        for (Class curClass = cls->superclass;
             curClass != nil;
             curClass = curClass->superclass)
        {
            // Halt if there is a cycle in the superclass chain.
            if (--attempts == 0) {
                _objc_fatal("Memory corruption in class list.");
            }

            // Superclass cache.
            // 在父类缓存中找
            imp = cache_getImp(curClass, sel);
            if (imp) {
                if (imp != (IMP)_objc_msgForward_impcache) {
                    // Found the method in a superclass. Cache it in this class.
                    // 父类中找到了，则在本类缓存并返回 IMP
                    log_and_fill_cache(cls, imp, sel, inst, curClass);
                    goto done;
                }
                else {
                    // ⚠️ 父类的方法转发入口，停止循环
                    // Found a forward:: entry in a superclass.
                    // Stop searching, but don't cache yet; call method
                    // resolver for this class first.
                    break;
                }
            }

            // Superclass method list.
            // 父类缓存未找到，则在父类的方法列表中查找
            Method meth = getMethodNoSuper_nolock(curClass, sel);
            if (meth) {
                // 找到则在本类缓存
                log_and_fill_cache(cls, meth->imp, sel, inst, curClass);
                imp = meth->imp;
                goto done;
            }
        }
    }

    // No implementation found. Try method resolver once.
    // IMP 找不到，则进入方法动态解析一次。详见下文「动态方法解析」一节。
    if (resolver  &&  !triedResolver) {
        runtimeLock.unlock();
        _class_resolveMethod(cls, sel, inst);
        runtimeLock.lock();
        // Don't cache the result; we don't hold the lock so it may have
        // changed already. Re-do the search from scratch instead.
        // 标记为 YES
        triedResolver = YES;
        goto retry;
    }

    // No implementation found, and method resolver didn't help.
    // Use forwarding.
    // 实现无法找到，方法解析无效，尝试方法转发。

    imp = (IMP)_objc_msgForward_impcache;
    cache_fill(cls, sel, imp, inst);

 done:
    runtimeLock.unlock();

    return imp;
}

static method_t *
getMethodNoSuper_nolock(Class cls, SEL sel)
{
    runtimeLock.assertLocked();

    assert(cls->isRealized());
    // fixme nil cls?
    // fixme nil sel?

    for (auto mlists = cls->data()->methods.beginLists(),
              end = cls->data()->methods.endLists();
         mlists != end;
         ++mlists)
    {
        // ⬇️ 在方法列表中查找方法
        method_t *m = search_method_list(*mlists, sel);
        if (m) return m;
    }

    return nil;
}

/***********************************************************************
* getMethodNoSuper_nolock
* fixme
* Locking: runtimeLock must be read- or write-locked by the caller
**********************************************************************/
static method_t *search_method_list(const method_list_t *mlist, SEL sel)
{
    int methodListIsFixedUp = mlist->isFixedUp();
    int methodListHasExpectedSize = mlist->entsize() == sizeof(method_t);

    if (__builtin_expect(methodListIsFixedUp && methodListHasExpectedSize, 1)) {
        // 在已排序的方法列表中查找
        return findMethodInSortedMethodList(sel, mlist);
    } else {
        // Linear search of unsorted method list
        // 线性查找未排序方法列表
        for (auto& meth : *mlist) {
            if (meth.name == sel) return &meth;
        }
    }

#if DEBUG
    // sanity-check negative results
    if (mlist->isFixedUp()) {
        for (auto& meth : *mlist) {
            if (meth.name == sel) {
                _objc_fatal("linear search worked when binary search did not");
            }
        }
    }
#endif

    return nil;
}

/***********************************************************************
* log_and_fill_cache
* Log this method call. If the logger permits it, fill the method cache.
* 记录该方法调用。如果记录器允许，填充方法缓存。
* cls is the method whose cache should be filled.
* 方法应当填充在 cls 的缓存中。
* implementer is the class that owns the implementation in question.
* implementer 指拥有相关实现的类。
**********************************************************************/
static void
log_and_fill_cache(Class cls, IMP imp, SEL sel, id receiver, Class implementer)
{
#if SUPPORT_MESSAGE_LOGGING
    if (objcMsgLogEnabled) {
        bool cacheIt = logMessageSend(implementer->isMetaClass(),
                                      cls->nameForLogging(),
                                      implementer->nameForLogging(),
                                      sel);
        if (!cacheIt) return;
    }
#endif
    // ⬇️ 填充缓存
    cache_fill (cls, sel, imp, receiver);
}

// objc-cache.mm

void cache_fill(Class cls, SEL sel, IMP imp, id receiver)
{
#if !DEBUG_TASK_THREADS
    mutex_locker_t lock(cacheUpdateLock);
    // ⬇️ 填充缓存
    cache_fill_nolock(cls, sel, imp, receiver);
#else
    _collecting_in_critical();
    return;
#endif
}

static void cache_fill_nolock(Class cls, SEL sel, IMP imp, id receiver)
{
    cacheUpdateLock.assertLocked();

    // Never cache before +initialize is done
    // 若类未初始化，则返回
    if (!cls->isInitialized()) return;

    // Make sure the entry wasn't added to the cache by some other thread
    // before we grabbed the cacheUpdateLock.
    // 若缓存中已存在，则返回
    if (cache_getImp(cls, sel)) return;

    cache_t *cache = getCache(cls);
    // ⬇️ 获取缓存 key，本质即 SEL
    cache_key_t key = getKey(sel);

    // Use the cache as-is if it is less than 3/4 full
    // 如果小于等于 3/4 满，则使用缓存
    // newOccupied 为当前占用数 + 1
    mask_t newOccupied = cache->occupied() + 1;
    // capacity 为容量（mask + 1 或 0）
    mask_t capacity = cache->capacity();
    if (cache->isConstantEmptyCache()) {
        // 缓存为空
        // Cache is read-only. Replace it.
        // 重新分配内存
        cache->reallocate(capacity, capacity ?: INIT_CACHE_SIZE);
    }
    else if (newOccupied <= capacity / 4 * 3) {
        // Cache is less than 3/4 full. Use it as-is.
        // 缓存已占用比例小于等于 3/4，则使用
    }
    else {
        // Cache is too full. Expand it.
        // ⬇️ 大于 3/4 则先扩容。
        cache->expand();
    }

    // Scan for the first unused slot and insert there.
    // 扫描首个未使用的间隙并插入。
    // There is guaranteed to be an empty slot because the
    // minimum size is 4 and we resized at 3/4 full.
    // 能够被确保有空间隙是因为最小大小为 4，并重调为 3/4 满。
    // ⬇️ 查找要存入的 bucket_t
    bucket_t *bucket = cache->find(key, receiver);
    // key 为空，则为新占用缓存，占用数需自增
    if (bucket->key() == 0) cache->incrementOccupied();
    // 存入 bucket
    bucket->set(key, imp);
}

mask_t cache_t::capacity()
{
    return mask() ? mask()+1 : 0;
}

cache_key_t getKey(SEL sel)
{
    assert(sel);
    // 将 SEL 强转为 cache_key_t 类型
    return (cache_key_t)sel;
}

// 🌟 根据 key 查找 bucket_t
bucket_t * cache_t::find(cache_key_t k, id receiver)
{
    assert(k != 0);

    // b 为 buckets 数组首地址
    bucket_t *b = buckets();
    mask_t m = mask();
    // begin 为方法在散列表的索引
    mask_t begin = cache_hash(k, m);
    // 从索引开始遍历
    mask_t i = begin;
    do {
        // 如果该索引对应的 bucket_t 中的 key（SEL）对应了我们查找的 key（即已存在）或为空
        // 则代表当前 bucket_t 可插入
        if (b[i].key() == 0  ||  b[i].key() == k) {
            return &b[i];
        }
        // 索引冲突，则进入当前索引的下一格
    } while ((i = cache_next(i, m)) != begin);

    // hack
    Class cls = (Class)((uintptr_t)this - offsetof(objc_class, cache));
    cache_t::bad_cache(receiver, (SEL)k, cls);
}

// Class points to cache. SEL is key. Cache buckets store SEL+IMP.
// Caches are never built in the dyld shared cache.

static inline mask_t cache_hash(cache_key_t key, mask_t mask)
{
    // key & mask 获得索引
    return (mask_t)(key & mask);
}

static inline mask_t cache_next(mask_t i, mask_t mask) {
    return (i+1) & mask;
}

// 缓存扩容
void cache_t::expand()
{
    cacheUpdateLock.assertLocked();

    uint32_t oldCapacity = capacity();
    // 扩容大小为原空间 2 倍（若原为空，则扩容为初始大小）
    uint32_t newCapacity = oldCapacity ? oldCapacity*2 : INIT_CACHE_SIZE;

    if ((uint32_t)(mask_t)newCapacity != newCapacity) {
        // mask overflow - can't grow further
        // fixme this wastes one bit of mask
        newCapacity = oldCapacity;
    }

    reallocate(oldCapacity, newCapacity);
}

/* Initial cache bucket count. INIT_CACHE_SIZE must be a power of two. */
enum {
    INIT_CACHE_SIZE_LOG2 = 2,
    // 左移 2 位，为 4
    INIT_CACHE_SIZE      = (1 << INIT_CACHE_SIZE_LOG2)
};
```

如上，消息发送的代码被分为两个部分：其一是快速路径（Fast Path），这一部分由汇编语言实现；其二是慢速路径（Slow Path），由 C 语言实现。当未命中缓存时，将调用 C 语言代码来查找方法列表，并缓存方法。

#### 当命中缓存时

当方法被再次调用时，将可以命中缓存得以快速执行：

![6](https://kingcos.me/img/2019/objc_msgsend/6.png)

#### SUPPORT_INDEXED_ISA

`SUPPORT_INDEXED_ISA`，即是否支持索引化 isa 我们可以在源码中找到这段定义的宏：

```objectivec
// objc-config.h

// Define SUPPORT_INDEXED_ISA=1 on platforms that store the class in the isa
// field as an index into a class table.
// 在将类存储在 isa 域中并作为类表索引的平台上定义 SUPPORT_INDEXED_ISA=1。
// Note, keep this in sync with any .s files which also define it.
// Be sure to edit objc-abi.h as well.
#if __ARM_ARCH_7K__ >= 2  ||  (__arm64__ && !__LP64__)
#   define SUPPORT_INDEXED_ISA 1
#else
#   define SUPPORT_INDEXED_ISA 0
#endif
```

比较简单的验证方式是我们可以直接在指定真机运行的代码中尝试获取最终的值：

```objectivec
#if __ARM_ARCH_7K__ >= 2  ||  (__arm64__ && !__LP64__)
#   define SUPPORT_INDEXED_ISA 1
#else
#   define SUPPORT_INDEXED_ISA 0
#endif

// Use of undeclared identifier '__ARM_ARCH_7K__'
// NSLog(@"%d", __ARM_ARCH_7K__);
NSLog(@"%d", __arm64__);           // 1
NSLog(@"%d", __LP64__);            // 1
NSLog(@"%d", SUPPORT_INDEXED_ISA); // 0
```

当然，我还是要细究一下。

`__ARM_ARCH_7K__` 根据名称可以得出是定义在目标为 ARM 7k 架构 CPU 的代码中的标志宏。我们可以在 LLVM 开源的「ARM.cpp」找到其定义：

```cpp
// ARM.cpp

// Unfortunately, __ARM_ARCH_7K__ is now more of an ABI descriptor. The CPU
// happens to be Cortex-A7 though, so it should still get __ARM_ARCH_7A__.
if (getTriple().isWatchABI())
  Builder.defineMacro("__ARM_ARCH_7K__", "2");
```

`__arm64__` 即当目标为 ARM 64 架构 CPU 时为 `1`；`__LP64__` 即 Long Pointer，该标志宏为 `1` 的代码中 `long int` 和指针类型（指针中存储的是内存地址，也即内存地址）的长度为 64 位（8 字节），`int` 为 32 位（4 字节）。

综上，在 iOS 的真机设备中，`SUPPORT_INDEXED_ISA` 的值最终为 `0`。

#### 尾递归调用

🚧

### 动态方法解析

#### What

当一个类或元类自身及其所有父类中都没有相应的方法实现时，将尝试动态方法解析。即调用 `resolveInstanceMethod:` 或 `resolveClassMethod` 类方法（两者依次对应解析实例方法、类方法），如果我们在其中动态将方法添加，那么将可以执行到相应的方法中：

```objectivec
@interface Foo : NSObject
- (void)foo;
+ (void)classFoo;
- (void)tryC;
@end

@implementation Foo

- (void)bar {
    NSLog(@"%s", __func__);
}

+ (void)classBar {
    NSLog(@"%s", __func__);
}

void c_func(id self, SEL _cmd) {
    NSLog(@"%p - %@", self, NSStringFromSelector(_cmd));
}

+ (BOOL)resolveInstanceMethod:(SEL)sel {
    if (sel == @selector(foo)) {
        // 通过 Runtime API 获得类对象中的实例方法
        Method method = class_getInstanceMethod(self, @selector(bar));
        // 动态添加方法
        class_addMethod(self, sel, method_getImplementation(method), method_getTypeEncoding(method));

        return YES;
    }

    if (sel == @selector(tryC)) {
        // 也可以将 C 函数转换为 Method 格式作为动态方法；
        class_addMethod(self, sel, (IMP)c_func, "v16@0:8");
    }

    // 当实现了动态方法解析时，最好按要求返回 YES，但目前看返回值并不影响结果（详见下源码）
    return [super resolveInstanceMethod:sel];
}

+ (BOOL)resolveClassMethod:(SEL)sel {
    if (sel == @selector(classFoo)) {
        // 通过 Runtime API 获得元类对象中的类方法
        Method method = class_getClassMethod(object_getClass(self), @selector(classBar));
        // 动态添加方法（注意将k类方法添加到元类对象中）
        class_addMethod(object_getClass(self), sel, method_getImplementation(method), method_getTypeEncoding(method));

        return YES;
    }

    return [super resolveClassMethod:sel];
}
@end

Foo *foo = [[Foo alloc] init];
[foo foo];

[Foo classFoo];

// OUTPUT:
// -[Foo bar]
// +[Foo classBar]
// 0x2802d0a50 - tryC
```

这里的 `Method` 是一个类似 `Class` 的不透明类型，我们可以在 objc4 源码中看到它的结构，本质即 `method_t`：

```objectivec
// runtime.h

/// An opaque type that represents a method in a class definition.
typedef struct objc_method *Method;

struct objc_method {
    SEL _Nonnull method_name                                 OBJC2_UNAVAILABLE;
    char * _Nullable method_types                            OBJC2_UNAVAILABLE;
    IMP _Nonnull method_imp                                  OBJC2_UNAVAILABLE;
}

// objc-private.h

#if __OBJC2__
typedef struct method_t *Method;
// ...
```

而 `class_addMethod` 将把新方法放置在一个一维方法列表中，并最终附加在 Obj-C 类中 `class_rw_t` 的二维 `method_array_t methods;` 中（因此 `class_addMethod` 对于每个方法只会调用一次）：

```cpp
// objc-runtime-new.mm

BOOL
class_addMethod(Class cls, SEL name, IMP imp, const char *types)
{
    if (!cls) return NO;

    mutex_locker_t lock(runtimeLock);
    // ⬇️
    return ! addMethod(cls, name, imp, types ?: "", NO);
}

/**********************************************************************
* addMethod
* fixme
* Locking: runtimeLock must be held by the caller
**********************************************************************/
static IMP
addMethod(Class cls, SEL name, IMP imp, const char *types, bool replace)
{
    IMP result = nil;

    runtimeLock.assertLocked();

    checkIsKnownClass(cls);

    assert(types);
    assert(cls->isRealized());

    method_t *m;
    if ((m = getMethodNoSuper_nolock(cls, name))) {
        // already exists
        if (!replace) {
            result = m->imp;
        } else {
            result = _method_setImplementation(cls, m, imp);
        }
    } else {
        // fixme optimize
        // 初始化新的 method_list_t
        method_list_t *newlist;
        newlist = (method_list_t *)calloc(sizeof(*newlist), 1);
        newlist->entsizeAndFlags =
            (uint32_t)sizeof(method_t) | fixed_up_method_list;
        newlist->count = 1;
        // 将方法放置在新的方法列表中
        newlist->first.name = name;
        newlist->first.types = strdupIfMutable(types);
        newlist->first.imp = imp;

        // 方法列表的准备工作
        prepareMethodLists(cls, &newlist, 1, NO, NO);
        // ⬇️ 附加方法列表
        cls->data()->methods.attachLists(&newlist, 1);
        flushCaches(cls);

        result = nil;
    }

    return result;
}

static void
prepareMethodLists(Class cls, method_list_t **addedLists, int addedCount,
                   bool baseMethods, bool methodsFromBundle)
{
    runtimeLock.assertLocked();

    if (addedCount == 0) return;

    // Don't scan redundantly
    bool scanForCustomRR = !cls->hasCustomRR();
    bool scanForCustomAWZ = !cls->hasCustomAWZ();

    // There exist RR/AWZ special cases for some class's base methods.
    // But this code should never need to scan base methods for RR/AWZ:
    // default RR/AWZ cannot be set before setInitialized().
    // Therefore we need not handle any special cases here.
    if (baseMethods) {
        assert(!scanForCustomRR  &&  !scanForCustomAWZ);
    }

    // Add method lists to array.
    // Reallocate un-fixed method lists.
    // The new methods are PREPENDED to the method list array.

    for (int i = 0; i < addedCount; i++) {
        method_list_t *mlist = addedLists[i];
        assert(mlist);

        // Fixup selectors if necessary
        if (!mlist->isFixedUp()) {
            fixupMethodList(mlist, methodsFromBundle, true/*sort*/);
        }

        // Scan for method implementations tracked by the class's flags
        if (scanForCustomRR  &&  methodListImplementsRR(mlist)) {
            cls->setHasCustomRR();
            scanForCustomRR = false;
        }
        if (scanForCustomAWZ  &&  methodListImplementsAWZ(mlist)) {
            cls->setHasCustomAWZ();
            scanForCustomAWZ = false;
        }
    }
}

// objc-runtime-new.h

template <typename Element, typename List>
class list_array_tt {
    // ...

    void attachLists(List* const * addedLists, uint32_t addedCount) {
        if (addedCount == 0) return;

        if (hasArray()) {
            // many lists -> many lists
            // 已成二维，则先分配空间，挪动原表，放置新表
            //（关于 memmove & momcpy 可参考文末 Reference 中「iOS 中的 Category」一文）
            uint32_t oldCount = array()->count;
            uint32_t newCount = oldCount + addedCount;
            setArray((array_t *)realloc(array(), array_t::byteSize(newCount)));
            array()->count = newCount;
            memmove(array()->lists + addedCount, array()->lists,
                    oldCount * sizeof(array()->lists[0]));
            memcpy(array()->lists, addedLists,
                   addedCount * sizeof(array()->lists[0]));
        }
        else if (!list  &&  addedCount == 1) {
            // 0 lists -> 1 list
            // 空表则直接附加
            list = addedLists[0];
        }
        else {
            // 1 list -> many lists
            // 一维单表附加至二维
            List* oldList = list;
            uint32_t oldCount = oldList ? 1 : 0;
            uint32_t newCount = oldCount + addedCount;
            setArray((array_t *)malloc(array_t::byteSize(newCount)));
            array()->count = newCount;
            if (oldList) array()->lists[addedCount] = oldList;
            memcpy(array()->lists, addedLists,
                   addedCount * sizeof(array()->lists[0]));
        }
    }

    // ...
};
```

#### How

正如上所述，在上面未命中缓存且本类及所有父类中都无法找到要调用的方法时，将进入 `lookUpImpOrForward` 中的 Method Resovle 即「动态方法解析」：

```cpp
// objc-runtime-new.mm

IMP lookUpImpOrForward(Class cls, SEL sel, id inst,
                       bool initialize, bool cache, bool resolver)
    // ...

    // No implementation found. Try method resolver once.
    // IMP 找不到，则进入方法动态解析一次。
    if (resolver  &&  !triedResolver) {
        runtimeLock.unlock();
        // ⬇️ 尝试方法解析
        _class_resolveMethod(cls, sel, inst);
        runtimeLock.lock();
        // Don't cache the result; we don't hold the lock so it may have
        // changed already. Re-do the search from scratch instead.
        // 标记为 YES
        triedResolver = YES;
        // 添加到方法列表后，进而进入再次尝试从方法列表中获取并存入缓存
        goto retry;
    }

    // ...
}

/***********************************************************************
* _class_resolveMethod
* Call +resolveClassMethod or +resolveInstanceMethod.
* Returns nothing; any result would be potentially out-of-date already.
* Does not check if the method already exists.
**********************************************************************/
void _class_resolveMethod(Class cls, SEL sel, id inst)
{
    if (! cls->isMetaClass()) {
        // 非元类对象，则解析类对象
        // try [cls resolveInstanceMethod:sel]
        _class_resolveInstanceMethod(cls, sel, inst);
    }
    else {
        // 解析元类对象
        // try [nonMetaClass resolveClassMethod:sel]
        // and [cls resolveInstanceMethod:sel]
        _class_resolveClassMethod(cls, sel, inst);
        if (!lookUpImpOrNil(cls, sel, inst,
                            NO/*initialize*/, YES/*cache*/, NO/*resolver*/))
        {
            _class_resolveInstanceMethod(cls, sel, inst);
        }
    }
}

/***********************************************************************
* _class_resolveInstanceMethod
* Call +resolveInstanceMethod, looking for a method to be added to class cls.
* 调用 +resolveInstanceMethod，并查找要添加到 cls 类的方法。
* cls may be a metaclass or a non-meta class.
* cls 可能是元类或非元类。
* Does not check if the method already exists.
* 如果方法已经存在则不检查。
**********************************************************************/
static void _class_resolveInstanceMethod(Class cls, SEL sel, id inst)
{
    // 如果未实现 resolveInstanceMethod 则返回
    if (! lookUpImpOrNil(cls->ISA(), SEL_resolveInstanceMethod, cls,
                         NO/*initialize*/, YES/*cache*/, NO/*resolver*/))
    {
        // Resolver not implemented.
        return;
    }

    BOOL (*msg)(Class, SEL, SEL) = (typeof(msg))objc_msgSend;
    // 使用 objc_msgSend 执行 resolveInstanceMethod，将返回值保存为 resolved
    bool resolved = msg(cls, SEL_resolveInstanceMethod, sel);

    // 根据 resolved 做一些日志等处理
    // Cache the result (good or bad) so the resolver doesn't fire next time.
    // +resolveInstanceMethod adds to self a.k.a. cls
    IMP imp = lookUpImpOrNil(cls, sel, inst,
                             NO/*initialize*/, YES/*cache*/, NO/*resolver*/);

    if (resolved  &&  PrintResolving) {
        if (imp) {
            _objc_inform("RESOLVE: method %c[%s %s] "
                         "dynamically resolved to %p",
                         cls->isMetaClass() ? '+' : '-',
                         cls->nameForLogging(), sel_getName(sel), imp);
        }
        else {
            // Method resolver didn't add anything?
            _objc_inform("RESOLVE: +[%s resolveInstanceMethod:%s] returned YES"
                         ", but no new implementation of %c[%s %s] was found",
                         cls->nameForLogging(), sel_getName(sel),
                         cls->isMetaClass() ? '+' : '-',
                         cls->nameForLogging(), sel_getName(sel));
        }
    }
}

/***********************************************************************
* _class_resolveClassMethod
* Call +resolveClassMethod, looking for a method to be added to class cls.
* 调用 +resolveClassMethod，并查找要添加到 cls 类的方法。
* cls should be a metaclass.
* cls 应当是元类。
* Does not check if the method already exists.
* 如果方法已经存在则不检查。
**********************************************************************/
static void _class_resolveClassMethod(Class cls, SEL sel, id inst)
{
    assert(cls->isMetaClass());

    if (! lookUpImpOrNil(cls, SEL_resolveClassMethod, inst,
                         NO/*initialize*/, YES/*cache*/, NO/*resolver*/))
    {
        // Resolver not implemented.
        return;
    }

    BOOL (*msg)(Class, SEL, SEL) = (typeof(msg))objc_msgSend;
    bool resolved = msg(_class_getNonMetaClass(cls, inst),
                        SEL_resolveClassMethod, sel);

    // Cache the result (good or bad) so the resolver doesn't fire next time.
    // +resolveClassMethod adds to self->ISA() a.k.a. cls
    IMP imp = lookUpImpOrNil(cls, sel, inst,
                             NO/*initialize*/, YES/*cache*/, NO/*resolver*/);

    if (resolved  &&  PrintResolving) {
        if (imp) {
            _objc_inform("RESOLVE: method %c[%s %s] "
                         "dynamically resolved to %p",
                         cls->isMetaClass() ? '+' : '-',
                         cls->nameForLogging(), sel_getName(sel), imp);
        }
        else {
            // Method resolver didn't add anything?
            _objc_inform("RESOLVE: +[%s resolveClassMethod:%s] returned YES"
                         ", but no new implementation of %c[%s %s] was found",
                         cls->nameForLogging(), sel_getName(sel),
                         cls->isMetaClass() ? '+' : '-',
                         cls->nameForLogging(), sel_getName(sel));
        }
    }
}

/***********************************************************************
* lookUpImpOrNil.
* Like lookUpImpOrForward, but returns nil instead of _objc_msgForward_impcache
* 类似 lookUpImpOrForward，但返回 nil 而非 _objc_msgForward_impcache
**********************************************************************/
IMP lookUpImpOrNil(Class cls, SEL sel, id inst,
                   bool initialize, bool cache, bool resolver)
{
    IMP imp = lookUpImpOrForward(cls, sel, inst, initialize, cache, resolver);
    // 若找不到该方法（返回了消息转发），则返回 nil
    if (imp == _objc_msgForward_impcache) return nil;
    else return imp;
}
```

### 消息转发

#### What

当动态方法解析也无能为力时，将最终尝试消息转发。即 `- (id)forwardingTargetForSelector:(SEL)aSelector` 实例方法或 `+ (id)forwardingTargetForSelector:(SEL)aSelector` 类方法，如果我们将需要转发到的目标返回，那么目标就可以执行到转发的相同方法：

```objectivec
@interface FooBackup : NSObject
@end

@implementation FooBackup
- (void)foo {
    NSLog(@"%s", __func__);
}

+ (void)foo {
    NSLog(@"%s", __func__);
}

+ (void)classFoo {
    NSLog(@"%s", __func__);
}

- (void)classFoo {
    NSLog(@"%s", __func__);
}
@end

@interface Foo : NSObject
- (void)foo;
+ (void)classFoo;
@end

@implementation Foo
- (id)forwardingTargetForSelector:(SEL)aSelector {
    if (aSelector == @selector(foo)) {
        // 实例方法也可以转发给类对象
        // return [FooBackup class];
        return [[FooBackup alloc] init];
    }

    return [super forwardingTargetForSelector:aSelector];
}

+ (id)forwardingTargetForSelector:(SEL)aSelector {
    if (aSelector == @selector(classFoo)) {
        // return [[FooBackup alloc] init];
        return [FooBackup class];
    }

    return [super forwardingTargetForSelector:aSelector];
}
@end

Foo *foo = [[Foo alloc] init];
[foo foo];

[Foo classFoo];

// OUTPUT:
// -[FooBackup foo]
// +[FooBackup classFoo]
```

正如《Effective Objective-C 2.0》一书中所提到的，通过这种方式我们可以模拟出多重继承（Multiple Inheritance），即在一个对象内部使用一系列其它对象来处理相应的消息。另外需要注意的是，在这一步骤我们无法对消息本身进行更改，我们只能返回处理消息的对象。

如果 `forwardingTargetForSelector:` 也没有转发到目标，消息将尝试从 `- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector`/`+ (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector` 获取方法签名，方法签名可以根据方法的类型编码获得；接下来将可以通过 `- (void)forwardInvocation:(NSInvocation *)anInvocation`/`+ (void)forwardInvocation:(NSInvocation *)anInvocation` 执行，原来的消息将被封装在 `NSInvocation` 中：

```objectivec
@interface FooBackup : NSObject
@end

@implementation FooBackup
- (void)foo {
    NSLog(@"%s", __func__);
}

+ (void)classFoo {
    NSLog(@"%s", __func__);
}
@end

@interface Foo : NSObject
- (void)foo;
+ (void)classFoo;
@end

@implementation Foo
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector {
    if (aSelector == @selector(foo)) {
        // return [NSMethodSignature signatureWithObjCTypes:"v@:"];
        return [NSMethodSignature signatureWithObjCTypes:"v16@0:8"];
    }

    return [super methodSignatureForSelector:aSelector];
}

- (void)forwardInvocation:(NSInvocation *)anInvocation {
    if (anInvocation.selector == @selector(foo)) {
        [anInvocation invokeWithTarget:[[FooBackup alloc] init]];
    }
}

+ (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector {
    if (aSelector == @selector(classFoo)) {
        // return [NSMethodSignature signatureWithObjCTypes:"v@:"];
        return [NSMethodSignature signatureWithObjCTypes:"v16@0:8"];
    }

    return [super methodSignatureForSelector:aSelector];
}

+ (void)forwardInvocation:(NSInvocation *)anInvocation {
    if (anInvocation.selector == @selector(classFoo)) {
        [anInvocation invokeWithTarget:[FooBackup class]];
    }
}
@end
```

#### How

正如上所述，当动态方法解析也无法奏效或者我们在动态方法解析中并没有添加了正确的方法时，将进入 `lookUpImpOrForward` 中的 Method Forward 即「消息转发」：

```cpp
IMP lookUpImpOrForward(Class cls, SEL sel, id inst,
                       bool initialize, bool cache, bool resolver)
    // ...

    // No implementation found, and method resolver didn't help.
    // Use forwarding.
    // 实现无法找到，方法解析无效，尝试方法转发。

    imp = (IMP)_objc_msgForward_impcache;
    cache_fill(cls, sel, imp, inst);

    // ...
}
```

`_objc_msgForward_impcache` 则又是在汇编中：

```asm
// objc-msg-arm.s
/********************************************************************
*
* id _objc_msgForward(id self, SEL _cmd,...);
*
* _objc_msgForward is the externally-callable
*   function returned by things like method_getImplementation().
* _objc_msgForward_impcache is the function pointer actually stored in
*   method caches.
*
********************************************************************/

	STATIC_ENTRY __objc_msgForward_impcache

	// No stret specialization.
	b	__objc_msgForward

	END_ENTRY __objc_msgForward_impcache

	ENTRY __objc_msgForward

	adrp	x17, __objc_forward_handler@PAGE
	ldr	p17, [x17, __objc_forward_handler@PAGEOFF]
	TailCallFunctionPointer x17

	END_ENTRY __objc_msgForward
```

最终会发现 objc4 中并没有开源的 `objc_msgForward` 实现：

```cpp
// objc-runtime.mm

// Default forward handler halts the process.
__attribute__((noreturn)) void
objc_defaultForwardHandler(id self, SEL sel)
{
    _objc_fatal("%c[%s %s]: unrecognized selector sent to instance %p "
                "(no message forward handler is installed)",
                class_isMetaClass(object_getClass(self)) ? '+' : '-',
                object_getClassName(self), sel_getName(sel), self);
}
void *_objc_forward_handler = (void*)objc_defaultForwardHandler;
```

---

综上，一个 Obj-C 方法调用的过程可以描述为：

1. `objc_msgSend` 判断消息接收者是否为 `nil`
2. 当非 `nil` 时，将根据 `isa` 指针找到缓存所在的类或元类对象的缓存中寻找；
3. 当无法在缓存中找到时，将从本类开始到父类（到父类的父）在其方法列表中查找，如果找到会同时缓存到原有类中一份；
4. 如果方法列表也无法找到将尝试动态方法解析，即进入 `resolveInstanceMethod`/`resolveClassMethod`，如果其中将方法正确地动态添加了，则从方法列表中调用并缓存；
5. 如果仍无，将尝试 `forwardingTargetForSelector`，其返回将作为被转发到的目标尝试执行相应方法；
6. 如果转发目标为 `nil`，将最终尝试 `methodSignatureForSelector:` 返回方法签名并在 `forwardInvocation:` 决定根据消息的信息选择如何执行；
7. 如果在 `methodSignatureForSelector:` 返回了空方法签名，将最终导致「unrecognized selector sent to instance」。

正如《Effective Objective-C 2.0》一书中提到的 `CALayer` 使用了消息转发来实现兼容 KVC 的容器类：

```objectivec
@interface MyLayer : CALayer
@property (nonatomic, copy) NSString *foo;
@end

@implementation MyLayer
@dynamic foo; // 不自动生成 getter & setter
@end

MyLayer *layer = [[MyLayer alloc] init];
[layer setFoo:@"kingcos.me"];
NSLog(@"%@", [layer foo]);
NSLog(@"%@", [layer valueForKey:@"foo"]);

// OUTPUT:
// kingcos.me
// kingcos.me
```

## Reference

- [Dissecting objc_msgSend on ARM64 - Mike Ash](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)
- [ARM Software development tools - arm.com](http://infocenter.arm.com/help/index.jsp)
- [1b and 1f in GNU assembly - StackOverflow](https://stackoverflow.com/questions/27353096/1b-and-1f-in-gnu-assembly)
- [ARM.cpp - clang](https://clang.llvm.org/doxygen/Basic_2Targets_2ARM_8cpp_source.html)
- [预定义宏 - IBM](https://www.ibm.com/support/knowledgecenter/zh/SSXVZZ_13.1.0/com.ibm.xlcpp131.linux.doc/getstart/predef_macro_v10v12.html)
- [Obj-C 中的对象 - kingcos](https://kingcos.me/posts/2019/objects_in_obj-c/)
- [iOS 中的 Category - kingcos](https://kingcos.me/posts/2019/category_in_ios/)
- [Objective-C 消息发送与转发机制原理 - 杨萧玉](http://yulingtianxia.com/blog/2016/06/15/Objective-C-Message-Sending-and-Forwarding/)

## TODO

- 尾递归调用
- 尝试逆向得到消息转发部分的步骤
- 消息发送流程图
- 尝试使用 Swift 实现整个过程
