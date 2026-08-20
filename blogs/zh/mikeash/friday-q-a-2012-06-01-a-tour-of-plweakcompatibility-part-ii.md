---
title: 'Friday Q&A 2012-06-01：PLWeakCompatibility 导览：第二部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5fb859d5d42fccc0'
translated: true
---

> 原文：[Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)　·　mikeash.com Friday Q&A

发表于 2012-06-01 13:38 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2012-06-22: Objective-C Literals](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)
上一篇文章：[Friday Q&A 2012-05-18: A Tour of PLWeakCompatibility: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)
标签：[arc](https://www.mikeash.com/pyblog/?tag=arc) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-06-01：PLWeakCompatibility 导览：第二部分

作者：[Mike Ash](https://www.mikeash.com/)

**回顾**
PLWeakCompatibility 实现了以下函数，它们会被编译器生成的代码直接调用：

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location);
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val);
    void objc_destroyWeak(PLObjectPtr *addr);
    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from);
    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from);
    PLObjectPtr objc_loadWeak(PLObjectPtr *location);
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj);
```

这里的 `PLObjectPtr` 只是 `void *` 的 typedef，用来阻止 ARC 在这些明确不应插入内存管理代码的函数中插入相关代码。所有这些函数开头的代码，都会在 Objective-C 运行时提供相应实现时转调运行时实现。当官方运行时函数不可用时，这七个函数会拆解为以下三个基本函数来实现：

```
    PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location);
    void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj);
    void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj);
```

`PLLoadWeakRetained` 从给定位置加载弱引用：如果其中有对象，就返回该对象的保留引用，否则返回 `nil`。`PLRegisterWeak` 将某个内存位置注册为给定对象的弱引用，`PLUnregisterWeak` 则移除这一注册。接下来要做的，就是实现这三个函数。

**MAZeroingWeakRef**
我们的目标是让 PLWeakCompatibility 完全自包含，拥有自己的置零弱引用实现；这必然会是一个相对简单的实现。不过，只要应用中存在 MAZeroingWeakRef，我们也希望使用它，因为这通常意味着开发者喜欢那套实现，既然已经存在，就不妨利用起来。因此，第一步是检测 MAZeroingWeakRef 是否存在；如果存在，就用它来实现三个基本函数。

首先，需要一种检测 MAZeroingWeakRef 是否存在、并在存在时取得其类引用的方法。我们把这件事封装在一个简单函数中：它在 `dispatch_once` 调用内使用 `NSClassFromString` 尝试获取 `MAZeroingWeakRef` 类，以尽量降低开销。函数还带有一个额外标志，可以在测试时禁用 MAZeroingWeakRef 功能：

```
    static Class MAZWR = Nil;
    static bool mazwrEnabled = true;
    static inline bool has_mazwr () {
        if (!mazwrEnabled)
            return false;

        static dispatch_once_t lookup_once = 0;
        dispatch_once(&lookup_once, ^{
            MAZWR = NSClassFromString(@"MAZeroingWeakRef");
        });

        if (MAZWR != nil)
            return true;
        return false;
    }
