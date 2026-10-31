---
title: 'imageBrowser(_:cellWasRightClickedAt:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasrightclickedat:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasrightclickedat:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Acellwasrightclickedat%3Awith%3A%29.json'
content_hash: 'sha256:047123083607d77e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:cellWasRightClickedAt:with:)

<sub>实例方法</sub>

当用户在图像浏览器视图中右键点按某个项目时执行自定义任务。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAt index: Int, with event: NSEvent!)
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `index` — 单元格的索引。

- `event` — 调用该方法的事件。

## 讨论

此方法表示用户右键点按了浏览器中的某个项目，或在按住 Alt 键时左键点按了该项目。若要在此时执行自定义任务，可以实现此方法。
