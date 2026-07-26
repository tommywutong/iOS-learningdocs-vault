---
title: ScenePhase.active
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenephase/active
source_url: 'https://developer.apple.com/documentation/swiftui/scenephase/active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenephase/active.json'
content_hash: 'sha256:64f065e01d322823'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScenePhase](../scenephase.md)

# ScenePhase.active

<sub>Case</sub>

The scene is in the foreground and interactive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case active
```

## Discussion

An active scene isn’t necessarily front-most. For example, a macOS window might be active even if it doesn’t currently have focus. Nevertheless, all scenes should operate normally in this phase.

An app or custom scene in this phase contains at least one active scene instance.

## See Also

### Getting scene phases

- [ScenePhase.inactive](inactive.md) — The scene is in the foreground but should pause its work.
- [ScenePhase.background](background.md) — The scene isn’t currently visible in the UI.
