---
title: 'authorizationViewDidHide(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/authorizationviewdidhide%28_%3A%29.json'
content_hash: 'sha256:d0219af3579b3ce1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# authorizationViewDidHide(_:)

<sub>实例方法</sub>

发送给委托，以指示视图的可见性已更改。

<sub>macOS</sub>

```swift
func authorizationViewDidHide(_ view: SFAuthorizationView!)
```

## 讨论

如果存在此委托方法，则每当调用 [isHidden](../../appkit/nsview/ishidden.md) 方法以显示或隐藏视图时都会调用它。
