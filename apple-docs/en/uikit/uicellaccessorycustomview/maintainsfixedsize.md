---
title: maintainsFixedSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicellaccessorycustomview/maintainsfixedsize
source_url: 'https://developer.apple.com/documentation/uikit/uicellaccessorycustomview/maintainsfixedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicellaccessorycustomview/maintainsfixedsize.json'
content_hash: 'sha256:2c85d5ee6100cc78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICellAccessoryCustomView](../uicellaccessorycustomview.md)

# maintainsFixedSize

<sub>Instance Property</sub>

A Boolean value that determines whether to preserve the frame size of the custom view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL maintainsFixedSize;
```

## Discussion

When the value of this property is [true](../../swift/true.md), the system preserves the current frame size of the view. When the value of this property is [false](../../swift/false.md), the system sizes the view during layout of the accessories.

The default value of this property is [false](../../swift/false.md).

## See Also

### Accessing Configuration Options

- [customView](customview.md) — The custom view to display for the accessory.
- [placement](placement.md) — The placement for the accessory.
- [position](position.md) — The index position of the cell accessory in relation to the other accessories in the accessories array.
