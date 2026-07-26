---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/delegate.json'
content_hash: 'sha256:3fd25b0bd99050e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# delegate

<sub>Instance Property</sub>

The object you use to receive life-cycle events associated with the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delegate: (any UISceneDelegate)? { get set }
```

## Discussion

The system creates a default delegate object based on the the class name you provide in your app’s `Info.plist` file, or that your app delegate specifies when configuring the scene. You can change this default delegate object later, as needed.

## See Also

### Managing the life cycle of a scene

- [UISceneDelegate](../uiscenedelegate.md) — The core methods you use to respond to life-cycle events occurring within a scene.
