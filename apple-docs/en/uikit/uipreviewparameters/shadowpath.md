---
title: shadowPath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewparameters/shadowpath
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewparameters/shadowpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewparameters/shadowpath.json'
content_hash: 'sha256:4aa63981d9a34153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewParameters](../uipreviewparameters.md)

# shadowPath

<sub>Instance Property</sub>

The path to use for drawing the preview’s shadow.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var shadowPath: UIBezierPath? { get set }
```

## Discussion

If `nil`, the system uses the [visiblePath](visiblepath.md) to draw the shadow.

## See Also

### Configuring the preview attributes

- [backgroundColor](backgroundcolor.md) — The background color to display behind the preview.
- [visiblePath](visiblepath.md) — The portion of the view to show in the preview.
