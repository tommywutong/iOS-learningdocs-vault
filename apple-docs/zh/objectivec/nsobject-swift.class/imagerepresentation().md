---
title: imageRepresentation()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imagerepresentation()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagerepresentation%28%29.json'
content_hash: 'sha256:54f2d0acd95339cf'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageRepresentation()

<sub>实例方法</sub>

返回要显示的图像。

<sub>macOS</sub>

```swift
func imageRepresentation() -> Any!
```

## 返回值

要显示的图像；如果该项没有要显示的图像，可以返回 `nil`。

## 讨论

你的数据源必须实现此方法。此方法会被频繁调用，因此接收者应缓存返回的实例。
