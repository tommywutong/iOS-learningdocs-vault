---
title: 'visible(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/threshold/visible(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold/visible(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/threshold/visible%28_%3A%29.json'
content_hash: 'sha256:2c003e36de3df880'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ScrollTransitionConfiguration](../../scrolltransitionconfiguration.md) · [Threshold](../threshold.md)

# visible(_:)

<sub>Type Method</sub>

The target view is visible by the given amount, where zero is fully hidden, and one is fully visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func visible(_ amount: Double) -> ScrollTransitionConfiguration.Threshold
```

## Discussion

Values less than zero or greater than one are clamped.

## See Also

### Getting the threshold

- [centered](centered.md) — The target view is centered within the container
- [hidden](hidden.md)
- [visible](visible.md)
