---
title: 'authorizationViewShouldDeauthorize(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize%28_%3A%29.json'
content_hash: 'sha256:b47e54e543a5442a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewShouldDeauthorize(_:)

<sub>实例方法</sub>

当用户点击打开的锁图标时发送给委托。

<sub>macOS</sub>

```swift
func authorizationViewShouldDeauthorize(_ view: SFAuthorizationView!) -> Bool
```

## 讨论

委托可以在取消授权发生前对此作出反应，并通过返回 [NO](../no.md) 来避免它。当你调用 [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) 时不会调用此委托方法。

## 另请参阅

### 相关文档

- [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) — 将授权状态设置为未授权，并锁定视图中的锁图标。
