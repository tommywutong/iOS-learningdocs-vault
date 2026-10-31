---
title: 'imageBrowserSelectionDidChange(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange%28_%3A%29.json'
content_hash: 'sha256:d5777776daf14110'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowserSelectionDidChange(_:)

<sub>实例方法</sub>

在选中项更改时执行自定义任务。

<sub>macOS</sub>

```swift
func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)
```

## 参数

- `aBrowser` — 图像浏览器视图。

## 讨论

此方法表示用户更改了图像浏览器视图中的选中项。若想在此时执行自定义任务，可以实现此方法。
