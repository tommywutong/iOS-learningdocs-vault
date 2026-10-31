---
title: 'numberOfItems(inImageBrowser:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/numberofitems(inimagebrowser:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/numberofitems(inimagebrowser:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/numberofitems%28inimagebrowser%3A%29.json'
content_hash: 'sha256:f2756fb6f209929e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# numberOfItems(inImageBrowser:)

<sub>实例方法</sub>

返回数据源对象管理的记录数。

<sub>macOS</sub>

```swift
func numberOfItems(inImageBrowser aBrowser: IKImageBrowserView!) -> Int
```

## 参数

- `aBrowser` — 图像浏览器视图。

## 返回值

图像浏览器视图管理的记录数。

## 讨论

你的数据源必须实现此方法。[IKImageView](../../quartz/ikimageview.md) 对象使用此方法确定应创建和显示多少个单元格。
