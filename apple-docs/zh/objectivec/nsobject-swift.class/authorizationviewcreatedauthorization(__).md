---
title: 'authorizationViewCreatedAuthorization(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewcreatedauthorization%28_%3A%29.json'
content_hash: 'sha256:803e5283d9e3f9cc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewCreatedAuthorization(_:)

<sub>实例方法</sub>

发送给委托，以指示授权对象已创建或更改。

<sub>macOS</sub>

```swift
func authorizationViewCreatedAuthorization(_ view: SFAuthorizationView!)
```

## 讨论

如果出于自身目的保存了授权对象的副本，应将其丢弃，并调用 [authorization()](<../../securityinterface/sfauthorizationview/authorization().md>) 以获取新的授权对象。
