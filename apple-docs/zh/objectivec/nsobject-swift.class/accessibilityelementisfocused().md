---
title: accessibilityElementIsFocused()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityelementisfocused()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementisfocused()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityelementisfocused%28%29.json'
content_hash: 'sha256:982da76c11ebc19d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityElementIsFocused()

<sub>实例方法</sub>

返回一个布尔值，指示辅助技术是否正聚焦于该辅助功能元素。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityElementIsFocused() -> Bool
```

## 返回值

如果辅助技术虚拟聚焦于该元素，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 另请参阅

### 获取焦点信息

- [- accessibilityElementDidBecomeFocused](<accessibilityelementdidbecomefocused().md>) — 在某个辅助技术将其虚拟焦点设置到该辅助功能元素上之后发送。
- [- accessibilityElementDidLoseFocus](<accessibilityelementdidlosefocus().md>) — 在辅助技术已从其辅助功能元素移除虚拟焦点之后发送。
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<accessibilityassistivetechnologyfocusedidentifiers().md>) — 返回一组标识符键，指示哪个辅助 App 聚焦在该辅助功能元素上。
