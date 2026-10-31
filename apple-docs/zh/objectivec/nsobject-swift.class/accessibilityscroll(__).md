---
title: 'accessibilityScroll(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityscroll(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityscroll%28_%3A%29.json'
content_hash: 'sha256:02970e1d1ba12c65'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityScroll(_:)

<sub>实例方法</sub>

以应用特定的方式滚动屏幕内容，并返回操作成功或失败。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool
```

## 参数

- `direction` — 指定滚动操作方向的常量。有效常量的说明参见 [UIAccessibilityScrollDirection](../../uikit/uiaccessibilityscrolldirection.md)。

## 返回值

如果滚动操作成功，则为 [YES](../yes.md)；否则为 [NO](../no.md)。默认情况下，此方法返回 [NO](../no.md)。

## 讨论

如果视图层次结构中的某个视图支持按页滚动操作，请实现此方法。

- 如果指定方向的滚动操作成功，返回 [YES](../yes.md) 并发送 [pageScrolled](../../uikit/uiaccessibility/notification/pagescrolled.md) 通知。
- 如果滚动操作失败，会在层次结构中的父视图上调用 `accessibilityScroll:`。

## 另请参阅

### 执行操作

- [- accessibilityActivate](<accessibilityactivate().md>) — 告知元素激活自身，并报告操作成功或失败。
- [- accessibilityIncrement](<accessibilityincrement().md>) — 告知辅助功能元素递增其内容的值。
- [- accessibilityDecrement](<accessibilitydecrement().md>) — 告知辅助功能元素递减其内容的值。
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — 关闭模态视图，并返回操作成功或失败。
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — 执行一个显著操作。
