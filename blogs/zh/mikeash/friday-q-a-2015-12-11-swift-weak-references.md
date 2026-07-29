---
title: 'Friday Q&A 2015-12-11：Swift 弱引用'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:18f5882ecc606c6c'
translated: true
---

> 原文：[Friday Q&A 2015-12-11: Swift Weak References](https://www.mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)　·　mikeash.com Friday Q&A

发表于 2015-12-11 14:16 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2015-12-25：Swifty Target/Action](https://www.mikeash.com/pyblog/friday-qa-2015-12-25-swifty-targetaction.html)  
上一篇：[Friday Q&A 2015-11-20：协变与逆变](https://www.mikeash.com/pyblog/friday-qa-2015-11-20-covariance-and-contravariance.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2015-12-11：Swift 弱引用

作者：[Mike Ash](https://www.mikeash.com/)

本文也有[匈牙利语（Zsolt Boros 翻译）](http://www.forallworld.com/swift-gyenge-hivatkozasok/)、[立陶宛语（Giedrius Sadauskas 翻译）](http://crowfer.com/swift-silpnas-nuorodos/)版本。

**弱引用**  
在垃圾回收或引用计数的语言中，强引用会保持目标对象存活。弱引用则不会。当存在强引用时，对象不能被销毁；但当存在弱引用时，对象可以被销毁。

当我们说“弱引用”时，通常指的是**归零（zeroing）**弱引用。也就是说，当弱引用的目标被销毁时，弱引用会变为 `nil`。也可能存在非归零的弱引用，它们会导致陷阱、崩溃或“恶魔的鼻息”。Objective-C 中使用 `unsafe_unretained`，或 Swift 中使用 `unowned` 时，就会得到这种结果。（注意，Objective-C 给我们的是恶魔鼻息版本，而 Swift 则负责可靠地崩溃。）

归零弱引用非常有用，在引用计数语言中极其便利。它们允许存在循环引用而不产生保留循环，并且无需手动断开反向引用。它们非常有用，以至于早在 Apple 引入 ARC 并让语言级的弱引用能在垃圾回收代码之外使用之前，我就[实现过自己的弱引用版本](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)。

**它是如何工作的？**  
归零弱引用的典型实现是维护一个列表，记录指向每个对象的所有弱引用。当创建一个指向某对象的弱引用时，该引用被添加到列表中。当该引用被重新赋值或超出作用域时，从列表中移除。当对象被销毁时，列表中的所有引用都被归零。在多线程环境（即今天的所有环境）中，实现必须同步获取弱引用和销毁对象的操作，以避免竞态条件——当一个线程释放对某个对象的最后一个强引用的同时，另一个线程尝试加载对它的弱引用时发生。

在我的实现中，每个弱引用都是一个完整的对象。弱引用列表只是一个弱引用对象的集合。这会因为额外的间接性和内存使用而带来一些低效，但将引用视为完整对象是很方便的。

在 Apple 的 Objective-C 实现中，每个弱引用是一个指向目标对象的简单指针。编译器不直接读写这些指针，而是使用辅助函数。当写入弱指针时，存储函数将该指针位置注册为目标对象的弱引用。当读取弱指针时，读取函数与引用计数系统集成，确保它永远不会返回指向正在被 dealloc 的对象的指针。

**归零实战**  
让我们构建一些代码，以便观察这些情况的发生。

我们想要能够转储对象内存的内容。这个函数接受一块内存区域，将其分解为指针大小的块，并将整个内容转换为方便的十六进制字符串：

```
    func contents(ptr: UnsafePointer<Void>, _ length: Int) -> String {
        let wordPtr = UnsafePointer<UInt>(ptr)
        let words = length / sizeof(UInt.self)
        let wordChars = sizeof(UInt.self) * 2

        let buffer = UnsafeBufferPointer<UInt>(start: wordPtr, count: words)
        let wordStrings = buffer.map({ word -> String in
            var wordString = String(word, radix: 16)
            while wordString.characters.count < wordChars {
                wordString = "0" + wordString
            }
            return wordString
        })
        return wordStrings.joinWithSeparator(" ")
    }
```

下一个函数为一个对象创建一个转储函数。用一个对象调用它一次，它会返回一个函数，该函数将转储此对象的内容。在内部，它保存一个指向该对象的 `UnsafePointer`，而不是使用正常的引用。这确保了它不会与语言的引用计数系统交互。它还允许我们在对象被销毁后转储其内存，这将在后面派上用场。

```
    func dumperFunc(obj: AnyObject) -> (Void -> String) {
        let objString = String(obj)
        let ptr = unsafeBitCast(obj, UnsafePointer<Void>.self)
        let length = class_getInstanceSize(obj.dynamicType)
        return {
            let bytes = contents(ptr, length)
            return "\(objString) \(ptr): \(bytes)"
        }
    }
```

这是一个用于持有弱引用以便我们能够检查它的类。我在两边添加了虚拟变量，以便清楚地看到弱引用在内存转储中的位置：

```
    class WeakReferer {
        var dummy1 = 0x1234321012343210
        weak var target: WeakTarget?
        var dummy2: UInt = 0xabcdefabcdefabcd
    }
```

让我们试试看！我们首先创建一个 referer 并转储它：

```
    let referer = WeakReferer()
    let refererDump = dumperFunc(referer)
    print(refererDump())
```

这会打印：

```
    WeakReferer 0x00007f8a3861b920: 0000000107ab24a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
```

我们可以在开头看到 `isa`，后面跟着一些其他内部字段。`dummy1` 占据第 4 块，`dummy2` 占据第 6 块。我们可以看到它们之间的弱引用是零，符合预期。

现在让它指向一个对象，看看它是什么样子。我会在一个 `do` 块中执行此操作，这样我们可以控制目标何时超出作用域并被销毁：

```
    do {
        let target = NSObject()
        referer.target = target
        print(target)
        print(refererDump())
    }
```

这会打印：

```
    <NSObject: 0x7fda6a21c6a0>
    WeakReferer 0x00007fda6a000ad0: 00000001050a44a0 0000000200000004 1234321012343210 00007fda6a21c6a0 abcdefabcdefabcd
```

正如预期，指向目标的指针直接存储在弱引用中。让我们在 `do` 块结束时目标被销毁后再转储一次：

```
    print(refererDump())
```

```
    WeakReferer 0x00007ffe32300060: 000000010cfb44a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
```

它被归零了。完美！

只是为了好玩，我们用纯 Swift 对象作为目标重复实验。在不必要时牵扯到 Objective-C 不太好。这是一个纯 Swift 目标：

```
    class WeakTarget {}
```

让我们试试看：

```
    let referer = WeakReferer()
    let refererDump = dumperFunc(referer)
    print(refererDump())
    do {
        class WeakTarget {}
        let target = WeakTarget()
        referer.target = target
        print(refererDump())
    }
    print(refererDump())
```

目标开始时如预期为零，然后被赋值：

```
    WeakReferer 0x00007fbe95000270: 00000001071d24a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
    WeakReferer 0x00007fbe95000270: 00000001071d24a0 0000000200000004 1234321012343210 00007fbe95121ce0 abcdefabcdefabcd
```

然后当目标离开作用域时，引用应该被归零：

```
    WeakReferer 0x00007fbe95000270: 00000001071d24a0 0000000200000004 1234321012343210 00007fbe95121ce0 abcdefabcdefabcd
```

哦天哪。它没有被归零。也许目标没有被销毁。一定有什么东西让它保持存活！让我们再检查一下：

```
    class WeakTarget {
        deinit { print("WeakTarget deinit") }
    }
```

再次运行代码，我们得到：

```
    WeakReferer 0x00007fd29a61fa10: 0000000107ae44a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
    WeakReferer 0x00007fd29a61fa10: 0000000107ae44a0 0000000200000004 1234321012343210 00007fd29a42a920 abcdefabcdefabcd
    WeakTarget deinit
    WeakReferer 0x00007fd29a61fa10: 0000000107ae44a0 0000000200000004 1234321012343210 00007fd29a42a920 abcdefabcdefabcd
```

所以它确实正在被销毁，但弱引用没有被归零。怎么样，我们在 Swift 中发现了一个 bug！过了这么久它还没被修复，真是太惊人了。你会认为之前应该有人注意到。让我们继续通过访问引用来制造一个漂亮的崩溃，然后我们可以向 Swift 项目报告一个 bug：

```
    let referer = WeakReferer()
    let refererDump = dumperFunc(referer)
    print(refererDump())
    do {
        class WeakTarget {
            deinit { print("WeakTarget deinit") }
        }
        let target = WeakTarget()
        referer.target = target
        print(refererDump())
    }
    print(refererDump())
    print(referer.target)
```

崩溃来了：

```
    WeakReferer 0x00007ff7aa20d060: 00000001047a04a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
    WeakReferer 0x00007ff7aa20d060: 00000001047a04a0 0000000200000004 1234321012343210 00007ff7aa2157f0 abcdefabcdefabcd
    WeakTarget deinit
    WeakReferer 0x00007ff7aa20d060: 00000001047a04a0 0000000200000004 1234321012343210 00007ff7aa2157f0 abcdefabcdefabcd
    nil
```

哦天哪的平方！爆炸在哪里？本该有场惊天动地的大爆炸！输出显示一切最终还是正常的，但我们可以从转储中清楚地看到，它根本就没正常工作。

让我们非常仔细地检查一切。这里是 `WeakTarget` 的修订版本，带有一个虚拟变量，以便也能更好地转储其内容：

```
    class WeakTarget {
        var dummy = 0x0123456789abcdef

        deinit {
            print("Weak target deinit")
        }
    }
```

这里有一些新代码，它执行相同的过程，并在每一步转储两个对象：

```
    let referer = WeakReferer()
    let refererDump = dumperFunc(referer)
    print(refererDump())
    let targetDump: Void -> String
    do {
        let target = WeakTarget()
        targetDump = dumperFunc(target)
        print(targetDump())

        referer.target = target

        print(refererDump())
        print(targetDump())
    }
    print(refererDump())
    print(targetDump())
    print(referer.target)
    print(refererDump())
    print(targetDump())
```

让我们逐步分析输出。referer 像之前一样开始生命，带有一个已归零的 `target` 字段：

```
    WeakReferer 0x00007fe174802520: 000000010faa64a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
```

目标开始作为一个普通对象，带有各种头部字段，后跟我们的虚拟字段：

```
    WeakTarget 0x00007fe17341d270: 000000010faa63e0 0000000200000004 0123456789abcdef
```

在赋值给 `target` 字段后，我们可以看到指针值被填充了：

```
    WeakReferer 0x00007fe174802520: 000000010faa64a0 0000000200000004 1234321012343210 00007fe17341d270 abcdefabcdefabcd
```

目标与之前大致相同，但其中一个头部字段增加了 `2`：

```
    WeakTarget 0x00007fe17341d270: 000000010faa63e0 0000000400000004 0123456789abcdef
```

目标按预期被销毁：

```
    Weak target deinit
```

我们看到 referer 对象仍然有一个指向目标的指针：

```
    WeakReferer 0x00007fe174802520: 000000010faa64a0 0000000200000004 1234321012343210 00007fe17341d270 abcdefabcdefabcd
```

而目标本身看起来仍然非常活跃，尽管与我们上次看到它相比，另一个头部字段减少了 `2`：

```
    WeakTarget 0x00007fe17341d270: 000000010faa63e0 0000000200000002 0123456789abcdef
```

访问 `target` 字段产生了 `nil`，尽管它没有被归零：

```
    nil
```

再次转储 referer 显示，仅仅访问 `target` 字段的行为就已经改变了它。*现在*它被归零了：

```
    WeakReferer 0x00007fe174802520: 000000010faa64a0 0000000200000004 1234321012343210 0000000000000000 abcdefabcdefabcd
```

目标现在完全被抹去了：

```
    WeakTarget 0x00007fe17341d270: 200007fe17342a04 300007fe17342811 ffffffffffff0002
```

越来越有趣了。我们看到头部字段在递增和递减一点，让我们看看能不能让它更多：

```
    let target = WeakTarget()
    let targetDump = dumperFunc(target)
    do {
        print(targetDump())
        weak var a = target
        print(targetDump())
        weak var b = target
        print(targetDump())
        weak var c = target
        print(targetDump())
        weak var d = target
        print(targetDump())
        weak var e = target
        print(targetDump())

        var f = target
        print(targetDump())
        var g = target
        print(targetDump())
        var h = target
        print(targetDump())
        var i = target
        print(targetDump())
        var j = target
        print(targetDump())
        var k = target
        print(targetDump())
    }
    print(targetDump())
```

这会打印：

```
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000200000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000400000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000600000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000800000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000a00000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c00000004 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c00000008 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c0000000c 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c00000010 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c00000014 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c00000018 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000c0000001c 0123456789abcdef
    WeakTarget 0x00007fd883205df0: 00000001093a4840 0000000200000004 0123456789abcdef
```

我们可以看到，这个头字段中的第一个数字每增加一个新的弱引用就增加 `2`。第二个数字每增加一个新的强引用就增加 `4`。

回顾一下，我们目前所看到的是：

- 弱指针在内存中看起来像普通指针。
- 当弱目标的 `deinit` 运行时，目标*没有*被释放，弱指针*没有*被归零。
- 当弱指针在目标的 `deinit` 运行后被访问时，它在访问时被归零，弱目标被释放。
- 弱目标包含一个用于弱引用的引用计数，与强引用计数分开。

**Swift 代码**  
既然 Swift 是开源的，我们现在可以将这个观察到的行为与源代码关联起来了。

Swift 标准库使用位于 [stdlib/public/SwiftShims/HeapObject.h](https://github.com/apple/swift/blob/swift-2.2-SNAPSHOT-2015-12-01-b/stdlib/public/SwiftShims/HeapObject.h#L33) 中的 `HeapObject` 类型来表示在堆上分配的对象。它看起来像：

```
    struct HeapObject {
    /// 这始终是一个指向元数据对象的有效指针。
    struct HeapMetadata const *metadata;

    SWIFT_HEAPOBJECT_NON_OBJC_MEMBERS;
    // FIXME：在 32 位平台上分配两个字的元数据

    #ifdef __cplusplus
    HeapObject() = default;

    // Initialize a HeapObject header as appropriate for a newly-allocated object.
    constexpr HeapObject(HeapMetadata const *newMetadata) 
        : metadata(newMetadata)
        , refCount(StrongRefCount::Initialized)
        , weakRefCount(WeakRefCount::Initialized)
    { }
    #endif
    };
```

`metadata` 字段是 Swift 中相当于 Objective-C 中 `isa` 字段的东西，事实上它们是兼容的。然后是一个宏中定义的 `NON_OBJC_MEMBERS`：

```
    #define SWIFT_HEAPOBJECT_NON_OBJC_MEMBERS       \
      StrongRefCount refCount;                      \
      WeakRefCount weakRefCount
```

看看那个！这就是我们的两个引用计数。

（额外问题：为什么在这里强计数在前面，而在上面的转储中弱计数在前面？）

引用计数由位于 [stdlib/public/runtime/HeapObject.cpp](https://github.com/apple/swift/blob/swift-2.2-SNAPSHOT-2015-12-01-b/stdlib/public/runtime/HeapObject.cpp) 中的一堆函数管理。例如，这里是 `swift_retain`：

```
    void swift::swift_retain(HeapObject *object) {
    SWIFT_RETAIN();
        _swift_retain(object);
    }
    static void _swift_retain_(HeapObject *object) {
        _swift_retain_inlined(object);
    }
    auto swift::_swift_retain = _swift_retain_;
```

这里有一堆间接调用，但它最终会调用头文件中的这个内联函数：

```
    static inline void _swift_retain_inlined(HeapObject *object) {
      if (object) {
        object->refCount.increment();
      }
    }
```

正如你所料，它增加了引用计数。这是 `increment` 的实现：

```
    void increment() {
      __atomic_fetch_add(&refCount, RC_ONE, __ATOMIC_RELAXED);
    }
```

`RC_ONE` 来自一个 `enum`：

```
    enum : uint32_t {
      RC_PINNED_FLAG = 0x1,
      RC_DEALLOCATING_FLAG = 0x2,

      RC_FLAGS_COUNT = 2,
      RC_FLAGS_MASK = 3,
      RC_COUNT_MASK = ~RC_FLAGS_MASK,

      RC_ONE = RC_FLAGS_MASK + 1
    };
```

我们可以看到为什么每次新的强引用计数增加 `4`。该字段的前两个位用于 flags。回顾转储，我们可以看到这些 flags 在起作用。这里是一个弱目标在最后一个强引用消失前后：

```
    WeakTarget 0x00007fe17341d270: 000000010faa63e0 0000000400000004 0123456789abcdef
    Weak target deinit
    WeakTarget 0x00007fe17341d270: 000000010faa63e0 0000000200000002 0123456789abcdef
```

该字段从 `4`（表示引用计数为 1，没有 flags）变为 `2`（表示引用计数为零并设置了 `RC_DEALLOCATING_FLAG`）。这个 `deinit` 之后的对象被置于某种 `DEALLOCATING` 中间状态。

（顺便问一下，`RC_PINNED_FLAG` 是干什么的？我浏览了整个代码库，除了知道它表示“pinned object”之外，无法弄清楚更多内容，这一点从名字上已经很清楚了。如果你弄清楚了或者有一个合理的猜测，请发表评论。）

我们趁现在看一下弱引用计数的实现。它有同样类型的 `enum`：

```
    enum : uint32_t {
      // 这里并没有真正意义上的 flag。
      // 使 weak RC_ONE == strong RC_ONE 可节省
      // arm64 上分配时的一条指令。
      RC_UNUSED_FLAG = 1,

      RC_FLAGS_COUNT = 1,
      RC_FLAGS_MASK = 1,
      RC_COUNT_MASK = ~RC_FLAGS_MASK,

      RC_ONE = RC_FLAGS_MASK + 1
    };
```

这就是 `2` 的来源：为一个目前未使用的 flag 预留了空间。奇怪的是，这段代码中的注释似乎不正确，因为这里的 `RC_ONE` 等于 `2`，而强引用的 `RC_ONE` 等于 `4`。我猜它们曾经相等，然后被更改了，而注释没有更新。这恰恰表明注释是无用的，你不应该写注释。

这一切如何与加载弱引用相关联？这由 [一个名为 `swift_weakLoadStrong` 的函数](https://github.com/apple/swift/blob/swift-2.2-SNAPSHOT-2015-12-01-b/stdlib/public/runtime/HeapObject.cpp#L636) 处理：

```
    HeapObject *swift::swift_weakLoadStrong(WeakReference *ref) {
      auto object = ref->Value;
      if (object == nullptr) return nullptr;
      if (object->refCount.isDeallocating()) {
        swift_weakRelease(object);
        ref->Value = nullptr;
        return nullptr;
      }
      return swift_tryRetain(object);
    }
```

从这里可以看出惰性归零的工作原理。当加载一个弱引用时，如果目标正在 deallocating，就将引用归零。否则，尝试保留目标并返回它。再深入一点，我们可以看到 `swift_weakRelease` 如果这是最后一个引用，如何释放对象的内存：

```
    void swift::swift_weakRelease(HeapObject *object) {
      if (!object) return;

      if (object->weakRefCount.decrementShouldDeallocate()) {
        // 只有类对象可以被弱保留（weak-retained）和弱释放（weak-released）。
        auto metadata = object->metadata;
        assert(metadata->isClassObject());
        auto classMetadata = static_cast<const ClassMetadata*>(metadata);
        assert(classMetadata->isTypeMetadata());
        swift_slowDealloc(object, classMetadata->getInstanceSize(),
                          classMetadata->getInstanceAlignMask());
      }
    }
```

（注意：如果你在仓库中查看代码，在大多数情况下命名已更改为使用“unowned”而不是“weak”。上述命名在撰写本文时是最新快照的情况，但开发仍在继续。你可以查看 2.2 快照时的仓库以看到像我这里的代码，或者获取最新的代码，但要注意命名的变化，以及可能的实现变化。）

**整合在一起**  
我们现在从头到尾都看到了。Swift 弱引用实际工作方式的高级视图是什么？

1. 弱引用只是指向目标对象的指针。
2. 弱引用*不是*像 Objective-C 中那样单独跟踪的。
3. 相反，每个 Swift 对象在其强引用计数旁边都有一个弱引用计数。
4. Swift 将对象的去初始化（deinitialization）与对象的内存释放（deallocation）解耦。一个对象可以被去初始化，释放其外部资源，而不释放对象本身占用的内存。
5. 当一个 Swift 对象的强引用计数达到零，而弱计数仍然大于零时，该对象会被去初始化但不会被释放。
6. 这意味着指向已释放（deallocated）对象的弱指针*仍然是有效的指针*，可以解引用而不会崩溃或加载垃圾数据。它们只是指向处于僵尸（zombie）状态的对象。
7. 当加载一个弱引用时，运行时会检查目标的状态。如果目标是僵尸，那么它将弱引用归零，递减弱引用计数，并返回 `nil`。
8. 当指向僵尸对象的所有弱引用都被归零后，僵尸就被释放了。

与 Objective-C 的方法相比，这种设计有一些有趣的结果：

- 没有在任何地方维护弱引用列表。这简化了代码并提高了性能。
- 不存在一个线程上归零弱引用和另一个线程上加载该弱引用之间的竞态条件。这意味着加载弱引用和销毁弱引用对象可以在不获取锁的情况下完成。这提高了性能。
- 指向一个对象的弱引用会导致该对象的内存即使在没有任何强引用时仍然保持分配状态，直到所有弱引用被加载或丢弃。这会暂时增加内存使用量。请注意，影响很小，因为虽然目标对象的内存仍被分配，但只是实例本身的内存。所有外部资源（包括 `Array` 或 `Dictionary` 属性的存储）在最后一个强引用消失时都被释放。弱引用可以导致单个实例保持分配状态，但不会导致整个对象树。
- 需要额外的内存来在每个对象上存储弱引用计数。在实践中，在 64 位系统上，这似乎是无关紧要的。头部字段希望占用整数个指针大小的块，而强引用计数和弱引用计数共享一个。如果没有弱引用计数，强引用计数将独自占用全部 64 位。也有可能通过使用[非指针 `isa`](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) 将强引用移动到 `isa` 中，但我不确定这有多重要，也不确定从长远来看会如何发展。对于 32 位系统，看起来弱引用计数使对象大小增加了四个字节。然而，32 位的重要性正在逐日减弱。
- 因为访问弱指针非常廉价，可以使用相同的机制来实现 `unowned` 的可靠语义。在底层，`unowned` 的工作方式与 `weak` 完全相同，不同之处在于如果目标消失，它不会返回 `nil`，而是大声失败。在 Objective-C 中，`__unsafe_unretained` 被实现为一个原始指针，如果你延迟访问它，行为是未定义的，因为它应该是快的，而加载弱指针有点慢。

**结论**  
Swift 的弱指针采用了一种有趣的方法，提供了正确性、速度和低内存开销。通过跟踪每个对象的弱引用计数，并将对象的去初始化与内存释放解耦，弱引用可以既安全又快速地解决。标准库源代码的可用性让我们能够确切地看到源代码层面发生了什么，而不是像我们经常做的那样在反汇编和内存转储中摸索。当然，正如你上面看到的，完全打破这种习惯很难。

今天就到这里。下次再来获取更多好东西。那可能是几周后，因为有假期介入，但我打算在此之前争取写一篇短文章。无论如何，请继续提出主题建议。Friday Q&A 由读者的想法驱动，所以如果你有一个想看到被涵盖的主题，[请告诉我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在出售整本整本的书！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-12-11-swift-weak-references.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
