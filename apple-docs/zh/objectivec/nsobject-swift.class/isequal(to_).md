---
title: 'isEqual(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isequal%28to%3A%29.json'
content_hash: 'sha256:a4ec26dfc6ddcfc5'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isEqual(to:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否等于另一个给定对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func isEqual(to object: Any?) -> Bool
```

## 参数

- `object` — 用于与接收者比较的对象。

## 返回值

若接收者等于 `object` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。实际上，若接收者为 `nil` 则返回 [NO](../no.md)。

## 讨论

在求值包含运算符为 `NSEqualToComparison` 的测试的 `NSWhoseSpecifier` 对象期间，若潜在指定对象和被测对象均未实现 [- scriptingIsEqualTo:](<scriptingisequal(to_).md>) 方法，则可能向每个潜在指定对象发送 [- isEqualTo:](<isequal(to_).md>) 消息。

由 `NSObject` 提供的此方法默认实现会在向同一对象发送 `isEqualTo:` 消息将返回 [YES](../yes.md) 时返回 [YES](../yes.md)。
