---
title: reservedLayoutWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessory-c.class/reservedlayoutwidth
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessory-c.class/reservedlayoutwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessory-c.class/reservedlayoutwidth.json'
content_hash: 'sha256:284c5ed78f7226b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessory](../uicellaccessory-c.class.md)

# reservedLayoutWidth

<sub>Instance Property</sub>

The layout width that the system reserves for the accessory and then centers the accessory within.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat reservedLayoutWidth;
```

## Discussion

Use this property to ensure consistent horizontal alignment from both system and custom accessories to your content, even when the accessories vary in size.

The reserved layout width only affects the amount of space for the accessory, and its positioning within that space. It doesn’t affect the size of the accessory.

![](../../../../attachments/e3246a54d7c4b18fe3b2101d0a737694/media-3680733@2x.png)

<sub>Diagram of three cells, each of which contains one accessory on the leading side. The accessories vary in width, but use the same reserved layout width to achieve consistent alignment. Annotations running the height of the diagram illustrate the static width.</sub>

## See Also

### Customizing layout and placement

- [UICellAccessoryStandardDimension](../uicellaccessorystandarddimension.md) — The system standard layout dimension for accessories.
- [UICellAccessoryPlacement](../uicellaccessoryplacement.md) — Constants that describe the placement of the accessory within the cell.
- [UICellAccessoryPosition](../uicellaccessoryposition.md) — The index position of the cell accessory in relation to the other accessories in the specified array.
- [UICellAccessoryPositionAfterAccessoryOfClass](../uicellaccessorypositionafteraccessoryofclass.md) — Provides a position after the accessory that matches the specified class, or at the end if there’s no matching class.
- [UICellAccessoryPositionBeforeAccessoryOfClass](../uicellaccessorypositionbeforeaccessoryofclass.md) — Provides a position before the accessory that matches the specified class, or at the beginning if there’s no matching class.
