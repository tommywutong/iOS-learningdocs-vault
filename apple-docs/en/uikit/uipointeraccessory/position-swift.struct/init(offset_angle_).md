---
title: 'init(offset:angle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipointeraccessory/position-swift.struct/init(offset:angle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipointeraccessory/position-swift.struct/init(offset:angle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointeraccessory/position-swift.struct/init%28offset%3Aangle%3A%29.json'
content_hash: 'sha256:b9442317e5ab97be'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPointerAccessory](../../uipointeraccessory.md) · [Position](../position-swift.struct.md)

# init(offset:angle:)

<sub>Initializer</sub>

Creates a custom accessory position with the specified offset and angle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(offset: CGFloat = Position.defaultOffset, angle: CGFloat = 0)
```

## See Also

### Creating a custom accessory position

- [angle](angle.md) — The angle of the accessory’s position, measured in radians clockwise from the top of the primary pointer.
- [offset](offset.md) — The offset of the accessory from the primary pointer.
- [defaultOffset](defaultoffset.md) — A constant that specifies the default offset of an accessory from the primary pointer shape.
