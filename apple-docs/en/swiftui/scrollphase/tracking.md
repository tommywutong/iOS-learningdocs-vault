---
title: ScrollPhase.tracking
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollphase/tracking
source_url: 'https://developer.apple.com/documentation/swiftui/scrollphase/tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollphase/tracking.json'
content_hash: 'sha256:37f57d85d139e677'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPhase](../scrollphase.md)

# ScrollPhase.tracking

<sub>Case</sub>

The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case tracking
```

## Discussion

For example, on iOS, the user may start touching content inside of the scroll view. Until the user moves their finger the scroll view would be tracking the finger. Not all platforms or kinds of scroll may trigger this phase.

## See Also

### Getting scroll gesture states

- [ScrollPhase.animating](animating.md) — The animating phase where the scroll view is animating towards a final target.
- [ScrollPhase.decelerating](decelerating.md) — The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](idle.md) — The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](interacting.md) — The interacting phase where the user is interacting with the scroll view.
