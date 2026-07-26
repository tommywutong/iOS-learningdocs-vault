---
title: 'init(name:sessionRole:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisceneconfiguration/init(name:sessionrole:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:sessionrole:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/init%28name%3Asessionrole%3A%29.json'
content_hash: 'sha256:7e6ab8f7bae418d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# init(name:sessionRole:)

<sub>Initializer</sub>

Creates a scene-configuration object with the specified role and app-specific name.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(name: String?, sessionRole: UISceneSession.Role)
```

## Parameters

- `name` — The app-specific name you want to assign to the scene. For scenes you specify in your Info.plist file, this value corresponds to the string assigned to the [UISceneConfigurationName](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md) key.

- `sessionRole` — The role of the scene. For a list of possible roles, see [Role](../uiscenesession/role-swift.struct.md).

## Return Value

A new scene-configuration object.

## Discussion

After creating a scene-configuration object, supply values for the [sceneClass](sceneclass.md), [delegateClass](delegateclass.md), and [storyboard](storyboard.md) properties.

## See Also

### Creating a configuration object

- [- initWithName:](<init(name_).md>) — Creates a scene-configuration object with the specified name. _(beta)_
- [- init](<init().md>) — Creates a scene-configuration object.
