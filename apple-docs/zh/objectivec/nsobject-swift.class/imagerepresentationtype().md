---
title: imageRepresentationType()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/imagerepresentationtype()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagerepresentationtype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagerepresentationtype%28%29.json'
content_hash: 'sha256:941a597ff4422c2f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageRepresentationType()

<sub>实例方法</sub>

返回要显示图像的表示类型。

<sub>macOS</sub>

```swift
func imageRepresentationType() -> String!
```

## 返回值

指定图像表示类型的字符串。该字符串可以是 [Image Representation Types](../../quartz/image-representation-types.md) 中定义的任意常量。

## 讨论

你的数据源必须实现此方法。
