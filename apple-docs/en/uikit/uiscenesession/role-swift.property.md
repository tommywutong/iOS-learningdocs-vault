---
title: role
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesession/role-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession/role-swift.property.json'
content_hash: 'sha256:b1d9c7c6c804873c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSession](../uiscenesession.md)

# role

<sub>Instance Property</sub>

The role played by the scene’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var role: UISceneSession.Role { get }
```

## Discussion

Use this property to determine how the user interacts with the content of the associated scene. UIKit sets the initial value of this property based on the information in your app’s `Info.plist` file. If you don’t provide scene configuration data for your app, UIKit sets the role to an appropriate value.

## See Also

### Getting the scene information

- [scene](scene.md) — The scene associated with the current session.
- [Role](role-swift.struct.md) — Constants that indicate the possible roles for a scene.
