---
title: ScrollPhase.animating
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollphase/animating
source_url: 'https://developer.apple.com/documentation/swiftui/scrollphase/animating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollphase/animating.json'
content_hash: 'sha256:0668342f96e8306e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPhase](../scrollphase.md)

# ScrollPhase.animating

<sub>Case</sub>

The animating phase where the scroll view is animating towards a final target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case animating
```

## Discussion

This phase is the result of a programmatic scroll when using a [ScrollViewReader](../scrollviewreader.md) or [scrollPosition(id:anchor:)](<../view/scrollposition(id_anchor_).md>) modifier.

SwiftUI provides you a value of this type when using the [onScrollPhaseChange(_:)](<../view/onscrollphasechange(__).md>) modifier with a scrollable view like [ScrollView](../scrollview.md) or [List](../list.md).

## See Also

### Getting scroll gesture states

- [ScrollPhase.decelerating](decelerating.md) — The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](idle.md) — The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](interacting.md) — The interacting phase where the user is interacting with the scroll view.
- [ScrollPhase.tracking](tracking.md) — The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.
