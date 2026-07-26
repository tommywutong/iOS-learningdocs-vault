---
title: init()
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/init()
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/init%28%29.json'
content_hash: 'sha256:a4d767eb7f000225'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# init()

<sub>Initializer</sub>

Creates a scene-configuration object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init()
```

## Discussion

Scene sessions created from this configuration will have their role automatically set by the system.

## See Also

### Creating a configuration object

- [- initWithName:sessionRole:](<init(name_sessionrole_).md>) — Creates a scene-configuration object with the specified role and app-specific name.
- [- initWithName:](<init(name_).md>) — Creates a scene-configuration object with the specified name. _(beta)_
