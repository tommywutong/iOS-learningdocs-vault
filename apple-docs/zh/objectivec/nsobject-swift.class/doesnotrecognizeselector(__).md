---
title: 'doesNotRecognizeSelector(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector%28_%3A%29.json'
content_hash: 'sha256:a0b1b13ad150561c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# doesNotRecognizeSelector(_:)

<sub>实例方法</sub>

处理接收者不识别的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func doesNotRecognizeSelector(_ aSelector: Selector!)
```

## 参数

- `aSelector` — 标识接收者未实现或不识别的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

## 讨论

每当对象收到无法响应或转发的 `aSelector` 消息时，运行时系统都会调用此方法。此方法随之引发 `NSInvalidArgumentException` 并生成错误消息。

任何 [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) 消息通常仅由运行时系统发送。不过，也可在程序代码中使用它们以阻止方法被继承。例如，`NSObject` 子类可以通过重新实现 [- copy](<copy().md>) 或 [- init](<init().md>) 方法并在其中包含 [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) 消息来放弃这些方法，如下所示：

```objc
- (id)copy
{
    [self doesNotRecognizeSelector:_cmd];
}
```

`_cmd` 变量是传给每个方法的隐藏参数，表示当前选择器；在此示例中，它标识 `copy` 方法的选择器。此代码可防止子类实例响应 `copy` 消息，也防止超类转发 `copy` 消息——尽管 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) 仍会报告接收者可以访问 `copy` 方法。

若重写此方法，必须在实现末尾调用 `super` 或引发 [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) 异常。换言之，此方法不得正常返回；它必须始终导致抛出异常。
