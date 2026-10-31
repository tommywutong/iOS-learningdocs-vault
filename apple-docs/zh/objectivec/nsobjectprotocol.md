---
title: NSObjectProtocol
framework: Objective-C Runtime
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol.json'
content_hash: 'sha256:1f6e7dd8fa85bbb9'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# NSObjectProtocol

<sub>协议</sub>

对所有 Objective-C 对象都至关重要的那组方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSObjectProtocol
```

## 概述

> [!note] 注意
> 此协议导入到 Swift 时名称为 `NSObjectProtocol`。

符合此协议的对象可被视为一等对象。可以询问此类对象有关其：

- 类，以及其类在继承层次结构中的位置。
- Conformance to protocols.
- Ability to respond to a particular message.

Cocoa 根类 [NSObject](nsobject-swift.class.md) 采用此协议，因此所有继承自 [NSObject](nsobject-swift.class.md) 的对象都具有此协议描述的功能。

## 关系

- **Conforming Types**: [NSObject](nsobject-swift.class.md)

## 主题

### 识别类

- [superclass](nsobjectprotocol/superclass.md) — 返回接收者超类的类对象。

### 识别和比较对象

- [- isEqual:](<nsobjectprotocol/isequal(__).md>) — 返回一个布尔值，指示接收者与给定对象是否相等。
- [hash](nsobjectprotocol/hash.md) — 返回可用作哈希表结构中表地址的整数。
- [- self](<nsobjectprotocol/self().md>) — 返回接收者。

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<nsobjectprotocol/iskind(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例，或是否为继承自该类的任意类的实例。
- [- isMemberOfClass:](<nsobjectprotocol/ismember(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例。
- [- respondsToSelector:](<nsobjectprotocol/responds(to_).md>) — 返回一个布尔值，指示接收者是否实现或继承了可响应指定消息的方法。
- [- conformsToProtocol:](<nsobjectprotocol/conforms(to_).md>) — 返回一个布尔值，指示接收者是否符合给定协议。

### 描述对象

- [description](nsobjectprotocol/description.md) — 接收者的文本表示。
- [debugDescription](nsobjectprotocol/debugdescription.md) — 供调试器使用的接收者文本表示。

### 发送消息

- [- performSelector:](<nsobjectprotocol/perform(__).md>) — 向接收者发送指定消息并返回消息的结果。
- [- performSelector:withObject:](<nsobjectprotocol/perform(__with_).md>) — 向接收者发送带有一个对象作为参数的消息。
- [- performSelector:withObject:withObject:](<nsobjectprotocol/perform(__with_with_).md>) — 向接收者发送带有两个对象作为参数的消息。

### Identifying Proxies

- [- isProxy](<nsobjectprotocol/isproxy().md>) — 返回一个布尔值，指示接收者是否不继承自 [NSObject](nsobject-swift.class.md)。
