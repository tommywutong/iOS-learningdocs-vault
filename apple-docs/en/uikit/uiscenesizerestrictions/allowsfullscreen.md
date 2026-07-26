---
title: allowsFullScreen
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 16.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesizerestrictions/allowsfullscreen
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesizerestrictions/allowsfullscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesizerestrictions/allowsfullscreen.json'
content_hash: 'sha256:51fb8b00d2f1752e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSizeRestrictions](../uiscenesizerestrictions.md)

# allowsFullScreen

<sub>Instance Property</sub>

A Boolean value that indicates whether the scene can appear full screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsFullScreen: Bool { get set }
```

## Discussion

The system only checks the value of this property in Mac Catalyst apps.

## See Also

### Setting the size restrictions

- [minimumSize](minimumsize.md) — The minimum width and height supported by your app’s windows.
- [maximumSize](maximumsize.md) — The maximum width and height supported by your app’s windows.
