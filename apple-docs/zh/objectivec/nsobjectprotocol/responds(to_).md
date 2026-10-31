---
title: 'responds(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/responds(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/responds(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/responds%28to%3A%29.json'
content_hash: 'sha256:bf23290f06079660'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# responds(to:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否实现或继承了可以响应指定消息的方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func responds(to aSelector: Selector!) -> Bool
```

## 参数

- `aSelector` — A selector that identifies a message.

## 返回值

若接收者实现或继承了可以响应 `aSelector` 的方法，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

应用程序负责确定是否应将 [NO](../no.md) 响应视为错误。

你不能通过使用 `super` 关键字向对象发送 [- respondsToSelector:](<responds(to_).md>) 来测试对象是否从其超类继承了方法。此方法仍将测试整个对象，而不仅仅是超类的实现。因此，向 `super` 发送 [- respondsToSelector:](<responds(to_).md>) 等效于向 `self` 发送。相反，你必须直接在对象的超类上调用 `NSObject` 类方法 [+ instancesRespondToSelector:](<../nsobject-swift.class/instancesrespond(to_).md>)，如下列代码片段所示。

```objc
if( [MySuperclass instancesRespondToSelector:@selector(aMethod)] ) {
    // invoke the inherited method
    [super aMethod];
}
```

你不能简单地使用 `[[self superclass] instancesRespondToSelector:@selector(aMethod)]`，因为若由子类调用，这可能导致该方法失败。

请注意，若接收者能够将 `aSelector` 消息转发给另一个对象，则它将能够响应该消息（尽管是间接的），即使此方法返回 [NO](../no.md)。

## 另请参阅

### 相关文档

- [+ instancesRespondToSelector:](<../nsobject-swift.class/instancesrespond(to_).md>) — 返回一个布尔值，指示接收者的实例是否能够响应给定选择器。

### Testing Object Inheritance, Behavior, and Conformance

- [- isKindOfClass:](<iskind(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例，或是否为继承自该类的任意类的实例。
- [- isMemberOfClass:](<ismember(of_).md>) — 返回一个布尔值，指示接收者是否为给定类的实例。
- [- conformsToProtocol:](<conforms(to_).md>) — 返回一个布尔值，指示接收者是否符合给定协议。
