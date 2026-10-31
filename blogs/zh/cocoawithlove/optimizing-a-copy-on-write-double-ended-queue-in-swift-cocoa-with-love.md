---
title: '优化 Swift 中的写时复制双端队列 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/09/22/deque.html'
original_language: en
published: 2016-09-22
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:ed20d3af7671c32c'
translated: true
---

> 原文：[Optimizing a copy-on-write double-ended queue in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/09/22/deque.html)　·　Cocoa with Love (Matt Gallagher)

我在 Swift 里实现了一个双端队列类型（deque），以满足某个程序里的特定需求。算法本身并不特别有趣，我只会简短讨论。

相反，我会把重点放在：在 Swift 中实现写时复制（copy-on-write）类型所面临的挑战，以及如何优化代码，以满足我的核心目标——在用作先进先出（FIFO）队列、队列长度约 20 时，至少与 `Array` 一样快。

事实证明，这是一项棘手的优化任务，问题出在用于访问写时复制缓冲区的那些函数上。跟我一起看看如何优化一个 Swift 写时复制集合。

## 引言

Swift 标准库内置的容器类型并不多。直到 Swift 1.2 才引入基本的 `Set` 类型。虽然有不少实用存储类型，例如 `CollectionOfOne`，但总体而言，Swift 作为通用集合类型只提供了 `Array`、`Dictionary` 和 `Set`。

FIFO 队列常用的数据结构是双端队列或 `Deque` 类型，但 Swift 缺少这种类型，也没有其他特别适合用作 FIFO 队列的类型。

