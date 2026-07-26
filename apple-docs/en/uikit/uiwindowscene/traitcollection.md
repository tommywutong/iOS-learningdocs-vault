---
title: traitCollection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/traitcollection
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/traitcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/traitcollection.json'
content_hash: 'sha256:24d94c0b0d16321b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# traitCollection

<sub>Instance Property</sub>

The traits that describe the current environment of the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var traitCollection: UITraitCollection { get }
```

## Discussion

Use this property to get additional information about the current scene, such as the size class and scale factor. For more information about the available traits, see [UITraitCollection](../uitraitcollection.md).

## See Also

### Getting the interface attributes

- [sizeRestrictions](sizerestrictions.md) — The minimum and maximum size of the app’s windows.
- [UISceneSizeRestrictions](../uiscenesizerestrictions.md) — An object that specifies the minimum and maximum sizes for resizable windows.
