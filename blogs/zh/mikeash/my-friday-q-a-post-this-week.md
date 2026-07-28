---
title: 'Friday Q&A 2010-07-16：Objective-C 中的归零弱引用'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b29d67a58328e208'
translated: true
---

> 原文：[Friday Q&A 2010-07-16: Zeroing Weak References in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)　·　mikeash.com Friday Q&A

发布于 2010-07-16 20:18 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Introducing MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)  
上一篇文章：[Friday Q&A 2010-07-02: Background Timers](https://www.mikeash.com/pyblog/friday-qa-2010-07-02-background-timers.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [garbagecollection](https://www.mikeash.com/pyblog/?tag=garbagecollection) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-07-16：Objective-C 中的归零弱引用

作者：[Mike Ash](https://www.mikeash.com/)

**弱引用**  
首先，什么是弱引用？简单来说，弱引用是一个指向对象的引用（在 Objective-C 中是指针），它不参与保持该对象存活。例如，在使用内存管理时，这个 setter 会创建一个指向新对象的弱引用：

```
    - (void)setFoo: (id)newFoo
    {
        _foo = newFoo;
    }
```

因为 setter 没有使用 `retain`，所以这个引用不会让新对象保持存活。当然，只要它被其他引用 retain 住，它就会保持存活。但一旦那些引用消失，即使 `_foo` 仍然指向它，该对象也会被释放。

弱引用在 Cocoa 中很常见，用于处理[保留循环](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)。Cocoa 中的委托（delegate）几乎总是弱引用，正是因为这个原因。

**归零弱引用**  
弱引用对于避免保留循环之类的事情很有用，但其效用受到固有危险的限制。在 Objective-C 中使用普通的弱引用，当目标对象被销毁时，你会留下一个悬空指针（dangling pointer）。如果你的代码尝试使用那个指针，它会崩溃或更糟。

归零弱引用消除了这种危险。它们的工作方式与常规弱引用类似，只是当目标对象被销毁时，它们会自动变成 `nil`。每当你通过归零弱引用访问对象时，都保证你要么访问到一个有效的、存活的对象，要么得到 `nil`。只要你的代码能处理 `nil`，就完全安全。

由于这种安全性，归零弱引用可以比不安全的那种用于更多场合。一个例子是对象缓存。使用弱引用的对象缓存可以在对象存活时引用它们，然后在不再需要时让它们释放。如果客户端请求一个仍然存活的对象，它可以不用创建新对象就能获得它。如果对象已经被销毁，缓存可以安全地创建一个新对象。

它们也可以用于更平淡的目的，适用于任何你想保留对对象的引用但不想让该对象超出其正常生命周期而留在内存中的情况。例如，你可能会追踪一个窗口（window），但不想在它关闭后将其保留在内存中。你可以通过设置一个通知观察者并观察窗口何时消失来处理这个问题，但归零弱引用是一种更简单的方法。另一个例子，在 `block` 中对 `self` 的归零弱引用可以防止保留循环，同时确保如果在 `self` 被释放后调用了该 `block`，程序不会崩溃。即使是标准的委托指针，使用归零弱引用也会变得更好，因为它消除了如果委托在指向它的对象之前被释放可能出现的罕见但恼人的 bug。

如果你在 Objective-C 中使用垃圾回收（garbage collection），那么好消息来了！Objective-C 垃圾回收器已经使用类型修饰符 `__weak` 支持归零弱引用。你可以像这样声明任何实例变量：

```
    __weak id _foo;
```

它会自动成为一个归零弱引用。编译器负责发出适当的读写屏障，以便访问始终安全。

但是，如果你没有使用垃圾回收呢？虽然我们都能使用垃圾回收会很棒，但许多人出于各种原因无法使用，最常见的原因之一是 iOS 根本不支持垃圾回收。好吧，到目前为止，在 Objective-C 中使用手动内存管理时，你在归零弱引用方面一直不走运。

**Introducing `MAZeroingWeakRef`**  
我们这些使用手动内存管理的人现在可以受益于归零弱引用了！`MAZeroingWeakRef` 实现了以下接口：

```
    @interface MAZeroingWeakRef : NSObject
    {
        id _target;
    }
    
    + (id)refWithTarget: (id)target;
    
    - (id)initWithTarget: (id)target;
    
    - (void)setCleanupBlock: (void (^)(id target))block;
    
    - (id)target;
    
    @end
```

用法非常简单。用一个目标对象初始化它。在需要使用库时检索目标对象。`-target` 方法要么返回目标对象（已 retain/autorelease 以保证在你使用完之前它会保持存活），要么如果目标已经被销毁，它会返回 `nil`。

`-setCleanupBlock:` 方法用于更高级的使用。通常，归零弱引用是一个被动对象。你可以随时查询它的目标，它要么给你一个对象，要么给你 `nil`。但有时候，当引用被归零时，你想采取一些额外的操作，例如取消注册一个通知观察者。传递给 `-setCleanupBlock:` 的 `block` 在引用被归零时执行，允许你设定这样的额外操作。

作为一个例子，以下是使用 `MAZeroingWeakRef` 编写标准委托模式的方法：

```
    // 实例变量
    MAZeroingWeakRef *_delegateRef;
    
    // setter
    - (void)setDelegate: (id)newDelegate
    {
        [_delegateRef release];
        _delegateRef = [[MAZeroingWeakRef alloc] initWithTarget: newDelegate];
    }
    
    - (void)doSomethingAndCallDelegate
    {
        [self _doSomething];
        
        id delegate = [_delegateRef target];
        if([delegate respondsToSelector: @selector(someDelegateMethod)])
            [delegate someDelegateMethod];
    }
```

这只比使用普通的、危险的弱引用稍微难一点，并提供了完全的安全性。（如果你使用这种模式，请记住你现在必须在 `-dealloc` 中释放 `_delegateRef`！）

`MAZeroingWeakRef` 是完全线程安全的（thread safe），无论是从多个线程访问它，还是在一个线程中目标对象被销毁而同时从另一个线程访问弱引用。

**它是如何工作的？**  
归零弱引用如何工作的概念相当直接。追踪所有对某个目标的此类引用。当一个对象被销毁时，在调用 `dealloc` 之前将所有这些引用归零。将所有内容包裹在一个锁中，以使其是线程安全的。

然而，完成每个步骤的细节可能会变得棘手。

追踪所有对某个目标的归零弱引用并不难。一个全局 `CFMutableDictionary` 将目标映射到 `CFMutableSet` 对象，这些对象保存指向每个目标的归零弱引用。我使用 CF 类以便可以自定义内存管理；我不希望目标或弱引用被 retain。

在调用 `dealloc` 之前归零所有弱引用变得稍微棘手一些……

答案是利用动态子类化（dynamic subclassing），就像在[键值观察](http://www.mikeash.com/pyblog/friday-qa-2009-01-23.html)的实现中所做的那样。当一个对象成为归零弱引用的目标时，会创建该对象类的一个新子类。新子类的 `-dealloc` 方法负责归零所有弱引用，然后通过 `super` 调用，以便可以发生正常的释放链。新的子类还会覆写 `-release` 以获取锁，从而使所有内容都是线程安全的。（没有那个覆写，可能一个线程在 `release` 一个 retain 计数为 1 的对象，而同时另一个线程从 `MAZeroingWeakRef` 检索该对象。然后检索会尝试在对象已被标记为销毁后复活它，这是不合法的。）

当然，你不会想为每个被目标化的对象创建一个新的子类，每个目标类只需要一个子类。一个小的覆写类表格确保为每个普通类创建的子类不超过一个。

作为最后一步，目标对象的类被设定为新的子类，确保新方法生效。

**CoreFoundation 的棘手之处**  
上述策略在遇到[无缝桥接类（toll-free bridged classes）如 `NSCFString`](http://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html) 时会遇到问题。由于它们的实现方式，更改此类对象的类会导致无限递归，并且一旦有人尝试使用它们就会崩溃。CoreFoundation 代码看到更改后的类，假设它是一个纯 Objective-C 类，并通过对应的 Objective-C 方法调用。`NSCF` 方法然后回调 CoreFoundation。很快就会发生崩溃。

虽然我确实找到了一个解决这个问题的方法，但它非常复杂且繁琐，我将把它留到两周后的一篇单独文章中发表。

**代码**  
像往常一样，你可以从我的公共 Subversion 仓库获取 `MAZeroingWeakRef` 的代码：

```
    svn co http://mikeash.com/svn/ZeroingWeakRef/
```

或者只需点击上面的链接来浏览代码。

我将逐步介绍一个稍微简化的 `MAZeroingWeakRef` 版本。由于我上面提到的 CoreFoundation 解决方法的疯狂特性，我本周将跳过那些部分，只讨论理智的 Objective-C 部分。有一个名为 `COREFOUNDATION_HACK_LEVEL` 的宏（macro），它允许控制启用多少 CoreFoundation 黑客手段（hackery）。在级别 `2`，你获得完整的黑客手段，完全支持对 CoreFoundation 对象的弱引用。在级别 `1`，会引用和使用一些不太重要的私有符号来可靠地判断一个对象是否为桥接对象，并且代码在尝试创建指向桥接对象的弱引用时只会断言。在级别 `0`，代码在尝试创建指向桥接对象的弱引用时断言，并且仅在类名称中查找 `NSCF` 前缀来检查桥接。本周，我将讨论代码，就像它是用级别 `0` 编译的一样。

**全局变量**  
`MAZeroingWeakRef` 使用一些全局变量来进行各种内务管理。首先是互斥锁（mutex）：

```
    static pthread_mutex_t gMutex;
```

这用于保护其他全局数据结构，以及附加到每个目标对象的归零弱引用表。

接下来，需要一个 `CFMutableDictionary` 来将目标对象映射到指向它们的弱引用：

```
    static CFMutableDictionaryRef gObjectWeakRefsMap; // 将（未 retain 的）对象映射到包含弱引用的 CFMutableSetRef
```

接下来，使用一个 `NSMutableSet` 来追踪创建的动态子类，并使用一个 `NSMutableDictionary` 来将普通类映射到它们的动态子类：

```
    static NSMutableSet *gCustomSubclasses;
    static NSMutableDictionary *gCustomSubclassMap; // 将普通类映射到其自定义子类
```

最后，实现 `+initialize` 来设定所有这戏变量。这里唯一棘手的事情是它使用递归互斥锁而不是常规互斥锁。在某些情况下，临界区可能会被重新进入，例如创建一个指向另一个 `MAZeroingWeakRef` 的 `MAZeroingWeakRef`，使用递归互斥锁可以使其正常运作。

```
    + (void)initialize
    {
        if(self == [MAZeroingWeakRef class])
        {
            CFStringCreateMutable(NULL, 0);
            pthread_mutexattr_t mutexattr;
            pthread_mutexattr_init(&mutexattr;);
            pthread_mutexattr_settype(&mutexattr, PTHREAD_MUTEX_RECURSIVE);
            pthread_mutex_init(&gMutex, &mutexattr;);
            pthread_mutexattr_destroy(&mutexattr;);
            
            gCustomSubclasses = [[NSMutableSet alloc] init];
            gCustomSubclassMap = [[NSMutableDictionary alloc] init];
        }
    }
```

我还写了一个快速的辅助函数，在持有锁时执行一段代码块：

```
    static void WhileLocked(void (^block)(void))
    {
        pthread_mutex_lock(&gMutex;);
        block();
        pthread_mutex_unlock(&gMutex;);
    }
```

以及另外三个辅助函数，用于处理向对象的 `CFMutableSet` 添加弱引用、从对象中移除弱引用以及清空对象的所有弱引用：

```
    static void AddWeakRefToObject(id obj, MAZeroingWeakRef *ref)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        if(!set)
        {
            set = CFSetCreateMutable(NULL, 0, NULL);
            CFDictionarySetValue(gObjectWeakRefsMap, obj, set);
            CFRelease(set);
        }
        CFSetAddValue(set, ref);
    }
    
    static void RemoveWeakRefFromObject(id obj, MAZeroingWeakRef *ref)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        CFSetRemoveValue(set, ref);
    }
    
    static void ClearWeakRefsForObject(id obj)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        [(NSSet *)set makeObjectsPerformSelector: @selector(_zeroTarget)];
        CFDictionaryRemoveValue(gObjectWeakRefsMap, obj);
    }
```

**`MAZeroingWeakRef` 的实现**  
有了这些基础，我现在将采用自上而下的方法来处理其余的实现。

首先，是便利构造器（convenience constructor）和初始化方法。大部分都很直接：

```
    + (id)refWithTarget: (id)target
    {
        return [[[self alloc] initWithTarget: target] autorelease];
    }
    
    - (id)initWithTarget: (id)target
    {
        if((self = [self init]))
        {
            _target = target;
            RegisterRef(self, target);
        }
        return self;
    }
```

唯一棘手的地方是调用 `RegisterRef`。那是一个内部实用函数，负责将弱引用对象连接到目标对象，必要时对目标类进行子类化，以及将目标对象的类更改为自定义子类。

`dealloc` 实现类似地调用一个实用函数来移除弱引用对象：

```
    - (void)dealloc
    {
        UnregisterRef(self);
        [_cleanupBlock release];
        [super dealloc];
    }
```

加入一个简单的 `description` 方法，以便我们可以看到内部发生的事情：

```
    - (NSString *)description
    {
        return [NSString stringWithFormat: @"<%@: %p -> %@>", [self class], self, [self target]];
    }
```

以及一个用于设定清理 block 的标准 setter：

```
    - (void)setCleanupBlock: (void (^)(id target))block
    {
        block = [block copy];
        [_cleanupBlock release];
        _cleanupBlock = block;
    }
```

`target` 方法变得更复杂一些。因为目标可以在任何时候被销毁，所以它需要在持有全局弱引用锁的同时获取其值。它还需要在持有该锁的同时 retain 目标，以确保如果目标还存活，它在接收者完成使用之前一直保持存活。这当然随后会与一个 autorelease 平衡：

```
    - (id)target
    {
        __block id ret;
        WhileLocked(^{
            ret = [_target retain];
        });
        return [ret autorelease];
    }
```

最后，有一个用于归零目标的私有方法，当目标对象被释放时由内部机制调用。由于全局锁已由该机制持有，因此无需在此处显式锁定。此方法只会调用并释放清理 block（如果有的话），并清空目标：

```
    - (void)_zeroTarget
    {
        if(_cleanupBlock)
        {
            _cleanupBlock(_target);
            [_cleanupBlock release];
            _cleanupBlock = nil;
        }
        _target = nil;
    }
```

就是这样！很容易，对吧？当然，所有有趣的位置都在那些实用函数中，以及它们调用的实用函数，依此类推……

**实用函数的实现**  
`UnregisterRef` 的实现很简单。从 `MAZeroingWeakRef` 中获取目标，取得指向目标的引用表，并移除给定的引用。将所有内容包裹在一个锁中，以确保在此操作期间目标不会被释放：

```
    static void UnregisterRef(MAZeroingWeakRef *ref)
    {
        WhileLocked(^{
            id target = ref->_target;
            
            if(target)
                RemoveWeakRefFromObject(target, ref);
        });
    }
```

`RegisterRef` 类似。除了将引用添加到引用表之外，它还会调用 `EnsureCustomSubclass`。该函数将在必要时创建一个新的自定义子类，并将目标对象的类设定为该子类。

```
    static void RegisterRef(MAZeroingWeakRef *ref, id target)
    {
        WhileLocked(^{
            EnsureCustomSubclass(target);
            AddWeakRefToObject(target, ref);
        });
    }
```

`EnsureCustomSubclass` 的实现分成许多部分。首先，它检查对象是否*已经*是自定义子类的一个实例。如果是，则无需执行任何操作。如果不是，它会查找与对象当前类对应的自定义子类，并相应地设定目标对象的类。如果尚未创建自定义子类，则创建它。

```
    static void EnsureCustomSubclass(id obj)
    {
        if(!GetCustomSubclass(obj))
        {
            Class class = object_getClass(obj);
            Class subclass = [gCustomSubclassMap objectForKey: class];
            if(!subclass)
            {
                subclass = CreateCustomSubclass(class, obj);
                [gCustomSubclassMap setObject: subclass forKey: class];
                [gCustomSubclasses addObject: subclass];
            }
            object_setClass(obj, subclass);
        }
    }
```

`GetCustomSubclass` 的实现很简单。获取对象的类，并检查它是否在 `gCustomSubclasses` 集合中。如果不在，则获取超类（superclass），并沿着链向上追踪直到找到一个。如果没有找到，则此对象没有自定义子类。（追踪链的原因是，即使某些其他代码（如键值观察）在 `MAZeroingWeakRef` 设定一个之后设定自己的自定义子类，此代码仍能正确执行。）

```
    static Class GetCustomSubclass(id obj)
    {
        Class class = object_getClass(obj);
        while(class && ![gCustomSubclasses containsObject: class])
            class = class_getSuperclass(class);
        return class;
    }
```

同样，不难。真正的乐趣始于 `CreateCustomSubclass`。它做的第一件事是检查对象是否为 CoreFoundation 无缝桥接对象。正如我上面讨论的，子类化方法对这些对象会失效，因此需要拒绝它们：

```
    static Class CreateCustomSubclass(Class class, id obj)
    {
        if(IsTollFreeBridged(class, obj))
        {
            NSCAssert(0, @"Cannot create zeroing weak reference to object of type %@ with COREFOUNDATION_HACK_LEVEL set to %d", class, COREFOUNDATION_HACK_LEVEL);
            return class;
        }
        else
        {
```

（`COREFOUNDATION_HACK_LEVEL` 是 `#define`，它决定启用多少 CoreFoundation 黑客手段。正如我上面提到的，我将像没有启用它一样来浏览代码。）

`IsTollFreeBridged` 的实现只是检查类名称是否以 `NSCF` 开头：

```
    static BOOL IsTollFreeBridged(Class class, id obj)
    {
        return [NSStringFromClass(class) hasPrefix: @"NSCF"];
    }
```

对于 `else` 分支，首要任务是为新类创建一个名称。由于 Objective-C 类名称必须是唯一的，它基于原始名称和一个唯一后缀构造一个新名称：

```
            NSString *newName = [NSString stringWithFormat: @"%s_MAZeroingWeakRefSubclass", class_getName(class)];
            const char *newNameC = [newName UTF8String];
```

接下来，调用 `objc_allocateClassPair` 来创建一个新的类对（class pair）。（在 Objective-C 中，每个类都有一个对应的元类（metaclass），这与运行时的运作方式有关。`objc_allocateClassPair` 函数一次性创建两者。）

```
            Class subclass = objc_allocateClassPair(class, newNameC, 0);
```

新类实现了两个方法，`release` 和 `dealloc`。下一步是将这两个方法添加到类中，将它们指向实现它们的函数：

```
            Method release = class_getInstanceMethod(class, @selector(release));
            Method dealloc = class_getInstanceMethod(class, @selector(dealloc));
            class_addMethod(subclass, @selector(release), (IMP)CustomSubclassRelease, method_getTypeEncoding(release));
            class_addMethod(subclass, @selector(dealloc), (IMP)CustomSubclassDealloc, method_getTypeEncoding(dealloc));
```

最后，调用 `objc_registerClassPair` 向运行时注册新类，并返回新创建的类：

```
            objc_registerClassPair(subclass);
            
            return subclass;
        }
    }
```

接下来，`CustomSubclassRelease`。从概念上讲，此类的实现很简单。获取全局弱引用锁，并在持有锁的情况下调用 `[super release]`。这样做的目的是确保对象的最终 release 及其释放是原子发生的，并且对象不会在两者之间被一个尚未归零的弱引用复活。

问题在于，仅仅写 `[super release]` 是行不通的，因为编译器只允许在真正的、编译时的方法实现中这样做。为了执行等效的操作，需要找出自定义弱引用子类的超类。这是使用一个简单的辅助函数完成的，该函数调用 `GetCustomSubclass` 并返回该类的超类：

```
    static Class GetRealSuperclass(id obj)
    {
        Class class = GetCustomSubclass(obj);
        NSCAssert(class, @"Coudn't find ZeroingWeakRef subclass in hierarchy starting from %@, should never happen", object_getClass(obj));
        return class_getSuperclass(class);
    }
```

有了这个辅助函数，`CustomSubclassRelease` 的实现可以使用它来查找超类，使用它来查找超类的 `release` 实现，然后在持有锁的情况下调用它：

```
    static void CustomSubclassRelease(id self, SEL _cmd)
    {
        Class superclass = GetRealSuperclass(self);
        IMP superRelease = class_getMethodImplementation(superclass, @selector(release));
        WhileLocked(^{
            ((void (*)(id, SEL))superRelease)(self, _cmd);
        });
    }
```

快完成了！剩下的一个函数是 `CustomSubclassDealloc`。它获取指向该对象的弱引用表，并告诉它们全部 `_zeroTarget`。然后，它使用与 `CustomSubclassRelease` 相同的技术调用 `dealloc` 的超类实现。

```
    static void CustomSubclassDealloc(id self, SEL _cmd)
    {
        ClearWeakRefsForObject(self);
        Class superclass = GetRealSuperclass(self);
        IMP superDealloc = class_getMethodImplementation(superclass, @selector(dealloc));
        ((void (*)(id, SEL))superDealloc)(self, _cmd);
    }
```

就是这样！你现在拥有了对 Objective-C 对象的归零弱引用（除了桥接的 CoreFoundation 对象，我将在下周介绍）。

**例子：**  
`MAZeroingWeakRef` 的基本用法很简单：

```
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSObject *obj = [[NSObject alloc] init];
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: obj];
    
    NSLog(@"%@", [ref target]);
    [obj release];
    [pool release];
    
    NSLog(@"%@", [ref target]);
```

第一个 `NSLog` 将打印该对象，第二个将打印 `(null)`。使用自动释放池是为了确保对象真正被销毁，因为使用 `target` 会将对象放入池中，否则它会存活更长时间。

使用清理 `block` 同样简单：

```
    NSObject *obj = [[NSObject alloc] init];
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: obj];
    [ref setCleanupBlock: ^(id target) { NSLog(@"Cleaned object %p!", target); }];
    [obj release];
```

当调用 `[obj release]` 时会打印日志。当然，你可以采取比简单打印更多的操作。但是，由于清理 `block` 是在持有全局弱引用锁时调用的，你应该尽量将其中的活动保持在最低限度。如果你需要做大量工作，请设定一个延迟调用，使用 `performSelectorOnMainThread:`、GCD、NSOperationQueue 等，并在那里执行额外的工作。

一个将常规实例变量转换为归零弱引用的简单方法是在你的 getter 和 setter 中使用 `MAZeroingWeakRef`，然后确保在其他代码中始终使用你的 getter：

```
    // 实例变量
    MAZeroingWeakRef *_somethingWeakRef;
    
    // 访问器
    - (void)setSomething: (Something *)newSomething
    {
        [_somethingWeakRef release];
        _somethingWeakRef = [[MAZeroingWeakRef alloc] initWithTarget: newSomething];
    }
    
    - (Something *)something
    {
        return [_somethingWeakRef target];
    }
    
    // 使用
    - (void)doThing
    {
        [[self something] doThingWithObject: self];
    }
```

当然，如果你这样做，你必须确保在 `-dealloc` 中释放你的引用，就像你 alloc 的任何其他对象一样。只是不要释放目标。

对于更高级的使用，这里是 `NSNotificationCenter` 的一个扩展，它消除了在 `dealloc` 中手动移除观察者的需要：

```
    @implementation NSNotificationCenter (MAZeroingWeakRefAdditions)
    
    - (void)addWeakObserver: (id)observer selector: (SEL)selector name: (NSString *)name object: (NSString *)object
    {
        [self addObserver: observer selector: selector name: name object: object];
        
        MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: observer];
        [ref setCleanupBlock: ^(id target) {
            [self removeObserver: target name: name object: object];
            [ref autorelease];
        }];
    }
    
    @end
```

请注意使用清理 `block` 来在对象被销毁时移除通知观察者。你只需要在通知观察者中调用 `addWeakObserver:` 而不是 `addObserver:`，你就再也不会忘记在 `dealloc` 中移除观察者。

类似地，如果你厌倦了由 NSTableView 数据源在视图本身之前被释放导致的奇怪崩溃，你可以轻松修复它：

```
    @implementation NSTableView (MAZeroingWeakRefAdditions)
    
    - (void)setWeakDataSource: (id <NSTableViewDataSource>)source
    {
        [self setDataSource: source];
        
        MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: observer];
        [ref setCleanupBlock: ^(id target) {
            if([self dataSource] == target) // 双重检查以确保安全
                [self setDataSource: nil];
            [ref autorelease];
        }];
    }
    
    @end
```

如果你预见到频繁更改表格视图数据源的情况，你会想编写一些更复杂的代码来在添加新的弱引用时清除旧的弱引用。然而，这不是一个常见的情况。

基本上，每当你有一个弱引用（你没有 retain 或 copy 的对象引用），你应该使用 `MAZeroingWeakRef` 而不是原始的未 retain 指针。它会为你省去麻烦和痛苦，并且非常易于使用。

**归零集合**  
仓库包括 `MAWeakArray` 和 `MAWeakDictionary`，它们是 `NSMutableArray` 和 `NSMutableDictionary` 的子类，对它们的内容使用归零弱引用。`MAWeakDictionary` 使用强键到弱对象，这对于许多缓存场景会很有用。我在这里不详细介绍它们的代码，但它们很简单，如果你好奇，可以检视仓库中的代码。

虽然我没有编写它们，但可以创建一个使用弱键而不是或除了弱对象之外的 `NSMutableSet` 和 `NSMutableDictionary` 的弱版本。由于弱引用的哈希/相等性问题，这些会更棘手，但肯定可以做到。

**结论**  
归零弱引用是许多语言中存在的一个极其有用的构造。即使在垃圾回收下运行的 Objective-C 也有它们，但没有 GC，Objective-C 代码一直受限使用非归零弱引用，这既棘手又危险。

`MAZeroingWeakRef` 将归零弱引用带入了手动内存管理的 Objective-C。虽然它在内部使用了一些技巧，但 API 非常易于使用。通过自动归零弱引用，你可以避免许多潜在的崩溃和数据损坏。归零弱引用也可以用于诸如对象缓存在内的非归零弱引用完全不实际的用途。

该代码在 BSD 许可证下提供。

对于两周后的下一期 Friday Q&A，我将讨论 `MAZeroingWeakRef` 如何绕过 CoreFoundation 对象的问题。在此之前，请尽情享受！

你喜欢这篇文章吗？我正在销售包含满满这些文章的整套书籍！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)

发表你的想法，发表评论：

垃圾邮件和离题的帖子将在不通知的情况下被删除。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
