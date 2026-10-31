---
title: 'accessibilityZoomIn(at:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/accessibilityzoomin(at:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityzoomin(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilityzoomin%28at%3A%29.json'
content_hash: 'sha256:fefad85c747fd38f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityZoomIn(at:)

<sub>实例方法</sub>

放大指定点处的内容。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func accessibilityZoomIn(at point: CGPoint) -> Bool
```

## 参数

- `point` — 用户执行放大操作的位置。

## 返回值

如果此方法成功处理缩放，则为 [YES](../yes.md)；否则为 [NO](../no.md)。默认情况下，此方法返回 [NO](../no.md)。

## 讨论

如果元素具有 [supportsZoom](../../uikit/uiaccessibilitytraits/supportszoom.md) trait，则需要实现此方法以及 [- accessibilityZoomOutAtPoint:](<accessibilityzoomout(at_).md>)。使用此方法在指定点放大。例如，如果元素允许用展开手势放大视图内容，请实现此方法，使 VoiceOver 缩放操作获得相同行为。
