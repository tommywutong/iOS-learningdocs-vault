---
title: damping
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisnapbehavior/damping
source_url: 'https://developer.apple.com/documentation/uikit/uisnapbehavior/damping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisnapbehavior/damping.json'
content_hash: 'sha256:08d3b5a11c918ced'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISnapBehavior](../uisnapbehavior.md)

# damping

<sub>Instance Property</sub>

The amount of oscillation of a dynamic item during the conclusion of a snap.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var damping: CGFloat { get set }
```

## Discussion

The valid range for damping extends from `0.0`, for maximum oscillation, through `1.0`, for minimum oscillation. The default value is `0.5`.

## See Also

### Configuring a snap behavior

- [snapPoint](snappoint.md) — The point to which to snap.
