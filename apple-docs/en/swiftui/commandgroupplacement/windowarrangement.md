---
title: windowArrangement
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/windowarrangement
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/windowarrangement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/windowarrangement.json'
content_hash: 'sha256:9a87f82948d79577'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# windowArrangement

<sub>Type Property</sub>

Placement for commands that arrange all of an app’s windows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let windowArrangement: CommandGroupPlacement
```

## Discussion

By default, this group includes the following command in macOS:

- Bring All to Front

## See Also

### Windows

- [singleWindowList](singlewindowlist.md) — Placement for commands that describe and reveal any windows that the app defines.
- [windowList](windowlist.md) — Placement for commands that describe and reveal the app’s open windows.
- [windowSize](windowsize.md) — Placement for commands that control the size of the window.
