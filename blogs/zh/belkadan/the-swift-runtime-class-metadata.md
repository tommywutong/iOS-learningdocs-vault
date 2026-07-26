---
title: 'Swift 运行时：类元数据'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/'
original_language: en
published: 2020-09-29
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ddc2ffc7f0d896d4'
translated: true
---

> 原文：[The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 运行时：唯一化缓存](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)

[Swift 运行时：类元数据初始化](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/) »

« [Swift 运行时：唯一化缓存](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift)

[Swift 运行时：类元数据初始化](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift) »

« [Swift 运行时：唯一化缓存](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift-runtime)

[Swift 运行时：类元数据初始化](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift-runtime) »

## [Swift 运行时：类元数据](#)

欢迎来到 [Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)系列的第五篇。这个系列的目标是过一遍 Swift 运行时的各项功能，把我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)里学到的东西当作参照。上次我们讲完了 struct 和 enum 的元数据是怎么搭起来的；这次我们要聊聊 class。

正如之前提到的，我用 Swift 尽可能实现了这个精简版运行时，不过为此不得不用上几个没有文档记录的 Swift 特性。整个系列里我会展示我的运行时代码片段，完整代码可以在 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)里看到。

### Struct 和 class

Swift 跟它的一些同代语言（Rust、Go、Kotlin）不一样的地方之一，就是它明确区分了 struct 和 class。最大的区别在于，struct 实例是按*值*传递的，而 class 实例是按*引用*传递的。^[1](#fn:semantics) 但 struct 和 class 都可以有存储属性、声明方法、遵守协议。struct 和 class 之间只有几个重要的不同点：^[2](#fn:diagram)

- 因为 class 实例在做赋值或调用函数时不会被隐式拷贝，所以它们可以有*反初始化方法（deinitializer）*来清理资源。（[只能移动的值类型（move-only value type）以后也能做到这一点](https://github.com/apple/swift/blob/master/docs/OwnershipManifesto.md)。）
- 因为 class 实例只在一个地方分配、并且终生待在那里，它在内存里的地址就可以用来唯一[标识](https://developer.apple.com/documentation/swift/objectidentifier)它，至少在它存活期间是这样。（原始指针也是这样工作的。）
- 因为 class 实例会[随身带着自己的类型](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)，它们不需要用到泛型就能表现出*多态行为*。实际上这意味着「你可以从另一个 class 继承，并且重写它的方法」。（协议类型的值也是这样工作的。）

你可以看到，靠只能移动的类型、指针，以及协议类型的值（用 Rust 的写法大概是 `Arc<dyn View>`）这些零件，其实也能拼出很像 class 的东西，但 Swift 还是觉得把这些行为捆在一起更有用，尤其是因为它从一开始就得支持跟 Objective-C 互操作。

在实现层面，由这个设计（以及语言里其他一些实现上的选择）会带来不少差异。我们来看看。

### 类元数据的结构

还记得 struct 元数据有多简单吗？

| Struct 元数据 |
|---|
| value witness table |
| kind* |
| type descriptor |

* 记住，value witness table 的指针存在这张表*之前*；「kind」字段是「第一个」值，也就是偏移量为 0 处的值。

没错，class 就没这么简单了。

| Class 元数据 |
|---|
| destroyer |
| value witness table |
| kind* |
| superclass |
| _ObjC method cache_ |
| _ObjC method cache_ |
| _ObjC 兼容数据_ |
| flags |
| 实例「address point」 |
| 实例大小 |
| 实例对齐掩码 + 一些预留位 |
| class 大小 |
| class「address point」 |
| type descriptor |
| ivar destroyer |
| （方法与泛型参数） |
| （方法与泛型参数） |
| … |

* 「kind」依然在偏移量 0 处。

这里的东西可真不少！这些*到底*是什么？为什么我们不能像之前那样，把有意思的东西都塞回 type descriptor 里？为什么这些都得要？*深吸一口气* 好吧，我们一步步来看：

- **destroyer** 会调用反初始化方法，然后释放这个 class 的内存。我们在[本系列第一篇](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)里聊过它。
- 我们*依然*还没深入讲过 **value witness table**，这次也还是不讲，但每个 class 用的都是同一张表，因为所有用来操作 class 的「值」都只是引用，而且所有对象引用的行为都一样。^[3](#fn:objc)
- 每份元数据都有一个 **kind**。正如[本系列第一篇](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)提到过的，class 的 kind 值被精心挑选过，不会和任何合法地址重叠……只不过在现代 Apple 平台上，为了兼容 Objective-C，这个字段被换成了指向一个「[metaclass](http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)」对象的指针。
- class 可以有**超类**！如果没有，这个字段就是 `nil`。
- 接下来三个字段是为了兼容 Objective-C。Swift 本身不用它们做任何事，实际上[在非 Apple 平台上，它们已经在上游被移除了](https://github.com/apple/swift/pull/31811)，就在我为这个项目切出自己的分支后没几周。（[多谢 Alejandro 提供的线索](https://twitter.com/aalonso128/status/1310992586543443969)。）
- **flags** 嘛，就是一堆标志位，不过我的运行时用不上它们存的那些信息。
- 实例的「**address point**」指定了在这个 class 被实例化时，是否要在对象的元数据指针*之前*分配一些字段。为什么会想这么做？嗯，这样一来，即便你子类化了一个 class，你依然能引用「第一个『负偏移』字段」，而不需要知道超类到底有多大。

  Swift 目前没有实现这个（也就是说这个字段永远是 0），所以我在自己的运行时里没管它，但*理论上*真正的编译器和运行时是可以开始用它的。
- 实例的**大小**和**对齐方式**必须存在元数据里，因为 value witness table 里的类型布局，是一个*引用*的布局，而不是 class 实例本身的布局。既然对齐方式不可能特别大，这个字段里有一些位就被留给运行时存任意数据。对我们来说这些位是没用到的。
- 类元数据本身也有一个**大小**和 **address point**，跟实例的这两项差不多。不过这里数的不是存储属性，而是需要存在 class 里的方法和泛型参数。

  这个字段其实用不太上，因为你很少需要知道类元数据*本身*占多少内存。它是被 Objective-C 运行时用来做动态子类化的，因为动态子类同样得指望 Swift 的方法和泛型参数在那儿；反射（reflection）想读取*整份*元数据时也会用到它。这两者跟我的运行时都没什么关系。
- 我们在讲[struct 元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#representing-types-at-run-time)的时候聊过 **type descriptor**：它存着如何实例化泛型 class 的信息，也为泛型和非泛型 class 存了额外的元数据。
- **ivar destroyer** 用于一种特殊情况：一个可失败的初始化方法在调用 `super.init` *之前*就失败了，但*之后*子类已经完成了初始化。这种情况下，子类的字段已经初始化过了，但跑完整的反初始化方法并不安全。（我其实没实现对这种情况的支持——它要用到运行时函数 `swift_dealloc­Partial­ClassInstance`——不过它并不复杂。）
- 最后是方法和泛型参数：先是根类的泛型参数（如果有的话），然后是方法，接着是第一层子类的泛型参数，然后是方法，依此类推。这些方法组成一张 vtable（虚函数表，即 *virtual dispatch table*），所以重写方法的做法，就是把方法列表里「超类那一段」里的某个方法指针替换掉。

  （我的同事 [David Smith](https://twitter.com/Catfish_Man) 曾评论说，挺奇怪的是 Swift 把方法调用做得这么高效——在类元数据里做一次偏移量查找——结果转头又推崇一些跟 class 层级结构没什么关系的写法。让方法派发跟 C++ 一样快，是一个限制，挡住了一些[有意思的想法](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)。）

老实说，这趟类元数据之旅，可能比跟 class 相关的那些运行时函数本身还更有信息量，不过我们还是会把它们讲一遍。

## 分配泛型类元数据

class、struct 和 enum 都用同一个入口来访问可能被缓存的元数据，那就是 [`swift_get­GenericMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)。但真正要*分配*这份元数据的时候，class 的需求就不一样了。它一开始遵循一个相当眼熟的模式：

```
@_cdecl("swift_allocateGenericClassMetadata")
func swift_allocateGenericClassMetadata(
  _ rawDescription: TypeErasedPointer<ClassDescriptor>,
  _ arguments: UnsafePointer<UnsafeRawPointer>,
  _ rawPattern: TypeErasedPointer<GenericValueMetadataPattern>
) -> TypeErasedPointer<ClassMetadata> {
  let description = rawDescription.assumingMemoryBound(to: ClassDescriptor.self)
  let pattern = rawPattern.assumingMemoryBound(to: GenericClassMetadataPattern.self)

  let allocationBounds = description[].metadataBounds
```

我们首先要知道的是元数据的「边界（bounds）」，在这里指的是它的负向和正向范围。这会告诉我们需要分配的总大小，以及最终要返回的那个「零偏移」指针应该放在哪儿。我把这部分拆成了 ClassDescriptor 上的一个辅助属性：

```
var metadataBounds: ClassMetadataBounds {
  let immediateMembersOffsetInWords =
    self._.metadataPositiveSizeInWords &- self._.numImmediateMembers
  let immediateMembersOffset =
    Int(immediateMembersOffsetInWords) &* MemoryLayout<Int>.size
  return ClassMetadataBounds(
    negativeSizeInWords: self._.metadataNegativeSizeInWords,
    positiveSizeInWords: self._.metadataPositiveSizeInWords,
    immediateMembersOffset: immediateMembersOffset)
}
```

我们一会儿再回来讲 `immediateMembersOffset`。现在，这些信息已经足够让我们真正调用分配器了。

```
let bytes = swift_slowAlloc(
  size: allocationBounds.totalSizeInBytes,
  alignMask: MemoryLayout<UnsafeRawPointer>.alignment &- 1)
let rawMetadata = (bytes + allocationBounds.addressPointOffsetInBytes)
let metadata = rawMetadata.bindMemory(to: ClassMetadata.self, capacity: 1)
```

插一句：等等，要是超类的大小变了呢？这些值不就失效了吗？确实会，但在 Swift 里，这种改动本来就要求客户端代码重新编译，除非基础库是带着[库演进（library evolution）支持](https://swift.org/blog/library-evolution/)构建的（或者除非这个 class 的某个祖先来自 Objective-C）。我这个跑在 Classic 上的 Swift 运行时不支持这个，所以我干脆把那部分逻辑全都省掉了。

现在我们分配好了元数据，接下来先填「负偏移」字段：

```
rawMetadata.storeBytes(
  of: pattern.destroyFn[],
  toByteOffset: -2 &* MemoryLayout<Int>.size,
  as: Optional<UnsafeRawPointer>.self)
rawMetadata.storeBytes(
  of: swift_getObjectValueWitnessTable(),
  toByteOffset: -1 &* MemoryLayout<Int>.size,
  as: UnsafePointer<ValueWitnessTable>.self)
```

然后是普通字段：

```
metadata[]._.base.rawKind = TypeMetadata.Kind.class.rawValue
metadata[]._.superclass = nil
// This is an "is Swift" bit that isn't really needed on non-ObjC platforms.
metadata[]._.objcCompatibleData = 1
metadata[]._.flags = pattern[]._.classFlags

// Layout, filled in later.
metadata[]._.instanceAddressPoint = 0
metadata[]._.instanceSize = 0
metadata[]._.instanceAlignMask = 0

metadata[]._.classSize = UInt32(bounds.totalSizeInBytes)
metadata[]._.classAddressPoint = UInt32(bounds.addressPointOffsetInBytes)

metadata[]._.description = description
metadata[]._.ivarDestroyer = pattern.ivarDestroyer?[]
```

如你所见，这里其实没多少事要做！大部分信息要么是从我们手头已有的东西直接拷过来的，要么就是先塞个占位值，之后再填。真的就这么点事吗？

其实还不完全是。原来我漏掉了之前的两样东西：[struct 元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields)里那个「额外数据」pattern，还有一个专门用于 class「直属（immediate）」成员的额外数据 pattern——也就是那些可以被重写、但自身并不是重写别人的成员。前者确实会给 class 的分配大小加量；后者则已经包含在里面了。所以 `swift_allocate­Generic­ClassMetadata` 真正的第一部分是这样的：

```
let bounds = description[].metadataBounds
var allocationBounds = bounds
if let extraDataPattern = pattern.extraDataPattern {
  allocationBounds.positiveSizeInWords &+=
    UInt32(extraDataPattern[]._.offsetInWords) &+
    UInt32(extraDataPattern[]._.sizeInWords)
}
```

有了元数据之后，我们需要用这些 pattern 来初始化它：

```
if let extraDataPattern = pattern.extraDataPattern {
  // Note: not using allocationBounds here
  let extraDataOffset =
    Int(bounds.positiveSizeInWords) &* MemoryLayout<Int>.size
  (rawMetadata + extraDataOffset).initialize(from: extraDataPattern)
}

let immediateMembers = rawMetadata + bounds.immediateMembersOffset
memset(
  immediateMembers,
  0,
  Int(description[]._.numImmediateMembers) &* MemoryLayout<Int>.size)
if let immediateMembersPattern = pattern.immediateMembersPattern {
  immediateMembers.initialize(from: immediateMembersPattern)
}
```

好了，*现在*一切都初始化好了。最后还有一件事要做，跟 struct 一样：把泛型参数存进元数据里。

```
installGenericArguments(
  in: rawMetadata.assumingMemoryBound(to: TypeMetadata.self),
  at: bounds.immediateMembersOffset,
  description: rawDescription.assumingMemoryBound(to: TypeContextDescriptor.self),
  from: arguments)
return UnsafeRawPointer(rawMetadata)
```

我们[在本系列第三篇](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields)里见过 `installGenericArguments(in‍:at‍:description‍:from‍:)`。这里没什么变化，除了泛型参数的偏移量是基于这个特定 class 的边界来算的。正如前面提到的，它就放在「直属成员」这一段的开头。

到这一步，我们的 class 算是分配好了……但要说它已经能用了，那还差得远。

## 小结

这篇文章已经有点长了，所以我打算先写到这儿，虽然我们其实只讲完了一个函数。[下次我们会看类元数据初始化的另一半](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/)，主要是关于怎么从超类那儿把数据填进来。

1. 这跟「值语义」和「引用语义」并*不完全*是一回事，那本身就是一个足够单独开一场讲座的话题。事实上，[Alexis Gallagher 在 2016 年就做过这么一场讲座](https://academy.realm.io/posts/swift-gallagher-value-semantics/)，有兴趣的话可以去看看。[↩︎](#fnref:semantics)
2. 我之前为这个画过一张[探索性的图](https://twitter.com/UINT_MIN/status/902355871404965889)。[↩︎](#fnref:diagram)
3. 当 Swift 得跟 Objective-C 互操作的时候，这一点就不完全成立了！因为[并不是所有 Objective-C 对象都表示成指针](https://mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)，运行时对它们能做的事情，规则会稍有不同。这里我不打算细讲，但重点是：Swift 对象引用有更多的*空闲位（spare bit）*，这让它们能在某些 enum 里被打包得更紧凑。[↩︎](#fnref:objc)

这篇文章发表于 [2020](https://belkadan.com/blog/2020) 年 [9](https://belkadan.com/blog/2020/09) 月 29 日，归类于 [Technical](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
</content>
