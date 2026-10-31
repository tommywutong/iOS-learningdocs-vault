---
title: accessibilityActivate()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityactivate()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityactivate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityactivate%28%29.json'
content_hash: 'sha256:ed89932beed028d5'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityActivate()

<sub>实例方法</sub>

告知元素激活自身，并报告操作的成功或失败。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityActivate() -> Bool
```

## 返回值

如果元素已激活则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

你可以使用此方法让复杂控件更容易被用户访问。当 VoiceOver 用户双击所选元素时，辅助功能系统会调用此方法。你对此方法的实现应激活该元素，并执行它认为合适的其他任务。例如，你可能会用此方法激活一个需要复杂手势、而 VoiceOver 用户难以执行的控件——可能是因为在 VoiceOver 运行时该手势具有不同含义。

在执行任何任务之后，返回适当的布尔值以指示成功或失败。

## 另请参阅

### 执行操作

- [- accessibilityIncrement](<accessibilityincrement().md>) — 告知辅助功能元素递增其内容的值。
- [- accessibilityDecrement](<accessibilitydecrement().md>) — 告知辅助功能元素递减其内容的值。
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — 以特定于 App 的方式滚动屏幕内容，并返回操作的成功或失败。
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — 关闭模态视图，并返回操作的成功或失败。
- [- accessibilityPerformMagicTap](<accessibilityperformmagictap().md>) — 执行一项显著操作。
