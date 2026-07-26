---
title: 'position(before:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicellaccessory-swift.struct/placement/position(before:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/placement/position(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/placement/position%28before%3A%29.json'
content_hash: 'sha256:4cf1d19ab6d269fd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICellAccessory](../../uicellaccessory-swift.struct.md) · [Placement](../placement.md)

# position(before:)

<sub>Type Method</sub>

Provides a position before the accessory that matches the specified type, or at the beginning if there’s no matching type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func position(before accessory: UICellAccessory) -> UICellAccessory.Placement.Position
```

## See Also

### Specifying position

- [position(after:)](<position(after_).md>) — Provides a position after the accessory that matches the specified type, or at the end if there’s no matching type.
- [Position](position.md) — The index position of the cell accessory in relation to the other accessories in the specified array.
