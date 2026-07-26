---
title: TransitionPhase.identity
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionphase/identity
source_url: 'https://developer.apple.com/documentation/swiftui/transitionphase/identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionphase/identity.json'
content_hash: 'sha256:b16efde6ecb3dc6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TransitionPhase](../transitionphase.md)

# TransitionPhase.identity

<sub>Case</sub>

The transition is being applied to a view that is in the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case identity
```

## Discussion

In this phase, a transition should show its steady state appearance, which will generally not make any visual change to the view.

## See Also

### Getting the phase

- [TransitionPhase.willAppear](willappear.md) — The transition is being applied to a view that is about to be inserted into the view hierarchy.
- [TransitionPhase.didDisappear](diddisappear.md) — The transition is being applied to a view that has been requested to be removed from the view hierarchy.
