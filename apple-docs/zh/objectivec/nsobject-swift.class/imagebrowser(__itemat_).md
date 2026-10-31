---
title: 'imageBrowser(_:itemAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:itemat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:itemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Aitemat%3A%29.json'
content_hash: 'sha256:aedc196d5eba5e40'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:itemAt:)

<sub>实例方法</sub>

返回图像浏览器视图中对应于指定索引的项目对象。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, itemAt index: Int) -> Any!
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `index` — 要检索的项目的索引。

## 返回值

一个 `IKImageBrowserItem` 对象。

## 讨论

你的数据源必须实现此方法。返回的对象必须实现 IKImageBrowserItem 协议的必需方法。
