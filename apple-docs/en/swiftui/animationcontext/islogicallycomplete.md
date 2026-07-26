---
title: isLogicallyComplete
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationcontext/islogicallycomplete
source_url: 'https://developer.apple.com/documentation/swiftui/animationcontext/islogicallycomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcontext/islogicallycomplete.json'
content_hash: 'sha256:45e261ad64be84e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationContext](../animationcontext.md)

# isLogicallyComplete

<sub>Instance Property</sub>

Set this to `true` to indicate that an animation is logically complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLogicallyComplete: Bool
```

## Discussion

This controls when AnimationCompletionCriteria.logicallyComplete completion callbacks are fired. This should be set to `true` at most once in the life of an animation, changing back to `false` later will be ignored. If this is never set to `true`, the behavior is equivalent to if this had been set to `true` just as the animation finished (by returning `nil`).
