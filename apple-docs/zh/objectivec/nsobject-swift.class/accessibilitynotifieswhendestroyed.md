---
title: accessibilityNotifiesWhenDestroyed
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed.json'
content_hash: 'sha256:fb420fd97e8ed1bb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityNotifiesWhenDestroyed

<sub>实例属性</sub>

一个布尔值，指示自定义辅助功能对象在其对应 UI 元素被销毁时是否发送通知。

<sub>macOS</sub>

```swift
var accessibilityNotifiesWhenDestroyed: Bool { get }
```

## 讨论

在 macOS 10.9 及更高版本中，作为 [NSObject](../nsobject-swift.class.md) 子类的自定义辅助功能对象在满足以下条件时可以发送辅助功能通知：

- 自定义辅助功能对象的生命周期必须与 App UI 中对应元素的生命周期匹配。

通常，作为屏幕上 UI 元素代理的自定义辅助功能对象会在 App 响应辅助功能请求后立即被自动释放并释放内存。此类对象无法发送辅助功能通知，因为对象一被释放，所有已注册的观察者就会被移除。为纠正这一点，App 必须保证自定义辅助功能对象在其对应 UI 元素保持可见期间一直处于已分配状态。

- 对象必须在适当时机发送 [uiElementDestroyed](../../appkit/nsaccessibility-swift.struct/notification/uielementdestroyed.md) 通知。适当时机通常是对应 UI 元素从屏幕移除时，也可以是对象自身被释放时。
- 对象必须实现 `accessibilityNotifiesWhenDestroyed` 并返回 [YES](../yes.md)。
