---
title: minimum
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifloatrange/minimum
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrange/minimum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrange/minimum.json'
content_hash: 'sha256:428252d11c59ab16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFloatRange](../uifloatrange.md)

# minimum

<sub>Instance Property</sub>

The minimum range of motion for sliding and pin attachments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimum: CGFloat
```

## Discussion

For sliding attachments, it represents the number of points to move along the axis of translation in the negative direction. For pin attachments, it represents the number of radians to rotate in the counter-clockwise direction. This value must be less than or equal to `0`.

## See Also

### Getting the range values

- [maximum](maximum.md) — The maximum range of motion for sliding and pin attachments.
