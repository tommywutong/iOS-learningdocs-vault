---
title: 'isGreaterThan(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isgreaterthan(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isgreaterthan(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isgreaterthan%28_%3A%29.json'
content_hash: 'sha256:346be6c1be0c37c1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isGreaterThan(_:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否大于另一个给定对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func isGreaterThan(_ object: Any?) -> Bool
```

## 参数

- `object` — 用于与接收者比较的对象。

## 返回值

若接收者大于 `object` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

在求值包含运算符为 `NSGreaterThanComparison` 的测试的 `NSWhoseSpecifier` 对象期间，若潜在指定对象未实现 [- scriptingIsGreaterThan:](<scriptingisgreaterthan(__).md>) 方法，且被测对象未实现 [- scriptingIsLessThanOrEqualTo:](<scriptingislessthanorequal(to_).md>) 方法，则可能向每个潜在指定对象发送 [- isGreaterThan:](<isgreaterthan(__).md>) 消息。

由 `NSObject` 提供的此方法默认实现会在向同一对象发送 `compare:` 消息将返回 `NSOrderedDescending` 时返回 [YES](../yes.md)。
