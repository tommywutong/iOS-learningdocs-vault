---
title: offset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointeraccessory/position-swift.struct/offset
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct/offset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/position-swift.struct/offset.json'
content_hash: 'sha256:f3e3eaf3ea779736'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPointerAccessory](../../uipointeraccessory.md) · [Position](../position-swift.struct.md)

# offset

<sub>Instance Property</sub>

The offset of the accessory from the primary pointer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var offset: CGFloat
```

## Discussion

This property only supports positive values.

## See Also

### Creating a custom accessory position

- [init(offset:angle:)](<init(offset_angle_).md>) — Creates a custom accessory position with the specified offset and angle.
- [angle](angle.md) — The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [defaultOffset](defaultoffset.md) — A constant that specifies the default offset of an accessory from the primary pointer shape.
