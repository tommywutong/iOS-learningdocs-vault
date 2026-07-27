---
title: UIAccessibilityDragging
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/uiaccessibilitydragging
source_url: 'https://developer.apple.com/documentation/objectivec/uiaccessibilitydragging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/uiaccessibilitydragging.json'
content_hash: 'sha256:77cc74fdfe25b759'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# UIAccessibilityDragging

<sub>API 集合</sub>

一对属性，可让你微调拖放操作如何暴露给辅助技术。

## 概述

默认情况下，如果一个可辅助访问的视图或其子树具有拖动和/或放置交互，辅助技术会自动将其暴露出来。但是，如果存在不止一个这样的交互，每个拖动或放置都应该有一个名称来消除歧义，从而提供良好的用户体验。此外，在某些情况下，你可能希望从某个元素暴露拖动或放置操作，而这些交互安装在不属于该元素视图层级结构子树的视图上。

当该元素根本不是一个视图，而是 `UIAccessibilityElement` 的一个实例时，就属于这种情况，而且这种情况很直观。

另一个例子是，某个容器视图维护着与其子视图在逻辑上相关联的交互。

例如，`UITableView` 关联了允许拖动其行的拖动交互；为了让辅助技术能够拖动这些行，`UITableViewCell` 提供了拖动描述符，描述在表格视图中的哪个位置开始拖动才能激活该单元格的拖动。

> [!note] Note
> 这里提到的实现细节仅用于说明目的，可能随时发生变化，恕不另行通知。

这里定义的属性可让你微调拖放操作如何暴露给辅助技术。这两个属性的 getter 方法都可以被重写，以按需提供信息。

对于每个位置描述符，其关联的视图应该是拥有该拖动或放置对应的合适 `UIInteraction` 对象的 `UIView`。

## 主题

### Fine-Tuning Drag and Drop

- [accessibilityDragSourceDescriptors](nsobject-swift.class/accessibilitydragsourcedescriptors.md) — 一个位置描述符对象数组，用来定义可以从该元素发起哪些拖动。
- [accessibilityDropPointDescriptors](nsobject-swift.class/accessibilitydroppointdescriptors.md) — 一个位置描述符对象数组，用来定义在该元素上的哪些位置可以进行放置。

## 另请参阅

### 相关文档

- [Accessibility Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785)

### Improving Accessibility

- [UIAccessibility](../uikit/uiaccessibility-protocol.md) — 一组方法，提供关于 App 用户界面中视图和控制的辅助功能信息。
- [UIAccessibilityContainer](../uikit/uiaccessibilitycontainer.md) — 提供一组方法，供视图子类用来将子组件公开为独立的辅助功能元素。
- [UIAccessibilityAction](uiaccessibilityaction.md) — 一组方法，辅助功能元素可以用它们来支持特定的动作。
- [UIAccessibilityFocus](uiaccessibilityfocus.md) — 一个非正式协议，提供一种方式来判断像 VoiceOver 这样的辅助 App 是否聚焦在某个辅助功能元素上。
