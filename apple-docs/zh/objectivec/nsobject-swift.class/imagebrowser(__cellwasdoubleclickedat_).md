---
title: 'imageBrowser(_:cellWasDoubleClickedAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasdoubleclickedat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasdoubleclickedat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Acellwasdoubleclickedat%3A%29.json'
content_hash: 'sha256:60b1217244980184'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:cellWasDoubleClickedAt:)

<sub>实例方法</sub>

当用户在图像浏览器视图中双击某个项目时执行自定义任务。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAt index: Int)
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `index` — 单元格的索引。

## 讨论

此方法表示用户在图像浏览器视图中双击了某个项目。若要在此时执行自定义任务，可以实现此方法。
