---
title: 'accessibilityActivationPoint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityactivationpoint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityactivationpoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityactivationpoint%28_%3A%29.json'
content_hash: 'sha256:2e2acf4112fece2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityActivationPoint(_:)

<sub>Instance Method</sub>

The activation point for an element is the location assistive technologies use to initiate gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityActivationPoint(_ activationPoint: CGPoint) -> ModifiedContent<Content, Modifier>
```

## Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derrived from one of the accessibility elements decendents or from the center of the accessibility frame.
