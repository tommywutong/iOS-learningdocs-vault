---
title: UICellAccessoryPositionBeforeAccessoryOfClass
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessorypositionbeforeaccessoryofclass
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessorypositionbeforeaccessoryofclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessorypositionbeforeaccessoryofclass.json'
content_hash: 'sha256:1d16f1b74d39ee90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICellAccessoryPositionBeforeAccessoryOfClass

<sub>Function</sub>

Provides a position before the accessory that matches the specified class, or at the beginning if there’s no matching class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern UICellAccessoryPosition UICellAccessoryPositionBeforeAccessoryOfClass(Class accessoryClass);
```

## See Also

### Customizing layout and placement

- [reservedLayoutWidth](uicellaccessory-c.class/reservedlayoutwidth.md) — The layout width that the system reserves for the accessory and then centers the accessory within.
- [UICellAccessoryStandardDimension](uicellaccessorystandarddimension.md) — The system standard layout dimension for accessories.
- [UICellAccessoryPlacement](uicellaccessoryplacement.md) — Constants that describe the placement of the accessory within the cell.
- [UICellAccessoryPosition](uicellaccessoryposition.md) — The index position of the cell accessory in relation to the other accessories in the specified array.
- [UICellAccessoryPositionAfterAccessoryOfClass](uicellaccessorypositionafteraccessoryofclass.md) — Provides a position after the accessory that matches the specified class, or at the end if there’s no matching class.
