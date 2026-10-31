---
title: accessibilityAssistiveTechnologyFocusedIdentifiers()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers%28%29.json'
content_hash: 'sha256:7f0909d4b9b23ca8'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityAssistiveTechnologyFocusedIdentifiers()

<sub>实例方法</sub>

返回一组标识符键，指示哪个辅助 App 聚焦于该辅助功能元素。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<UIAccessibility.AssistiveTechnologyIdentifier>?
```

## 另请参阅

### 获取焦点信息

- [- accessibilityElementDidBecomeFocused](<accessibilityelementdidbecomefocused().md>) — 在辅助技术将其虚拟焦点设置到辅助功能元素之后发送。
- [- accessibilityElementDidLoseFocus](<accessibilityelementdidlosefocus().md>) — 在辅助技术从其虚拟焦点移除某个辅助功能元素之后发送。
- [- accessibilityElementIsFocused](<accessibilityelementisfocused().md>) — 返回一个布尔值，指示辅助技术是否聚焦于该辅助功能元素。
