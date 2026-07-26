---
title: 'windowScene(_:didUpdateEffectiveGeometry:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdateeffectivegeometry:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/windowscene%28_%3Adidupdateeffectivegeometry%3A%29.json'
content_hash: 'sha256:478ee8511a55143d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# windowScene(_:didUpdateEffectiveGeometry:)

<sub>Instance Method</sub>

Called when the window scene’s effective geometry has changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func windowScene(_ windowScene: UIWindowScene, didUpdateEffectiveGeometry previousEffectiveGeometry: UIWindowScene.Geometry)
```

## Discussion

Always called when a `UIWindowScene` moves between screens.
