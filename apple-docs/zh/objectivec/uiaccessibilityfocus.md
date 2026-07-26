---
title: UIAccessibilityFocus
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/uiaccessibilityfocus
source_url: 'https://developer.apple.com/documentation/objectivec/uiaccessibilityfocus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/uiaccessibilityfocus.json'
content_hash: 'sha256:f7a1460c6dade60b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# UIAccessibilityFocus

<sub>API 集合</sub>

一个非正式协议，提供一种方式来判断像 VoiceOver 这样的辅助 App 是否聚焦在某个辅助功能元素上。

## 概述

VoiceOver 和其他辅助技术会在元素上放置一个虚拟焦点，让用户可以在不激活元素的情况下检视它。如果你知道虚拟焦点当前的位置，就可以为辅助技术的用户优化用户体验。例如，如果你的应用希望用户通过单击一次来选择某个对象、再双击来激活它，那么 VoiceOver 用户在点按选择该对象之前，必须额外多点一次才能让 VoiceOver 聚焦到该对象上。为了改善 VoiceOver 用户的体验，你可以在 VoiceOver 聚焦到某个元素的同时，将选择也移动到该元素上。这样一来，用户就无需再次点按来选择该元素，就可以直接激活它。

## 主题

### Getting focus information

- [- accessibilityElementDidBecomeFocused](<nsobject-swift.class/accessibilityelementdidbecomefocused().md>) — 在某个辅助技术将其虚拟焦点设置到该辅助功能元素上之后发送。
- [- accessibilityElementDidLoseFocus](<nsobject-swift.class/accessibilityelementdidlosefocus().md>) — 在某个辅助技术从某个辅助功能元素上移除其虚拟焦点之后发送。
- [- accessibilityElementIsFocused](<nsobject-swift.class/accessibilityelementisfocused().md>) — 返回一个布尔值，指示某个辅助技术当前是否聚焦在该辅助功能元素上。
- [- accessibilityAssistiveTechnologyFocusedIdentifiers](<nsobject-swift.class/accessibilityassistivetechnologyfocusedidentifiers().md>) — 返回一组标识符键，指示哪个辅助 App 聚焦在该辅助功能元素上。

## 另请参阅

### Related Documentation

- [Accessibility Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — 一组方法，提供关于 App 用户界面中视图和控制的辅助功能信息。
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — 提供一组方法，供视图子类用来将子组件公开为独立的辅助功能元素。
- [UIAccessibilityAction](uiaccessibilityaction.md) — 一组方法，辅助功能元素可以用它们来支持特定的动作。
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — 一对属性，可让你微调拖放操作如何暴露给辅助技术。
