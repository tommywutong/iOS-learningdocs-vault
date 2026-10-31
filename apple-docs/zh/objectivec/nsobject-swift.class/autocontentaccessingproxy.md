---
title: autoContentAccessingProxy
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/autocontentaccessingproxy.json'
content_hash: 'sha256:13861320fdf8ecd9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# autoContentAccessingProxy

<sub>实例属性</sub>

接收对象的代理

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var autoContentAccessingProxy: Any { get }
```

## 讨论

如果接收者采用了 [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) 协议且仍有尚未丢弃的内容，此属性会返回接收对象的代理。

该代理会对接收者调用 [beginContentAccess()](<../../foundation/nsdiscardablecontent/begincontentaccess().md>)，以在代理存活期间保持内容可用，并在代理被释放时调用 [endContentAccess()](<../../foundation/nsdiscardablecontent/endcontentaccess().md>)。

除此之外，该包装对象是 [NSProxy](../../foundation/nsproxy.md) 的子类，并像 [NSProxy](../../foundation/nsproxy.md) 一样将消息转发给原始接收对象。

此方法可用于通过创建一个响应相同消息、但在所创建代理存活期间保持原始接收者内容可用的对象，来隐藏 [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) 对象的内容易失性。如此隐藏后，可将该 [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) 对象（通过代理）交给不知情的接收方；否则这些接收方可能不知道，在特定用法（取决于每个 [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) 对象）中需要围绕对该 [NSDiscardableContent](../../foundation/nsdiscardablecontent.md) 对象的使用调用 [beginContentAccess()](<../../foundation/nsdiscardablecontent/begincontentaccess().md>) 和 [endContentAccess()](<../../foundation/nsdiscardablecontent/endcontentaccess().md>)。
