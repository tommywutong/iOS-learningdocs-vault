---
title: 'forwardInvocation:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/forwardinvocation:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/forwardinvocation:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/forwardinvocation%3A.json'
content_hash: 'sha256:73607d864288930a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# forwardInvocation:

<sub>实例方法</sub>

由子类重写，以便将消息转发给其他对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) forwardInvocation:(NSInvocation *) anInvocation;
```

## 参数

- `anInvocation` — The invocation to forward.

## 讨论

当向对象发送它没有对应方法的消息时，运行时系统会给接收者一次机会将该消息委托给另一个接收者。它通过创建一个表示该消息的 `NSInvocation` 对象，并向接收者发送包含此 `NSInvocation` 对象作为参数的 [forwardInvocation:](forwardinvocation_.md) 消息来委托该消息。然后，接收者的 [forwardInvocation:](forwardinvocation_.md) 方法可以选择将该消息转发给另一个对象。（若该对象也无法响应此消息，它也会获得转发机会。）

因此，[forwardInvocation:](forwardinvocation_.md) 消息允许对象与其他对象建立关系，这些对象将针对某些消息代表它采取行动。在某种意义上，转发对象能够“继承”它将消息转发给的对象的一些特征。

> [!important] 重要
> 要响应你的对象本身无法识别的方法，除了 [forwardInvocation:](forwardinvocation_.md) 之外，还必须重写 [methodSignatureForSelector:](methodsignatureforselector_.md)。转发消息的机制使用从 [methodSignatureForSelector:](methodsignatureforselector_.md) 获得的信息来创建要转发的 `NSInvocation` 对象。你的重写方法必须为给定选择器提供适当的方法签名，方法是预先制定一个，或向另一个对象请求一个。

[forwardInvocation:](forwardinvocation_.md) 方法的实现有两项任务：

- 定位可以响应 `anInvocation` 中编码的消息的对象。此对象不必对所有消息都相同。
- 使用 `anInvocation` 将该消息发送给该对象。`anInvocation` 将保存结果，运行时系统将提取此结果并将其交付给原始发送者。

在简单情况下，对象仅将消息转发到一个目标（如下例中假设的 `friend` 实例变量），[forwardInvocation:](forwardinvocation_.md) 方法可以像这样简单：

```objc
- (void)forwardInvocation:(NSInvocation *)invocation
{
    SEL aSelector = [invocation selector];
 
    if ([friend respondsToSelector:aSelector])
        [invocation invokeWithTarget:friend];
    else
        [super forwardInvocation:invocation];
}
```

转发的消息必须具有固定数量的参数；不支持可变数量的参数（`printf()` 风格）。

转发消息的返回值会返回给原始发送者。可以向发送者交付所有类型的返回值：`id` 类型、结构体、双精度浮点数。

[forwardInvocation:](forwardinvocation_.md) 方法的实现可以做的不仅仅是转发消息。例如，[forwardInvocation:](forwardinvocation_.md) 可用于整合响应各种不同消息的代码，从而避免必须为每个选择器编写单独的方法。[forwardInvocation:](forwardinvocation_.md) 方法也可能让多个其他对象参与对给定消息的响应，而不是仅转发给一个对象。

`NSObject` 的 [forwardInvocation:](forwardinvocation_.md) 实现仅调用 [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) 方法；它不转发任何消息。因此，若你选择不实现 [forwardInvocation:](forwardinvocation_.md)，向对象发送无法识别的消息将引发异常。

## 另请参阅

### 转发消息

- [- forwardingTargetForSelector:](<forwardingtarget(for_).md>) — 返回应首先将无法识别的消息定向到的对象。
