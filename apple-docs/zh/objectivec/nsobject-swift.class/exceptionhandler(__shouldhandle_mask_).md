---
title: 'exceptionHandler(_:shouldHandle:mask:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldhandle:mask:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exceptionhandler(_:shouldhandle:mask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exceptionhandler%28_%3Ashouldhandle%3Amask%3A%29.json'
content_hash: 'sha256:7fb74c4c35d5889c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exceptionHandler(_:shouldHandle:mask:)

<sub>实例方法</sub>

由委托实现，用于评估委托方异常处理程序是否应处理给定异常。

<sub>macOS</sub>

```swift
func exceptionHandler(_ sender: NSExceptionHandler!, shouldHandle exception: NSException!, mask aMask: Int) -> Bool
```

## 参数

- `sender` — 发送该消息的 [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) 对象。

- `exception` — 描述待评估异常的 [NSException](../../foundation/nsexception.md) 对象。

- `aMask` — 指示 [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) 对象所处理异常类型的位掩码。有关可能的 `enum` 常量说明，请参阅 Logging and Handling Constants 与 System Hang Constants。

## 返回值

若要让 [NSExceptionHandler](../../exceptionhandling/nsexceptionhandler.md) 对象处理该异常则为 [YES](../yes.md)，否则为 [NO](../no.md)。
