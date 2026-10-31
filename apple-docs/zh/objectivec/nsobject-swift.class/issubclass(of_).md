---
title: 'isSubclass(of:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/issubclass(of:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/issubclass(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/issubclass%28of%3A%29.json'
content_hash: 'sha256:e25046c275d4fad4'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isSubclass(of:)

<sub>类型方法</sub>

返回一个布尔值，指示接收类是否为给定类的子类，或与给定类相同。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func isSubclass(of aClass: AnyClass) -> Bool
```

## 参数

- `aClass` — 类对象。

## 返回值

如果接收类是 `aClass` 的子类或与之相同，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 另请参阅

### 识别类

- [+ superclass](<superclass().md>) — 返回接收者超类的类对象。
