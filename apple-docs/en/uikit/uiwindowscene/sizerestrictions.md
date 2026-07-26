---
title: sizeRestrictions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/sizerestrictions
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/sizerestrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/sizerestrictions.json'
content_hash: 'sha256:55baacfce9a08195'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# sizeRestrictions

<sub>Instance Property</sub>

The minimum and maximum size of the app’s windows.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sizeRestrictions: UISceneSizeRestrictions? { get }
```

## Discussion

When the value of this property is not `nil`, use it to change the default minimum and maximum window sizes for your app. If the value of this property is `nil,` the system doesn’t allow you to set window size restrictions.

## See Also

### Getting the interface attributes

- [traitCollection](traitcollection.md) — The traits that describe the current environment of the scene.
- [UISceneSizeRestrictions](../uiscenesizerestrictions.md) — An object that specifies the minimum and maximum sizes for resizable windows.
