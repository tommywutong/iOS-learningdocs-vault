---
title: isPortrait
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterfaceorientation/isportrait
source_url: 'https://developer.apple.com/documentation/uikit/uiinterfaceorientation/isportrait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterfaceorientation/isportrait.json'
content_hash: 'sha256:1570324f7f5adf27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterfaceOrientation](../uiinterfaceorientation.md)

# isPortrait

<sub>Instance Property</sub>

A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isPortrait: Bool { get }
```

## Discussion

The interface orientation can be different than the device orientation. You typically call this function in your view controller code to check the current orientation.

## See Also

### Interface orientation

- [UIInterfaceOrientationIsLandscape](islandscape.md) — A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.
