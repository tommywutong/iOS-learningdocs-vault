---
title: ScrollTransitionPhase.identity
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltransitionphase/identity
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionphase/identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionphase/identity.json'
content_hash: 'sha256:872811ae2e288c00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionPhase](../scrolltransitionphase.md)

# ScrollTransitionPhase.identity

<sub>Case</sub>

The scroll transition is being applied to a view that is in the visible area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case identity
```

## Discussion

In this phase, a transition should show its steady state appearance, which will generally not make any visual change to the view.

## See Also

### Getting the phase

- [ScrollTransitionPhase.topLeading](topleading.md) — The scroll transition is being applied to a view that is about to move into the visible area at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.
- [ScrollTransitionPhase.bottomTrailing](bottomtrailing.md) — The scroll transition is being applied to a view that is about to move into the visible area at the bottom edge of a vertical scroll view, or the trailing edge of a horizontal scroll view.
