---
title: logicallyComplete
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationcompletioncriteria/logicallycomplete
source_url: 'https://developer.apple.com/documentation/swiftui/animationcompletioncriteria/logicallycomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcompletioncriteria/logicallycomplete.json'
content_hash: 'sha256:3974d4e4756cd126'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationCompletionCriteria](../animationcompletioncriteria.md)

# logicallyComplete

<sub>Type Property</sub>

The animation has logically completed, but may still be in its long tail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let logicallyComplete: AnimationCompletionCriteria
```

## Discussion

If a subsequent change occurs that creates additional animations on properties with `logicallyComplete` completion callbacks registered, then those callbacks will fire when the animations from the change that they were registered with logically complete, ignoring the new animations.

## See Also

### Getting the completion criteria

- [removed](removed.md) — The entire animation is finished and will now be removed.
