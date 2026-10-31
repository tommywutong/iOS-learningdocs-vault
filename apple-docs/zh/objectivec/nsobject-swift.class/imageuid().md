---
title: imageUID()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imageuid()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imageuid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imageuid%28%29.json'
content_hash: 'sha256:576914081998a548'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageUID()

<sub>实例方法</sub>

返回标识数据源项的唯一字符串。

<sub>macOS</sub>

```swift
func imageUID() -> String!
```

## 返回值

标识数据源项的字符串

## 讨论

你的数据源必须实现此方法。图像浏览器视图使用此标识符将数据源项与其缓存关联。
