---
title: 'Swift 运行时：堆对象'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/'
original_language: en
published: 2020-08-31
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b83291eb996539da'
translated: true
---

> 原文：[The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/)

[Swift 运行时：类型布局](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/) »

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=swift)

[Swift 运行时：类型布局](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift) »

[Swift 运行时：类型布局](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift-runtime) »

## [The Swift Runtime: Heap Objects](#)

欢迎来到 [Swift runtime](https://belkadan.com/blog/tags/swift-runtime) 系列的第一篇。这个系列的目标是过一遍 Swift runtime 的各项功能，参考的是我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) 中学到的东西。今天我们从 class 实例和闭包的共同基础讲起：堆对象（heap object）。

要注意的是，这不会是一份对整个 Swift runtime 的详尽指南。我的项目里有好几个部分没有实现，而且我有种预感，光是这个系列写下来就已经够长了。

前面提到过，我尽量把这个精简版 runtime 用 Swift 实现，虽然为此不得不用上一些没有文档记录的 Swift 特性。这些文章里我会展示我 runtime 代码的片段，完整内容可以去 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)里看。

### 基础

不同 class 的实例里存的数据各不相同，但它们都以同样的两个隐藏字段开头：

| 堆对象头部（Heap object header） |
|---|
| isa 指针 |
| 引用计数 |

