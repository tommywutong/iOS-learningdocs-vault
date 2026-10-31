---
title: objc_msgSend
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_msgsend
source_url: 'https://developer.apple.com/documentation/objectivec/objc_msgsend'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_msgsend.json'
content_hash: 'sha256:bf2ec70cd2a2b495'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_msgSend

<sub>函数</sub>

向某个类的实例发送带有简单返回值的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void objc_msgSend();
```

## 参数

- **`self`** — 指向将接收该消息的类实例的指针。
- **`op`** — 处理该消息的方法的选择器（selector）。
- **`...`** — 包含该方法参数的可变参数列表。

## 返回值

该方法的返回值。

## 讨论

当编译器遇到方法调用时，会生成对 `objc_msgSend`、`objc_msgSend_stret`、`objc_msgSendSuper` 或 `objc_msgSendSuper_stret` 之一的调用。发送给对象超类的消息（使用 `super` 关键字）通过 `objc_msgSendSuper` 发送；其他消息通过 `objc_msgSend` 发送。返回值为数据结构的方法通过 `objc_msgSendSuper_stret` 和 `objc_msgSend_stret` 发送。

## 另请参阅

### 发送消息

- [objc_msgSend_fpret](objc_msgsend_fpret.md) — 向某个类的实例发送带有浮点返回值的消息。
- [objc_msgSend_stret](objc_msgsend_stret.md) — 向某个类的实例发送带有数据结构返回值的消息。
- [objc_msgSendSuper](objc_msgsendsuper.md) — 向某个类实例的超类发送带有简单返回值的消息。
- [objc_msgSendSuper_stret](objc_msgsendsuper_stret.md) — 向某个类实例的超类发送带有数据结构返回值的消息。
