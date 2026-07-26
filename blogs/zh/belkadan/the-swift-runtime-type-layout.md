---
title: 'Swift 运行时：类型布局'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/'
original_language: en
published: 2020-09-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e6f5eb87ac6d74a2'
translated: true
---

> 原文：[The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 运行时：堆对象](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/) »

« [Swift 运行时：堆对象](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/?tag=swift)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift) »

« [Swift 运行时：堆对象](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/?tag=swift-runtime)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift-runtime) »

## [The Swift Runtime: Type Layout](#)

欢迎来到 [Swift runtime](https://belkadan.com/blog/tags/swift-runtime) 系列的第二篇。这个系列的目标是过一遍 Swift runtime 的各项功能，参考的是我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) 中学到的东西。这次我们要聊聊 tuple 和 struct 在运行时是怎么排布的。

前面提到过，我尽量把这个精简版 runtime 用 Swift 实现，虽然为此不得不用上一些没有文档记录的 Swift 特性。这些文章里我会展示我 runtime 代码的片段，完整内容可以去 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)里看。

### 类型布局

类型布局（type layout）指的是拿到一个 struct 或 tuple，根据每个字段的_大小_和_对齐_来决定怎么把这些字段排布在内存里。排布完成后，你就知道这个 struct 或 tuple 的总大小和总对齐，以及每个字段的偏移。举个例子，考虑下面这个 struct：

```
struct Product {
  var id: UInt16
  var amountInGrams: Float
  var isOnSale: Bool
}
```

先别管这是不是个_好_ struct；我们只关心怎么把这些字段排布在内存里。最简单的做法当然是把它们一个接一个地放：

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `id` | `amountInGrams` | `isOnSale` |  |  |  |  |

