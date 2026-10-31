---
title: objc_msgSend_stret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_msgsend_stret
source_url: 'https://developer.apple.com/documentation/objectivec/objc_msgsend_stret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_msgsend_stret.json'
content_hash: 'sha256:fb4106b6b084f095'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_msgSend_stret

<sub>函数</sub>

向某个类的实例发送带有数据结构返回值的消息。

<sub>macOS</sub>

```objc
extern void objc_msgSend_stret();
```

## 参数：

- stretAddr: 输入时，指向一块足以容纳方法返回值的内存的指针。输出时，包含方法的返回值。
- theReceiver: 指向将接收消息的类实例的指针。
- theSelector: 类型为 [SEL](sel.md) 的指针。传入处理该消息的方法的选择器。
- …: 包含方法参数的可变参数列表。

## 讨论

遇到方法调用时，编译器会生成对 `objc_msgSend`、`objc_msgSend_stret`、`objc_msgSendSuper` 或 `objc_msgSendSuper_stret` 之一的调用。发送给对象超类的消息（使用 `super` 关键字）通过 `objc_msgSendSuper` 发送；其他消息通过 `objc_msgSend` 发送。返回值为数据结构的方法通过 `objc_msgSendSuper_stret` 和 `objc_msgSend_stret` 发送。

## 另请参阅

### 发送消息

- [objc_msgSend](objc_msgsend.md) — 向某个类的实例发送带有简单返回值的消息。
- [objc_msgSend_fpret](objc_msgsend_fpret.md) — 向某个类的实例发送带有浮点返回值的消息。
- [objc_msgSendSuper](objc_msgsendsuper.md) — 向某个类实例的超类发送带有简单返回值的消息。
- [objc_msgSendSuper_stret](objc_msgsendsuper_stret.md) — 向某个类实例的超类发送带有数据结构返回值的消息。
