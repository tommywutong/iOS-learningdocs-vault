---
title: offset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointeraccessoryposition/offset
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessoryposition/offset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessoryposition/offset.json'
content_hash: 'sha256:9dcefc7dc477b9fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerAccessoryPosition](../uipointeraccessoryposition.md)

# offset

<sub>Instance Property</sub>

The offset of the accessory from the primary pointer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
CGFloat offset;
```

## Discussion

This property only supports positive values.

## See Also

### Creating a custom accessory position

- [UIPointerAccessoryPositionMake](../uipointeraccessorypositionmake.md) — Creates a custom accessory position with the specified offset and angle.
- [angle](angle.md) — The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
