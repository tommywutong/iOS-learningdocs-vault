---
title: UIAccessibilityAction
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/uiaccessibilityaction
source_url: 'https://developer.apple.com/documentation/objectivec/uiaccessibilityaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/uiaccessibilityaction.json'
content_hash: 'sha256:d6134225ae5a6892'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# UIAccessibilityAction

<sub>API 集合</sub>

一组方法，辅助功能元素可以用它们来支持特定的动作。

## 概述

`UIAccessibilityAction` 这个非正式协议为辅助功能元素提供了一种支持特定动作的方式，例如在某个范围内选择值，或滚动查看屏幕上的信息。例如，为了响应滚动手势，你需要实现 [- accessibilityScroll:](<nsobject-swift.class/accessibilityscroll(__).md>) 方法，并附带新的页面状态（例如「第 3 页，共 9 页」）发布 [pageScrolled](../uikit/uiaccessibility/notification/pagescrolled.md)。或者，要让滑块或选择器视图这类元素具备辅助功能，你首先需要通过包含 [adjustable](../uikit/uiaccessibilitytraits/adjustable.md) 特性来对其进行描述。然后，你必须实现 [- accessibilityIncrement](<nsobject-swift.class/accessibilityincrement().md>) 和 [- accessibilityDecrement](<nsobject-swift.class/accessibilitydecrement().md>) 方法。这样做之后，辅助技术的用户就可以使用该辅助技术特有的手势来调整该元素。

## 主题

### Performing an action

- [- accessibilityActivate](<nsobject-swift.class/accessibilityactivate().md>) — 告知元素激活自身，并报告该操作的成功或失败。
- [- accessibilityIncrement](<nsobject-swift.class/accessibilityincrement().md>) — 告知辅助功能元素增加其内容的值。
- [- accessibilityDecrement](<nsobject-swift.class/accessibilitydecrement().md>) — 告知辅助功能元素减少其内容的值。
- [- accessibilityScroll:](<nsobject-swift.class/accessibilityscroll(__).md>) — 以应用特定的方式滚动屏幕内容，并返回该动作的成功或失败结果。
- [- accessibilityPerformEscape](<nsobject-swift.class/accessibilityperformescape().md>) — 关闭一个模态视图，并返回该动作的成功或失败结果。
- [- accessibilityPerformMagicTap](<nsobject-swift.class/accessibilityperformmagictap().md>) — 执行一个显著动作。

### Accessing custom actions

- [accessibilityCustomActions](nsobject-swift.class/accessibilitycustomactions.md) — 与内置动作一起显示的自定义动作数组。

### Constants

- [UIAccessibilityScrollDirection](../uikit/uiaccessibilityscrolldirection.md) — 滚动动作的方向。

## 另请参阅

### Related Documentation

- [Accessibility Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — 一组方法，提供关于 App 用户界面中视图和控制的辅助功能信息。
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — 提供一组方法，供视图子类用来将子组件公开为独立的辅助功能元素。
- [UIAccessibilityFocus](uiaccessibilityfocus.md) — 一个非正式协议，提供一种方式来判断像 VoiceOver 这样的辅助 App 是否聚焦在某个辅助功能元素上。
- [UIAccessibilityDragging](uiaccessibilitydragging.md) — 一对属性，可让你微调拖放操作如何暴露给辅助技术。
