---
title: Swift 运行时：枚举
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/'
original_language: en
published: 2020-10-20
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:41f2ef88872bcf87'
translated: true
---

> 原文：[The Swift Runtime: Enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/)

[Negotiate Your Offers!](https://belkadan.com/blog/2020/11/Negotiate-Your-Offers/) »

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift)

[Swift Regret: Protocol Syntax](https://belkadan.com/blog/2021/08/Swift-Regret-Protocol-Syntax/?tag=swift) »

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift-runtime)

## [The Swift Runtime: Enums](#)

欢迎来到 Swift 运行时系列文章的第七篇。本系列的目标是，以我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)中学到的知识为参考，逐一讲解 Swift 运行时的各个函数。我们已经讨论过结构体和类，那么下一个显而易见的选择就是枚举——Swift 三种“具体的”用户可定义类型中的最后一种。

如前所述，我尽可能用 Swift 来实现我精简版的运行时，不过为此我不得不使用了一些未归档的 Swift 特性。在后面的文章中，我会展示我运行时代码的片段，你可以在 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)中查看完整代码。

### “区分联合（discriminated union）”

Swift 中的枚举由一组 case 定义，每个 case 可以带有负载（payload），也可以不带。最著名的枚举是 `Optional`^[1](#fn:bool)，它有一个带负载的 case 和一个不带负载的 case：

```
enum Optional<Wrapped> {
  case none
  case some(Wrapped)
}
```

`Optional` 在 Swift 中如此重要，以至于它有自己的[语法糖](https://en.wikipedia.org/wiki/Syntactic_sugar)（`Int?` 代替 `Optional<Int>`）、隐式转换（`Int` 转为 `Optional<Int>`）以及专用的语言特性（`if let`、`?.` 等）。但是 `Optional` 的底层功能对任何定义类似形式枚举的人来说都是可用的：

```
enum Maybe<Value> {
  case just(Value)
  case nothing
}
```

带负载的枚举的功能通常被称为[区分联合（discriminated union）](https://en.wikipedia.org/wiki/Tagged_union)（还有其他一些名称）。Swift 选择将其称为“enum”，沿用了更简单的 C 语言特性（C 的 enum 不支持负载），但在其开发过程中，我们曾称之为“one-of”（源自 [CLU，最早拥有类型安全区分联合的语言](https://en.wikipedia.org/wiki/CLU_(programming_language))），后来又被称为“[union](https://github.com/apple/swift/commit/674a03b08583037a0e1906266fdb5a5f0065dc87)”，最终才确定为“enum”。Rust 也使用“enum”，所以我们并不孤单。

总之，我已经向可能早已了解枚举的读者讲了很多，那我们就开始深入底层吧。编译器将 Swift 枚举分为三组：无负载（no-payload）、单负载（single-payload）和多负载（multi-payload）。我们接下来逐一讨论。

### 无负载枚举

```
enum NamedColor<ColorSpace> {
  case white, yellow, orange, red
  case magenta, purple, blue, cyan
  case green, darkGreen, brown, tan
  case lightGrey, mediumGrey, darkGrey, black
  // https://en.wikipedia.org/wiki/List_of_software_palettes#Apple_Macintosh_default_16-color_palette
}
```

无负载枚举类似于 C 语言的枚举：其 case 只是互斥的名称。这意味着编译器可以简单地为每个 case 分配一个数值表示，然后就完成了。不需要运行时布局。^[2](#fn:evolution) 当然，无负载枚举仍然可以有泛型参数，这些参数可能会在方法等地方使用，但枚举值中没有任何 _存储_ 的泛型内容，因此除了 [`swift_allocate­Generic­ValueMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/) 中已有的逻辑外，不需要做其他事情。

与 C 语言枚举相比，无负载枚举还有一个不同之处：如果你使用 Swift 的“原始值”支持，内存中的表示可能仍然不同于原始值：

```
enum Multiplier: Int {
  case deca = 10
  case hecto = 100
  case kilo = 1_000
  case mega = 1_000_000
  case giga = 1_000_000_000

  case kibi = 0x400
  case mebi = 0x10_0000
  case gibi = 0x4000_0000
}
```

当前编译器的实现将 `Multiplier.kilo` 的值表示为“2”，并且还指出它仅占用一个字节。当用户请求 `Multiplier.kilo.rawValue` 时，调用的是一个编译器生成（并优化）的 switch 语句来获取原始值，_而不是_ 简单地将该值重新解释为整数。这有利于节省空间，对于原始值为字符串的情况也是如此！^[3](#fn:objc)

关于无负载枚举，基本上就是这些了。

### 单负载枚举

如果枚举只有一个带有负载的 case，编译器和运行时就会~联手~协作，根据负载的类型和无负载 case 的数量，选择最有效的布局。在最简单的情况下，这最终只是“如果设置了此标志，则此处存在有效值，否则不存在”。下面是 `Optional<Int32>` 的一个示例：

|  | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `.some(0x11223344)` | `0x11223344` | `0` |  |  |  |
| `.none` |  | `1` |  |  |  |

（如果你想知道为什么 0 是“有效值”标志而不是 1，请考虑其他枚举可能有多个无负载 case。）

让我们先假设这是我们能做到的最好情况，然后编写一些代码。我们需要哪些操作？

- 确定为无负载 case 分配多少额外空间。
- 提供获取和设置枚举“标签”（tag）的方法，以记录我们当前处于哪个 case。（我们不需要获取或设置实际的负载，因为要么它是有效的，要么不是。）

这些转化为一些（大部分）相当直接的伪代码，首先是计算枚举类型的布局：

```
assert(numberOfCases <= UInt32.max)
let numTagBytes = (
  numberOfCases <= 1 ? 0 :
  numberOfCases <= UInt8.max ? 1 :
  numberOfCases <= UInt16.max ? 2 : 4)

var layout = payloadTypeLayout
layout._.size += numTagBytes
// 必须为更大的尺寸重新计算这些值。
layout.computeStride()
layout.computeInline()
```

然后是获取标签：

```
let tagBytesAddr = enumValueRawAddr + payloadTypeLayout._.size
let numTagBytes = enumLayout._.size - payloadTypeLayout._.size
return tagBytesAddr.loadUnalignedBigEndianValue(size: numTagBytes)

extension UnsafeRawPointer {
  func loadUnalignedBigEndianValue(size: Int) -> UInt32 {
    var result: UInt32 = 0
    for i in 0..<size {
      result <<= 8
      result |= UInt32(self.load(fromByteOffset: i, as: UInt8.self))
    }
    return result
  }
}
```

（我省略了设置部分，因为它与获取基本相同。）

理论上，这就是创建一个区分联合所需的一切。我们甚至根据 case 的数量尽可能紧凑地打包了标签，但由于我们没有做出任何对齐保证，我们必须逐字节地从头开始组装和反汇编它。但对于其他类型，我们可以做得更好，而且为了与 C 的互操作性，我们 _必须_ 做得更好。

### “额外居民（Extra inhabitants）”

Swift 相对于 Objective-C 最大的改进之一（依我愚见）是效仿其他语言，使用 `Optional` 来明确指针的可空性：`Optional<UIView>` 可以是 `nil`，但普通的 `UIView` 引用则不能。然而，为了在不使用某种转换操作的情况下做到这一点，我们需要一个更智能的 `Optional` 表示：一种可以使用与 C 用于 `NULL` 相同的表示来表示 `nil` 的方式。也就是说，对于 PowerPC 上的 `Optional<UnsafePointer<Int32>>`，我们希望布局如下：

|  | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| （有效指针） | （其地址） |  |  |  |
| `nil` | `0x00000000` |  |  |  |

编译器和运行时如何知道 `0x00000000` 不是一个有效指针？我的意思是，是的，它会在某处硬编码，但硬编码标准库的指针结构体不足以满足 Swift 的基本布局保证之一：**包含单个存储属性的结构体与该属性具有相同的布局**。也就是说，如果我编写一个包含单个四字节 `UnsafePointer` 的包装结构体 `FooPointer`（请记住，经典 Mac 使用 32 位 PowerPC CPU），Swift 应该足够智能，只为 `Optional<FooPointer>` 也使用四个字节。这样做的目的是让人们能够安心地编写抽象，而不必担心它们会比它们所构建的原始类型使用更多的内存——这是一个有价值的目标！那么我们如何做到这一点呢？

答案来自于我们已经见过的东西，尽管只是顺便提及：[TypeLayout 结构体](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#run-time-representation)中的_额外居民计数（extra inhabitant count）_。

> 至于“额外居民计数”，它是对类型永远不会成为有效值的那些内存表示的计数，这意味着运行时可以使用它们来在可选值中表示 `nil`。当我们讨论枚举时，会进一步讨论这个话题。目前，我们可以只讨论 Swift 计算结构体和元组额外居民计数的策略：选择具有最高计数的元素并使用它。
>
> ```
> extraInhabitantCount = fieldTypes.lazy.map {
>   $0.extraInhabitantCount
> }.max() ?? 0
> ```

如上所述，额外居民是特定类型从未使用过的内存表示。最常见的是“0 永远不会是一个有效指针”，但我们还可以想到其他一些情况，例如上面枚举中的“100 不代表有效的 Multiplier 值”。Swift 编译器和运行时足够智能，可以利用这些额外的“位模式”来表示单负载枚举中的无负载 case。

因此，假设我们已经有了类型的“额外居民”信息，现在我们需要修改我们的分配和获取/设置逻辑来考虑它。

### `swift_init­Enum­Metadata­SinglePayload`

让我们开始介绍真正的函数：

```
@_cdecl("swift_initEnumMetadataSinglePayload")
func swift_initEnumMetadataSinglePayload(
  _ opaqueEnumType: TypeErasedMutablePointer<EnumMetadata>,
  _ rawLayoutFlags: UInt,
  _ opaquePayloadType: TypeErasedPointer<TypeLayout>,
  _ emptyCases: UInt32
) {
  let enumType = opaqueEnumType.assumingMemoryBound(to: EnumMetadata.self)
  let layoutFlags = EnumLayoutFlags(rawValue: rawLayoutFlags)
  let payloadTypeLayout =
    opaquePayloadType.assumingMemoryBound(to: TypeLayout.self)[]
```

在最佳情况下，我们将能够为所有无负载 case 使用额外居民。但如果不能，我们将需要额外空间。

```
let unusedExtraInhabitants =
  Int(payloadType._.extraInhabitantCount) - Int(emptyCases)
let remainingEmptyCases = max(0, -unusedExtraInhabitants)

let extraTagBytes = getExtraTagBytes(
  payloadTypeLayout._.size,
  remainingEmptyCases,
  1)
```

我们稍后会回到 `getExtra­TagBytes`，但首先让我们完成此函数的其余部分。大部分看起来像之前的伪代码，但增加了额外居民信息：

```
var layout = payloadTypeLayout
layout._.size += UInt(extraTagBytes)
layout._.flags.hasEnumWitnesses = true
layout._.extraInhabitantCount = UInt32(max(0, unusedExtraInhabitants))
layout.computeStride()
layout.computeInline()

let vwtable = enumType.getOrCreateMutableVWTableForInit(layoutFlags)
vwtable[]._.base.publishLayout(layout)
```

[我们之前在结构体中见过 `getOr­Create­Mutable­VWTable­ForInit`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs)，而枚举的版本基本相同。然而，枚举的值见证表（value witness table）有一些额外的操作（“见证方法”）用于获取标签和负载，这比在枚举布局是静态已知的情况下调用泛型运行时函数更直接。它还允许编译器为那些 _不_ 使用 `swift_init­Enum­Metadata­SinglePayload` 的枚举进行自定义打包——Swift 中没有任何规定说单负载枚举 _必须_ 使用此布局，只要生成的代码不尝试直接访问标签或负载。

我保证我们最终会有一整篇关于值见证表的博文，但现在让我们继续看那个辅助函数 `getExtra­TagBytes`。它主要只是我们之前所做测量的一个更智能的版本。

```
func getExtraTagBytes(
  _ payloadSize: UInt,
  _ emptyCases: Int,
  _ payloadCases: Int
) -> Int {
  let numEmptyCasePayloadUnits: Int
  if emptyCases == 0 {
    numEmptyCasePayloadUnits = 0
  } else if payloadSize >= 4 {
    numEmptyCasePayloadUnits = 1
  } else {
    let bits = payloadSize &* 8
    let casesPerPayloadUnit = 1 &<< bits
    let emptyCasesRoundedUp =
      UInt(emptyCases).roundedUpToAlignMask(casesPerPayloadUnit &- 1)
    numEmptyCasePayloadUnits = Int(emptyCasesRoundedUp &>> bits)
  }

  let numTags = numEmptyCasePayloadUnits + payloadCases
  return (
    numTags <= 1 ? 0 :
    numTags <= UInt8.max ? 1 :
    numTags <= UInt16.max ? 2 : 4)
}
```

就我们的目的而言，`payloadCases` 始终为 1，但相同的逻辑也可以用于布局多负载枚举。另一方面，`emptyCases` 将是 _不能_ 放入负载额外居民中的无负载 case 的数量——即我们需要额外空间来存放的那些。然后 `getExtra­TagBytes` 对一些常见情况进行了特殊处理：

- 如果没有剩余的无负载 case，我们只需要区分不同类型的负载。对于单负载枚举，这意味着我们根本不需要任何额外的存储。
- 如果负载至少是四个字节，那么我们可以将无负载 case 的数字 _放在那里_，并使用单个标签位来区分我们处于“负载”表示还是“无负载”表示。Swift 不支持超过 2³² 个 case（也称为 4 [gibicase](https://en.wikipedia.org/wiki/Binary_prefix)）的枚举。

但是，如果我们有一个小的负载，那么可能无法在该位置容纳所有剩余的空 case。在这种情况下，我们测量负载，将空 case 的数量向上舍入到下一个“负载单元”数量（使用我们之前见过的 [`roundUp­To­AlignMask`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#show-me-some-code) 的变体），然后计算出表示所有空 case 需要多少个负载单元。这就是我们将需要的标签数量，由此我们可以执行最初做的相同的“0、1、2 或 4”字节检查。

### `swift_store­Enum­Tag­Single­PayloadGeneric`

我们之前在我们的玩具示例中做了获取方法；这次，我们将看看设置方法。（实际上，从其结构方式来看，它比获取方法更容易理解。）

```
@_silgen_name("swift_storeEnumTagSinglePayloadGeneric")
func swift_storeEnumTagSinglePayloadGeneric(
  _ enumAddr: UnsafeMutableRawPointer,
  _ whichCase: UInt32,
  _ numEmptyCases: UInt32,
  _ payloadType: UnsafePointer<TypeMetadata>,
  _ storeExtraInhabitantTag: storeExtraInhabitantTagFn?
) {
  let payloadLayout = payloadType.valueWitnessTable[]._.typeLayout
```

哎呀，这里有很多东西！特别之处在于，函数签名中已经有一些不同寻常的东西：`storeExtraInhabitantTag`。这是做什么的？好吧，仅仅因为负载类型有额外居民，并不意味着运行时知道如何访问它们！这必须被传递到这个函数中，毕竟，这个函数应该是任何单负载枚举和负载类型的泛型实现。那个回调看起来像这样：

```
typealias storeExtraInhabitantTagFn = @convention(thin) (
  _ enumAddr: UnsafeMutableRawPointer,
  _ whichCase: UInt32,
  _ numEmptyCases: UInt32,
  _ payloadType: UnsafePointer<TypeMetadata>
) -> Void
```

你很可能从未在任何地方见过 `@convention(thin)`。它是 Swift 自定义回调约定的最后一个，与 `@convention(c)` 和 `@convention(block)` 并列，它指的是一个使用 Swift 调用约定但没有捕获的函数。它的名称中没有下划线，但[它仍然没有得到官方支持](https://forums.swift.org/t/use-of-convention-thin-to-avoid-allocating-closures/12087/6)。尽管如此，它是这里完全正确的唯一方式，尽管在实践中，我认为 Swift 的任何平台（包括 Swift-on-Classic）都不会将这个特定的回调区别对待，即使它被替换为 `@convention(c)`。

好的，解决了这个奇怪之处，让我们看看函数体。与分配一样，我们首先检查是否有任何标签字节。与我们的玩具示例不同，我们没有得到枚举的完整大小，因此我们必须再次使用 `getExtra­TagBytes`：

```
let numExtraTagBytes = getExtraTagBytes(
  payloadSize,
  max(0, Int(numEmptyCases &- payloadLayout._.numExtraInhabitants)),
  1)
```

现在我们可以开始工作了。我们要尝试的第一件事是使用负载的额外居民。（这也处理了负载本身，它保证由标签 0 表示。）

```
let extraTagBitAddr = enumAddr + Int(payloadSize)
if whichCase <= payloadLayout._.numExtraInhabitants {
  extraTagBitAddr.storeUnalignedBigEndianValue(0, size: numExtraTagBytes)
  if whichCase != 0 {
    storeExtraInhabitantTag!(
      enumAddr,
      whichCase,
      payloadLayout._.numExtraInhabitants,
      payloadType)
  }
  return
}
```

注意，一旦我们知道值在范围内，我们就直接使用传递给我们的回调。我们还传递了我们期望的额外居民总数，这在负载类型本身就是另一个单负载枚举的情况下使用！（考虑 `Optional<Optional<Multiplier>>`，它 _仍然_ 只应该占用一个字节的内存。）这允许实现区分 `.none` 和 `.some(.none)`，而不会意外地为两者使用相同的标签，并且不需要额外的包装函数或专门检查类型。

（你可能也想知道，为什么我们在传递负载类型的同时还要传递额外居民的数量。我花了一段时间才弄清楚，但是 `StoreExtraInhabitantTag` 函数被设计为，如果你传递的 _空_ case 多于空居民，它也能工作……在这种情况下，它会计算出要使用多少个额外的标签字节，并将它们自身置零。我认为这是因为编译器有时会直接调用这些回调函数，但遗憾的是我们现在有两个相同事物的实现。）

如果要存储的 case 不适合额外居民，我们会继续使用无负载表示。我们要做的第一件事是减去我们已经尝试过的表示：额外居民和负载 case。

```
let caseIndexToStore = whichCase &- payloadLayout._.numExtraInhabitants &- 1
```

接下来，我们将再次将该索引分解为适合负载的部分和进入额外标签字节的部分。

```
let payloadIndex, extraTagIndex: UInt32
if payloadSize >= 4 {
  extraTagIndex = 1
  payloadIndex = caseIndexToStore
} else {
  let payloadBits = payloadSize &* 8
  extraTagIndex = 1 &+ (caseIndexToStore &>> payloadBits)
  payloadIndex = caseIndexToStore & ((1 &<< payloadBits) &- 1)
}
```

和之前一样，对于大的负载，我们直接传递索引，对于小的负载，则按“负载单元”分解。（请记住，使用 2 的幂减 1 进行掩码操作等同于取余数。）“额外标签”部分总是从 1 开始，因为 0 已经表示“负载或额外居民表示”。

```
let payloadIndexSize = max(payloadSize, 4)
let payloadIndexAddr = enumAddr + Int(payloadSize &- payloadIndexSize)
payloadIndexAddr.storeUnalignedBigEndianValue(
  payloadIndex,
  size: Int(payloadIndexSize))
extraTagBitAddr.storeUnalignedBigEndianValue(
  extraTagIndex,
  size: numExtraTagBytes)
```

最后，我们将索引的两个部分存储在负载和额外字节中。但是等等，为什么 case 索引存储在负载的 _最后_ 四个字节而不是第一个？这是因为编译器将整个负载视为一个大整数……而在运行 Classic 的 PowerPC 上，整数是以[大端序（big-endian）](https://en.wikipedia.org/wiki/Endianness#Classical_example)存储的。因此，存储一个小于 2³² 的负载值永远只会使用负载的最后四个字节。^[4](#fn:endian)

就是这样：我们已经存储了我们的枚举 case 标签！如果没有涉及负载，我们就完成了，如果有，调用此函数的代码将完成其余部分。

（我不会展示获取方法，但它与设置方法相反。）

### 多负载枚举

…是我在 [ROSE-8](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) 中不需要的，因此我没有实现它们。抱歉！

…不过说真的，多负载枚举是另一个话题，并包含许多纯编译时的优化，不提及它们是不合适的。所以，虽然它们 _不会在本系列中涵盖_，但我仍然希望在未来的某天讨论它们。但不做保证！

### 总结

我们现在已经了解了 Swift 如何处理类似 C 语言的枚举以及只有一个带负载 case 的枚举，以及它如何超越最简单的实现，将更多信息打包到更少的字节中（并保持与 C 的 `NULL` 兼容）。至此，我们已经讨论了所有 Swift 的“具体的”用户可定义类型：结构体、类和枚举。

不幸的是，在编写这些文章时，我储备的内容已经用完了！因此，在回到协议、动态类型转换以及那些被反复提及的 _值见证表_ 之前，我将暂停一段时间（很可能是几周）。对于那些渴望更多内容的人（以及当时没有看到的人），我参加了 JP Simard 和 Jesse Squires 的 _[Swift Unwrapped](https://spec.fm/podcasts/swift-unwrapped/1DMLbJg5)_ 播客，讨论了该项目以及与 Swift 运行时相关的其他事情。

1. 在一个有枚举的语言中，最著名的枚举 _应该_ 是 Bool，带有 case“false”和“true”。然而，早期版本的 Swift 对于检查枚举位于哪个 case 并没有生成非常好的代码，这意味着 _每个 `if` 语句都会导致代码膨胀_。因此，Swift.Bool 被定义为一个围绕 1 位原始值的结构体（在内存中存储时为 1 字节），而不是作为一个枚举。唉。 [↩︎](#fnref:bool)
2. 请记住，本系列文章基本忽略了[库进化（library evolution）](https://swift.org/blog/library-evolution/)支持，这要求枚举的数值对于针对不同库版本进行编译的客户端保持一致。但是，这仍然不需要任何运行时支持；编译器只需为每个枚举 case 发出一个全局常量，客户端可以使用该常量，而不是使用字面整数表示。 [↩︎](#fnref:evolution)
3. 此规则的例外是标记为 `@objc` 的枚举，它们需要能够与 Objective-C 互操作。这些枚举遵循 C 语言的规则，使用原始值作为表示，并利用 Objective-C 的“固定底层枚举类型”特性（[从 C++ 借用的](https://clang.llvm.org/docs/LanguageExtensions.html#enumerations-with-a-fixed-underlying-type)）来确保两种语言中大小匹配。 [↩︎](#fnref:objc)
4. 老实说，我怀疑这种行为是一个意外，是源于小端序平台实现的一个副产品。要“修复”它也并不难，但你必须同时修改编译器和运行时。 [↩︎](#fnref:endian)

这篇文章发布于 [2020 年](https://belkadan.com/blog/2020)[10 月](https://belkadan.com/blog/2020/10) 20 日，归类于[技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift), [Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)
