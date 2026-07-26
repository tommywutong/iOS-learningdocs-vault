---
title: 'accessibilityActivationPoint(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilityactivationpoint(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityactivationpoint(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilityactivationpoint%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:ec7af403d379cac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilityActivationPoint(_:isEnabled:)

<sub>Instance Method</sub>

The activation point for an element is the location assistive technologies use to initiate gestures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilityActivationPoint(_ activationPoint: CGPoint, isEnabled: Bool) -> ModifiedContent<Content, Modifier>
```

## Parameters

- `activationPoint` — The accessibility activation point to apply.

- `isEnabled` — If true the accessibility activation point is applied; otherwise the accessibility activation point is unchanged.

## Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derived from one of the accessibility elements decedents or from the center of the accessibility frame.
