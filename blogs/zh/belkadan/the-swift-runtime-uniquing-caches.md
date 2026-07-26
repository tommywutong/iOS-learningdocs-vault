---
title: 'Swift 运行时：唯一化缓存'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/'
original_language: en
published: 2020-09-21
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ae1d1f225573ab9'
translated: true
---

> 原文：[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift 运行时：类型元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)

[Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/) »

« [Swift 运行时：类型元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift)

[Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift) »

« [Swift 运行时：类型元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift-runtime)

[Swift 运行时：类元数据](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift-runtime) »

## [Swift 运行时：唯一化缓存](#)

欢迎来到 [Swift 运行时](https://belkadan.com/blog/tags/swift-runtime)系列的第四篇。这个系列的目标是过一遍 Swift 运行时的各项功能，把我在 [Swift on Mac OS 9 项目](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)里学到的东西当作参照。这次我们要聊的是用来唯一化类型元数据（以及其他需要唯一化的东西）的缓存。

正如之前提到的，我用 Swift 尽可能实现了这个精简版运行时，不过为此不得不用上几个没有文档记录的 Swift 特性。整个系列里我会展示我的运行时代码片段，完整代码可以在 [ppc-swift 仓库](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime)里看到。

### 从上次停下的地方接着讲

[上次讲到](https://belkadan.com/blog/2020/07/Swift-Runtime-Type-Metadata/)，我们刚写完 `swift_allocate­Generic­ValueMetadata`，它用来实例化带参数的泛型类型。但 `swift_allocate­Generic­ValueMetadata` 并不是被直接调用的；它只会在元数据第一次需要创建时才出现。实际被调用的是另一个函数，`swift_get­GenericMetadata`。

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse
```

我们打算从后往前推。我们知道最终会需要一个缓存（这样才不会在内存里堆出成千上万份 `Array<Int>` 的拷贝），但在没有命中缓存的情况下，我们必须调用 `swift_allocate­Generic­ValueMetadata`。是这样吗？

```
let genericMetadataHeader = description.fullGenericContextHeader

let pattern = genericMetadataHeader.instantiationPattern
let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)

if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
  var completionContext = MetadataCompletionContext()
  _ = pattern.completionFunction![](metadata, &completionContext, pattern)
}

return MetadataResponse(metadata: metadata, state: .complete)
```

呃……好像也不全是。我们确实拿到了上次提到的那个「模式（pattern）」，但没有直接把它传给 `swift_allocate­Generic­ValueMetadata`，而是调用了存在这个 pattern 里的某种「实例化函数」。这给了编译器一个机会，可以在真正做分配之前插入一些自定义逻辑，比如为 [指针认证（pointer authentication）](https://developer.apple.com/documentation/security/preparing_your_app_to_work_with_pointer_authentication) 正确地给参数签名。但它最终还是会调用 `swift_allocate­Generic­ValueMetadata`，把新的元数据还给我们。

然后我们还有*第二个*回调，如果类型在实例化之后处于「未完成」状态，就会立刻调用它。这是怎么回事？原来真正的 Swift 运行时是能处理[类型之间循环依赖](https://bugs.swift.org/browse/SR-263)的，而我的实现……没有。在真正的 Swift 运行时里，为某个类型实例化元数据可能会导致它的依赖也被实例化，但这些新实例化出来的元数据的「完成函数（completion function）」要等到所有依赖都实例化完并且记录到那个我们还没建好的缓存里之后才会被调用。这一点，再加上确保依赖只访问类型里最基本的信息（通常只有它的身份和泛型参数），就解决了循环依赖的问题。我决定干脆不支持这个，因为大多数类型在实例化时都不存在循环依赖。^[1](#fn:circular)（顺便说一句，处理循环依赖也正是那个 `request` 参数的用途所在。我们打算直接忽略它。）

所以，*实例化函数*会尽可能多地分配并填好泛型元数据，然后可能还会有一个*完成函数*做一些额外的工作，把类型做成完整、可以直接使用的状态。希望这样讲得通！

### 这些函数是从哪儿来的？

我们要绕个道，去看看 `instantiationFunction` 和 `completionFunction` 这两个属性。就像上次的 `fullGenericContextHeader` 一样，这些属性是直接定义在指针上的，因为它们需要相对于第一个指针计算出一个新指针。和 `fullGenericContextHeader` 不同的是，这个新指针指向内存里别的地方，而不是紧挨着 pattern 的前面或后面。

```
struct RelativePointerOffset<Pointee> {
  var value: Int32
}

