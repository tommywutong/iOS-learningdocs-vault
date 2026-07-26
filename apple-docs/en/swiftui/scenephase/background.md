---
title: ScenePhase.background
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenephase/background
source_url: 'https://developer.apple.com/documentation/swiftui/scenephase/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenephase/background.json'
content_hash: 'sha256:e3ca6682bd6b44e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScenePhase](../scenephase.md)

# ScenePhase.background

<sub>Case</sub>

The scene isn’t currently visible in the UI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case background
```

## Discussion

Do as little as possible in a scene that’s in the `background` phase. The `background` phase can precede termination, so do any cleanup work immediately upon entering this state. For example, close any open files and network connections. However, a scene can also return to the [ScenePhase.active](active.md) phase from the background.

Expect an app that enters the `background` phase to terminate.

## See Also

### Getting scene phases

- [ScenePhase.active](active.md) — The scene is in the foreground and interactive.
- [ScenePhase.inactive](inactive.md) — The scene is in the foreground but should pause its work.
