---
title: objc_msgSend_fpret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_msgsend_fpret
source_url: 'https://developer.apple.com/documentation/objectivec/objc_msgsend_fpret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_msgsend_fpret.json'
content_hash: 'sha256:b4b1d31195ac45a1'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_msgSend_fpret

<sub>函数</sub>

向某个类的实例发送带有浮点返回值的消息。

<sub>macOS</sub>

```objc
extern void objc_msgSend_fpret();
```

## 参数

- **`self`** — 指向将接收消息的类实例的指针。
- **`op`** — 处理该消息的方法的选择器。
- **`...`** — 包含方法参数的可变参数列表。

## 讨论

在 i386 平台上，返回浮点值的函数的 ABI 与返回整数类型的函数不兼容。因此，在 i386 平台上，对于返回非整数类型的函数，_必须_ 使用 `objc_msgSend_fpret`。对于 `float` 或 `long double` 返回类型，请先将函数强制转换为适当的函数指针类型。

此函数不在 PPC 或 PPC64 平台上使用。

## 另请参阅

### 发送消息

- [objc_msgSend](objc_msgsend.md) — 向某个类的实例发送带有简单返回值的消息。
- [objc_msgSend_stret](objc_msgsend_stret.md) — 向某个类的实例发送带有数据结构返回值的消息。
- [objc_msgSendSuper](objc_msgsendsuper.md) — 向某个类实例的超类发送带有简单返回值的消息。
- [objc_msgSendSuper_stret](objc_msgsendsuper_stret.md) — 向某个类的实例的超类发送带有数据结构返回值的消息。
