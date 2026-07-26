---
title: connectedScenes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/connectedscenes
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/connectedscenes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/connectedscenes.json'
content_hash: 'sha256:afb433d057ab4d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# connectedScenes

<sub>Instance Property</sub>

The app’s currently connected scenes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var connectedScenes: Set<UIScene> { get }
```

## Discussion

Connected scenes are those that are in memory and potentially doing active work. A connected scene may be in the foreground or background, and it may be onscreen or offscreen.

## See Also

### Getting scene information

- [supportsMultipleScenes](supportsmultiplescenes.md) — A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [openSessions](opensessions.md) — The sessions whose scenes are either currently active or archived by the system.
