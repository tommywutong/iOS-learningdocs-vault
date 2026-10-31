---
title: accessibilityTextInputResponder
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponder
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitytextinputresponder.json'
content_hash: 'sha256:884758004de5622d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityTextInputResponder

<sub>实例属性</sub>

处理此辅助功能元素文本输入调用的对象。

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor weak var accessibilityTextInputResponder: (any UITextInput)? { get set }
```

## 讨论

如果你的辅助功能元素表示使用 [UITextInput](../../uikit/uitextinput.md) 协议支持文本操作的视图，请使用此属性将 `UITextInput` 调用转发到后备视图。
