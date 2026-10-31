---
title: 'imageBrowser(_:moveItemsAt:to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/imagebrowser(_:moveitemsat:to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:moveitemsat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/imagebrowser%28_%3Amoveitemsat%3Ato%3A%29.json'
content_hash: 'sha256:cb0cc25beb07110a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# imageBrowser(_:moveItemsAt:to:)

<sub>实例方法</sub>

发出信号，指示应将指定项目移动到指定目标位置。

<sub>macOS</sub>

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, moveItemsAt indexes: IndexSet!, to destinationIndex: Int) -> Bool
```

## 参数

- `aBrowser` — 图像浏览器视图。

- `indexes` — 应重新排序的项目的索引。

- `destinationIndex` — 项目应移动到的目标起始索引。

## 返回值

成功则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

此方法是可选的。在 Image Kit 确定应应用重新排序操作后，由图像浏览器视图调用。数据源应通过重新排序其元素来更新自身。

## 另请参阅

### 相关文档

- [setAllowsReordering(_:)](<../../quartz/ikimagebrowserview/setallowsreordering(__).md>) — 控制用户是否可以重新排序项目。
