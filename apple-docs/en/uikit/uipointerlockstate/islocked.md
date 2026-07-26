---
title: isLocked
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerlockstate/islocked
source_url: 'https://developer.apple.com/documentation/uikit/uipointerlockstate/islocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerlockstate/islocked.json'
content_hash: 'sha256:e7cee214cefb4846'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerLockState](../uipointerlockstate.md)

# isLocked

<sub>Instance Property</sub>

A Boolean value that indicates whether the pointer is locked.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isLocked: Bool { get }
```

## Discussion

This value reflects the status of the pointer lock for the scene, as determined by the system. A view controller specifies its preferred pointer lock value, but the system may not honor the request.

This property is key-value observable. The [UIPointerLockStateDidChangeNotification](didchangenotification.md) is posted when it changes.
