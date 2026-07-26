---
title: contentVerticalAlignment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/contentverticalalignment-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/contentverticalalignment-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/contentverticalalignment-swift.property.json'
content_hash: 'sha256:a2fbc9065b81e065'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# contentVerticalAlignment

<sub>Instance Property</sub>

The vertical alignment of content within the control’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentVerticalAlignment: UIControl.ContentVerticalAlignment { get set }
```

## Parameters

- `contentAlignment` — A constant that specifies the vertical alignment of text or images within the control. For a list of possible values, see [ContentVerticalAlignment](contentverticalalignment-swift.enum.md).

## Discussion

For controls that contain configurable text or image content, use this property to align that content appropriately inside the control’s bounds. Not all control subclasses have content that can be aligned, and it’s the responsibility of the subclass to determine how to apply this value. The default value of this property is [UIControlContentVerticalAlignmentTop](contentverticalalignment-swift.enum/top.md).

## See Also

### Specifying content alignment

- [ContentVerticalAlignment](contentverticalalignment-swift.enum.md) — Constants for specifying the vertical alignment of content (text and images) in a control.
- [contentHorizontalAlignment](contenthorizontalalignment-swift.property.md) — The horizontal alignment of content within the control’s bounds.
- [effectiveContentHorizontalAlignment](effectivecontenthorizontalalignment.md) — The horizontal alignment currently in effect for the control.
- [ContentHorizontalAlignment](contenthorizontalalignment-swift.enum.md) — The horizontal alignment of content (text and images) within a control.
