---
title: effectiveContentHorizontalAlignment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/effectivecontenthorizontalalignment
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/effectivecontenthorizontalalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/effectivecontenthorizontalalignment.json'
content_hash: 'sha256:cc568abbab958fd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# effectiveContentHorizontalAlignment

<sub>Instance Property</sub>

The horizontal alignment currently in effect for the control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment { get }
```

## Discussion

This property always contains the value [UIControlContentHorizontalAlignmentLeft](contenthorizontalalignment-swift.enum/left.md) or [UIControlContentHorizontalAlignmentRight](contenthorizontalalignment-swift.enum/right.md), even when the actual horizontal alignment is [UIControlContentHorizontalAlignmentLeading](contenthorizontalalignment-swift.enum/leading.md) or [UIControlContentHorizontalAlignmentTrailing](contenthorizontalalignment-swift.enum/trailing.md).

## See Also

### Specifying content alignment

- [contentVerticalAlignment](contentverticalalignment-swift.property.md) — The vertical alignment of content within the control’s bounds.
- [ContentVerticalAlignment](contentverticalalignment-swift.enum.md) — Constants for specifying the vertical alignment of content (text and images) in a control.
- [contentHorizontalAlignment](contenthorizontalalignment-swift.property.md) — The horizontal alignment of content within the control’s bounds.
- [ContentHorizontalAlignment](contenthorizontalalignment-swift.enum.md) — The horizontal alignment of content (text and images) within a control.
