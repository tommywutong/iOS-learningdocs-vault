---
title: 'Friday Q&A 2014-07-18：探索 Swift 内存布局'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4645cb12ee92d746'
translated: true
---

> 原文：[Friday Q&A 2014-07-18: Exploring Swift Memory Layout](https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html)　·　mikeash.com Friday Q&A

发布于 2014-07-18 13:57 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2014-08-01：探索 Swift 内存布局（第二部分）](https://www.mikeash.com/pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html)  
上一篇文章：[Friday Q&A 2014-07-04：Swift 速度的奥秘](https://www.mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-07-18：探索 Swift 内存布局

作者：[Mike Ash](https://www.mikeash.com/)

**可能会变更**  
Swift 的一切都可能会变更，但像这样的内部实现细节更是如此。了解这些内容很方便，对调试也可能有用，但不要编写依赖它的生产代码，否则后果自负。

这些转储来自为 `x86-64` 编译、在 10.9 上运行的 Swift 代码。除了未来编译器版本可能出现的变化外，在不同的 CPU 架构或操作系统版本上，一切可能都不同。在阅读转储内容时，请注意这是小端架构，所以所有数字都是反向的。

如果你想知道这些数据从何而来，我使用标准运行时 API 读取 Objective-C 运行时结构，并使用 `mach_vm_read_overwrite` 通过递归追踪指针来读取原始内存，这一切都通过一个自定义 Swift 程序完成，我希望能在一篇后续文章中讨论它。

**结构体**  
让我们从一个简单的 `struct` 开始：

```
    struct TestStruct {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb
    }
```

转储一个实例的内容，会显示这样一块普通的内存：

```
    aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

让我们尝试一个包含更复杂内容的结构体：

```
    struct PaddingTestStruct {
        let a: UInt8 = 0xaa
        let b: UInt16 = 0xbbbb
        let c: UInt64 = 0xcccccccccccccccc
    }
```

这会产生：

```
    aaa0bbbbff7f0000 cccccccccccccccc
```

我们可以看到 `b` 和 `c` 都按其大小对齐，中间有一些填充着垃圾数据的填充区域。

让我们尝试添加一些函数：

```
    struct FuncTestStruct {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func dummy1() {}
        func dummy2() {}
        func dummy3() {}
    }
```

这会产生：

```
    aaaaaaaaaaaaaaaa
```

这些函数虽然概念上与结构体相关联，但实际上并没有出现在内存内容中。由于 Swift 中的结构体不允许继承，因此除了变量之外不需要其他任何东西。

我们可以看到 Swift 结构体的行为与 C 结构体非常相似。它们按声明顺序在内存中存储变量，没有任何注解或元数据。尽管 Swift 允许结构体包含函数，但在运行时，这些函数并不与结构体的实例相关联。

**对象**  
让我们检查一个包含实例变量和几个方法的简单类：

```
    class TestClass {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func method1() {}
        func method2() {}
    }
```

实例化该类并转储实例的内容，会产生以下内存转储：

```
    00393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa
```

它看起来类似于 Objective-C 对象，但有 16 字节的元数据，而 Objective-C 只有 8 字节。事实证明，它*是*一个可以使用 `objc/runtime.h` 中的 API 进行检查的 Objective-C 对象。以下是它产生的内容：

```
    Objective-C class _TtC6memory9TestClass:
        Ivar: a 
    Objective-C class SwiftObject:
        Ivar: magic {SwiftObject_s="isa"^v"refCount"q}
        Property: hash TQ,R
        Property: superclass T#,R
        Property: description T@"NSString",R,C
        Property: debugDescription T@"NSString",R,C
        Method: __usesNativeSwiftReferenceCounting B16@0:8
        Method: .cxx_construct @16@0:8
        Method: release v16@0:8
        Method: autorelease @16@0:8
        Method: dealloc v16@0:8
        Method: class @16@0:8
        Method: retain @16@0:8
        Method: isEqual: c24@0:8@16
        Method: hash Q16@0:8
        Method: superclass #16@0:8
        Method: self @16@0:8
        Method: zone ^{_NSZone=}16@0:8
        Method: performSelector: @24@0:8:16
        Method: performSelector:withObject: @32@0:8:16@24
        Method: performSelector:withObject:withObject: @40@0:8:16@24@32
        Method: isProxy c16@0:8
        Method: isKindOfClass: c24@0:8#16
        Method: isMemberOfClass: c24@0:8#16
        Method: conformsToProtocol: c24@0:8@16
        Method: respondsToSelector: c24@0:8:16
        Method: retainCount Q16@0:8
        Method: description @16@0:8
        Method: debugDescription @16@0:8
        Method: doesNotRecognizeSelector: v24@0:8:16
```

关于这一点，有几件有趣的事：

1. `TestClass` 的名称被修饰后，产生了一个 Objective-C 类名，不仅包含 Swift 名称，还包含 Swift 模块（本例中为 "memory"）和其他一些东西。
2. `TestClass` 获得了一个 Objective-C 实例变量，但其方法并未显示出来。该实例变量没有类型注解，只有一个名称。
3. 它的超类是 `SwiftObject`，这是一个新的根类。普通的 Swift 类并不是 `NSObject` 的（直接或间接）子类。`SwiftObject` 确实实现了 `NSObject` 协议，因此它可以在一定程度上扮演 `NSObject` 的角色。
4. `SwiftObject` 包含一个名为 `magic` 的实例变量。很巧妙。
5. `magic` 实际上是一个包含两个成员的 `struct`。第一个是我们熟悉的 `isa`，而第二个是一个名为 `refCount` 的 `long long`。
6. `SwiftObject` 还包含一个名为 `__usesNativeSwiftReferenceCounting` 的方法。这告诉我们存在一种原生 Swift 引用计数。我不确定为什么需要在运行时检查原生 Swift 引用计数，但显然是通过这个方法来实现的。

让我们仔细看看那个 `refCount` 字段。以下是该对象最初的样子，以及被 retain 五次之后的样子：

```
    00393b0701000000 0800000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1000000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1400000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1800000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1c00000001000000 aaaaaaaaaaaaaaaa
```

看起来低两位是保留的，每次 retain 都会将 `refCount` 字段增加 `4`。（请记住，这些是小端数字，所以它们是反向的。）数字更高处的那个 `1` 看起来像是某种标志，但含义未知。

让我们为测试类创建一个子类，看看它会产生什么：

```
    class TestSubclass : TestClass {
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb

        override func method2() {}
        func method3() {}
        func method4() {}
    }
```

内存内容与我们预想的一致：

```
    b0393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

它看起来与 `TestClass` 相同，只是多了一个实例变量和一个不同的 `isa` 指针。Objective-C 端只包含一个实例变量：

```
    Objective-C class _TtC6memory12TestSubclass:
        Ivar: b
```

让我们尝试一个 `NSObject` 的子类：

```
    class TestNSClass: NSObject {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func method1() {}
        func method2() {}
    }
```

该实例包含：

```
    50333b0701000000 0000000000000000 aaaaaaaaaaaaaaaa 0000000000000000
```

看起来它为 `SwiftObject` 中额外的 `magic` 存储预留了空间，但第二块内存没有被使用。使用 Objective-C 运行时检查该类，会发现除了实例变量之外，还有一些实际的方法：

```
    Objective-C class _TtC6memory11TestNSClass:
        Ivar: a 
        Method: method1 v16@0:8
        Method: method2 v16@0:8
        Method: a Q16@0:8
        Method: init @16@0:8
```

实例变量仍然没有类型注解，但方法正如我们预期的那样。两个方法都存在，以及实例变量的 getter 方法和一个 `init` 方法。

让我们为它创建一个子类，看看效果：

```
    class TestNSSubclass : TestNSClass {
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb

        override func method2() {}
        func method3() {}
        func method4() {}
    }
```

这个类的实例包含：

```
    d0333b0701000000 0000000000000000 aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

正如我们预期的那样，它保持了与超类相同的布局，只是在末尾添加了额外的 ivar。Objective-C 类也包含我们预期的东西：一个新的 ivar、新方法的条目，以及被覆盖的 `method2` 的条目：

```
    Objective-C class _TtC6memory14TestNSSubclass:
        Ivar: b 
        Method: method2 v16@0:8
        Method: method3 v16@0:8
        Method: method4 v16@0:8
        Method: b Q16@0:8
        Method: init @16@0:8
```

**类**  
让我们更深入地研究一下实际的类结构。它们是 Objective-C 类，但它们还包含什么？转储 `TestClass` 的原始数据会产生：

```
    c0383b0701000000 2002610701000000 10bac588ff7f0000 0000000000000000 f14a4099e97f0000 1800000007000000 7800000010000000 70223b0701000000 30443a0701000000 d0433a0701000000 e0433a0701000000 50443a0701000000 1000000000000000 0000000000000000 4802610701000000 c0383b0701000000
```

所有这些乱七八糟的是什么东西？我们知道它是个 Objective-C 类，其结构可以在 [Apple 的运行时源码](http://www.opensource.apple.com/source/objc4/objc4-551.1/runtime/objc-runtime-new.h) 中找到：

```
    struct objc_class : objc_object {
        // Class ISA;
        Class superclass;
        cache_t cache;
        uintptr_t data_NEVER_USE;  // class_rw_t * plus custom rr/alloc flags
```

第一块是 `isa`，即该类的类。果然，第一个指针指向了 `TestClass` 的元类：

```
    0x00000001073b38c0: Symbol _TMmC6memory9TestClass
```

接下来是超类：

```
    0x0000000107610220: Symbol OBJC_CLASS_$_SwiftObject ObjC class SwiftObject
```

接着是缓存和 `data_NEVER_USE`，然后还有更多超出基本 Objective-C 类数据的东西。其中一些是神秘的，似乎不指向任何东西，但在类内部偏移量 56（上面第 8 个指针大小的块）处开始有一些有趣的片段：

```
    0x00000001073b2270: Symbol _TMnC6memory9TestClass
    0x00000001073a4430: Symbol _TFC6memory9TestClassg1aVSs6UInt64
    0x00000001073a43d0: Symbol _TFC6memory9TestClass7method1fS0_FT_T_
    0x00000001073a43e0: Symbol _TFC6memory9TestClass7method2fS0_FT_T_
    0x00000001073a4450: Symbol _TFC6memory9TestClasscfMS0_FT_S0_
```

第一个有点神秘，但它看起来像是一个 Swift 级别的元类。Apple 的 `swift-demangle` 工具将它描述为 "nominal type descriptor for `memory.TestClass`"。其他的是方法实现。有 `a` 的 getter、`method1` 和 `method2` 的实现，最后是 init 方法。这大概就是 Swift 代码中用于方法分发的虚函数表。

`TestSubclass` 看起来类似：

```
    70393b0701000000 00393b0701000000 e0e54099e97f0000 0300000002000000 714b4099e97f0000 2000000007000000 9800000010000000 a0223b0701000000 30443a0701000000 d0433a0701000000 c0443a0701000000 50453a0701000000 1000000000000000 30453a0701000000 d0443a0701000000 e0443a0701000000
```

它以 Objective-C 类数据开始，然后包含同样类型的额外内容：

```
    0x00000001073b22a0: Symbol _TMnC6memory12TestSubclass
    0x00000001073a4430: Symbol _TFC6memory9TestClassg1aVSs6UInt64
    0x00000001073a43d0: Symbol _TFC6memory9TestClass7method1fS0_FT_T_
    0x00000001073a44c0: Symbol _TFC6memory12TestSubclass7method2fS0_FT_T_
    0x00000001073a4550: Symbol _TFC6memory12TestSubclasscfMS0_FT_S0_
    0x00000001073a4530: Symbol _TFC6memory12TestSubclassg1bVSs6UInt64
    0x00000001073a44d0: Symbol _TFC6memory12TestSubclass7method3fS0_FT_T_
    0x00000001073a44e0: Symbol _TFC6memory12TestSubclass7method4fS0_FT_T_
```

再次，我们有类型描述符条目，后面跟着虚函数表。它保持相同的布局，并且包含一些相同的条目。我们可以清楚地看到 `method1` 来自 `TestClass`，而 `method2` 被覆盖了。在 `TestSubclass` 中添加的新方法被添加到了末尾。

这说明了虚函数表分发是如何工作的。对于一个 `TestClass` 的实例，查找 `method2` 的槽位会产生 `_TFC6memory9TestClass7method2fS0_FT_T_`，即 `TestClass` 的实现。对于一个 `TestSubclass` 的实例，同一个槽位包含 `_TFC6memory12TestSubclass7method2fS0_FT_T_`，因此一个简单的数组索引操作就足以定位要调用的函数。

`TestNSClass` 和 `TestNSSubclass` 显示出相同的结构，包括虚函数表。尽管它们的方法在 Objective-C 运行时中可用，但它们也同样暴露给了 Swift 的虚函数表分发机制。我不确定在这种情况下虚函数表是否真的会被用到，但这个调查只好留到改日了。

**结论**  
持有协议（protocol）类型的变量会有一些有趣的事情，因为它们可以同时持有对象和结构体。数组和字典的布局也有一些有趣的东西可看。然而，我的篇幅已经太长，时间有限，因此这些只能等到下一篇文章了。到目前为止，我们已经看到结构体和对象的布局基本如我们预期，对象包含一些用于引用计数的额外数据。Swift 类是 Objective-C 类，即使它们不是从 `NSObject` 派生子类也是如此。在这种情况下，它们子类化 `SwiftObject`，这是一个新的根类，遵循 `NSObject` 协议。除了正常的 Objective-C 类结构之外，Swift 类还在类内部内联包含了其所有方法的虚函数表。

今天就到这里，但我们很快会回来，继续探索 Swift 运行时内存结构。

你喜欢这篇文章吗？我正出售整本整本的书呢！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
