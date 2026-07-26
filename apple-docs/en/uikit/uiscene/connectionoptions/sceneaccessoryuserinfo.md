---
title: sceneAccessoryUserInfo
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/sceneaccessoryuserinfo
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/sceneaccessoryuserinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/sceneaccessoryuserinfo.json'
content_hash: 'sha256:8b7ec17f602fa509'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# sceneAccessoryUserInfo

<sub>Instance Property</sub>

An optional user info object, provided when creating the `UISceneAccessory` for this scene accessory.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var sceneAccessoryUserInfo: Any? { get }
```

## Discussion

This object can be used to associate data to the scene accessory configuration to be passed to the scene delegate when the scene connects.
