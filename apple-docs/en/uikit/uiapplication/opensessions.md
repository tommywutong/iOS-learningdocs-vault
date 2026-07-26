---
title: openSessions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/opensessions
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/opensessions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/opensessions.json'
content_hash: 'sha256:d5d9158a9ec2f1cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# openSessions

<sub>Instance Property</sub>

The sessions whose scenes are either currently active or archived by the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var openSessions: Set<UISceneSession> { get }
```

## Discussion

An archived session doesn’t have a connected scene, but a snapshot of its UI does appear in the app switcher. When the user selects that UI in the app switcher, the system asks your app to recreate the UI from the session information.

## See Also

### Getting scene information

- [supportsMultipleScenes](supportsmultiplescenes.md) — A Boolean value that indicates whether the app may display multiple scenes simultaneously.
- [connectedScenes](connectedscenes.md) — The app’s currently connected scenes.