extension UnsafePointer {
  func applying<NewPointee>(
    _ offset: RelativePointerOffset<NewPointee>,
    additionalOffset: Int = 0
  ) -> UnsafePointer<NewPointee>? {
    if offset.value == 0 { return nil }
    let newPointer = UnsafeRawPointer(self) + Int(offset.value) + additionalOffset
    return newPointer.assumingMemoryBound(to: NewPointee.self)
  }
}

extension UnsafePointer where Pointee == GenericMetadataPattern {
  var instantiationFunction: UnsafePointer<GenericMetadataPattern.Instantiator> {
    return self.applying(self[]._.instantiationFunction)!
  }
}
```

为什么要用这种*相对指针（relative pointer）*？想想看，通常引用内存里别处的东西会用一个普通指针。在 [64 位地址空间](https://en.wikipedia.org/wiki/64-bit_computing)下，指针在内存里占 64 位，而且因为库被加载到内存里的位置是不确定的，静态数据里的指针需要在 App 启动时被「修正」到正确的位置。这个过程是*动态链接*的一部分，通常会被大量优化，但终究不如干脆不做这份工作来得好。

相对指针在引用「已知位于同一个库或可执行文件内」的东西时，提供了一种更高效的替代方案。只要假设单个编译出来的二进制永远不会超过 2 [GiB](https://en.wikipedia.org/wiki/Gibibyte)，它就可以用一个带符号的 32 位偏移量来引用另一个地址。而且只要一个库总是作为一整块被加载，这个偏移量就与库被加载到哪个地址无关。代价是，等到真正*使用*这个指针的时候，不再只是一次载入；现在还需要做一次加法。不过这是个非常快的操作。（[我以前的同事在 2018 年 LLVM 开发者大会的一场演讲里详细讲了相对指针以及更多内容](https://youtu.be/G3bpj-4tWVU)。）

对了，那个「额外偏移量（additional offset）」参数是为了应对相对指针指向的字段*不是*目标结构体第一个字段的情况。理想情况下我应该用 [`MemoryLayout.offset(of:)`](https://developer.apple.com/documentation/swift/memorylayout/2996397-offset) 来处理这个，但[它不是编译期常量](https://bugs.swift.org/browse/SR-12961)，而且我这个项目其实也没有实现 key path 的运行时表示，所以这条路走不通。

不过这就是这里发生的事：泛型元数据的 pattern 存了一个指向实例化函数的相对引用，而我定义了一个便利属性来解析这个相对引用。^[2](#fn:functions)

### 挑选我们的缓存键

好了，回到正题。缓存的工作方式，需要我们写出大概长这样的代码：

```
let key = Key(uniquing constraints)
if let existingValue = cache[key] {
  return existingValue
}
let newValue = makeValue()
cache[key] = newValue
return newValue
```

「生成值」的部分我们已经聊过了，但「键」要怎么处理？对于这种「唯一化」缓存来说，键需要唯一地描述被创建出来的值。那么，在 Swift 里，什么能唯一地描述一个泛型类型呢？就是基础类型和泛型参数，也就是我们被传进来的那些参数。

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse
```

……嗯。我们怎么知道有多少个参数？哦对，会在 `description` 里。但是，嗯，用哪个计数？

```
struct GenericContextDescriptorHeader {
  var `_`: (
    numParams: UInt16,
    numRequirements: UInt16,
    numKeyArguments: UInt16,
    numExtraArguments: UInt16
  )
  
  var totalArgumentCount: Int {
    Int(self._.numKeyArguments) &+ Int(self._.numExtraArguments)
  }
}
```

