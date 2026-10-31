---
title: accessibilityCustomActions
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitycustomactions
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitycustomactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitycustomactions.json'
content_hash: 'sha256:5203df97b6ec48b0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityCustomActions

<sub>实例属性</sub>

要与内置操作一起显示的自定义操作数组。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var accessibilityCustomActions: [UIAccessibilityCustomAction]? { get set }
```

## 讨论

该数组包含一个或多个定义受支持操作的 `UIAccessibilityCustomAction` 对象。VoiceOver 等辅助技术会在适当时机向用户显示你的自定义操作。
