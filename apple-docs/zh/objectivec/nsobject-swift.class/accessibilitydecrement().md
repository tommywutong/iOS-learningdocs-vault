---
title: accessibilityDecrement()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitydecrement()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitydecrement()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitydecrement%28%29.json'
content_hash: 'sha256:838ac69dea445642'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityDecrement()

<sub>实例方法</sub>

告知辅助功能元素递减其内容的值。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityDecrement()
```

## 讨论

如果元素具有 [adjustable](../../uikit/uiaccessibilitytraits/adjustable.md) trait，则必须实现此方法。使用此方法递减元素的值。例如，[UISlider](../../uikit/uislider.md) 对象使用此方法将其值递减适当的量。

## 另请参阅

### 执行操作

- [- accessibilityActivate](<accessibilityactivate().md>) — 告知元素激活自身，并报告该操作的成功或失败。
- [- accessibilityIncrement](<accessibilityincrement().md>) — 告知辅助功能元素增加其内容的值。
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — 以应用特定的方式滚动屏幕内容，并返回该动作的成功或失败结果。
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — 关闭一个模态视图，并返回该动作的成功或失败结果。
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — 执行一个显著动作。