isa 指针主要用来做几件事：调用可重写的方法，以及确保 class 的析构函数被正确调用。^[1](#fn:isa) 引用计数字段在真正的 Swift runtime 里相当复杂（至少得处理普通的 retain，以及对 `unowned` 和 `weak` 的追踪），但在我的项目里我把它简化成只追踪普通的强引用。

一个对象的生命周期从分配开始：

```
@_cdecl("swift_allocObject")
func swift_allocObject(
  rawMetadata: UnsafeRawPointer,
  requiredSize: Int,
  requiredAlignmentMask: Int
) -> UnsafeMutableRawPointer {
  let result = UnsafeMutableRawPointer(NewPtrClear(requiredSize)!)
  result.storeBytes(of: rawMetadata, as: UnsafeRawPointer.self)
  return result
}
```

相当简单。它用操作系统的分配器（这里是 `NewPtrClear`）分配一个对象，然后把 _metadata_ 指针（也就是 class）放进第一个字段。我选择让引用计数字段采用一种_偏移（biased）_表示法，让初始值「0」代表引用计数为「1」。这个 0 是 `NewPtrClear` 隐式给出的，所以甚至都不用显式设置。

（你也能看出这不是 `swift_allocObject` 的完美实现：如果所需的对齐要求比 `NewPtrClear` 提供的更严格，调用这段代码的地方很容易崩溃。）

_在这个系列里你会经常看到 `@_cdecl`。真正的 Swift runtime 函数都是用 C++ 定义的，为了简单起见它们都用未经名字改编（unmangled）的名字——函数的名字就是符号的名字。这个 runtime 也是在 Swift 有自己的调用约定之前就已经开始存在了，所以存在时间最久的那些函数用的是 C 的调用约定。`@_cdecl` 目前还不是一个受支持的属性，不过[你可以帮忙推动它成为一个](https://forums.swift.org/t/best-way-to-call-a-swift-function-from-c/9829/6)！_

一旦对象存活，它就会被 retain

```
@_cdecl("swift_retain")
func swift_retain(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) -> UnsafeMutableRawPointer? {
  guard let rawObjectRef = maybeObjectRef else { return maybeObjectRef }
  IncrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  return rawObjectRef
}
```

以及被 release（并最终被销毁）。

```
@_cdecl("swift_release")
func swift_release(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) {
  guard let rawObjectRef = maybeObjectRef else { return }
  let oldRefCount = DecrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  guard oldRefCount == 0 else { return }

  let metadata = rawObjectRef.load(as: UnsafePointer<TypeMetadata>.self)
  let destroyPtr = UnsafeRawPointer(metadata) - 8
  swift_invokeDestroyer(destroyPtr, rawObjectRef)
}
```

我把这两个放在一起展示，是为了让人看清它们互为对偶：两者都先检查 `nil`，然后原子地增减对象的第二个字段。同样，这跟真正的 runtime 所做的相比是简化过的，但因为 retain 和 release 对象这件事可能发生得非常频繁，就算是真正的 runtime 在常见情形下也力求做到这么快。

Swift 版本的自动引用计数的工作方式是：当最后一个引用消失时，对象的销毁会同步发生。所以 `swift_retain` 在更新引用计数之后就结束了，而 `swift_release` 得检查是否应该销毁对象。如果旧的引用计数表示值是 0（记住，这是一种偏移表示法），那这次 release 针对的就是最后一个引用，该销毁对象了。如前所述，这个信息存在相对于 class metadata 的位置，而它的地址是通过加载对象的第一个字段得到的。^[2](#fn:negative)

析构函数的调用约定跟普通 Swift 函数略有不同，所以在 Swift 里没法写出一个 100% 正确的调用。取而代之，我用了一个 C++ 辅助函数 `swift_invokeDestroyer` 来正确地调用它，这个辅助函数得用一个跟 Swift 兼容的 Clang 版本编译。（我就不在这里展示了。）

析构函数的职责是：如果 class 有 deinitializer 就调用它，然后释放对象。这也有对应的 runtime 函数：

```
@_cdecl("swift_deallocClassInstance")
func swift_deallocClassInstance(
  _ object: UnsafeMutableRawPointer,
  allocatedSize: Int,
  allocatedAlignmentMask: Int
) {
  DisposePtr(object.assumingMemoryBound(to: CChar.self))
}
```

这只是调用了操作系统的内存释放函数，用 `assumingMemoryBound(to:)` 让类型和 C 声明对上。你会注意到 `allocatedSize` 和 `allocatedAlignmentMask` 在这里没被用到；事实证明它们**不可信**。传进来的值匹配的是这个 class 的默认大小和对齐，但如果这个 class 有「尾部分配（tail allocation）」（就像 [ManagedBuffer](https://developer.apple.com/documentation/swift/managedbuffer)，或者 Array 的底层存储那样），那这个大小甚至对齐都可能是错的！还好在我的实现里根本用不上它们。

### 闭包

我希望前面对 class 是怎么运作的讲清楚了，那闭包呢？其实闭包_也_有两部分：

| 闭包值（Closure value） |
|---|
| 函数指针 |
| 对捕获内容的引用 |

闭包的第一个字段是一个带有特殊调用约定的函数指针：它接收闭包的参数，外加一个用来访问任何被捕获绑定（参数、变量或常量，或者捕获列表里显式指定的绑定）的额外参数。这个额外参数是从第二个字段里加载出来的，你可以把它想成一种存着捕获内容的「匿名 class」。传递一个闭包就意味着 retain 和 release 这个「捕获内容对象」，它会在引用计数归零时像其他任何对象一样被销毁。如果这个闭包没有任何捕获，这个字段就会是 `nil`。^[3](#fn:blocks)

### Core Foundation

在 Swift 出现之前，Objective-C 是给 Apple 系统写程序的主要方式。但如果你只用纯 C，还有一个更底层的面向对象层可以用，叫做 _Core Foundation_。这是一套跟 Objective-C 兼容、但对外呈现纯 C 接口的对象系统，直到今天它依然存在（虽然现在 Core Foundation 的大部分也是用 Objective-C 实现的了）。因为有些 API 仍然在用 Core Foundation，Swift 第一个发布版本就内置了用自动引用计数追踪 CF 对象的支持（Swift 和 Objective-C 对象也是一样）。

不过 Core Foundation 还有另一个用途：[它是 Mac OS 9 的 _Toolbox_ API 和 Mac OS X（现在的「macOS」）的 _Cocoa_ API 之间的桥梁](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-a-mac-osnbsp9)。这也就意味着它在 Mac OS 9 上同样存在且可用，_而_这也意味着我自己的 runtime 项目也得处理 CF 对象。CF 对象未必跟 Swift 对象有一样的布局，所以 `swift_retain` 和 `swift_release` 不能直接戳字节来增减引用计数。不过……

> 我在进一步探索时的一个便利发现：Classic 下的 CF 类型第一个字仍然为 isa 指针保留着，只是从来没被设过值。这意味着我可以通过第一个字是不是 null 来区分 Swift 对象和 CF 对象！
>
> — Jordan Rose (@UINT_MIN) [April 9, 2020](https://twitter.com/UINT_MIN/status/1248154940318482432?ref_src=twsrc%5Etfw)

所以我实际版本的 `swift_retain` 是这样的：

```
@_cdecl("swift_retain")
func swift_retain(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) -> UnsafeMutableRawPointer? {
  guard let rawObjectRef = maybeObjectRef else { return maybeObjectRef }
  // NEW
  guard isNativeSwiftObject(rawObjectRef) else {
    return _CFRetain(rawObjectRef)
  }
  IncrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  return rawObjectRef
}
```

（注意我得为 `CFRetain` 提供一个 C 包装函数，因为通常 Swift 不允许你直接调用它，以免搞乱 ARC。）

而为了同时处理 Classic 和 [Carbon](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-a-mac-osnbsp9) 这两种环境，`isNativeSwiftObject` 是这样写的：

```
private func isNativeSwiftObject(_ objectRef: UnsafeRawPointer) -> Bool {
  let lowestValidPointer = 0x1000

  // Some CF types do not have isa pointers.
  let isaField = objectRef.load(as: UInt.self)
  guard isaField >= lowestValidPointer else {
    return false
  }
  let type = UnsafeRawPointer(bitPattern: isaField)!

  // ObjC classes have an isa pointer too (like objects),
  // while the types of Swift heap allocations do not
  // (except on modern Apple platforms,
  // where Swift classes are valid ObjC classes).
  let possibleMetaclassPointer = type.load(as: UInt.self)
  return possibleMetaclassPointer < lowestValidPointer
}
```

那个 `0x1000` 是从哪来的？^[4](#fn:cf) 在包括 Mac OS X 在内的许多现代操作系统上，「地址空间」低端的一段会被保留下来，用来捕获那些表现为空指针解引用的 bug。Mac OS 9 没有_完全_一样的保证，但幸运的是它把内存的最低那部分留给了操作系统的各种用途，所以我们可以放心地认为低于 `0x1000` 的值不会被应用程序内存使用。所以我们最终要检查的情况是这样的：

| 对象的第一个字段 | 类型的第一个字段 | 分类 |
|---|---|---|
| `0..<­0x1000` | （不适用） | CF（非 ObjC） |
| `0x1000...` | `0..<­0x1000` | **Swift** |
| `0x1000...` | `0x1000...` | CF（ObjC） |

这套分类让我们能决定是用我们刚实现的引用计数，还是交给 CFRetain 去处理，这样一来，ARC 就能在 Mac OS 9 上、乃至 Mac OS X 的 Carbon 环境下对 CF 对象生效了。

### ……以及其余部分

还有几个跟堆对象相关的函数，不过都不算特别精彩。`swift_isUniquely­Referenced_­nonNull_native` 就是简单检查引用计数字段是不是 0。`swift_init­StackObject` 跟 `swift_alloc­ClassInstance` 类似，只是内存已经分配好了。还有几个别的，但唯一另一个有意思的是 `swift_init­StaticObject`：

```
@_cdecl("swift_initStaticObject")
func swift_initStaticObject(
  _ metadata: UnsafeRawPointer,
  _ object: UnsafeMutableRawPointer
) -> UnsafeMutableRawPointer {
  let token = (object - MemoryLayout<UInt32>.size).assumingMemoryBound(to: UInt32.self)
  swift_once(token) {
    object.storeBytes(of: metadata, as: UnsafeRawPointer.self)
  }
  return object
}
```

这是针对编译器发现一个类型为 class 实例的全局 `let` 时所做的优化。如果编译器能在编译期保证这个 class 的大小，这个对象的数据就可以放在静态内存里而不是堆上。^[5](#fn:immortal) 这种情况下编译器得把这个全局变量的初始化「折叠」进来，所以它会调用 `swift_once` 这个辅助函数，确保这个对象只被初始化一次。而且 `swift_init­StaticObject` 并没有为「token」传一个单独的参数；它跟编译器之间有一份约定：紧挨在对象数据前面必定会有一个 token。

`swift_once` 是怎么工作的？真正的实现会调用平台上已经存在的东西来干这个脏活，要么是 [`dispatch_once`](https://developer.apple.com/documentation/dispatch/1447167-dispatch_once_f)，要么是 [`std::call_once`](https://en.cppreference.com/w/cpp/thread/call_once)。但这两个在 Mac OS 9 上都用不了，所以我得自己写一个：

```
func swift_once(
  _ token: UnsafeMutablePointer<UInt32>,
  _ action: () -> Void
) {
  if CompareAndSwap(0, 1, token) {
    action()
    token.pointee = 2
  } else {
    while token.pointee != 2 {
      MPYield()
    }
  }
}

@_cdecl("swift_once")
func swift_once(
  _ flag: UnsafeMutablePointer<UInt32>,
  _ action: @convention(c) (UnsafeMutableRawPointer) -> Void,
  _ context: UnsafeMutableRawPointer
) {
  swift_once { action(context) }
}
```

这里是一个小小的状态机：如果 `token` 是 0，表示什么都还没发生；如果是 1，表示初始化正在进行；如果是 2，表示已经完成。这段代码用 `CompareAndSwap` 确保只有一个线程真正去执行这个 action，如果失败了，就等到初始化完成为止，期间视需要让其他线程运行。^[6](#fn:threading)（「MP」代表「multiprocessing」，是实现了抢占式线程的 Classic Mac OS 库的名字。）

第二个重载版本带有 C 兼容接口，供编译器在普通、未经优化的全局初始化里使用。

### 小结

呼！我们过了六个函数，篇幅还是不小。而且我不得不说，这其实是最简单的一篇。runtime 剩下的部分有更多结构化的数据，所以之后的文章里我们会去看一些实打实的类型，以及一些复杂得多的操作。[下一篇：struct 和 tuple 的布局](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/)。

1. 「isa」指针之所以叫这个名字，是因为它指向这个对象「是一个（is a(n)）」实例的那个 class，比如「`superview` is a `View`」。[↩︎](#fnref:isa)
2. 如果你好奇为什么「destroyer」放在一个_负_偏移处，那是因为 Swift 的 class 被设计成跟 Objective-C 兼容，而 Objective-C 里_没有_一个显式指向函数、用来反初始化并释放 class 实例的指针；它只是调用一个叫 `dealloc` 的方法。Swift 的 destroyer 本可以放在 Objective-C 字段_之后_，但对其他种类的引用计数堆对象（比如闭包捕获）来说那就浪费了。它也可以放在 type metadata_紧前面_、偏移 `-4` 的地方（Mac OS 9 上指针是 32 位的），但那个位置已经被用来放_value witness table_ 了，我们会在后面的文章里聊到它。[↩︎](#fnref:negative)
3. 注意这跟 Clang / Objective-C 的做法——[block](https://clang.llvm.org/docs/BlockLanguageSpec.html)——是不一样的。一个 block 被实现成一个带 isa 指针的普通对象，函数指针被当作跟所有捕获内容并列的一个字段。这意味着它可以像一个普通的对象引用那样被传来传去，retain 和 release 都不需要什么特殊规则……但这也意味着，什么都不捕获的 block 的最低开销，要比 Swift 里的闭包更大。什么都是权衡！[↩︎](#fnref:blocks)
4. 这个_想法_来自 Core Foundation 项目本身：[CFInternal.h](https://opensource.apple.com/source/CF/CF-368.28/Base.subproj/CFInternal.h.auto.html) 里有个叫 `CF_IS_OBJC` 的宏，用来测试一个对象是原生的 _Core Foundation_ 类型还是「桥接」过来的 Objective-C 类型。这个宏同样用 `0x1000`（实际上是 `0xFFF`）作为边界值，不过它只需要处理 Mac OS X 就够了。[↩︎](#fnref:cf)
5. 真正的 runtime 还会给这个对象一个特殊的引用计数，表示它是不朽的（immortal）。我在自己的实现里没有费心去做这个。[↩︎](#fnref:immortal)
6. 严格来说，这么做仍然违反了 Swift 正式的[内存访问规则](https://github.com/apple/swift-evolution/blob/master/proposals/0282-atomics.md)，因为它是在另一个线程可能正在修改这个指针的过程中去读取它。Swift 目前没有办法告诉_编译器_在这里做一次「安全」的读取。我们只是运气好：编译器为单线程模式生成的代码，在多线程模式下碰巧也能用。[↩︎](#fnref:threading)

本文发布于 [2020](https://belkadan.com/blog/2020) 年 [8](https://belkadan.com/blog/2020/08) 月 31 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)
