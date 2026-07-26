---
title: systemProtectionDidChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/systemprotectiondidchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/systemprotectiondidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/systemprotectiondidchangenotification.json'
content_hash: 'sha256:430178e8fe7f2e35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# systemProtectionDidChangeNotification

<sub>Type Property</sub>

A notification posted when the system-protection attributes of a scene change.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated class let systemProtectionDidChangeNotification: NSNotification.Name
```

## Discussion

The object of the notification is the scene for which protection attributes changed.

## See Also

### Working with system protection manager

- [systemProtectionManager](systemprotectionmanager-swift.property.md) — The system protection manager associated with this scene.
- [SystemProtectionManager](systemprotectionmanager-swift.class.md) — A class that represents the status of system protection for the scene.
