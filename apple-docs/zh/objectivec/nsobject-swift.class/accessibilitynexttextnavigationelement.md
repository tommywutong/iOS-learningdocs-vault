---
title: accessibilityNextTextNavigationElement
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement.json'
content_hash: 'sha256:296a3b966f4a31d9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityNextTextNavigationElement

<sub>实例属性</sub>

包含在语义上紧随此元素文本之后的文本的辅助功能元素。

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor var accessibilityNextTextNavigationElement: Any? { get set }
```

## 讨论

辅助技术在按文本粒度导航时（例如使用 VoiceOver 的“行”转子时）会切换到这些元素。
