---
title: 'init(name:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uisceneconfiguration/init(name:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/init%28name%3A%29.json'
content_hash: 'sha256:31b22d50825f0c45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# init(name:)

<sub>Initializer</sub>

Creates a scene-configuration object with the specified name.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(name: String?)
```

## Discussion

Scene sessions created from this configuration will have their role automatically set by the system.

## See Also

### Creating a configuration object

- [- initWithName:sessionRole:](<init(name_sessionrole_).md>) — Creates a scene-configuration object with the specified role and app-specific name.
- [- init](<init().md>) — Creates a scene-configuration object.
