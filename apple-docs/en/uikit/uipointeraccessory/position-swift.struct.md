---
title: UIPointerAccessory.Position
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointeraccessory/position-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/position-swift.struct.json'
content_hash: 'sha256:e2c2c3a16e187da7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerAccessory](../uipointeraccessory.md)

# UIPointerAccessory.Position

<sub>Structure</sub>

A structure that specifies the position of the accessory relative to the primary pointer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct Position
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting an accessory position

- [top](position-swift.struct/top.md) — An accessory position at the top of the primary pointer.
- [topRight](position-swift.struct/topright.md) — An accessory position at the top-right of the primary pointer.
- [right](position-swift.struct/right.md) — An accessory position at the right of the primary pointer.
- [bottomRight](position-swift.struct/bottomright.md) — An accessory position at the bottom-right of the primary pointer.
- [bottom](position-swift.struct/bottom.md) — An accessory position at the bottom of the primary pointer.
- [bottomLeft](position-swift.struct/bottomleft.md) — An accessory position at the bottom-left of the primary pointer.
- [left](position-swift.struct/left.md) — An accessory position at the left of the primary pointer.
- [topLeft](position-swift.struct/topleft.md) — An accessory position at the top-left of the primary pointer.

### Creating a custom accessory position

- [init(offset:angle:)](<position-swift.struct/init(offset_angle_).md>) — Creates a custom accessory position with the specified offset and angle.
- [angle](position-swift.struct/angle.md) — The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [offset](position-swift.struct/offset.md) — The offset of the accessory from the primary pointer.
- [defaultOffset](position-swift.struct/defaultoffset.md) — A constant that specifies the default offset of an accessory from the primary pointer shape.

## See Also

### Getting the position

- [position](position-swift.property.md) — The position of the accessory relative to the primary pointer.
