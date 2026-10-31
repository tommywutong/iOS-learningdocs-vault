---
title: accessibilityElementDidBecomeFocused()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityelementdidbecomefocused%28%29.json'
content_hash: 'sha256:35e9181467afa891'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityElementDidBecomeFocused()

<sub>实例方法</sub>

在辅助技术已将其虚拟焦点设置到辅助功能元素上之后发送。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityElementDidBecomeFocused()
```

## 讨论

如果需要知道辅助技术何时将虚拟焦点设置到辅助功能元素上，请重写 `accessibilityElementDidBecomeFocused`。

## 另请参阅

### 获取焦点信息

- [- accessibilityElementDidLoseFocus](<accessibilityelementdidlosefocus().md>) — 在辅助技术已从其辅助功能元素移除虚拟焦点之后发送。
- [- accessibilityElementIsFocused](<accessibilityelementisfocused().md>) — 返回一个布尔值，指示某个辅助技术当前是否聚焦在该辅助功能元素上。
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<accessibilityassistivetechnologyfocusedidentifiers().md>) — 返回一组标识符键，指示哪个辅助 App 聚焦在该辅助功能元素上。
