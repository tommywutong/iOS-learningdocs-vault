---
title: accessibilityPerformEscape()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityperformescape()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformescape()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityperformescape%28%29.json'
content_hash: 'sha256:cb4ad554c4479838'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityPerformEscape()

<sub>实例方法</sub>

关闭模态视图，并返回操作成功或失败。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityPerformEscape() -> Bool
```

## 返回值

如果模态视图成功关闭，则为 [YES](../yes.md)；否则为 [NO](../no.md)。默认情况下，此方法返回 [NO](../no.md)。

## 讨论

在可以以模态方式或在层次结构中显示的元素或容器视图上实现此方法。当 VoiceOver 用户执行关闭操作时，此方法会关闭该视图。例如，你可以为弹出框实现此方法，以便为用户提供可执行的明确关闭操作来关闭弹出框。

## 另请参阅

### 执行操作

- [- accessibilityActivate](<accessibilityactivate().md>) — 告知元素激活自身，并报告操作成功或失败。
- [- accessibilityIncrement](<accessibilityincrement().md>) — 告知辅助功能元素递增其内容的值。
- [- accessibilityDecrement](<accessibilitydecrement().md>) — 告知辅助功能元素递减其内容的值。
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — 以应用特定的方式滚动屏幕内容，并返回操作成功或失败。
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — 执行一个显著操作。
