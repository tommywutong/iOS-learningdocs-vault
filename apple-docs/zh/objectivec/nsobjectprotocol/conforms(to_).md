---
title: 'conforms(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/conforms(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/conforms(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/conforms%28to%3A%29.json'
content_hash: 'sha256:1e73b58ac38d978c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# conforms(to:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否符合给定协议。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func conforms(to aProtocol: Protocol) -> Bool
```

## 参数

- `aProtocol` — 表示特定协议的协议对象。

## 返回值

若接收者符合 `aProtocol` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

此方法与 [NSObject](../nsobject-swift.class.md) 中声明的 [+ conformsToProtocol:](<../nsobject-swift.class/conforms(to_).md>) 类方法完全相同。提供它是为了方便，这样你无需获取类对象即可了解实例是否能响应给定的一组消息。

## 另请参阅

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例，或是否为继承自该类的任意类的实例。
- [- isMemberOfClass:](<ismember(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例。
- [- respondsToSelector:](<responds(to_).md>) — 返回一个布尔值，指示接收者是否实现或继承了可响应指定消息的方法。
