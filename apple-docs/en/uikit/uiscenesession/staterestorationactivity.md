---
title: stateRestorationActivity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesession/staterestorationactivity
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession/staterestorationactivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession/staterestorationactivity.json'
content_hash: 'sha256:248f7f32f66ca23b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSession](../uiscenesession.md)

# stateRestorationActivity

<sub>Instance Property</sub>

An activity object you can use to restore the previous contents of your scene’s interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var stateRestorationActivity: NSUserActivity? { get set }
```

## Discussion

Before disconnecting a scene, the system asks your delegate for an [NSUserActivity](../../foundation/nsuseractivity.md) object containing state information for that scene. If you provide that object, the system puts a copy of it in this property. Use the information in the user activity object to restore the scene to its previous state.

The system encrypts your app’s state restoration on disk. If the file is unavailable at scene-connection time, perhaps because the device is still locked, the initial value in this property is `nil`. When the data becomes available, the system updates the value accordingly.

## See Also

### Getting additional session information

- [userInfo](userinfo.md) — Custom attributes that you can associate with the scene.
