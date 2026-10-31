---
title: NSMethodSignature
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmethodsignature
source_url: 'https://developer.apple.com/documentation/foundation/nsmethodsignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmethodsignature.json'
content_hash: 'sha256:ff6d724e63524807'
translated: true
---

> 导航： [技术](../technologies.md) · [Foundation](../foundation.md)

# NSMethodSignature

<sub>类</sub>

记录方法返回值与参数类型信息的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface NSMethodSignature : NSObject
```

## 概述

使用 [NSMethodSignature](nsmethodsignature.md) 对象转发接收对象不响应的消息——最典型的场景是分布式对象（distributed objects）。你通常使用 [NSObject](../objectivec/nsobject-swift.class.md) 的实例方法 [methodSignatureForSelector:](../objectivec/nsobject-swift.class/methodsignatureforselector_.md) 创建 [NSMethodSignature](nsmethodsignature.md) 对象（在 macOS 10.5 及更高版本中，也可以使用 [signatureWithObjCTypes:](nsmethodsignature/signaturewithobjctypes_.md)）。随后用它创建 [NSInvocation](nsinvocation.md) 对象，并作为参数传给 [forwardInvocation:](../objectivec/nsobject-swift.class/forwardinvocation_.md) 消息，以便将该调用转发给能够处理该消息的其他对象。在默认情况下，[NSObject](../objectivec/nsobject-swift.class.md) 会调用 [doesNotRecognizeSelector(_:)](<../objectivec/nsobject-swift.class/doesnotrecognizeselector(__).md>)，从而引发异常。对于分布式对象，[NSInvocation](nsinvocation.md) 对象会使用 [NSMethodSignature](nsmethodsignature.md) 对象中的信息进行编码，并发送给该消息接收者所代表的真实对象。

### 类型编码

`NSMethodSignature` 对象使用一组字符进行初始化，这些字符表示方法返回类型和参数类型的字符串编码。你可以使用 `@encode()` 编译器指令获取特定类型的字符串编码。由于字符串编码取决于具体实现，因此不应硬编码这些值。

方法签名由一个或多个表示方法返回类型的字符组成，后跟隐式参数 `self` 和 `_cmd` 的字符串编码，再后跟零个或多个显式参数。你可以使用 [methodReturnType](nsmethodsignature/methodreturntype.md) 和 [methodReturnLength](nsmethodsignature/methodreturnlength.md) 属性确定返回类型的字符串编码及其长度。你可以使用 [getArgumentTypeAtIndex:](nsmethodsignature/getargumenttypeatindex_.md) 方法和 [numberOfArguments](nsmethodsignature/numberofarguments.md) 属性逐个访问参数。

例如，`NSString` 实例方法 [- containsString:](<nsstring/contains(__).md>) 的方法签名具有以下参数：

1. `@encode(BOOL)` (`c`) 表示返回类型
2. `@encode(id)` (`@`) 表示接收者（`self`）
3. `@encode(SEL)` (`:`) 表示选择器（`_cmd`）
4. `@encode(NSString *)` (`@`) 表示第一个显式参数

更多信息请参阅 [Objective-C 运行时编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) 中的 [类型编码](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

## 主题

### 创建方法签名对象

- [signatureWithObjCTypes:](nsmethodsignature/signaturewithobjctypes_.md) — 根据给定的 Objective-C 方法类型字符串返回一个 `NSMethodSignature` 对象。

### 获取参数类型信息

- [getArgumentTypeAtIndex:](nsmethodsignature/getargumenttypeatindex_.md) — 返回给定索引处参数的类型编码。
- [numberOfArguments](nsmethodsignature/numberofarguments.md) — 接收者中记录的参数个数。
- [frameLength](nsmethodsignature/framelength.md) — 所有参数合在一起在栈上占用的字节数。

### 获取返回类型信息

- [methodReturnType](nsmethodsignature/methodreturntype.md) — 以 Objective-C 类型编码表示该方法返回类型的 C 字符串。
- [methodReturnLength](nsmethodsignature/methodreturnlength.md) — 返回值所需的字节数。

### 确定同步状态

- [isOneway](nsmethodsignature/isoneway.md) — 通过分布式对象调用时，接收者是否为异步。

## 另请参阅

### 调用

- [NSInvocation](nsinvocation.md) — 以对象形式呈现的 Objective-C 消息。
