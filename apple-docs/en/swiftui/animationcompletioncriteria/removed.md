---
title: removed
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationcompletioncriteria/removed
source_url: 'https://developer.apple.com/documentation/swiftui/animationcompletioncriteria/removed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcompletioncriteria/removed.json'
content_hash: 'sha256:d7d5693418bf0245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationCompletionCriteria](../animationcompletioncriteria.md)

# removed

<sub>Type Property</sub>

The entire animation is finished and will now be removed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let removed: AnimationCompletionCriteria
```

## Discussion

If a subsequent change occurs that creates additional animations on properties with `removed` completion callbacks registered, then those callbacks will only fire when _all_ of the created animations are complete.

## See Also

### Getting the completion criteria

- [logicallyComplete](logicallycomplete.md) — The animation has logically completed, but may still be in its long tail.
