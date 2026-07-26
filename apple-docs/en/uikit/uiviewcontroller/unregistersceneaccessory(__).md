---
title: 'unregisterSceneAccessory(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/unregistersceneaccessory(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/unregistersceneaccessory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/unregistersceneaccessory%28_%3A%29.json'
content_hash: 'sha256:98b92bd3c971ea20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# unregisterSceneAccessory(_:)

<sub>Instance Method</sub>

Unregisters a scene accessory with the specified registration.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func unregisterSceneAccessory(_ registration: UISceneAccessoryRegistration)
```

## Discussion

If the scene accessory associated to this registration is currently being presented, it will be dismissed.

## See Also

### Registering scene accessories

- [- registerSceneAccessory:](<registersceneaccessory(__).md>) — Registers a new scene accessory configuration associated with this view controller. _(beta)_
