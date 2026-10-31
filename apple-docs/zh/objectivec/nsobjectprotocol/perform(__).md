---
title: 'perform(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3A%29.json'
content_hash: 'sha256:2c8aa6b935d15e54'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:)

<sub>实例方法</sub>

向接收者发送指定消息并返回消息的结果。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!) -> Unmanaged<AnyObject>!
```

## 参数

- `aSelector` — 标识要发送的消息的选择器。该消息不应接受参数。若 `aSelector` 为 `NULL`，则引发 [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)。

## 返回值

作为消息结果的对象。

## 讨论

调用 [- performSelector:](<perform(__).md>) 方法等效于直接向接收者发送 `aSelector` 消息。例如，若 `anObject` 是 `MyObject` 的实例，则以下两者执行相同的操作：

**Swift**

```swift
let aClone = anObject.copy()
let aClone = anObject.perform(#selector(MyObject.copy)).takeRetainedValue()
```

**Objective-C**

```objc
id aClone = [anObject copy];
id aClone = [anObject performSelector:@selector(copy)];
id aClone = [anObject performSelector:sel_getUid("copy")];
```

[- performSelector:](<perform(__).md>) 方法允许你发送直到运行时才确定的消息。这意味着你可以将变量选择器作为参数传递：

**Swift**

```swift
let aSelector = findTheAppropriateSelectorForTheCurrentSituation()
let returnedObject = anObject.perform(aSelector).takeUnretainedValue()
```

**Objective-C**

```objc
SEL aSelector = findTheAppropriateSelectorForTheCurrentSituation();
id returnedObject = [anObject performSelector:aSelector];
```

这样做时要小心。此方法返回指向 `AnyObject` 实例的隐式解包可选未托管指针（[Unmanaged](../../swift/unmanaged.md)`<`[AnyObject](../../swift/anyobject.md)`>!`）。由你决定如何将该实例纳入 Swift 的内存管理方案。不同消息对其返回对象需要不同的内存管理策略，可能并不明显该使用哪一种。

通常，调用者不对返回实例的内存负责，在这种情况下你使用 [takeUnretainedValue()](<../../swift/unmanaged/takeunretainedvalue().md>)，如上所示。不过，对于任何创建方法（例如 [- copy](<../nsobject-swift.class/copy().md>)），调用者负责，你应改用 [takeRetainedValue()](<../../swift/unmanaged/takeretainedvalue().md>)。有关所有权期望的描述，请参阅 [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i) 中的 [Memory Management Policy](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html#//apple_ref/doc/uid/20000994)。

由于这种不确定性，若你在使用 ARC 管理内存时提供变量选择器，编译器会生成警告。因为它无法在编译时确定返回对象的所有权，ARC 假定调用者_不_需要获取所有权，但这可能并非如此。编译器警告提醒你可能发生内存泄漏。

为避免警告，若你知道 `aSelector` 没有返回值，或许可以使用 [- performSelectorOnMainThread:withObject:waitUntilDone:](<../nsobject-swift.class/performselector(onmainthread_with_waituntildone_).md>) 或 [NSObject](../nsobject-swift.class.md) 中可用的相关方法之一。

对于更通用的解决方案，请使用 [NSInvocation](../../foundation/nsinvocation.md) 构造可以用任意参数列表和返回值调用的消息。

或者，考虑重构代码以使用块作为通过 API 传递功能块的方式。有关详细信息，请参阅 [Blocks Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502)。

> [!important] 重要
> 由于固有的缺乏类型安全，除非你的代码特别依赖 Objective-C 运行时提供的动态方法解析，否则不建议在 Swift 中使用此 API。
>
> 有关在 Swift 中使用选择器以及 [- performSelector:](<perform(__).md>) 函数替代方案的更多信息，请阅读 [Using Objective-C Runtime Features in Swift](../../swift/using-objective-c-runtime-features-in-swift.md)。

## 另请参阅

### 发送消息

- [- performSelector:withObject:](<perform(__with_).md>) — 向接收者发送带有一个对象作为参数的消息。
- [- performSelector:withObject:withObject:](<perform(__with_with_).md>) — 向接收者发送带有两个对象作为参数的消息。
