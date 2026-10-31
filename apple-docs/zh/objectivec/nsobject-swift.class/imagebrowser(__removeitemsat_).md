---
title: 'imageBrowser(_:removeItemsAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:removeitemsat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:removeitemsat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Aremoveitemsat%3A%29.json'
content_hash: 'sha256:7a2608d5a132073a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:removeItemsAt:)

<sub>实例方法</sub>

表示应对指定项目应用移除操作。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, removeItemsAt indexes: IndexSet!)
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `indexes` — 应移除的项目的索引。

## 讨论

此方法是可选的。在 Image Kit 确定应应用移除操作后，图像浏览器会调用它。作为响应，数据源应通过移除指定项目来更新自身。
