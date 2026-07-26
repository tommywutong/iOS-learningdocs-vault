---
title: visiblePath
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewparameters/visiblepath
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewparameters/visiblepath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewparameters/visiblepath.json'
content_hash: 'sha256:48c74d842403cd73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewParameters](../uipreviewparameters.md)

# visiblePath

<sub>Instance Property</sub>

The portion of the view to show in the preview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var visiblePath: UIBezierPath? { get set }
```

## Discussion

Specify the path information in the coordinate space of the view being animated.

## See Also

### Configuring the preview attributes

- [backgroundColor](backgroundcolor.md) — The background color to display behind the preview.
- [shadowPath](shadowpath.md) — The path to use for drawing the preview’s shadow.
