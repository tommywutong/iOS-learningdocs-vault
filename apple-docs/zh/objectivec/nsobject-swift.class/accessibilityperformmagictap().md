---
title: accessibilityPerformMagicTap()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityperformmagictap%28%29.json'
content_hash: 'sha256:121aa73aba2bbb9f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityPerformMagicTap()

<sub>实例方法</sub>

执行一个显著操作。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityPerformMagicTap() -> Bool
```

## 返回值

如果 Magic Tap 操作成功，则为 [YES](../yes.md)；否则为 [NO](../no.md)。默认情况下，此方法返回 [NO](../no.md)。

## 讨论

此方法执行的确切操作取决于你的 App，通常用于切换 App 最重要的状态。例如，在电话 App 中接听和结束通话，在音乐 App 中播放和暂停，在时钟 App 中启动和停止计时器，在相机 App 中拍照。

## 另请参阅

### 执行操作

- [- accessibilityActivate](<accessibilityactivate().md>) — 告知元素激活自身，并报告操作成功或失败。
- [- accessibilityIncrement](<accessibilityincrement().md>) — 告知辅助功能元素递增其内容的值。
- [- accessibilityDecrement](<accessibilitydecrement().md>) — 告知辅助功能元素递减其内容的值。
- [- accessibilityScroll:](<accessibilityscroll(__).md>) — 以应用特定的方式滚动屏幕内容，并返回操作成功或失败。
- [- accessibilityPerformEscape](<accessibilityperformescape().md>) — 关闭模态视图，并返回操作成功或失败。
