---
title: 'imageBrowser(_:writeItemsAt:to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:writeitemsat:to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:writeitemsat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Awriteitemsat%3Ato%3A%29.json'
content_hash: 'sha256:77cbd511d4f11ad0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:writeItemsAt:to:)

<sub>实例方法</sub>

表示应开始拖放。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, writeItemsAt itemIndexes: IndexSet!, to pasteboard: NSPasteboard!) -> Int
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `itemIndexes` — 应拖动的项目的索引。

- `pasteboard` — 要将项目拷贝到的粘贴板。

## 返回值

写入粘贴板的项目数。

## 讨论

此方法是可选的。在 Image Kit 确定应开始拖放之后、拖放实际开始之前调用。
