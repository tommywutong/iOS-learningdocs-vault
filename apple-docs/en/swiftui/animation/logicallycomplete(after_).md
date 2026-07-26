---
title: 'logicallyComplete(after:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/logicallycomplete(after:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/logicallycomplete(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/logicallycomplete%28after%3A%29.json'
content_hash: 'sha256:ecb9fa33ea63a802'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# logicallyComplete(after:)

<sub>Instance Method</sub>

Causes the animation to report logical completion after the specified duration, if it has not already logically completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func logicallyComplete(after duration: TimeInterval) -> Animation
```

## Parameters

- `duration` — The duration after which the animation should  report that it is logically complete.

## Return Value

An animation that reports logical completion after the given duration.

## Discussion

Note that the indicated duration will not cause the animation to continue running after the base animation has fully completed.

If the animation is removed before the given duration is reached, logical completion will be reported immediately.