但这样是不合法的，因为 Float 要求 4 字节的_对齐_。（[Red Hat 的这篇文章](https://developers.redhat.com/blog/2016/06/01/how-to-avoid-wasting-megabytes-of-memory-a-few-bytes-at-a-time/)把对齐讲得挺清楚。^[1](#fn:alignment)）把这个考虑进去，我们得到的是这样：

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `id` |  | `amountInGrams` | `isOnSale` |  |  |  |  |  |

这里的算法很简单：对每个字段，从下一个可用偏移出发，向上取整到满足所需的对齐。struct 的大小就是用到的总字节数（这里是 9），对齐就是所有字段里最大的对齐（这里是 4）。但这并不是_唯一_可能的布局算法；比如你也可以把最大的字段排在最前面：

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `amountInGrams` | `id` | `isOnSale` |  |  |  |  |

这样就能把整个 struct 压缩到只用 7 字节，同时仍然遵守对齐规则。

那 Swift 是怎么做的呢？目前它就是做最简单的事：按顺序排布字段，向上取整到对齐边界。（这意味着你其实可以通过精心安排字段顺序来省内存，虽然这大概只有在你有大量该 struct 实例时才用得上。）但除了两种特定情况外，语言并没有正式保证这一点：

- 如果你在一个有[稳定 ABI](https://swift.org/blog/abi-stability-and-apple/) 的平台上（实际上就是 Apple 的各个系统），那么在启用了[库演进（library evolution）](https://swift.org/blog/swift-5-1-released/#module-stability)的 module 里，任何标了 `@frozen` 的公开 struct 都必须采用这种布局，这样一个库和它的客户端才能在布局上达成一致。
- [Tuple 保证采用这种布局。](https://forums.swift.org/t/how-to-define-structures-that-can-be-passed-to-c/23901/4)^[2](#fn:tuple)

实际上，至少截至 Swift 5.2，Swift 里定义的每个 struct 都是这种布局。对我来说改变它是没有意义的，尤其是因为编译器和 runtime 必须在 struct 是怎么排布这件事上达成一致。

### 类型布局……在运行时？

上面展示的「Product」例子是一个可以完全在编译期排布完成的 struct。但这并不总是可能的。考虑这个专门为教学目的设计的 struct：

```
struct Pair<First, Second> {
  var first: First
  var second: Second
}
```

`second` 的偏移是多少？显然这取决于 `First` 的大小，也取决于 `Second` 的对齐。如果 `First` 和 `Second` 的具体类型在编译期未知，那就得靠 runtime 来搞清楚了。^[3](#fn:compiletime) 但事情比这更复杂。考虑这段代码：

```
// A.swift
func makePair<First, Second>(_ first: First, _ second: Second) -> Pair<First, Second> {
  return Pair(first: first, second: second)
}

// B.swift
let pair: Pair<Int, String> = makePair(1, "abc")
print(pair.second)
```

`makePair` 这个函数必须靠 runtime 来给它的 Pair 实例排布布局，但 B.swift 里的调用方是知道所有类型的，而且会直接访问那个字符串。所以不仅 runtime 需要做类型布局，你现在也知道了为什么它必须跟编译器的做法保持一致。

### 上代码！

好吧，不过我得提醒你，这不算特别有意思！

我们先从上面一带而过的算法开始，看看顺序类型布局是怎么做的：

```
var size: UInt = 0
var alignMask: UInt = 0
for field in fieldTypes {
  size.roundUpToAlignMask(field.alignMask)
  size += field.size
  alignMask = max(alignMask, field.alignMask)
}
return (size, alignMask)
```

这里省略了不少细节，但作为起点已经足够了。不过这里已经有一处跟我上面描述的不一样了：我们用的是对齐_掩码（mask）_，而不是对齐本身。这是利用了这样一个事实：Swift 支持的系统上所有对齐都是 2 的幂，这意味着通过掩掉低位就能轻松地把某个值强制对齐。（对于 8/`0b1000` 的对齐，对齐掩码就是 7/`0b0111`。）比较下面这三个函数：

```
extension UInt {
  mutating func roundUpToArbitraryAlignment(_ alignment: UInt) {
    let offset = self % alignment
    if offset > 0 {
      self += alignment &- offset
    }
  }

  mutating func fastRoundUpToArbitraryAlignment(_ alignment: UInt) {
    self += alignment &- 1
    self &-= self % alignment
  }

  mutating func roundUpToAlignMask(_ alignMask: UInt) {
    self += alignMask
    self &= ~alignMask
  }
}
```

第一个是「向上取整到下一个倍数」的简单实现：它检查是否已经到位了，如果没有就「补齐剩下的距离」。第二个是个用来避开 `if` 检查的老技巧：如果原始偏移是 0，加上去的量会被立刻减掉，否则就会把我们推过下一个倍数。

第三个跟第二个想法一样，只是当对齐是 2 的幂时，利用了「减去余数」和「掩掉低位」这两者的等价性。这里我们加上比对齐少 1 的量，而掩码也是比对齐少 1，所以我们存的值本来就该是比对齐少 1。

上面展示的就是基本算法。类型布局的实际实现还顺带算了几个别的东西：这些字段里有没有需要自定义拷贝或销毁逻辑的（标记为 `isNonPOD`，非「plain old data」，借用了 C++ 里的一个类似概念，不过用 C++ 所说的非「[可平凡拷贝（trivially copyable）](https://en.cppreference.com/w/cpp/named_req/TriviallyCopyable)」来类比会更贴切），以及类似地，有没有需要自定义_移动_逻辑的（`isNonBitwiseTakable`）。

遍历完所有字段之后，还会填两个额外的字段：stride（步幅），也就是向上取整到对齐边界的大小；以及这个类型是否能内联存储在 Swift 的不透明对象缓冲区表示里。后者的判断条件很简单——「大小能塞进为三个指针大小、按指针对齐分配的存储空间里，并且仍然允许按位取走（bitwise taking）」——这里就不细讲了；它们基本上只用在 `Any` 和带协议类型的值（既存类型）上。stride 是在计算数组内的偏移时用到的，数组里会把同一类型的若干个值一个接一个地排在内存里。（老实说，我也不确定不预先算出这个会损失多少。）^[4](#fn:stride)

### 运行时表示

编译器和 runtime 不仅要在怎么排布类型上达成一致，_也_要在这份布局怎么表示上达成一致。我们可以把下面这些也看作 struct，不过我用的定义看起来有点奇怪：

```
struct TypeLayout {
  typealias Layout = (
    size: UInt,
    stride: UInt,
    flags: TypeLayoutFlags,
    extraInhabitantCount: UInt32
  )
  var `_`: Layout

  init(_ value: Layout) {
    self._ = value
  }
  
  static var initialLayoutForValueType: TypeLayout {
    return TypeLayout((size: 0, stride: 0, flags: .init(), extraInhabitantCount: 0))
  }
}
```

我这是想干什么？呃，我自己以前也是 Swift 编译器的开发者！我不想比必要的程度更依赖那些没有文档支持的行为，还记得我上面说的：Swift 里 struct 的布局是没有保证的，但 tuple 的布局是有保证的。所以这个系列里你会看到的所有 runtime 数据结构，都会用一个包在 struct 里的 tuple，来确保布局跟编译器生成的保持一致。

EDIT：我想说明一下，我认为这是个 hack；在 Swift 里获得具有特定布局的类型，「受支持」的方式是在 C 头文件里定义它们。这个项目里我选择用 tuple 的做法，是因为 (a) 我想尽量把 runtime 的更多部分留在 Swift 里，(b) 我用的是一个固定版本的编译器，所以它不会在我不知情的情况下发生变化。

那为什么变量名要用下划线呢？呃，反正在使用处看到它也不会有什么意义，所以我想要一个小小的、相对容易被忽略的东西。下划线通常是一个表示「忽略」的关键字，但加上反引号转义之后它就变成了一个合法的成员名。我不确定我会在一个公开项目里推荐这么做，但对于这个只有我一个人在写的项目来说，这似乎是个合理的用法。

在那个 TypeLayout struct 里，你会认出 `size` 和 `stride`，但 `alignMask` 不见了，还有一个我们完全没提过的字段：`extraInhabitantCount`。这是怎么回事？呃，对齐值不会_那么_大，所以 Swift 只为对齐掩码留了 8 位。UInt32 字段里剩下的 24 位用来放标志位：

```
struct TypeLayoutFlags {
  var rawValue: UInt32 = 0
  
  var alignMask: UInt {
    get { UInt(self.rawValue & 0xFF) }
    set {
      self.rawValue &= ~0xFF
      self.rawValue |= UInt32(newValue)
    }
  }

  var isNonPOD: Bool {
    get { rawValue.extractBit(at: 16) }
    set { rawValue.updateBit(at: 16, to: newValue) }
  }

  var isNonInline: Bool {
    get { rawValue.extractBit(at: 17) }
    set { rawValue.updateBit(at: 17, to: newValue) }
  }

  var isNonBitwiseTakable: Bool {
    get { rawValue.extractBit(at: 20) }
    set { rawValue.updateBit(at: 20, to: newValue) }
  }
}
```

我省略了几个我们还没聊过的标志位，也有一些目前还没用到任何用途。`extractBit(at:)` 和 `updateBit(at:to:)` 是顾名思义的辅助函数；我就不在这里展示了。

至于「额外可居留值数量（extra inhabitant count）」，指的是那些永远不会成为该类型合法值的内存表示的数量，也就是说 runtime 可以用它们来表示 Optional 里的 `nil`。等我们聊到 enum 的时候会再多说一些。现在，我们先聊聊 Swift 计算 struct 和 tuple 的额外可居留值数量所用的策略：挑出计数最高的那个元素，然后就用它。^[5](#fn:loop)

```
extraInhabitantCount = fieldTypes.lazy.map { $0.extraInhabitantCount }.max() ?? 0
```

### 汇总起来

下面是 tuple 类型布局的最终版本：

```
private func performBasicLayout<TypeLayouts>(
  _ layout: inout TypeLayout,
  _ fieldTypes: TypeLayouts,
  setOffset: (_ fieldIndex: Int, _ offset: UInt32) -> Void
) where TypeLayouts: Collection, TypeLayouts.Element == TypeLayout {
  for (i, field) in fieldTypes.enumerated() {
    layout._.size.roundUpToAlignMask(field._.flags.alignMask)
    setOffset(i, UInt32(layout._.size))

    layout._.size += field._.size

    layout._.flags.alignMask = max(layout._.flags.alignMask, field._.flags.alignMask)
    if field._.flags.isNonPOD {
      layout._.flags.isNonPOD = true
    }
    if field._.flags.isNonBitwiseTakable {
      layout._.flags.isNonBitwiseTakable = true
    }
  }

  layout.computeStride()
  layout.computeInline()
}

@_silgen_name("swift_getTupleTypeLayout")
func swift_getTupleTypeLayout(
  _ result: UnsafeMutablePointer<TypeLayout>,
  _ elementOffsets: UnsafeMutablePointer<UInt32>?,
  _ flags: TupleTypeFlags,
  _ rawElements: UnsafePointer<UnsafePointer<TypeLayout>>
) {
  result[] = TypeLayout.initialLayoutForValueType
  let fieldTypes = UnsafeBufferPointer(start: rawElements, count: flags.numElements)
  performBasicLayout(&result[], fieldTypes.lazy.map { $0[] }) {
    elementOffsets?[$0] = $1
  }
  result[]._.extraInhabitantCount = fieldTypes.lazy.map { $0[]._.extraInhabitantCount }.max() ?? 0
}

struct TupleTypeFlags {
  var rawValue: UInt

  var numElements: Int {
    Int(rawValue & 0xFFFF)
  }
}
```

你可以看到前面那种保证布局的 struct 用的下划线，还有一个我个人挺喜欢的、给指针加的扩展：

```
extension UnsafePointer {
  subscript() -> Pointee {
    self.pointee
  }
}
```

这里还有另一个没有文档记录的属性，`@_silgen_name`。跟上次的 `@_cdecl` 一样，`@_silgen_name` 允许给一个用 Swift 定义的函数指定一个未经名字改编的名字；跟 `@_cdecl` 不同的是，它不会改变调用约定。这也就意味着 `swift_get­Tuple­TypeLayout` 是后来才加进去的，是在我们已经决定给 runtime 函数用 Swift 调用约定之后。（你可以在 [RuntimeFunctions.def](https://github.com/apple/swift/blob/master/include/swift/Runtime/RuntimeFunctions.def) 里看到所有 runtime 函数的签名。）

### struct 呢？

对于 tuple，编译器会尽量_只_去请求布局，如果可能的话就不保留关于这个类型的其余信息。但 struct 不是这样工作的——一个运行时才能确定布局的 struct 会算一次布局，然后存在这个类型的_运行时 metadata_ 里，哪怕你只是访问一个字段也是如此。这个函数跟 `swift_get­Tuple­TypeLayout` 看起来几乎一样，只是开头和结尾多了一点东西：

```
@_cdecl("swift_initStructMetadata")
func swift_initStructMetadata(
  _ structType: TypeErasedMutablePointer<StructMetadata>,
  _ rawLayoutFlags: UInt,
  _ numFields: UInt,
  _ rawFieldTypes: TypeErasedPointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt32>
) {
  var layout = TypeLayout.initialLayoutForValueType
  let fieldTypes = UnsafeBufferPointer(
    start: rawFieldTypes.assumingMemoryBound(to: UnsafePointer<TypeLayout>.self),
    count: Int(numFields))

  performBasicLayout(&layout, fieldTypes.lazy.map { $0[] }) {
    // If the offsets are already correct, it might be immutable memory.
    if fieldOffsets[$0] != $1 { fieldOffsets[$0] = $1 }
  }

  layout._.extraInhabitantCount = fieldTypes.lazy.map { $0[]._.extraInhabitantCount }.max() ?? 0
  
  let layoutFlags = StructLayoutFlags(rawValue: rawLayoutFlags)
  let vwtable = structType.assumingMemoryBound(to: StructMetadata.self).getOrCreateMutableVWTableForInit(layoutFlags)
  vwtable[]._.typeLayout = layout
}
```

跟 `swift_get­Tuple­TypeLayout` 不同，这个函数用的是 `@_cdecl`，这意味着它的声明里必须使用 C 兼容的类型。这也就是说所有这些用 Swift 定义的 metadata struct 都不能直接用了，所以我编了一个不起眼的类型别名，来写清楚一个指针_原本打算_指向什么。

```
typealias TypeErasedMutablePointer<Pointee> = UnsafeMutableRawPointer
```

编译器完全不会去检查它，但对我自己而言算是一点文档。（我不太喜欢这个名字，但也想不出更好的。）

这里另一个新东西是这个「vwtable」，以及暗示存在的一个叫 StructMetadata 的类型。我们后面会详细聊到这些，但现在你只需要知道：每个类型都有一个指向 _value witness table_ 的指针，它定义了这个类型上的基本操作，而这张表里也包含了类型布局信息。`getOrCreate­Mutable­VWTable­ForInit(_:)` 只是判断这张表能不能就地修改；如果不能，它会分配一张新表，用原表的副本来初始化。

```
extension UnsafeMutablePointer where Pointee == StructMetadata {
  var valueWitnessTable: UnsafePointer<ValueWitnessTable> {
    get {
      UnsafeRawPointer(self).load(
        fromByteOffset: -MemoryLayout<UnsafePointer<ValueWitnessTable>>.size,
        as: UnsafePointer<ValueWitnessTable>.self)
    }
    nonmutating set {
      UnsafeMutableRawPointer(self).storeBytes(
        of: newValue,
        toByteOffset: -MemoryLayout<UnsafePointer<ValueWitnessTable>>.size,
        as: UnsafePointer<ValueWitnessTable>.self)
    }
  }

  func getOrCreateMutableVWTableForInit(
    _ flags: StructLayoutFlags
  ) -> UnsafeMutablePointer<ValueWitnessTable> {
    if flags.isValueWitnessTableMutable {
      return UnsafeMutablePointer<ValueWitnessTable>(mutating: self.valueWitnessTable)
    }
    let newVWT = UnsafeMutablePointer<ValueWitnessTable>.allocate(capacity: 1)
    newVWT.initialize(to: self.valueWitnessTable[])
    self.valueWitnessTable = UnsafePointer<ValueWitnessTable>(newVWT)
    return newVWT
  }
}
```

这还不是初始化一个带具体参数的泛型 struct 所需要的全部内容，但已经是个不错的开始。剩下的部分我们以后再讲。

### 小结

现在你知道 Swift runtime 是怎么把一个 struct 的字段或者一个 tuple 的元素排布到内存里的了——不只是算法本身，还有实际的实现。[下次我们要开始看类型的完整运行时表示：_type metadata_。](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)

1. 感谢 [@matt_dz](https://twitter.com/matt_dz/status/1273749196911206400) 的推荐。[↩︎](#fnref:alignment)
2. John McCall 在 2017 年的原始措辞给 tuple 在存进 struct 时被拆开留了余地；我觉得到现在这已经非常不可能了，因为有了像 [`MemoryLayout.offset(of:)`](https://developer.apple.com/documentation/swift/memorylayout/2996397-offset) 这样的特性，它可以让你查询 struct 里任何存储属性（包括 tuple）的偏移。不过出于优化目的，局部的 tuple 变量仍然可能被拆开。

  在我第一次发布这篇文章之后，[Lily Ballard](https://twitter.com/LilyInTech) 还推动我去问 Swift 核心团队，John 当时的说法是否真的算是对未来的一个承诺。[讨论仍在进行中。](https://forums.swift.org/t/guarantee-in-memory-tuple-layout-or-dont/40122) [↩︎](#fnref:tuple)
3. 在 C++ 和 Rust 这类语言里，泛型是作为编译的一部分、用具体类型_实例化（instantiated）_或者说_单态化（monomorphized）_的；如果一个泛型函数调用另一个泛型函数，顶层的具体类型会一路传递下去。这给分开编译的库带来了一个有意思的限制：除非把函数体暴露给客户端，否则一个库没法提供泛型函数或类型。另一方面，Swift 是少数支持这种运行时泛型的静态类型语言之一，因为这需要额外的间接层和更复杂的 runtime。[↩︎](#fnref:compiletime)
4. C 里给 struct 用的最常见算法跟 Swift 的布局算法非常像，只不过会在 struct_末尾_加上填充，确保它的大小是对齐的整数倍，这意味着大小和 stride 永远是一样的。这简化了不少事情，但也意味着当这个 struct 被嵌入一个更大的 struct 时会浪费空间——对齐要求更小的额外字段没法被塞进那段填充里。[↩︎](#fnref:stride)
5. 为什么这不是我们上面讲的那个循环的一部分？布局算法在好几个不同的地方都会用到，而在不同场景下对额外可居留值数量的需求是不一样的。[↩︎](#fnref:loop)

本文发布于 [2020](https://belkadan.com/blog/2020) 年 [9](https://belkadan.com/blog/2020/09) 月 07 日，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)
