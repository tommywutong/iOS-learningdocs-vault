---
title: isLandscape
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterfaceorientation/islandscape
source_url: 'https://developer.apple.com/documentation/uikit/uiinterfaceorientation/islandscape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterfaceorientation/islandscape.json'
content_hash: 'sha256:566d2e281b917edb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterfaceOrientation](../uiinterfaceorientation.md)

# isLandscape

<sub>Instance Property</sub>

A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isLandscape: Bool { get }
```

## Discussion

The interface orientation can be different than the device orientation. You typically call this function in your view controller code to check the current orientation.

## See Also

### Interface orientation

- [UIInterfaceOrientationIsPortrait](isportrait.md) — A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.
