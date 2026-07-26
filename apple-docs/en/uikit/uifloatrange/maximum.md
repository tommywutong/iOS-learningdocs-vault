---
title: maximum
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifloatrange/maximum
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrange/maximum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrange/maximum.json'
content_hash: 'sha256:6e322458d1d1c6f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFloatRange](../uifloatrange.md)

# maximum

<sub>Instance Property</sub>

The maximum range of motion for sliding and pin attachments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximum: CGFloat
```

## Discussion

For sliding attachments, it represents the number of points to move along the axis of translation in the positive direction. For pin attachments, it represents the number of radians to rotate in the clockwise direction. This value must be greater than or equal to `0`.

## See Also

### Getting the range values

- [minimum](minimum.md) — The minimum range of motion for sliding and pin attachments.
