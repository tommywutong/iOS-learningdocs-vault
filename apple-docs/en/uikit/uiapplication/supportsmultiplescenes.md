---
title: supportsMultipleScenes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/supportsmultiplescenes
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/supportsmultiplescenes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/supportsmultiplescenes.json'
content_hash: 'sha256:ca684039f825fe2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# supportsMultipleScenes

<sub>Instance Property</sub>

A Boolean value that indicates whether the app may display multiple scenes simultaneously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var supportsMultipleScenes: Bool { get }
```

## Discussion

UIKit sets this property to [true](../../swift/true.md) when the system allows the app to display multiple scenes and the app’s `Info.plist` file includes the [UIApplicationSupportsMultipleScenes](../../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) key with a value of [true](../../swift/true.md). If either of those conditions isn’t true, the value of this property is [false](../../swift/false.md).

Use the [connectedScenes](connectedscenes.md) property to determine whether multiple scenes are present.

## See Also

### Getting scene information

- [connectedScenes](connectedscenes.md) — The app’s currently connected scenes.
- [openSessions](opensessions.md) — The sessions whose scenes are either currently active or archived by the system.
