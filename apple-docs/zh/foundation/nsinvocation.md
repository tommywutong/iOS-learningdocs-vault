---
title: NSInvocation
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsinvocation
source_url: 'https://developer.apple.com/documentation/foundation/nsinvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinvocation.json'
content_hash: 'sha256:bb89b0eabe95b204'
translated: true
---

> 导航： [技术](../technologies.md) · [Foundation](../foundation.md)

# NSInvocation

<sub>类</sub>

一个被呈现为对象的 Objective-C 消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSInvocation : NSObject
```

## 概述

[NSInvocation](nsinvocation.md) 对象用于在对象之间以及应用程序之间存储和转发消息，主要由 [Timer](timer.md) 对象和分布式对象（distributed objects）系统使用。一个 [NSInvocation](nsinvocation.md) 对象包含 Objective-C 消息的全部要素：目标、选择器（selector）、参数以及返回值。其中每个要素都可以直接设置，而返回值会在该 [NSInvocation](nsinvocation.md) 对象被派发时自动设置。

一个 [NSInvocation](nsinvocation.md) 对象可以反复派发给不同的目标；可以在各次派发之间修改其参数以得到不同结果；甚至可以把它的选择器改成另一个具有相同方法签名（参数与返回类型）的选择器。这种灵活性使 [NSInvocation](nsinvocation.md) 适合用于重复发送带有大量参数和变化形式的消息；与其为每条消息重新输入略有不同的表达式，不如在每次派发给新目标之前按需修改该 [NSInvocation](nsinvocation.md) 对象。

[NSInvocation](nsinvocation.md) 不支持对具有可变数量参数或 `union` 参数的方法的调用。你应当使用 [invocationWithMethodSignature:](nsinvocation/invocationwithmethodsignature_.md) 类方法来创建 [NSInvocation](nsinvocation.md) 对象；不应使用 [alloc](../objectivec/nsobject-swift.class/alloc.md) 和 [init()](<../objectivec/nsobject-swift.class/init().md>) 来创建这些对象。

默认情况下，此类不会保留所含调用的参数。如果这些对象可能在你创建 [NSInvocation](nsinvocation.md) 实例之后、使用它之前消失，你应当自己显式保留这些对象，或者调用 [retainArguments](nsinvocation/retainarguments.md) 方法，让调用对象自行保留它们。

> [!note] 注意
> [NSInvocation](nsinvocation.md) 遵循 [NSCoding](nscoding.md) 协议，但仅支持由 [NSPortCoder](nsportcoder.md) 进行编码。[NSInvocation](nsinvocation.md) 不支持归档。

## 关系

- **继承自**： [NSObject](../objectivec/nsobject-swift.class.md)

## 主题

### 创建 NSInvocation 对象

- [invocationWithMethodSignature:](nsinvocation/invocationwithmethodsignature_.md) — 返回一个能够使用给定方法签名构造消息的 `NSInvocation` 对象。

### 配置调用对象

- [selector](nsinvocation/selector.md) — 接收者的选择器；若尚未设置则为 0。
- [target](nsinvocation/target.md) — 接收者的目标；若接收者没有目标则为 `nil`。
- [setArgument:atIndex:](nsinvocation/setargument_atindex_.md) — 设置接收者的一个参数。
- [getArgument:atIndex:](nsinvocation/getargument_atindex_.md) — 通过间接方式返回接收者在指定索引处的参数。
- [argumentsRetained](nsinvocation/argumentsretained.md) — 一个布尔值，指示接收者是否已保留其参数。
- [retainArguments](nsinvocation/retainarguments.md) — 若接收者尚未这样做，则保留接收者的目标及其所有对象参数，并复制其所有 C 字符串参数和 block。若已设置返回值，该返回值也会被保留或复制。
- [setReturnValue:](nsinvocation/setreturnvalue_.md) — 设置接收者的返回值。
- [getReturnValue:](nsinvocation/getreturnvalue_.md) — 获取该调用的返回值。

### 派发调用

- [invoke](nsinvocation/invoke.md) — 将接收者的消息（连同参数）发送给其目标，并设置返回值。
- [invokeWithTarget:](nsinvocation/invokewithtarget_.md) — 设置接收者的目标，将该消息（连同参数）发送给该目标，并设置返回值。

### 获取方法签名

- [methodSignature](nsinvocation/methodsignature.md) — 接收者的方法签名。

### 实例方法

- [invokeUsingIMP:](nsinvocation/invokeusingimp_.md)

## 另请参阅

### 调用

- [NSMethodSignature](nsmethodsignature.md) — 记录某个方法的返回值与参数的类型信息。
