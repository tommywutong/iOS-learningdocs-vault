---
title: isProxy()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/isproxy()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isproxy()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/isproxy%28%29.json'
content_hash: 'sha256:ecaaeb46038ebee2'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# isProxy()

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否不继承自 [NSObject](../nsobject-swift.class.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isProxy() -> Bool
```

## 返回值

如果接收者确实继承自 [NSObject](../nsobject-swift.class.md)，则为 [NO](../no.md)；否则为 [YES](../yes.md)。

## 讨论

此方法是必要的，因为向 [NSProxy](../../foundation/nsproxy.md) 对象发送 [- isKindOfClass:](<iskind(of_).md>) 或 [- isMemberOfClass:](<ismember(of_).md>) 会测试代理对象本身，而非它所代表的对象。