```

现在，代码只需调用 `has_mazwr`；如果它返回 true，就可以使用 `MAZWR` 获取该类的引用。

用 MAZeroingWeakRef 实现三个基本函数的策略相当直接。每个基本函数都会得到一个用于存放弱引用的位置，但并没有规定这个位置必须直接存储弱引用对象的指针。因此，我们利用传入的位置存储一个 `MAZeroingWeakRef` 实例的指针，而该实例再引用原始对象。`PLRegisterWeak` 只需创建一个新的 `MAZeroingWeakRef` 实例并放入给定位置；`PLUnregisterWeak` 只需释放该实例；`PLLoadWeakRetained` 则直接调用对象的 `-target` 方法即可。

每个基本函数开头都会检查 `has_mazwr`，据此决定后续操作。各基本函数开头与 `MAZeroingWeakRef` 相关的代码如下：

```
    static PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location) {
        if (has_mazwr()) {
            MAZeroingWeakRef *mazrw = (__bridge MAZeroingWeakRef *) *location;
            return objc_retain([mazrw target]);
        }
        ...

    static void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        if (has_mazwr()) {
            MAZeroingWeakRef *ref = [[MAZWR alloc] initWithTarget: obj];
            *location = (__bridge_retained PLObjectPtr) ref;
            return;
        }
        ...

    static void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        if (has_mazwr()) {
            if (*location != nil)
                objc_release(*location);
            return;
        }
        ...
```

**内置实现**
现在进入真正的核心：内置置零弱引用实现。我们的策略是对目标对象的 `release` 和 `dealloc` 做方法调配（swizzling）。调配后的 `release` 会把对象加入“正在释放”列表；在释放进行期间，任何试图解析弱引用的线程都会被阻塞，从而确保对象最后一次 `release` 触发 `dealloc` 时，不会再解析出弱引用。调配后的 `dealloc` 随后会清除指向该对象的所有弱引用。

首先需要一个互斥锁来保护所有共享数据结构：

```
    static pthread_mutex_t gWeakMutex;
```

还需要跟踪当前为每个对象注册的所有弱引用。这里使用一个 `CFMutableDictionary`，将对象映射到包含已注册弱地址的 `CFMutableSet`：

```
    static CFMutableDictionaryRef gObjectToAddressesMap;
```

同一个类很可能会出现多个实例的弱引用，因此需要跟踪哪些类已经完成调配，避免重复调配。我们通过一个集合记录已调配的类：

```
    static CFMutableSetRef gSwizzledClasses;
```

当前正处于 `release` 调用中的对象存放在一个 bag 中：

```
    static CFMutableBagRef gReleasingObjects;
```

有些代码需要等待 `gReleasingObjects` 发生变化，因此还需要一个条件变量供它们等待。（如果你不熟悉条件变量，稍后会再详细讨论。）

```
    static pthread_cond_t gReleasingObjectsCond;
```

还有一些数据需要存储在线程本地存储中。两个用于辅助调配过程的表就放在那里，它们存储在结构体中，并通过 `pthread` 线程本地存储键访问：

```
    static pthread_key_t gTLSKey;
```

为方便起见，我们还把调配所需的全部 selector 放进全局变量：

```
    static SEL releaseSEL;
    static SEL releaseSELSwizzled;
    static SEL deallocSEL;
    static SEL deallocSELSwizzled;
```

每个基本函数都需要访问这些变量，而它们必须在使用前完成初始化。所有初始化都封装在 `dispatch_once` 中：

```
    static void WeakInit(void) {
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
```

首先初始化互斥锁，并将其设置为递归属性：

```
            pthread_mutexattr_t attr;
            pthread_mutexattr_init(&attr);
            pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);

            pthread_mutex_init(&gWeakMutex, &attr);

            pthread_mutexattr_destroy(&attr);
```

然后创建对象到地址的映射表，以及已调配类的集合：

```
            gObjectToAddressesMap = CFDictionaryCreateMutable(NULL, 0, NULL, &kCFTypeDictionaryValueCallBacks);

            gSwizzledClasses = CFSetCreateMutable(NULL, 0, NULL);
```

给字典键回调和集合回调传入 `NULL`，可以确保 CoreFoundation 不会尝试对这些对象做任何内存管理。

接着初始化正在释放的对象集合，以及用于等待它的条件变量：

```
            gReleasingObjects = CFBagCreateMutable(NULL, 0, NULL);
            pthread_cond_init(&gReleasingObjectsCond, NULL);
```

下一步创建 `pthread` 线程本地存储键。这里的错误检查有些谨慎，因为这个函数确实可能失败。目前 Mac OS X 能创建的线程本地存储键数量有限且不多：512 个。这应该绰绰有余，但既然它确实可能失败，我希望它尽早、明确地失败：

```
            int err = pthread_key_create(&gTLSKey, DestroyTLS);
            if (err != 0) {
                NSLog(@"Error calling pthread_key_create, we really can't recover from that: %s (%d)", strerror(err), err);
                abort();
            }
```

`DestroyTLS` 函数会释放为线程本地存储分配的内存，稍后会展示它的实现。

最后初始化 selector。不能对 `release` 和 `dealloc` 使用标准的 `@selector` 构造，因为 ARC 不允许这样做。我们改用 `sel_getUid`（Objective-C 运行时中相当于 `NSSelectorFromString` 的函数），在 ARC 察觉不到的情况下取得 selector：

```
            releaseSEL = sel_getUid("release");
            releaseSELSwizzled = sel_getUid("release_PLWeakCompatibility_swizzled");
            deallocSEL = sel_getUid("dealloc");
            deallocSELSwizzled = sel_getUid("dealloc_PLWeakCompatibility_swizzled");
        });
    }
