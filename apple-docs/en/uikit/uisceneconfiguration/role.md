---
title: role
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/role
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/role'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/role.json'
content_hash: 'sha256:c26c6a07977f4565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# role

<sub>Instance Property</sub>

The role assigned to the scene configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var role: UISceneSession.Role { get }
```

## Discussion

UIKit populates this property with an appropriate role value based on the contents of your app’s `Info.plist` file. You also specify this value when you create a new scene-configuration object.

## See Also

### Getting the configuration attributes

- [name](name.md) — The app-specific name assigned to the scene configuration.
- [Role](../uiscenesession/role-swift.struct.md) — Constants that indicate the possible roles for a scene.
