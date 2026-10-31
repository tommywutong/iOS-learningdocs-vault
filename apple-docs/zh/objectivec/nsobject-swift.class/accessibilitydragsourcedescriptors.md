---
title: accessibilityDragSourceDescriptors
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitydragsourcedescriptors
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydragsourcedescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitydragsourcedescriptors.json'
content_hash: 'sha256:2aabd4989ee70ae7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityDragSourceDescriptors

<sub>实例属性</sub>

用于定义可从此元素发起哪些拖移的位置描述符对象数组。

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor var accessibilityDragSourceDescriptors: [UIAccessibilityLocationDescriptor]? { get set }
```

## 讨论

要恢复此属性的默认自动行为，请赋值或返回默认值 `nil`。

> [!note] 注意
> `nil` 值所描述的行为与空数组不同；空数组表示此元素没有任何相关交互。

## 另请参阅

### Fine-Tuning Drag and Drop

- [accessibilityDropPointDescriptors](accessibilitydroppointdescriptors.md) — 一个位置描述符对象数组，用来定义在该元素上的哪些位置可以进行放置。
