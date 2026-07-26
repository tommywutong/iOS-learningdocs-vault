---
title: systemProtectionManager
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/systemprotectionmanager-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/systemprotectionmanager-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/systemprotectionmanager-swift.property.json'
content_hash: 'sha256:c83de2ec11528e7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# systemProtectionManager

<sub>Instance Property</sub>

The system protection manager associated with this scene.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var systemProtectionManager: UIScene.SystemProtectionManager? { get }
```

## Discussion

To check whether the scene requires user authentication, inspect the manager’s [userAuthenticationEnabled](systemprotectionmanager-swift.class/isuserauthenticationenabled.md) property.

## See Also

### Working with system protection manager

- [SystemProtectionManager](systemprotectionmanager-swift.class.md) — A class that represents the status of system protection for the scene.
- [UISceneSystemProtectionDidChangeNotification](systemprotectiondidchangenotification.md) — A notification posted when the system-protection attributes of a scene change.
