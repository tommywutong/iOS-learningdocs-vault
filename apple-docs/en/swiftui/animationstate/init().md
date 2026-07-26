---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationstate/init()
source_url: 'https://developer.apple.com/documentation/swiftui/animationstate/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationstate/init%28%29.json'
content_hash: 'sha256:f523ce7eac78e778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationState](../animationstate.md)

# init()

<sub>Initializer</sub>

Create an empty state container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

You don’t typically create an instance of [AnimationState](../animationstate.md) directly. Instead, the [AnimationContext](../animationcontext.md) provides the animation state to an instance of [CustomAnimation](../customanimation.md).
