---
title: 'Objective-C 内部实现：关联引用'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj'
original_language: en
published: 2023-06-05
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fc6148cbab36b6ce'
translated: true
---

> 原文：[Objective-C Internals: Associated References A comparison of Apple’s Associated References implementation and one I wrote for historical context, with additional notes about use with tagged pointer ob](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj)　·　Always Processing (Brian T. Kelley)

# Objective-C 内部实现：关联引用

![两个孩子，各在一台计算机工作站前，在屏幕上的对象之间创建关联。](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/ae4bf923-51a5-438e-60a7-ecd731bb7f00/public)

比较 Apple 的 _关联引用_ 实现与我为历史背景编写的一个实现，并附有关于标记指针（tagged pointer）对象使用的额外说明，以及 `assign` 关联策略的实际作用。

我仍记得热切期盼我们将 [Microsoft Office 2016 for Mac](https://en.wikipedia.org/wiki/Microsoft_Office_2016) 的最低部署目标更改为 Mac OS X 10.6^[[1](#_footnotedef_1)] 的那一天。[Snow Leopard](https://en.wikipedia.org/wiki/Mac_OS_X_Snow_Leopard) 引入了大量新 API，包括 [Grand Central Dispatch](https://developer.apple.com/documentation/DISPATCH) 和 [block](https://en.wikipedia.org/wiki/Blocks_(C_language_extension))。但最令我兴奋的是终于可以开始使用 Objective-C 的[关联引用](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html)来替换一些糟糕的代码。

## 老方法

Objective-C 最大的优势（也是弱点）在于其[动态方法绑定](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch)。几乎所有主要的第三方 App 都会（滥）用这一特性来填补功能空白或缓解 App/系统架构之间的阻抗不匹配。

将一个对象的生命周期与由第三方（即 Apple）实例化和控制的另一个对象的生命周期绑定，就是这样一个功能空白。在运行时提供此功能之前，App 可以通过（部分地）预先打补丁修改 `-[NSObject dealloc]` 的实现来实现这个功能。下面的代码示例展示了第三方如何使用这种方法来实现 _关联引用_。

```
#import <Foundation/Foundation.h>
#import <objc/runtime.h>

static OSSpinLock s_lock;               // for main side table
static NSMapTable *s_associatedObjects; // main side table
static IMP s_NSObject_dealloc;          // original implementation

void APAssociatedObjectSet(id object, id association) {
  id previousAssociation = nil;

  // retain does not require the lock, so do it outside of the
  // lock to minimize time spent holding the lock
  [association retain];

  OSSpinLockLock(&s_lock);
  previousAssociation = [s_associatedObjects objectForKey:object];
  if (association != nil) {
    [s_associatedObjects setObject:association forKey:object];
  } else {
    [s_associatedObjects removeObjectForKey:object];
  }
  OSSpinLockUnlock(&s_lock);

  // release outside of the lock in case this is the last
  // release, as the dealloc implementation acquires the lock
  [previousAssociation release];
}

id APAssociatedObjectGet(id object) {
  OSSpinLockLock(&s_lock);
  id association = [s_associatedObjects objectForKey:object];
  // retain the associated object to ensure it's not deallocated
  // while in use by the caller in case another thread changes the
  // associated object between now and then
  [association retain];
  OSSpinLockUnlock(&s_lock);

  return [association autorelease];
}

static void APAssociatedObject_dealloc(id self, SEL _cmd) {
  // release any associated object and remove the side table entry
  APAssociatedObjectSet(self, nil);
  (*s_NSObject_dealloc)(self, _cmd);
}

void APAssociatedObjectInitialize(void) {
  s_lock = OS_SPINLOCK_INIT;
  // The key is weak to prevent the object from becoming immortal.
  // The value is weak to explicitly control the retain count to
  // prevent dealloc reentrancy deadlocks.
  s_associatedObjects=[NSMapTable mapTableWithWeakToWeakObjects];

  // Pre-patch -[NSObject dealloc] to clean up s_associatedObjects
  Method m = class_getInstanceMethod([NSObject class],
                                     @selector(dealloc));
  s_NSObject_dealloc = method_getImplementation(m);
  method_setImplementation(m, (IMP)&APAssociatedObject_dealloc);
}
```

虽然这个实现只有 59 行（包括空白和注释），但我想指出几点：

- 此实现支持 0 或 1 个对象关联，但只需稍作修改，就能支持任意数量的关联（就像 `objc_setAssociatedObject()` 那样）。或者，客户端可以使用 `NSMutableDictionary` 来关联任意数量的对象。
- 每个 `-dealloc` 都需要获取一个锁来执行簿记工作（除了运行时的锁和分配器的锁获取之外）。我们在之前的一篇文章中看到，对于_没有_关联引用（以及其他条件）的对象实例，运行时有一条[快速释放路径](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#has_assoc-has_cxx_dtor-weakly_referenced-and-has_sidetable_rc)，使其在大多数情况下可以避免锁定开销。
- 移除一个关联可能会导致被关联对象释放，而这又可能导致它的关联对象被释放。因此，在持有锁的情况下，实现必须避免递归，因为 `OSSpinLock` 是不可重入的。
- 在获得关联的对象的类上预先打补丁修改 `-dealloc` 不是一个可行的方法，原因有二：
    1. 类层次结构可能存在多层补丁。例如，在一个 `NSObject` 上设置了一个关联对象，又在 `NSView` 上设置了另一个，那么所有 `NSView` 实例（包括子类）在释放期间会两次调用补丁中的代码。一个实现可以处理这种情况，但代价是增加额外的复杂性。
    2. 从补丁调用正确的 `-dealloc` 变得更加困难。继续上面的例子，如果一个 `NSTableView` 正在释放，补丁如何知道它应该调用 `-[NSView dealloc]` 的实现还是 `-[NSObject dealloc]` 的实现？（`self` 的类身份总是 `NSTableView`。）需要大量的簿记工作来跟踪一个对象在它的释放链中的位置，并处理在其释放过程中发生的其他释放。
- Objective-C 自动引用计数（ARC）直到 OS X 10.7 Lion 才出现。所以我想强调两点，它们对现代 Objective-C 程序员来说已经不再相关：
    - `APAssociatedObjectGet()` 中的 `retain` 和 `autorelease` 调用确保了返回的对象在当前自动释放池作用域内存活。如果没有这些，另一个线程可能会导致该对象在从映射表中检索出来和返回给调用方之间被释放。
    - 在映射表的 `mapTableWithWeakToWeakObjects` 工厂方法中使用 _weak_ 并**没有** ARC 的零弱引用（zeroing weak reference）语义。相反，它等价于 ARC 的 `unsafe_unretained`。
- `APAssociatedObjectInitialize()` 可以使用 `__attribute__((constructor))` 在 `main()` 被调用之前初始化这个功能。我没有这样做，因为大型 App 通常有一个复杂的初始化系统来调用这个函数。

接下来，让我们看看 Apple 的 Objective-C 运行是如何实现这个功能的。

## Apple 的方法

上面第三方的实现和注释与 Apple 的实现惊人地一致。（我说惊人，是因为我在查阅 Apple 的实现之前就写好了上面的代码^[[2](#_footnotedef_2)]。）

首先，我们来看一下 [`objc_setAssociatedObject()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L657-L661)，它只是简单地调用了 [`_object_set_associative_reference()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L159-L220)。

`runtime/objc-references.mm` 第 [170-219](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L170-L219) 行

```
DisguisedPtr<objc_object> disguised{(objc_object *)object};
ObjcAssociation association{policy, value};

// retain the new value (if any) outside the lock.
association.acquireValue();

bool isFirstAssociation = false;
{
  AssociationsManager manager;
  AssociationsHashMap &associations(manager.get());

  if (value) {
    auto refs_result = associations.try_emplace(disguised, ObjectAssociationMap{});
    if (refs_result.second) {
      /* it's the first association we make */
      isFirstAssociation = true;
    }

    /* establish or replace the association */
    auto &refs = refs_result.first->second;
    auto result = refs.try_emplace(key, std::move(association));
    if (!result.second) {
      association.swap(result.first->second);
    }
  } else {
    auto refs_it = associations.find(disguised);
    if (refs_it != associations.end()) {
      auto &refs = refs_it->second;
      auto it = refs.find(key);
      if (it != refs.end()) {
        association.swap(it->second);
        refs.erase(it);
        if (refs.size() == 0) {
          associations.erase(refs_it);
        }
      }
    }
  }
}

if (isFirstAssociation)
  object->setHasAssociatedObjects();

// release the old value (outside of the lock).
association.releaseHeldValue();
```

鉴于与上一节的一致性，我将简单地强调与我实现相似和不同的关键点。

- [`DisguisedPtr`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L983-L1031) 用于抑制 `leaks` 等工具中的堆追踪。
- [`ObjcAssociation`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L49-L100) 辅助对象实现了关联策略（使用 `assign`、`retain` 或 `copy` 语义的存储，以及读取是 `atomic` 还是 `nonatomic`）。
- [`AssociationsManager`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L108-L123) 是一个 [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) 便利对象，用于锁定和解锁[关联自旋锁](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L45)（现在是一个[不公平锁（unfair lock）](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/Threading/darwin.h#L194-L224)）。
- 对象关联使用哈希映射（具体来说是 LLVM 的 [DenseMap](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/llvm-DenseMap.h)）存储。一个[顶层哈希映射](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L103)将对象指针映射到一个[关联哈希映射](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L102)，后者将键映射到 `ObjcAssociation`（对象及其保留策略）。
- 关联 `nil` 值会移除之前关联的任何对象。
- 当一个对象获得其第一个关联时，运行时会更新其状态以关闭[快速释放路径](https://alwaysprocessing.blog/2023/01/19/objc-class-isa#has_assoc-has_cxx_dtor-weakly_referenced-and-has_sidetable_rc)。
- 任何先前关联对象的释放都在锁外进行。

与 setter 类似，[`objc_getAssociatedObject()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L642-L646) 只是简单地调用了 [`_object_get_associative_reference()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L137-L157)。获取路径很直接，所以我没什么可评论的！🙊

Apple 的实现提供了一个有趣的函数 [`objc_removeAssociatedObjects()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime.mm#L663-L668)。老实说，我不确定为什么这是一个公开 API——[`runtime.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/runtime.h#L1650-L1664) 中的注释建议不要使用它（而且有充分的理由）：

> 此函数的主要目的是方便将对象返回到“原始状态”。你不应使用此函数来常规地从对象中移除关联，因为它也会移除其他客户端可能已添加到该对象的关联。通常，你应该使用 `objc_setAssociatedObject` 并传入 nil 值来清除关联。

与 getter 和 setter 函数一样，`objc_removeAssociatedObjects()` 调用 [`_object_remove_associations()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L222-L269)。但是，这个内部函数接受一个额外的参数：`bool deallocating`，当由 `objc_removeAssociatedObjects()` 调用时，该参数为 `false`。这个内部函数只有另一个调用者 [`objc_destructInstance()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L8569)，它毫不意外地为 `deallocating` 传递了 `true`。

那么，`deallocating` 标志是做什么用的呢？函数中的一条[注释](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L238)解释了它的用途：

> 如果我们不是正在释放，那么 `SYSTEM_OBJECT` 关联被保留。

Apple 有一个内部的策略标志 [`OBJC_ASSOCIATION_SYSTEM_OBJECT`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm#L42)，它能防止其关联对象被 `objc_removeAssociatedObjects()` 移除。使用这个函数可能会搬起石头砸自己的脚，但 Apple 会阻止你违反他们的假设。

我怀疑这就是关联键的类型是 `void *` 的原因：指针键在 Apple 的框架中很难被识别，进而在第三方 App 中（滥）用，而字符串键则相对容易查找和使用（例如 `NSNotificationName`）。

### 标记指针对象

在[标记指针对象](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr)上设置关联对象时会发生什么？效果与使用相同的存储策略将对象赋值给一个全局变量相同：该对象会一直存在，直到分配一个新值。因此，在标记指针对象上设置关联对象实际上会导致关联对象泄露。

关联对象实现没有处理标记指针的代码路径（甚至没有在控制台中记录警告）。因此，运行时会将该标记指针存储在关联哈希图中，它会无限期地存在，因为标记指针对象从不释放。

标记指针对象的另一个副作用是它们实际上会[对所有值进行驻留](https://en.wikipedia.org/wiki/Interning_(computer_science))。虽然已知某些类型（如 `NSNumber`）会实现[某种形式的驻留](https://github.com/apple-oss-distributions/CF/blob/CF-1153.18/CFNumber.c#L1037)，但 `NSString` 之前没有这种行为。但是，`NSString` 的标记指针代码路径足够激进，以至于[从磁盘加载的本地化字符串](https://markavitale.com/objc-tagged-pointers#the-explanation)可能会产生一个标记指针对象！因此，任何在 `NSString` 类型的对象上设置关联对象的代码，如果这些字符串实例是标记指针对象而不是不同的实例，可能会发现关联对象相互覆盖。

尽管标记指针对象的使用被认为是一个内部实现细节，但请查看[使用标记指针的类](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-internal.h#L447-L509)，并避免在这些类型的对象上使用关联对象。

### 深入探讨 assign 存储

在撰写这篇文章时，我意识到我十多年来一直在误用这个 API 🤦‍♂️。[`OBJC_ASSOCIATION_ASSIGN`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/runtime.h#L1639) 策略旁边的注释写着：

> 指定对被关联对象的弱引用。

如[老方法](#the-old-way)一节所述，在 ARC 之前，_弱引用（weak）_ 一词等价于 ARC 的 `unsafe_unretained`；此标志并**没有**使用 ARC 的零弱引用语义。通读[实现](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-references.mm)看看哪里用了 _weak_。根本没有！

我这周有很多 grep 和代码审查要做……​

## 结论

第三方的 _关联引用_ 实现几乎可以与 Apple 的第一方实现相媲美，第一方实现的主要优势在于可以为没有关联对象的对象提供一条快速释放路径。新的运行时优化（即标记指针对象）可能会导致代码行为异常，因为对象（与其关联的对象）的唯一性和生命周期在不同 OS 版本之间可能会发生变化。而历史背景至关重要——文档所依据的假设可能会随着时间的推移而改变，从而扭曲其含义。

---

[1](#_footnoteref_1). 到 Office 2016 发布时，macOS 10.12 Sierra 已是当前版本。因此，遵循 _n-2_ 模式，Office 的最低部署目标是 OS X 10.10 Yosemite。

[2](#_footnoteref_2). 在阅读完 Apple 的实现后，我做了一项修改，即在锁外执行关联对象的 retain 操作。