Foundation 库里也找不到双端队列，但 `CFArray`/`NSMutableArray` 通过在类队列操作下退化成二叉堆弥补了这一不足。这让你可以把 `NSMutableArray` 当作双端队列来用。一百万年以前（2005 年），[Ridiculous Fish 博客](http://ridiculousfish.com/blog/) 在一篇标题煞费苦心的文章「[Array](http://ridiculousfish.com/blog/posts/array.html)」里写过这件事。若你以前没读过，很值得一读。不过，`NSMutableArray` 中的元素需要堆分配，容器本身也不是写时复制——在 Swift 里这两者都不理想，所以我不想用这个选项。

有一个[现成的、常用的 `Deque` 实现](https://github.com/lorentey/Deque)，看起来扎实且维护良好。不过，我主要关心长度 0 到 20、初始容量为零的队列；在这些条件下，我发现该实现比 `Array` 更慢。我选择不用它，因为我想更好地聚焦这种小队列、小内存占用的用例。

我也可以尝试给 C++ 的 `std::deque` 接一个 Swift 写时复制包装，但最终也没选这条路——虽然以后仍想试试，因为我好奇用 C++ 存 Swift 数据会涉及什么（我假定 C++ 基本上只会充当字节级存储）。

最终，我发现必须自己写这个类型。我想满足以下目标：

1. 写时复制
2. 在加入第一个元素之前不做堆分配
3. 存储自动增长与缩小（缩小到最小容量）
4. 先 push 10 个元素再按 FIFO 全部 pop 时，与 `Array` 一样快（或更快）；50 个时明显更快
5. 实现全部 `RandomAccessCollection`、`RangeReplaceableCollection`、`ExpressibleByArrayLiteral` 和 `CustomDebugStringConvertible`

由于这是最容易实现的双端队列类型，我将实现「环形缓冲区」风格的双端队列——首元素允许相对存储前端有一个「偏移」，一端不断 pop、另一端不断 push 时，队列中已初始化的值会在存储内偏移，直到在末端绕回。

![Figure 1: a ring-buffer showing the indices of four initialized elements in a storage of capacity six](https://www.cocoawithlove.com/assets/blog/deque1.svg)

一个环形缓冲区，容量为六的存储中显示四个已初始化元素的下标

若只向双端队列末尾追加元素，它会表现得像标准数组。差异出现在你从前端移除元素时。

![Figure 2: the valid indices after removing the first three elements and appending three more](https://www.cocoawithlove.com/assets/blog/deque2.svg)

移除前三个元素并再追加三个之后的有效下标

若从 `Array` 前端移除元素，它会移动各值，使下标 `0` 位于缓冲区开头。相比之下，环形缓冲区允许下标 `0` 的元素在缓冲区内有偏移——在上一张图里，下标 `0` 的元素在缓冲区起点加 3 处。代价是存储可能不连续——在上一张图里，下标 `3` 的元素已绕回到缓冲区开头。

这通常不是双端队列的最优做法（那会涉及更复杂的 split-buffer 或堆存储），但我们看看效果如何。

## Swift 中的写时复制

在 Swift 中，惯用的集合类型通常是「写时复制」。这意味着把集合赋给新变量只会增加对原对象的引用计数。之后若尝试变更一个被多重引用的集合，被变更的引用会把自身复制到唯一位置，并变更这份唯一而非共享的版本。

这就是 `Array`、`Dictionary` 和 `Set` 的行为方式。

要做到这一点，集合的底层存储必须是引用计数的 class 类型。为避免多余分配（一次给引用计数 class，一次给原始存储缓冲区），我们使用 `ManagedBuffer<Header, Element>.create` 在单次分配中同时分配实例（`ManagedBuffer<Header, Element>` 的子类）和原始存储缓冲区。

再加上 `isKnownUniquelyReferenced` 函数（测试任意 class 类型是单引用还是多引用），我们就有了所需的全部工具。

## Deque 设计概览

使用 `ManagedBuffer<Header, Element>` 的 `Deque` 类型粗略描述如下：

```swift
public struct Deque<T>: RandomAccessCollection, RangeReplaceableCollection,
   ExpressibleByArrayLiteral, CustomDebugStringConvertible {
   public typealias Index = Int
   public typealias Indices = CountableRange<Int>
   public typealias Element = T

   var buffer: ManagedBuffer<DequeHeader, T>? = nil
   
   public init()
   public init(arrayLiteral: T...)
   public var debugDescription: String
   public subscript(_ at: Index) -> T
   public var startIndex: Index
   public var endIndex: Index
   
   public mutating func replaceSubrange<C>(_ subrange: Range<Int>, with newElements: C)
      where C: Collection, C.Iterator.Element == T {
      if isKnownUniquelyReferenced(&buffer) && /* values fit in existing storage */ {
         // Mutate in place
      } else {
         // Use the `create` method on ManagedBuffer
      }
   }
}

struct DequeHeader {
   var offset: Int
   var count: Int
   var capacity: Int
}
```

这就是全部必需的方法、属性和 typealias。你可以从 `Collection` 协议免费得到不少东西，最终都经由 `subscript` 或 `replaceSubrange` 函数。若 `Index` 不是 `Int` 会难得多，但幸好这里不是这种情况。

## 在未初始化缓冲区中安全存储值

第一个棘手障碍是：在不安全缓冲区中安全地维护实例生命周期。

在典型的 Swift 编程中，严格强制的初始化、引用计数和清理让我们可以忽略实例生命周期的大多数方面。使用不安全缓冲区则不是典型的 Swift 编程。缓冲区分配时是「未初始化」的（处于未知状态）。若我们像下面这样正常地把值赋进缓冲区：

```swift
buffer.withUnsafeMutablePointerToElements { pointer in
   pointer[index] = newValue
}
```

Swift 的自动引用计数会在把 `newValue` 赋到该位置之前，尝试自动释放 `pointer[index]` 处的对象。这是个问题：未初始化时，该位置可能是垃圾数据，尝试释放其内容可能导致 EXC_BAD_ACCESS 或其他崩溃或异常行为。

要正确处理不安全缓冲区，我们必须手动完成缓冲区内任何实例位置的建立与拆除。这意味着第一次把值复制进缓冲区时，必须使用 `initialize`：

```swift
buffer.withUnsafeMutablePointerToElements { pointer in
   pointer.advanced(by: index).initialize(to: newValue)
}
```

而在把值从一个不安全缓冲区位置移到另一个时：

```swift
oldBuffer.withUnsafeMutablePointerToElements { oldPointer in
   newBuffer.withUnsafeMutablePointerToElements { newPointer in
      newPointer.advanced(by: newIndex).moveInitialize(from: oldPointer.advanced(by:
         oldIndex), count: moveCount)
   }
}
```

用完之后，需要清理这些位置：

```swift
buffer.withUnsafeMutablePointerToElements { pointer in
   pointer.advanced(by: offset).deinitialize(count: valueCount)
}
```

用完值后需要 deinitialize，一般意味着我们要在 `deinit` 方法里执行 `deinitialize`——以便在 `Deque` 自身最终被释放时执行。在 `deinit` 里做自定义工作意味着我们*不能*只依赖默认的 `ManagedBuffer` 类；它会对 `Header` 调用 `deinitialize`，但对 `Element` 缓冲区什么也不做。至少，我们需要子类化 `ManagedBuffer`，并在 `deinit` 时对仍留在缓冲区中的任何值做 `deinitialize`。

## 一份事先准备好的实现

我根据目前讨论的信息，先把整个 `Deque` 实现好了。实现有点繁琐，但并不难。

虽非必需，我还是包含了下列函数的优化版本：

- `append(_:)`
- `insert(_:, at:)`
- `remove(at:)`

以改善常见操作的性能。

实现还包含运行时指定的 `minimumCapacity`，使队列能动态增长与缩小，但不会缩小到最小容量以下（默认值为零；回落到零容量会导致整个 `buffer` 对象被释放）。

由于我用来衡量成败的关键指标是：小队列场景下相对 `Array` 如何，我将用下列测试评估性能：

```swift
let outerCount = 100_000
let innerCount = 20
var accumulator = 0
for _ in 1...outerCount {
   var deque = Deque<Int>()
   for i in 1...innerCount {
      deque.append(i)
      accumulator ^= (deque.last ?? 0)
   }
   for _ in 1...innerCount {
      accumulator ^= (deque.first ?? 0)
      deque.remove(at: 0)
   }
}
XCTAssert(accumulator == 0)
```

该测试用例在新队列末尾依次追加 20 个元素，再从前端依次移除。该过程重复 100000 次。

我会与 `Array` 比较。两个测试唯一的区别是：`var deque = Deque<Int>` 这一行在 `Array` 版本中会变成 `var deque = Array<Int>`。

| 测试用例 | 耗时（秒） |
|---|---|
| 初始 `Deque` 实现 | 3.898 |
| `Array` | 0.130 |

大约比 `Array` 慢 40 倍。这不好。问题出在哪？

## 问题 1：需要特化

第一个难点是：相对第三方代码，标准库在「作弊」。

我的 `Deque` 实现被编译进单独模块，因此没有得到泛型特化；Swift 标准库总是被当作与同一模块的一部分来编译——因此总能利用泛型特化。

我的 `Deque` 实现所在的单独模块阻止了对 `Deque` 类型和函数的特化，导致下列进入缓冲区的访问器：

```swift
buffer.withUnsafeMutablePointerToElements { header, elements in
   elements.advanced(by: header.pointee.offset).initialize(to: newValue)
}
```

使用带堆分配开销的捕获闭包，而这占用了大部分执行时间。

与单独模块相关的性能问题是[我以前讨论过的问题](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html)。解决方案类似：确保 `Deque` 与测试用例作为同一模块的一部分链接，并确保启用「Whole program optimization」。

| 测试用例 | 耗时（秒） |
|---|---|
| 同一模块内编译的初始 `Deque` | 0.179 |
| `Array` | 0.135 |

好了，好了一个数量级以上，但仍然不够好。现在问题又是什么？

## 问题 2：deinit 闭包开销

事实证明，尽管已完全特化，Swift 仍在 `DequeBuffer.deinit` 函数中浪费大约三分之一的时间分配闭包——当它调用 `withUnsafeMutablePointers` 以获取 header 和 elements 的指针时。我不太理解其中原因，但无法绕过问题、按预期方式使用 `ManagedBuffer`。

因此我实现了自己的函数来计算 header 和 elements 的指针，并在 `deinit` 函数中绕过 `withUnsafeMutablePointers`。

```swift
private static var headerOffset: Int {
   return Int(roundUp(UInt(MemoryLayout<HeapObject>.size),
      toAlignment: MemoryLayout<DequeHeader>.alignment))
}
   
private static var elementOffset: Int {
   return Int(roundUp(UInt(headerOffset) + UInt(MemoryLayout<DequeHeader>.size),
      toAlignment: MemoryLayout<T>.alignment))
}
   
private var bodyPtr: UnsafeMutablePointer<T> {
   return Unmanaged<DequeBuffer<T>>.passUnretained(self).toOpaque()
      .advanced(by: DequeBuffer<T>.elementOffset).assumingMemoryBound(to: T.self)
}
   
private var headerPtr: UnsafeMutablePointer<DequeHeader> {
   return Unmanaged<DequeBuffer<T>>.passUnretained(self).toOpaque()
      .advanced(by: DequeBuffer<T>.headerOffset).assumingMemoryBound(to: DequeHeader.self)
}
```

可以看到，我真正做的只是把 `self` 指针推进到 `ManagedBuffer` 所分配缓冲区中 `Header` 和 `Elements` 的正确位置——这也是 `ManagedBuffer` 会做的同样工作。

这些函数及其在 `deinit` 中的用法，在代码里用 `#if true` 块包起来，以便容易禁用。

|  | 耗时（秒） |
|---|---|
| 最终 `Deque` 实现 | 0.062 |
| `Array` | 0.135 |

我们终于在这个测试用例里比 Swift 内置的 `Array` 类型更快了。

## 这不冒险吗？

我把指针偏移进一个并非我分配的缓冲区中间，并假定缓冲区内的布局将来不会改变。

这不是丑陋的 hack 吗？这不是违背我在「[A new era for Cocoa with Love](https://www.cocoawithlove.com/blog/2016/01/25/a-new-era-for-cocoa-with-love.html)」里为 Cocoa with Love 宣称的「可维护应用」目标吗？

是，而且是。

令人失望，但现实是：若用 `ManagedBuffer` 分配底层存储来实现 `Deque`，我们就被迫在两种方案间选择——「优化」版能给出合理性能，或「未优化」版慢到直到队列长度达到 80 到 200（取决于初始容量）才真正能与 `Array` 竞争。

坦率说，「未优化」版的性能问题极大限制了其用处，几乎无用。若你对内存安全偏执，那不如直接用 `Array`，或写一个不用 `ManagedBufferPointer` 的 `Deque`。

我选择走优化版，并用在构造 `DequeBuffer` 时的 `assert` 语句防范任何潜在不安全：确认访问器返回的值与 `ManagedBuffer` 的结果相同。这应能防范布局改变、指针失效。

## 与 std::deque 比较

击败 Swift 的 `Array` 算不上巨大成就：它本来就不是为这种场景设计成高性能的。让我们改为与专门用作 FIFO 队列的东西比较。

下面是 `Deque` 与 libc++ 的 `std::deque` 的比较：

|  | 耗时（秒） |
|---|---|
| 最终 `Deque` 实现 | 0.062 |
| `std::deque` | 0.043 |

哎哟。怎么又被打败了？

虽然 `std::deque` 的「split-buffer」比我们的「circular-buffer」实现更高效（扩展容量时不需要把已有内容搬到新分配的缓冲区），但这并不是这里问题的根源。

问题根源在于：这些小测试完全由内存分配决定，而 `std::deque` 只需 2 次分配就能超过容量 20（两次各 16 个元素的分配），我的实现则需要 3 次分配（在容量 5、12、26 时重新分配）。

若在构造我的 `Deque` 时把最小容量设为 `20`，数字就会反过来：

|  | 耗时（秒） |
|---|---|
| 最小容量为 20 的最终 `Deque` | 0.025 |
| `std::deque` | 0.045 |

这样操纵条件很难说公平，但要点是：两者具有竞争力，加减只在分配模式上，这就够了。

## 用法

> 包含此 `Deque` 实现的项目在 github 上：[mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils)。

[CwlDeque.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlDeque.swift?ts=3) 文件完全自包含，若只需要这个，可以直接复制该文件。否则，[项目的 ReadMe.md](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) 有关于克隆整个仓库、并把其产出的 framework 加到自己项目中的详细说明。

**注意：** CwlUtils 项目在其自身模块内编译 CwlDeque.swift。如本文所述，最佳性能需要把 CwlDeque.swift 文件拿到你自己的模块里编译。

## 结论

这件事一半有趣，一半令人沮丧。

在 Swift 中实现一个基本的写时复制、环形缓冲区 deque 很有趣。需要手动调用 initialize 和 deinitialize 感觉像回到 C 时代的愉快怀旧，但一旦意识到必须这样做，就很直接。

沮丧来自我试图理解性能问题的原因。虽然我对 Swift 编译器内部略知一二，但优化这类代码对我来说仍主要是黑盒练习：看性能分析结果，对问题区域胡乱尝试，指望情况有所改善。我不太清楚为什么 `ManagedBuffer.withUnsafeMutablePointers` 会在 `deinit` 中导致不想要的分配，也不知道是否本可以换一种方式修复。我确实知道：本不该需要我做任何事。

最终方案性能出色，但我对不安全的指针算术并不满意。有了双重检查指针算术的 `assert` 语句，它应能保持正确；但归根结底，我期待 Swift 解决根本原因后，可以禁用这段代码。

### 展望…

在未来的文章中，我将分享这个 Deque 类型的主要用例。**来自未来的编辑**…[它被用来在 CwlSignal 中排队消息](https://www.cocoawithlove.com/blog/cwlsignal.html)）。