```

每个基本函数都会先调用 `WeakInit`，确保所有这些变量已经设置好。为使讨论更简单，下面讲解这些函数的实现时，会省略这个调用以及 `MAZeroingWeakRef` 代码。

**线程本地存储**
`pthread` 线程本地存储键可以在线程级别设置和获取一个指针。为了存储多个值，我们分配一个包含所有所需内容的结构体。我们需要两个字典，帮助调配后的方法调用回原始实现。结构体如下：

```
    struct TLS {
        // Tables tracking the last class a swizzled method was sent to on an object
        CFMutableDictionaryRef lastReleaseClassTable;
        CFMutableDictionaryRef lastDeallocClassTable;
    };
```

由于这个结构体会在多个地方使用，我们需要一个包装函数来获取它；如果该线程此前还没有使用过 `TLS` 结构体，就按需创建。`pthread_getspecific` 会取出当前值；如果当前值为 `NULL`，函数就使用 `pthread_setspecific` 设置一个新键：

```
    static struct TLS *GetTLS(void) {
        struct TLS *tls = pthread_getspecific(gTLSKey);
        if (tls == NULL) {
            tls = calloc(1, sizeof(*tls));
            tls->lastReleaseClassTable = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            tls->lastDeallocClassTable = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            pthread_setspecific(gTLSKey, tls);
        }
        return tls;
    }
```

还需要一个销毁 `TLS` 结构体的函数。这个函数会传给 `pthread_key_create`，在线程销毁时由 `pthread` 自动调用：

```
    static void DestroyTLS(void *ptr) {
        struct TLS *tls = ptr;
        if (tls != NULL && tls->lastReleaseClassTable) {
            CFRelease(tls->lastReleaseClassTable);
            CFRelease(tls->lastDeallocClassTable);
        }
        free(tls);
    }
```

有了这些代码，任何线程只要调用 `GetTLS()`，就可以操作结构体中的数据；这些数据保证只对调用它的线程可见。

**基本函数**
`PLLoadWeakRetained` 的实现相对直接。它需要获取全局互斥锁，然后取出对象指针。如果对象当前正在释放，就必须等待它完成释放。

它首先获取全局互斥锁，然后尝试读取给定位置存储的值：

```
    static PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location) {
        PLObjectPtr obj;
        pthread_mutex_lock(&gWeakMutex); {
            obj = *location;
```

接下来检查给定对象是否位于正在释放列表中。如果在列表中，就用 `pthread_cond_wait` 阻塞在条件变量上，随后重新读取位置以取得最新值：

```
        while (CFBagContainsValue(gReleasingObjects, obj)) {
            pthread_cond_wait(&gReleasingObjectsCond, &gWeakMutex);
            obj = *location;
        }
```

`pthread_cond_wait` 会释放给定的互斥锁，然后等待某处发出条件变量信号。收到信号后，它会重新获取互斥锁并继续执行。这样，线程可以一直阻塞，直到另一个线程发出“正在释放对象表已改变”的信号，然后重新检查表。

这里使用 `while` 循环而不是简单的 `if`，有两个原因。首先，被发信号的变化可能与当前对象无关：整个表共用一个条件变量，被移除的可能是另一个对象。

另一个原因更有意思，称为[虚假唤醒（spurious wakeup）](http://en.wikipedia.org/wiki/Spurious_wakeup)。简而言之，由于各种实现细节，即使没有任何信号发到条件变量，`pthread_cond_wait` 也可能偶尔返回。因此，对 `pthread_cond_wait` 的任何调用都应该放在循环中，而不是简单的 `if` 语句里。

得到对象（或 `nil`）后，我们只需保留它、释放互斥锁，然后返回这个保留的对象。

```
            objc_retain(obj);
        }
        pthread_mutex_unlock(&gWeakMutex);

        return obj;
    }
