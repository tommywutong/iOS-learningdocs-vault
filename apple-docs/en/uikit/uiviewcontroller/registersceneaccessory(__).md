---
title: 'registerSceneAccessory(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/registersceneaccessory(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/registersceneaccessory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/registersceneaccessory%28_%3A%29.json'
content_hash: 'sha256:fde8b7f6ea78c6d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# registerSceneAccessory(_:)

<sub>Instance Method</sub>

Registers a new scene accessory configuration associated with this view controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func registerSceneAccessory(_ accessory: UISceneAccessory) -> UISceneAccessoryRegistration
```

## Parameters

- `accessory` — A configuration which defines system functionality necessary to present the scene accessory.

## Return Value

A registration object which can be used to monitor changes for the scene accessory or unregister it.

## Discussion

The delegate type that the configuration defines will be called for all lifecycle events associated with the scene accessory.

## See Also

### Registering scene accessories

- [- unregisterSceneAccessory:](<unregistersceneaccessory(__).md>) — Unregisters a scene accessory with the specified registration. _(beta)_
