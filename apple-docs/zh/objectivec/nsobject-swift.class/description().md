---
title: description()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/description()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/description()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/description%28%29.json'
content_hash: 'sha256:d79532bbf97fac45'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# description()

<sub>类型方法</sub>

返回表示接收类内容的字符串。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func description() -> String
```

## 返回值

表示接收类内容的字符串。

## 讨论

调试器的 print-object 命令会调用此方法以生成对象的文本描述。

`NSObject` 对此方法的实现仅打印类的名称。

## 另请参阅

### 相关文档

- [description](../nsobjectprotocol/description.md) — 接收者的文本表示。
