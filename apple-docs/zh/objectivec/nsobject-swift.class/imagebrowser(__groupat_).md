---
title: 'imageBrowser(_:groupAt:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:groupat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Agroupat%3A%29.json'
content_hash: 'sha256:7c386df014d42d7e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:groupAt:)

<sub>实例方法</sub>

返回指定索引处的组。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, groupAt index: Int) -> [AnyHashable : Any]!
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `index` — 要检索的组的索引。

## 返回值

定义该组的字典。此字典中的键可以是以下任一常量：[IKImageBrowserGroupStyleKey](../../quartz/ikimagebrowsergroupstylekey.md)、[IKImageBrowserGroupBackgroundColorKey](../../quartz/ikimagebrowsergroupbackgroundcolorkey.md)、[IKImageBrowserGroupTitleKey](../../quartz/ikimagebrowsergrouptitlekey.md) 和 [IKImageBrowserGroupRangeKey](../../quartz/ikimagebrowsergrouprangekey.md)。有关这些常量的更多信息，请参阅 [IKImageBrowserView](../../quartz/ikimagebrowserview.md)。

## 讨论

此方法是可选的。
