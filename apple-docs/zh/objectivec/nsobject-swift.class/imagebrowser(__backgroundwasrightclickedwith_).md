---
title: 'imageBrowser(_:backgroundWasRightClickedWith:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:backgroundwasrightclickedwith:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:backgroundwasrightclickedwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Abackgroundwasrightclickedwith%3A%29.json'
content_hash: 'sha256:470c58cf3581ee1d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:backgroundWasRightClickedWith:)

<sub>实例方法</sub>

当用户右键点按图像浏览器视图背景时执行自定义任务。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWith event: NSEvent!)
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `event` — 调用该方法的事件。

## 讨论

此方法表示用户右键点按了背景，或在按住 Alt 键时左键点按了背景。若要在此时执行自定义任务，可以实现此方法。
