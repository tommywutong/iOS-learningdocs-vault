---
title: ScenePhase.inactive
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenephase/inactive
source_url: 'https://developer.apple.com/documentation/swiftui/scenephase/inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenephase/inactive.json'
content_hash: 'sha256:832a8843ff42c109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScenePhase](../scenephase.md)

# ScenePhase.inactive

<sub>Case</sub>

The scene is in the foreground but should pause its work.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case inactive
```

## Discussion

A scene in this phase doesn’t receive events and should pause timers and free any unnecessary resources. The scene might be completely hidden in the user interface, minimized, visible in the app switcher, or otherwise unavailable. In some cases, scenes only pass through this phase temporarily on their way to the [ScenePhase.background](background.md) phase.

An app or custom scene in this phase contains no scene instances in the [ScenePhase.active](active.md) phase.

## See Also

### Getting scene phases

- [ScenePhase.active](active.md) — The scene is in the foreground and interactive.
- [ScenePhase.background](background.md) — The scene isn’t currently visible in the UI.
