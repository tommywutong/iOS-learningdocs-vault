---
title: 获取 Objective-C 类的子类 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/01/getting-subclasses-of-objective-c-class.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:f2f9f2f63e204aba'
translated: true
---

> 原文：[Getting the subclasses of an Objective-C class | Cocoa with Love](https://www.cocoawithlove.com/2010/01/getting-subclasses-of-objective-c-class.html)　·　Cocoa with Love (Matt Gallagher)

获取某个类的完整子类（subclass）列表是一个相当简单的任务，但它需要一些不常用的运行时函数，这可能会增加难度。在这篇文章中，我将探讨 Objective-C 中一个 Class 的定义方式，以及两种完全不同的获取子类的方法。

## 引言

考虑到 Objective-C 运行时提供了高度的反射和内省能力，你可能会以为在 Objective-C Runtime API 中很容易找到 `class_getSubclasses(Class parentClass)` 这样的函数，但实际上并没有这样的函数。

这个函数之所以被遗漏，可能有几个原因——动态类创建和加载、线程和锁定问题、`class_t` 结构在历史上的缺失、过早优化方面的考虑，甚至是有意引导程序员远离某些设计——但结果是，你必须自己来找出子类。

注意：获取一个类的子类并不常见，通常是在你无法控制的 API 上进行事后修改，或者作为仅用于调试的内省或 hack 手段。一般来说，由子类自行显式注册的设计，比在运行时查找子类要更好。例如，在我的[简单、可扩展的 HTTP 服务器](https://www.cocoawithlove.com/2009/07/simple-extensible-http-server-in-cocoa.html)中，每个 `HTTPResponseHandler` 都必须包含：

```objc
+ (void)load
{
    [HTTPResponseHandler registerHandler:self];
}
```

这样一来，当父类需要查找处理请求的 handler 时，那些“选择加入”的 `HTTPResponseHandler` 子类就会被发现。

然后，在无法加入这样的 `load` 方法，或者你有理由认为不需要这样做的情况下（例如，用于验证你编写的所有 `HTTPResponseHandlers` 是否确实注册了自己的调试用验证代码），就会使用获取子类的方法。

## 筛选所有类的列表

Objective-C 中类的传统定义如下：

```objc
struct objc_class {
    Class isa;
    Class super_class;
    const char *name;
    long version;
    long info;
    long instance_size;
    struct objc_ivar_list *ivars;
    struct objc_method_list **methodLists;
    struct objc_cache *cache;
    struct objc_protocol_list *protocols;
};
```

类中包含指向其超类（superclass）的指针，但不包含指向子类的指针。

由于没有专门的函数来获取子类，使用公共 API 的唯一方法是获取运行时中所有类的列表，然后逐一测试它们是否为目标类的子类。

如果你觉得这听起来有些粗笨，那你可能是对的。在 Mac OS X 10.6.2 中，仅 Foundation 框架就有 527 个类，而 Cocoa 框架中有 1966 个类。这还不包括你的项目添加的类，以及其他框架中的类。当然，检查所有这些类只需要一两毫秒，但这仍然不适合在紧密循环中执行——如果你需要重复使用某个类的子类列表，最好将其缓存起来。

在运行时中获取所有类非常简单：

```objc
int numClasses = objc_getClassList(NULL, 0);
Class *classes = NULL;

classes = malloc(sizeof(Class) * numClasses);
numClasses = objc_getClassList(classes, numClasses);

// 对 classes 做一些处理

free(classes);
```

接下来的问题是：我们如何确定哪些类是某个父类的实际子类？

直观的方法可能是使用 `isSubclassOfClass:` 方法：

```objc
NSMutableArray *result = [NSMutableArray array];
for (NSInteger i = 0; i < numClasses; i++)
{
    if ([classes[i] isSubclassOfClass:parentClass])
    {
        [result addObject:classes[i]];
    }
}
```

遗憾的是，我们不能这样做，因为当考虑运行时中的所有类时，并非所有类都拥有 `isSubclassOfClass:` 方法（因为 `isSubclassOfClass:` 是 `NSObject` 的方法）。

这里的问题在于，许多通常被认为由所有类实现的方法，实际上是由 `NSObject` 或 `NSObject` 协议的具体实现提供的。有些类，如 `_NSZombie_` 或 `NSProxy`，并非派生自 `NSObject`，即使它们实现了 `NSObject` 协议，其实现方式也可能无法预料（`_NSZombie_` 会对任何方法抛出异常，而 `NSProxy` 会将许多此类方法转发给其 `target`，而不是自行响应）。

因此，我们不能对任意类调用任何方法，而必须使用运行时函数。我们使用 `class_getSuperclass()` 来获取某个类的超类，并将其与 `parentClass` 进行比较。这样就得到了完整的解决方案：

```objc
NSArray *ClassGetSubclasses(Class parentClass)
{
    int numClasses = objc_getClassList(NULL, 0);
    Class *classes = NULL;

    classes = malloc(sizeof(Class) * numClasses);
    numClasses = objc_getClassList(classes, numClasses);
    
    NSMutableArray *result = [NSMutableArray array];
    for (NSInteger i = 0; i < numClasses; i++)
    {
        Class superClass = classes[i];
        do
        {
            superClass = class_getSuperclass(superClass);
        } while(superClass && superClass != parentClass);
        
        if (superClass == nil)
        {
            continue;
        }
        
        [result addObject:classes[i]];
    }

    free(classes);
    
    return result;
}
```

## 快速而危险的 hack 方法

我刚才给出的函数是在程序中使用的正确方法。但如果我不展示一种完全不同、完全不安全的做法，我会觉得这篇文章不够有趣。

这种方法需要 Objective-C Runtime 2.0（即 Mac OS X 64 位和 iPhone 上使用的那个版本）。在运行时的新版本中，一个类实际上包含一个指向其子类的直接链接。

根据 [Apple 开源仓库中的 objc-runtime-new.h](http://opensource.apple.com/source/objc4/objc4-437/runtime/objc-runtime-new.h)，一个类被声明如下：

```objc
typedef struct class_t {
    struct class_t *isa;
    struct class_t *superclass;
    Cache cache;
    IMP *vtable;
    class_rw_t *data;
} class_t;
```

以及 `class_rw_t` 结构体定义：

```objc
typedef struct class_rw_t {
    uint32_t flags;
    uint32_t version;

    const class_ro_t *ro;
    
    struct method_list_t **methods;
    struct chained_property_list *properties;
    struct protocol_list_t ** protocols;

    struct class_t *firstSubclass;
    struct class_t *nextSiblingClass;
} class_rw_t;
```

这意味着我们可以沿着 `firstSubclass` 和 `nextSiblingClass` 成员进行遍历，从而访问某个父类的所有子类，而无需读取运行时中的每个类。

然后，深度优先的递归遍历就可以得到某个类的完整子类列表：

```objc
typedef void *Cache;
#import "objc-runtime-new.h"

void AddSubclassesToArray(Class parentClass, NSMutableArray *subclasses)
{
    struct class_t *internalRep = (struct class_t *)parentClass;
    
    // 深度优先遍历
    Class subclass = (Class)internalRep->data->firstSubclass;
    while (subclass)
    {
        [subclasses addObject:subclass];
        AddSubclassesToArray(subclass, subclasses);
    
        // 然后进行广度优先遍历
        struct class_t *subclassInternalRep = (struct class_t *)subclass;
        subclass = (Class)subclassInternalRep->data->nextSiblingClass;
    }
}
```

然而，尽管与遍历整个类列表相比效率很高，但这种方法不能安全使用。根据 [objc-runtime-new.m](http://opensource.apple.com/source/objc4/objc4-437/runtime/objc-runtime-new.m)，对 `class_t` 的 `data` 成员的所有访问都必须由 `runtimeLock` 保护——而该锁在运行时库本身之外是无法访问的。

由于锁无法访问，这意味着这种方法无法保证安全，因为任何线程（包括 Cocoa 自动启动的线程）都可能导致崩溃。

这是一个有趣的实验，我希望 Apple 将来能提供一个可以安全实现此功能的函数。

## 结论

运行时没有提供简单的方法来访问一个类的子类——即使在较新版本的运行时中，这些数据实际上已经存储在该类的数据结构中。

由于运行时中存在不派生自 `NSObject` 的类，从所有类的列表中筛选子类会带来一些有趣的问题。但最终，一旦你了解了使用完整类列表的限制，获取子类就相当简单了。

尽管这不是你通常需要的数据，但如果 Apple 当初决定在新版本运行时中提供对子类数据的访问，那该多好。这样效率更高，并且如果需要，还可以按排序顺序生成列表。
