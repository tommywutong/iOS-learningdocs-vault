---
title: 'isEqual(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/isequal(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isequal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/isequal%28_%3A%29.json'
content_hash: 'sha256:76da95a58aac7d42'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isEqual(_:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者与给定对象是否相等。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(_ object: Any?) -> Bool
```

## 参数

- `object` — 要与接收者比较的对象。可以为 `nil`，此时此方法返回 [NO](../no.md)。

## 返回值

若接收者与 `anObject` 相等则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

此方法定义了实例相等的含义。例如，容器对象可能会定义：若两个容器中对应的对象都对 [- isEqual:](<isequal(__).md>) 请求返回 [YES](../yes.md)，则这两个容器相等。有关此方法用法的示例，请参见 [NSData](../../foundation/nsdata.md)、[NSDictionary](../../foundation/nsdictionary.md)、[NSArray](../../foundation/nsarray.md) 和 [NSString](../../foundation/nsstring.md) 类规范。

若两个对象相等，它们必须具有相同的哈希值。若你在子类中定义 [- isEqual:](<isequal(__).md>) 并打算将该子类的实例放入集合中，这一点尤为重要。请确保也在子类中定义 [hash](hash.md)。

## 另请参阅

### 识别和比较对象

- [hash](hash.md) — 返回可用作哈希表结构中表地址的整数。
- [- self](<self().md>) — 返回接收者。
