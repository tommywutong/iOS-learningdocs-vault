---
title: UICellAccessory.Placement
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-swift.struct/placement
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/placement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-swift.struct/placement.json'
content_hash: 'sha256:a4f221dd6bb7b6e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-swift.struct.md)

# UICellAccessory.Placement

<sub>Enumeration</sub>

Constants that describe the placement of the accessory within the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Placement
```

## Topics

### Specifying accessory placement

- [UICellAccessory.Placement.leading(displayed:at:)](<placement/leading(displayed_at_).md>) — The accessory appears on the leading edge of the cell.
- [UICellAccessory.Placement.trailing(displayed:at:)](<placement/trailing(displayed_at_).md>) — The accessory appears on the trailing edge of the cell.

### Specifying position

- [position(after:)](<placement/position(after_).md>) — Provides a position after the accessory that matches the specified type, or at the end if there’s no matching type.
- [position(before:)](<placement/position(before_).md>) — Provides a position before the accessory that matches the specified type, or at the beginning if there’s no matching type.
- [Position](placement/position.md) — The index position of the cell accessory in relation to the other accessories in the specified array.

## See Also

### Customizing appearance and placement

- [LayoutDimension](layoutdimension.md) — Constants that describe the layout dimension for the accessory.
- [DisplayedState](displayedstate.md) — Constants that describe the cell-editing states that the accessory appears in.
