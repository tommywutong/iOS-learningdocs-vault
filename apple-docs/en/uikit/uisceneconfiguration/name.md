---
title: name
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/name
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/name.json'
content_hash: 'sha256:5b0eb490d1096d5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# name

<sub>Instance Property</sub>

The app-specific name assigned to the scene configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var name: String? { get }
```

## Discussion

UIKit sets this property’s initial value using the [UISceneConfigurationName](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md) key from the appropriate scene in your app’s `Info.plist` file. You also specify this value when you create a new scene-configuration object.

## See Also

### Getting the configuration attributes

- [role](role.md) — The role assigned to the scene configuration.
- [Role](../uiscenesession/role-swift.struct.md) — Constants that indicate the possible roles for a scene.
