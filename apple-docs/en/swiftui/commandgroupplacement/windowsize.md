---
title: windowSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/windowsize
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/windowsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/windowsize.json'
content_hash: 'sha256:d78682b2da766bfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# windowSize

<sub>Type Property</sub>

Placement for commands that control the size of the window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let windowSize: CommandGroupPlacement
```

## Discussion

By default, this group includes the following commands in macOS:

- Minimize
- Zoom

## See Also

### Windows

- [singleWindowList](singlewindowlist.md) — Placement for commands that describe and reveal any windows that the app defines.
- [windowArrangement](windowarrangement.md) — Placement for commands that arrange all of an app’s windows.
- [windowList](windowlist.md) — Placement for commands that describe and reveal the app’s open windows.
