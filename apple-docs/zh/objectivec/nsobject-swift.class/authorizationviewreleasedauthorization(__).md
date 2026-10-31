---
title: 'authorizationViewReleasedAuthorization(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewreleasedauthorization%28_%3A%29.json'
content_hash: 'sha256:529aad0aa2e09729'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewReleasedAuthorization(_:)

<sub>实例方法</sub>

发送给委托，以指示即将取消授权。

<sub>macOS</sub>

```swift
func authorizationViewReleasedAuthorization(_ view: SFAuthorizationView!)
```

## 讨论

在取消授权获批之后（无论是你调用了 [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) 方法，还是用户点击了打开的锁图标且 [- authorizationViewShouldDeauthorize:](<authorizationviewshoulddeauthorize(__).md>) 委托方法未取消该操作），以及在用户被取消授权之前（也就是在调用 [- authorizationViewDidDeauthorize:](<authorizationviewdiddeauthorize(__).md>) 委托方法之前），会调用此方法。

## 另请参阅

### 相关文档

- [deauthorize(_:)](<../../securityinterface/sfauthorizationview/deauthorize(__).md>) — 将授权状态设置为未授权，并锁定视图中的锁图标。
