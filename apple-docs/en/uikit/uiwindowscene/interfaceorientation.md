---
title: interfaceOrientation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（26.0 起废弃）, iPadOS 13.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/interfaceorientation
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/interfaceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/interfaceorientation.json'
content_hash: 'sha256:a0d4423ef360bc5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# interfaceOrientation

<sub>Instance Property</sub>

The orientation to use when displaying content in your windows.

> [!warning] Deprecated
> Use effectiveGeometry.interfaceOrientation instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var interfaceOrientation: UIInterfaceOrientation { get }
```

## Discussion

The interface orientation normally corresponds to the device orientation, but it might also be different. For example, the interface orientation does not always match the device orientation when the user enables rotation lock for the device.

## See Also

### Deprecated symbols

- [coordinateSpace](coordinatespace.md) — The coordinate space occupied by the scene. _(deprecated)_
