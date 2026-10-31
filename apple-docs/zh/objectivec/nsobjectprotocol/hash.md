---
title: hash
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/hash
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/hash.json'
content_hash: 'sha256:ddacbf2bd8bd46f1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# hash

<sub>实例属性</sub>

返回可用作哈希表结构中表地址的整数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: Int { get }
```

## 返回值

可用作哈希表结构中表地址的整数。

## 讨论

若两个对象相等（由 [- isEqual:](<isequal(__).md>) 方法确定），它们必须具有相同的哈希值。若你在子类中定义 [hash](hash.md) 并打算将该子类的实例放入集合，最后这一点尤为重要。

若将可变对象添加到使用哈希值确定对象在集合中位置的集合中，则该对象的 [hash](hash.md) 方法返回的值在对象位于集合中时不得更改。因此，要么 [hash](hash.md) 方法不得依赖对象的任何内部状态信息，要么你必须确保对象在集合中时其内部状态信息不更改。因此，例如，可将可变字典放入哈希表，但不得在其位于其中时更改它。（请注意，可能难以知道给定对象是否位于集合中。）

## 另请参阅

### 识别和比较对象

- [- isEqual:](<isequal(__).md>) — 返回一个布尔值，指示接收者与给定对象是否相等。
- [- self](<self().md>) — 返回接收者。