刚开始的时候，我会以为 `numParams` 就是正确的值，但事实证明泛型类型的门道比这个多得多。我们一直在讲 `Array<Int>`，但 `Set<Int>` 呢？在这个例子里，实际上会有两个独立的底层泛型参数：类型 `Int`，以及一致性 `Int: Hashable`。这两者就是被算作「键参数（key argument）」的东西（呼应「缓存键」里的「键」）。

| 类型 | `num` `Params` | `num` `Require` `ments` | `num` `Key` `Argu``ments` | `num` `Extra` `Argu``ments` |
|---|---|---|---|---|
| `Array<T>` | 1 | 0 | 1 | 0 |
| `Set<T: Hashable>` | 1 | 1 | 2 | 0 |
| `Dictionary<K: Hashable, V>` | 2 | 1 | 3 | 0 |
| `Unmanaged<T: AnyObject>` | 1 | 1 | 1 | 0 |
| `Combine.Concatenate<` ` P: Publisher, S: Publisher` `> where P.Output == S.Output,` `P.Failure == S.Failure` | 2 | 4 | 4 | 0 |
| `extension Array` `where Element == Int {` ` struct Contrived {}` `}` | 1 | 1 | 0 | 0 |

理解上面这几个例子的「关键」在于：键参数的数量，等于参数的数量（包括父级作用域里的参数），减去被约束为具体类型的参数，再加上一致性约束的数量。^[3](#fn:objc-protos) 其他种类的约束，不管是布局（受限于 class）、超类还是同类型约束，都可以直接从类型本身推导出来，不需要一次全局查找。

那么，为什么*这些*是键参数而不是参数本身呢？首先，参数里可能包含一些在运行时根本不需要传进来的类型，比如 `Contrived` 例子里的 `Array.Element`。但另一个原因是要处理不同模块里定义的相互冲突的一致性。如果两个不同的模块给同一个类型定义了不同的 Hashable 一致性，那么在一个模块里创建的 Set，拿到另一个模块里用的时候就得不出正确的结果！Swift 社区目前仍在设法解决这个问题，但运行时至少能防止你拿到无意义的结果：即便两个 Set 的元素类型相同，它也会把它们视为不同的类型。这就是把一致性纳入键参数之后得到的效果。^[4](#fn:witness-tables)

那空着的 `numExtraArguments` 又是怎么回事？嗯，它目前没有被用到，但我以前的同事 John McCall 证实[它曾经被用来存一致性](https://twitter.com/pathofshrines/status/1282452532451844097)，也就是说过去它们*不*算作键参数。所以你能看出，「冲突的一致性」这个想法确实挺棘手的。（将来，编译器也许会用这个字段来添加一些不属于唯一化键的额外「泛型参数」，虽然我不确定那具体会是什么。）

所以：唯一标识一个类型所需要的信息，是「类型描述符」加上「键参数」列表。编译器实际上已经为每个类型的专属缓存留好了位置，所以我们真正需要的只是键参数列表。

```
let genericMetadataHeader = description.fullGenericContextHeader
let keyArguments = UnsafeBufferPointer(
  start: arguments,
  count: Int(genericMetadataHeader[]._.base._.numKeyArguments))
```

这样一看……其实还不算太糟！等到我们要比较两次实例化的时候，只需要比较那些唯一代表类型和一致性的不透明指针就行了。

### 真正的缓存

一个从不移除任何东西的缓存，用一个普通字典就能轻松实现，如果我们手头有完整的 Swift 标准库，我们可能会直接找 Dictionary 来做这件事。不过这里有两个问题：我从来没在这个项目里实现对 Hashable、Set 和 Dictionary 的支持，而且就算实现了，它们也得依赖我们正在实现的这个运行时函数本身！好在 Mac OS 9 上还有第二个选择：Core Foundation。[我在这个系列的第一篇里提到过 Core Foundation](https://belkadan.com/blog/2020/07/Swift-Runtime-Heap-Objects/#core-foundation)；现在我们就要靠它来实现我们的运行时缓存，让当初做的那些准备工作真正派上用场。

CF 的字典类型 [CFDictionary](https://developer.apple.com/documentation/corefoundation/cfdictionary-rum) 到今天都还在用。它的工作方式跟 Swift 的字典很像，只不过键和值都得能塞进单个指针里。因为 CF 没有类似「Any」（或 AnyHashable）的概念，所以它也允许你[手动自定义](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks)比较和拷贝键值时执行的操作。它还预定义了一些操作，用来支持本身就是 CF 对象的键或值，而在这些操作缺失的时候，就退回到对指针本身做按位操作。这对我们来说已经够用了。

因为 CFDictionary 非常灵活，它的 API 是用 UnsafeRawPointer 定义的，用起来不太方便。我们来加几个辅助方法处理这个问题。

```
extension CFMutableDictionary {
  private func withObjectAsKey<Result>(
    _ object: AnyObject,
    do body: (UnsafeMutableRawPointer) -> Result
  ) -> Result {
    return withExtendedLifetime(object) {
      let opaqueObject = Unmanaged.passUnretained(object).toOpaque()
      return body(opaqueObject)
    }
  }

  internal subscript(_ object: AnyObject) -> UnsafeRawPointer? {
    get {
      withObjectAsKey(object) {
        CFDictionaryGetValue(self, $0)
      }
    }
    set {
      withObjectAsKey(object) {
        CFDictionarySetValue(self, $0, newValue)
      }
    }
  }
}
```

这里没什么特别复杂的东西，但它能让我们把 CF 对象当作键、把原始指针当作值来用。这确实没有做类型检查，不太好，但比起我们在这个运行时里到处操作原始指针的做法，这已经算不上最不安全的事了。唯一有点讲究的地方是用了 `withExtendedLifetime`，它能确保对象不会在它的不透明引用被当作键使用之前就被释放。

现在我们可以把缓存逻辑的剩余部分补完了：

```
let rawArguments = UnsafeRawBufferPointer(keyArguments)
let cacheKey = CFDataCreate(nil,
  rawArguments.baseAddress?.assumingMemoryBound(to: UInt8.self),
  rawArguments.count).takeRetainedValue()

if let result = genericMetadataCache[cacheKey] {
  return MetadataResponse(
    metadata: result.assumingMemoryBound(to: TypeMetadata.self),
    state: .complete)
}

let pattern = genericMetadataHeader.instantiationPattern
let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)

if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
  var completionContext = MetadataCompletionContext()
  _ = pattern.completionFunction![](metadata, &completionContext, pattern)
}

genericMetadataCache[cacheKey] = UnsafeRawPointer(metadata)
return MetadataResponse(metadata: metadata, state: .complete)
```

如果你眼尖的话，可能会注意到我们对[一个本不该用 Unmanaged 的 CF 函数](https://developer.apple.com/documentation/corefoundation/1542359-cfdatacreate)的返回值用了 `takeRetainedValue()`。仔细想想的话这也不该觉得奇怪：[`CF_IMPLICIT_BRIDGING_ENABLED`](https://asciiwwdc.com/2013/sessions/404) 在 Automatic Reference Counting 出现之前根本不可能存在！可惜没有什么快捷的方式能不改头文件就启用它，而我到目前为止都还没去改。所以在 Classic Mac OS 上，所有 CF 的 API 都会返回 Unmanaged。没办法。

尽管如此，走到这一步我们已经差不多了！但是……这个缓存是从哪儿来的？它一开始是怎么建立起来的？

### 惰性缓存初始化

我们的缓存是一个 CFDictionary（准确说是 CFMutableDictionary），而这不是能在编译期创建出来的东西。（也不是我们想要的——如果你的程序从来没用过某个特定的泛型类型，那样做简直是浪费内存！）编译器真正给我们的，是一块指针大小、初始化为 0 的全局静态内存，可以通过类型描述符访问到。

运行时的其他部分还会需要别的惰性初始化缓存，所以我们再写一个辅助函数：

```
func lazyInitialize<Object: AnyObject>(
  _ rawStorage: inout UInt,
  by create: () -> Object
) -> Object {
  if rawStorage == 0 {
    rawStorage = UInt(bitPattern: Unmanaged.passRetained(create()).toOpaque())
  }
  let opaquePtr = UnsafeRawPointer(bitPattern: rawStorage)!
  return Unmanaged<Object>.fromOpaque(opaquePtr).takeUnretainedValue()
}
```

这里用 `passRetained(_:)` 却没有对应的 `takeRetainedValue()`，意味着创建出来的对象永远不会被释放，但这正是我们想要的——一个持续整个程序生命周期的缓存。真正的初始化过程则相当直白：

```
let rawCachePtr = genericMetadataHeader.instantiationCache
let genericMetadataCache: CFMutableDictionary = lazyInitialize(&rawCachePtr[]) {
  var keyCallbacks = kCFTypeDictionaryKeyCallBacks
  return CFDictionaryCreateMutable(
    /*allocator*/nil,
    /*maxCapacity*/0,
    &keyCallbacks,
    /*valueCallbacks*/nil
  ).takeRetainedValue()
}
```

现在我们有了缓存，也知道拿它来做什么，还知道在缓存里没有对应条目时该怎么实例化新的类型元数据。我们几乎、*几乎*要搞定 `swift_get­GenericMetadata` 了。只剩最后一件事……而事实上，在写「[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)」那篇之前，我压根没顾上把它实现完。

### 同步

是这样，尽管 Classic Mac OS 的 App 之间用的是协作式多任务，它们*同样*支持派生出抢占式任务——也就是我们在现代 macOS 这类 UNIX 系统上所说的线程。而且因为我们的缓存是跨线程全局共享的，我们得确保不会有两个线程同时更新缓存。CFDictionary 和我们的 `lazyInitialize` 函数都不是线程安全的。处理这个问题最简单的办法是加一把锁，Classic Mac OS 把这叫做*进入一个临界区（critical region）*。

```
func withMetadataLock<Result>(do body: () -> Result) -> Result {
  guard _MPIsFullyInitialized() else { return body() }

  _ = MPEnterCriticalRegion(criticalRegionID, /*timeout*/Duration(kDurationForever))
  defer { MPExitCriticalRegion(criticalRegionID) }

  return body()
}
```

这算不上一个*好*的实现，因为主协作任务可能会因为等待某个抢占式任务而被阻塞，而这会把机器上*所有*协作式的工作都锁住，直到另一个任务退出临界区为止。但这也够用了——我想不出办法能让出控制权给系统上的其他程序，同时又不处理当前程序里的任何事件。（也许在一个协作式的世界里，这本来就说不通。）注意，如果多任务处理库*没有*完全初始化，就不支持抢占式任务，所以我们也就不用担心线程安全问题了。

不过我们又引入了一个新问题：`criticalRegionID` 是从哪儿来的？我们得把*它*也全局分配出来，而且分配的过程*不能*加锁。这里的诀窍是用[原子的比较并交换（compare-and-swap）](https://en.wikipedia.org/wiki/Compare-and-swap)：

```
if rawCriticalRegionID == 0 {
  var newCriticalRegionID: MPCriticalRegionID?
  _ = MPCreateCriticalRegion(&newCriticalRegionID)
  let rawNewRegionID = UInt32(UInt(bitPattern: newCriticalRegionID))
  if CompareAndSwap(/*expected*/0, rawNewRegionID, &rawCriticalRegionID) {
    // If we lost the race, delete the region we created and use the other one.
    MPDeleteCriticalRegion(newCriticalRegionID)
  }
}
let criticalRegionID = MPCriticalRegionID(bitPattern: UInt(rawCriticalRegionID))!
```

这里有点别扭，因为 `CompareAndSwap` 是按 UInt32 而不是 UInt 定义的，但基本上能用。这是惰性初始化里相当标准的一种模式，不过一般来说**你不该自己去实现同步逻辑**。编译器能做哪些优化、CPU 又保证了什么，这两套规则搅在一起，真的很难确保自己面面俱到、没在哪里留下一个 bug。天哪，就算用锁，这都够难的了！在这个例子里，我*认为*这段代码是安全的（假设 `CompareAndSwap` 的实现是正确且保守的），因为只有三种可能：

1. 当前线程读到一个非零值，那它就一定是个有效的区域 ID。这个值也可能会被复用到 `rawCriticalRegionID` 的第二次引用上，而不是重新读一次全局变量，但这没关系。
2. 当前线程读到 0，用 `CompareAndSwap` 成功设置了区域 ID，然后读到刚设置好的那个值。编译器不能把第二次读操作优化掉，因为 `CompareAndSwap` 可能已经改变了那个全局变量。
3. 当前线程读到 0，*不管这个 0 本身对不对*，但随后在 `CompareAndSwap` 里没能设置成功区域 ID。这种情况下，编译器不知道 `CompareAndSwap` *为什么*失败，仍然得假设它可能改变了那个全局变量，所以第二次读操作依然会发生。

这段代码之所以能work，是因为这次初始化实际上是一次性的、单向的转变。如果我们还得区分「第一次比较并交换」和「后续的比较并交换」，事情可能会复杂得多。而且我还得说明一下，**这段代码依然违反了[正式规则](https://github.com/apple/swift-evolution/blob/master/proposals/0282-atomics.md)**，因为它在另一个线程可能正在修改某个全局变量的过程中去读取它。Swift 目前没有办法告诉*编译器*去做一次「安全」的读取。我们只是运气好，编译器为单线程模式生成的代码，在多线程模式下也照样能用。

……哦，另外我们还依赖这样一个事实：把一个全局变量以 `inout` 的方式传给一个期望指针的 API，实际用到的会是这个全局变量本身的存储地址，而不是一个临时变量。^[5](#fn:global)

不过有了这个辅助函数，我们现在就能用一个「临界区」来保护所有会修改全局状态的工作了。这就给出了 `swift_get­GenericMetadata` 的最终版本：

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse {
  return withMetadataLock {
    let genericMetadataHeader = description.fullGenericContextHeader

    let rawCachePtr = genericMetadataHeader.instantiationCache
    let genericMetadataCache: CFMutableDictionary = lazyInitialize(&rawCachePtr[]) {
      var keyCallbacks = kCFTypeDictionaryKeyCallBacks
      return CFDictionaryCreateMutable(
        /*allocator*/nil,
        /*maxCapacity*/0,
        &keyCallbacks,
        /*valueCallbacks*/nil
      ).takeRetainedValue()
    }

    let keyArguments = UnsafeBufferPointer(
      start: arguments,
      count: Int(genericMetadataHeader[]._.base._.numKeyArguments))
    let rawArguments = UnsafeRawBufferPointer(keyArguments)
    let cacheKey = CFDataCreate(nil,
      rawArguments.baseAddress?.assumingMemoryBound(to: UInt8.self),
      rawArguments.count).takeRetainedValue()

    if let result = genericMetadataCache[cacheKey] {
      return MetadataResponse(
        metadata: result.assumingMemoryBound(to: TypeMetadata.self),
        state: .complete)
    }

    let pattern = genericMetadataHeader.instantiationPattern
    let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
    let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)
    
    if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
      var completionContext = MetadataCompletionContext()
      _ = pattern.completionFunction![](metadata, &completionContext, pattern)
    }
    
    genericMetadataCache[cacheKey] = UnsafeRawPointer(metadata)
    return MetadataResponse(metadata: metadata, state: .complete)
  }
}
```

### 小结

现在我们知道了一个泛型类型是怎么被实例化的：从最初对 `swift_get­GenericMetadata` 的调用，到类型的布局，再到一路上处理的同步、缓存和泛型参数。[下次我们会讲讲这个过程在处理类元数据时有什么不同。](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)

1. 就连真正的 Swift，[直到 Swift 4.2](https://bugs.swift.org/browse/SR-263) 才实现了对循环依赖的正确处理。[↩︎](#fnref:circular)
2. 这里其实还有一件挺有意思的事，那就是我们说的是对一个*函数*的相对引用。在 Swift 里，对函数的引用不是用 UnsafePointer 表示的；它们有自己专门的类型。

  ```
  typealias Instantiator = @convention(c) (
    _ type: TypeErasedPointer<TypeContextDescriptor>,
    _ data: UnsafePointer<UnsafeRawPointer>?,
    _ pattern: TypeErasedPointer<GenericMetadataPattern>
  ) -> TypeErasedPointer<TypeMetadata>
  ```

  按常理，这就意味着要把得到的指针[强制位转换（bitcast）](https://developer.apple.com/documentation/swift/1641250-unsafebitcast)成函数引用——目前没有别的办法能在 Unsafe*Pointer 家族和 `@convention(c)` 函数引用之间互相转换。但这里还有*第二*层麻烦，来自使用 Classic Mac OS 这件事本身：在 Classic Mac OS 上，一个函数指针并不是直接指向函数的起始位置。相反，它指向一个二进制文件的「目录表（table of contents）」，里面既有函数本身，也有一个实际上是用来访问库里全局变量的「秘密参数」（称为「基址指针（base pointer）」）。通过函数指针调用一个函数，意味着先把这个隐藏参数载入寄存器，再载入函数代码的真实地址，*然后*才跳转过去。

  那这跟相对引用要怎么配合呢？理论上，我们可以往目录表里存一个相对引用，它在被载入的时候就会变成一个普通的函数指针。但我用的目标文件格式并不支持这样做，虽然我已经不记得[那条错综复杂的链路](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#gathering-materials)到底是在哪个环节出的问题。（完全有可能是目录表在 PowerPC 程序里被加载到跟常量数据不同的地址，这样任何编译期偏移量都没法用来引用它。）所以我选了一个更简单的答案：[多加一层间接层](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering)。实际上，这意味着我没能拿到相对引用的大部分好处，尤其是 Classic Mac OS 只有 32 位地址空间。但这确实意味着，包含相对引用的数据依然可以存在常量内存里，而且比起只在条件允许的时候才用相对引用，改编译器给函数指针插入一层间接层要容易得多。至少，我是这么认为的。

  相对引用本身在大量其他静态数据上都是原样使用的；只有函数指针需要这种特殊处理。[↩︎](#fnref:functions)
3. 不过，对 Objective-C 协议的一致性不算作键参数。在运行时，一个 Objective-C 协议一致性只是一个标记，用来说明「没错，这个类型支持这些方法」，所以一旦你确认约束已经满足，就没必要在类型里再存一份对这个标记的引用了。[↩︎](#fnref:objc-protos)
4. 在真正的 Swift 运行时里，这一点会更复杂，因为编译器会为从 C 导入的类型*合成*一致性。在这种情况下，我们*不*希望把不同模块里定义的一致性视为可能冲突的，这一点被记录在 *witness table* 里——也就是一致性在运行时的表示。在这种情况下，只要两个一致性定义在同一个类型上、针对同一个协议，并且都标记为编译器合成且非唯一，它们就是兼容的，这意味着我们不能只把两份键参数列表当作不透明指针来比较。我在 Classic Mac OS 运行时里从来没顾上实现这一点，所以理论上，我在传递 CF 类型之类的集合时可能会碰到这个问题。[↩︎](#fnref:witness-tables)
5. [我试着为这条规则找一个靠谱的出处](https://forums.swift.org/t/lazyweb-citation-for-stored-globals-have-stable-addresses/40451)，但没能找到！不过肯定有程序依赖这一点，我们这些 Swift 编译器开发者也在 Swift 论坛上非正式地说过很多次。[↩︎](#fnref:global)

这篇文章发表于 [2020](https://belkadan.com/blog/2020) 年 [9](https://belkadan.com/blog/2020/09) 月 21 日，归类于 [Technical](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
</content>
