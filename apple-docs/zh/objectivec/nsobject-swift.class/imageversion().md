---
title: imageVersion()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imageversion()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imageversion()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imageversion%28%29.json'
content_hash: 'sha256:e6d73a9fb84f0794'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageVersion()

<sub>实例方法</sub>

返回项的版本。

<sub>macOS</sub>

```swift
func imageVersion() -> Int
```

## 返回值

项的版本。

## 讨论

此方法是可选的。接收者可以返回新版本，以告知图像浏览器不应使用该项的缓存。
