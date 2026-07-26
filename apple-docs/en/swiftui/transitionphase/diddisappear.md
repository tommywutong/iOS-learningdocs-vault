---
title: TransitionPhase.didDisappear
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionphase/diddisappear
source_url: 'https://developer.apple.com/documentation/swiftui/transitionphase/diddisappear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionphase/diddisappear.json'
content_hash: 'sha256:a0b8bf6e13d13a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TransitionPhase](../transitionphase.md)

# TransitionPhase.didDisappear

<sub>Case</sub>

The transition is being applied to a view that has been requested to be removed from the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case didDisappear
```

## Discussion

In this phase, a transition should show the appearance that will be animated to make the disappearance transition.

## See Also

### Getting the phase

- [TransitionPhase.identity](identity.md) — The transition is being applied to a view that is in the view hierarchy.
- [TransitionPhase.willAppear](willappear.md) — The transition is being applied to a view that is about to be inserted into the view hierarchy.