```

`PLRegisterWeak` 稍微复杂一些。它首先取出给定对象对应的已注册地址集合，以便加入新条目：

```
    static void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        pthread_mutex_lock(&gWeakMutex); {
            CFMutableSetRef addresses = (CFMutableSetRef)CFDictionaryGetValue(gObjectToAddressesMap, obj);
```

如果这是给定对象的第一个弱引用，这个集合还不存在。此时函数必须创建它：

```
            if (addresses == NULL) {
                addresses = CFSetCreateMutable(NULL, 0, NULL);
                CFDictionarySetValue(gObjectToAddressesMap, obj, addresses);
                CFRelease(addresses);
            }
```

有了集合之后，就把传入的位置加入其中：

```
            CFSetAddValue(addresses, location);
```

最后调用辅助函数，确保所有适当的方法调配都已完成：

```
            EnsureDeallocationTrigger(obj);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

稍后会详细介绍这个辅助函数的实现。

`PLUnregisterWeak` 的实现基本上是 `PLRegisterWeak` 的逆操作，只是不需要操心调配（调配会一直保留），也不会在地址集合变空时删除它：

```
    static void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        pthread_mutex_lock(&gWeakMutex); {
            // Remove the location from the set of weakly referenced addresses.
            CFMutableSetRef addresses = (CFMutableSetRef)CFDictionaryGetValue(gObjectToAddressesMap, *location);
            if (addresses != NULL)
                CFSetRemoveValue(addresses, location);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

现在来看看 `EnsureDeallocationTrigger` 的实现。它首先取得给定对象的类；如果这个类已经完成调配，就直接返回：

```
    static void EnsureDeallocationTrigger(PLObjectPtr obj) {
        Class c = object_getClass(obj);
        if (CFSetContainsValue(gSwizzledClasses, (__bridge const void *)c))
            return;
```

如果尚未调配，它就使用一个小辅助函数调配 `release` 和 `dealloc`，最后把该类加入已调配类集合：

```
        Swizzle(c, releaseSEL, releaseSELSwizzled, (IMP)SwizzledReleaseIMP);
        Swizzle(c, deallocSEL, deallocSELSwizzled, (IMP)SwizzledDeallocIMP);

        CFSetAddValue(gSwizzledClasses, (__bridge const void *)c);
    }
```

`Swizzle` 的实现很简单：使用 `class_addMethod` 在新 selector 下注册此前的 `IMP`，再用 `class_replaceMethod` 把新的 `IMP` 放进原 selector：

```
    static void Swizzle(Class c, SEL orig, SEL new, IMP newIMP) {
        Method m = class_getInstanceMethod(c, orig);
        IMP origIMP = method_getImplementation(m);
        class_addMethod(c, new, origIMP, method_getTypeEncoding(m));
        class_replaceMethod(c, orig, newIMP, method_getTypeEncoding(m));
    }
```

基本上就这些了。剩下的只是 `SwizzledReleaseIMP` 和 `SwizzledDeallocIMP` 的实现，而事实证明，这两个实现相当困难和复杂。

**子类问题**
在可能的情况下，实现方法调配的最佳方式是将原始 `IMP` 保存到全局变量中，然后将其作为函数指针调用：

```
    // original implementation
    void (*origIMP)(id, SEL);

    // swizzle code
    origIMP = (void *)method_getImplementation(origMethod);
    class_replaceMethod(class, selector, newIMP, method_getTypeEncoding(origMethod));

    // swizzled IMP
    void newIMP(id self, SEL _cmd)
    {
        // do stuff here
        ...

        // call the original
        origIMP(self, _cmd);
    }
```

然而，这只在调配单个类时有效。调配多个类时，需要跟踪多个原始实现。此时更好的做法是：在同一个类上用一个新 selector 注册原始实现，然后通过这个 selector 查找：

```
    // swizzle code
    IMP origIMP = method_getImplementation(origMethod);
    class_addMethod(class, @selector(swizzled_method), origIMP, method_getTypeEncoding(origMethod));
    class_replaceMethod(class, selector, newIMP, method_getTypeEncoding(origMethod));

    // swizzled IMP
    void newIMP(id self, SEL _cmd)
    {
        // do stuff here
        ...

        // look up the original
        Class class = object_getClass(self);
        void (*origIMP)(id, SEL) = (void *)(class_getMethodImplementation(class, @selector(swizzled_method));

        // call the original
        origIMP(self, _cmd);
    }
```

但这只有在只调配叶子类时才有效。如果调配的两个类存在一个是另一个超类的情况，就会导致无限递归并崩溃。

为了理解原因，考虑两个都重写了 `dealloc` 的类 `A` 和 `B`：

```
    @interface A : NSObject
    - (void)dealloc; // clean up stuff
    @end

    @interface B : A
    - (void)dealloc; // clean up in aisle three
    @end
```

假设我们已经对 `A` 和 `B` 的 `dealloc` 都做了调配（大概是因为某处分别对 `A` 和 `B` 的实例创建了 `__weak` 引用）。现在某段代码释放一个 `B` 实例。

由于调配，对 `dealloc` 的调用最终会执行调配后的实现。目前一切正常。

调配后的实现查找并调用 `-[B swizzled_dealloc]`，后者调用 `-[B dealloc]` 的原始实现。到这里仍然没有问题。在这个原始实现的末尾，方法会调用 `[super dealloc]`，最终得到 `-[A dealloc]`。目前为止都很好。

`-[A dealloc]` 同样是调配后的实现，但这没有关系。如果希望拦截对 `A` 和 `B` 实例的调用，这个实现就必须支持重入。调配后的实现再次执行自己的逻辑，并且代码已经考虑了这种情况。然后它继续调用原始实现，问题就出在这里。

看看查找原始实现的代码：

```
    Class class = object_getClass(self);
    void (*origIMP)(id, SEL) = (void *)(class_getMethodImplementation(class, @selector(swizzled_method));
```

虽然这次调用来自 `A`，但 `object_getClass` 返回的仍然是 `B`。运行时不存在“从 `A` 调用”这样的概念；对象的类是 `B`，它取得的就是 `B`。因此在 `-[A dealloc]` 的末尾，调配后的实现查找并调用原始实现时，实际上又调用了 `-[B swizzled_dealloc]`！如果这个方法侥幸第二次运行而没有立即崩溃，它会再次调用 `-[A dealloc]`，后者又调用 `-[B swizzled_dealloc]`，如此反复，直到某段代码无法继续承受这种滥用，或者无限递归耗尽栈空间并崩溃。

要解决这个问题，调配后的实现需要知道自己附着在哪个类上。使用 `imp_implementationWithBlock` 为每个类创建略有不同的调配实现很容易做到。遗憾的是，`imp_implementationWithBlock` 仅在 iOS 4.3 及更高版本提供。如果 `PLWeakCompatibility` 依赖它，就必须放弃对 iOS 4.0-4.2 的支持，这会大大降低它的实用性。因此需要另想办法。

**模拟 `super`**
假设存在一次对 `super` 的调用，它会沿着类层次结构向上遍历，每次从更高一级的类取出原始 `IMP` 并调用。跟踪上一次取到的类，就可以模拟这种行为。对于每个方法，我们建立一张表，将对象映射到上次调用原始 `IMP` 时使用的类。每次调用时从那个类继续向上遍历，就能得到所需行为。

在上面的例子中，第一次调用 `dealloc` 时表中没有条目，因此调用 `B` 的 `dealloc` 并把 `B` 放入表中。下一次调用看到 `B`，于是调用 `A` 的 `dealloc`，并把 `A` 放入表中。再下一次看到 `A`，于是调用 `NSObject` 的 `dealloc`。这正是我们想要的结果。

这里还需要一个额外技巧。想象层次结构中还有一个类 `C`：

```
    @interface C : B
    // does not override dealloc
    @end
```

这会带来问题。第一次调用没有表条目，于是调用 `C` 的 `dealloc`，并把 `C` 放入表中。但由于 `C` 没有重写 `dealloc`，这个实现其实就是 `B` 的 `dealloc`。下一次调用看到表中的 `C`，又会调用……`B` 的 `dealloc`。这显然不对。

解决办法是沿类层次结构搜索拥有给定方法实现的最顶层类。`TopClassImplementingMethod` 函数从给定类开始向上搜索，找出给定 selector 对应的 `IMP` 发生变化的位置，并返回变化之前的最后一个类：

```
    static Class TopClassImplementingMethod(Class start, SEL sel) {
        IMP imp = class_getMethodImplementation(start, sel);

        Class previous = start;
        Class cursor = class_getSuperclass(previous);
        while (cursor != Nil) {
            if (imp != class_getMethodImplementation(cursor, sel))
                break;
            previous = cursor;
            cursor = class_getSuperclass(cursor);
        }

        return previous;
    }
```

在将条目写入表之前调用这个函数，就能解决问题。第一次调用没有表条目，调用 `C` 的 `dealloc`（实际上是 `B` 的 `dealloc`），但随后把 `B` 而不是 `C` 放入表中。下一次调用会到达 `A`，再下一次到达 `NSObject`，正如我们所需。

如果同一个方法在不同线程上多次调用，这些表会发生冲突。不过，把表放在线程本地存储中，就消除了这个问题。

**Release**
`release` 的调配实现首先获取线程本地结构体，因为整个方法都会使用其中的内容：

```
    static void SwizzledReleaseIMP(PLObjectPtr self, SEL _cmd) {
        struct TLS *tls = GetTLS();
```

接着将 `self` 加入正在释放的对象列表：

```
        pthread_mutex_lock(&gWeakMutex); {
            // Add this object to the list of releasing objects.
            CFBagAddValue(gReleasingObjects, self);
        } pthread_mutex_unlock(&gWeakMutex);
```

随后开始执行虚拟的 `super` 策略。第一步是查看当前表条目：

```
        Class lastSent = (__bridge Class)CFDictionaryGetValue(tls->lastReleaseClassTable, self);
```

然后选择目标类。如果表为空，目标就是 `self` 的类；如果表中已有类，就从该类的超类开始：

```
        Class targetClass = lastSent == Nil ? object_getClass(self) : class_getSuperclass(lastSent);
```

接着用 `TopClassImplementingMethod` 跳过没有重写 `release` 的类，并把结果写回表：

```
        targetClass = TopClassImplementingMethod(targetClass, releaseSELSwizzled);
        CFDictionarySetValue(tls->lastReleaseClassTable, self, (__bridge void *)targetClass);
```

有了目标类，代码就可以取得该类上 `release` 的 `IMP` 并调用它：

```
        void (*origIMP)(PLObjectPtr, SEL) = (__typeof__(origIMP))class_getMethodImplementation(targetClass, releaseSELSwizzled);
        origIMP(self, _cmd);
```

到这里，超类的代码已经执行完毕。如果这次调用释放了 `self` 的最后一个引用，对象现在已经销毁。首先要清理类表，这样下次在这个地址调用 `release` 时（可能是同一个尚未被这次 `release` 销毁的对象，也可能是分配在同一地址的新对象），表都是干净的：

```
        CFDictionaryRemoveValue(tls->lastReleaseClassTable, self);
```

最后重新获取互斥锁，把 `self` 从正在释放列表中移除，并调用 `pthread_cond_broadcast` 唤醒可能正在等待该对象的线程：

```
        pthread_mutex_lock(&gWeakMutex); {
            // We're no longer releasing.
            CFBagRemoveValue(gReleasingObjects, self);
            pthread_cond_broadcast(&gReleasingObjectsCond);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

**Dealloc**
调配后的 `dealloc` 实现大体相似。和调配后的 `release` 一样，它先获取线程本地存储结构体：

```
    static void SwizzledDeallocIMP(PLObjectPtr self, SEL _cmd) {
        struct TLS *tls = GetTLS();
```

接着获取全局锁，从全局映射取出地址并遍历它们，清除所有指向 `self` 的弱引用：

```
        pthread_mutex_lock(&gWeakMutex); {
            // Clear all weak references and delete the addresses set.
            CFSetRef addresses = CFDictionaryGetValue(gObjectToAddressesMap, self);
            if (addresses != NULL)
                CFSetApplyFunction(addresses, ClearAddress, NULL);
```

注意，`ClearAddress` 只是一个简单函数，本质上会对每个集合条目执行 `*(void **)value = NULL`，将它置零。集合清空后就不再需要了，因此将它从全局映射中移除：

```
            CFDictionaryRemoveValue(gObjectToAddressesMap, self);
```

最后通知所有正在等待“正在释放对象列表发生变化”的线程。严格来说，列表本身并没有变化；但等待 `self` 的线程现在会发现自己的弱引用包含 `nil`，而 `nil` 不在集合中，因此仍然需要通知它们重新检查：

```
            pthread_cond_broadcast(&gReleasingObjectsCond);
        } pthread_mutex_unlock(&gWeakMutex);
```

完成这些工作后，`dealloc` 使用与 `release` 相同的过程调用原始实现：

```
        Class lastSent = (__bridge Class)CFDictionaryGetValue(tls->lastDeallocClassTable, self);
        Class targetClass = lastSent == Nil ? object_getClass(self) : class_getSuperclass(lastSent);
        targetClass = TopClassImplementingMethod(targetClass, deallocSELSwizzled);
        CFDictionarySetValue(tls->lastDeallocClassTable, self, (__bridge void *)targetClass);

        // Call through to the original implementation.
        void (*origIMP)(PLObjectPtr, SEL) = (__typeof__(origIMP))class_getMethodImplementation(targetClass, deallocSELSwizzled);
        origIMP(self, _cmd);
```

此时 `self` 已被销毁。剩下的只是清理类表中的对应条目，让下一个占用这个地址的对象拥有干净的状态：

```
        CFDictionaryRemoveValue(tls->lastDeallocClassTable, self);
    }
```

**结语**
这是一个很难解决的问题，但通过谨慎的思考和编程，我们最终让它正常工作了。调配 `release` 和 `dealloc` 可以安全地将指向目标对象的弱引用置零。跟踪当前正在执行 `release` 的所有对象，可以确保没人取得即将销毁对象的引用。通过在外部表中跟踪调配方法被发送到的类，即使调配方法被递归调用，也能安全地完成方法调配。

今天就到这里。下次再来继续 Cocoa 编程世界的奇趣探索。Friday Q&A 的主题来自读者建议；如果你有希望在这里看到的主题，请[发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
