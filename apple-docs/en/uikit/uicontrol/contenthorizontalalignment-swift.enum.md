---
title: UIControl.ContentHorizontalAlignment
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/contenthorizontalalignment-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/contenthorizontalalignment-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/contenthorizontalalignment-swift.enum.json'
content_hash: 'sha256:008e370bd1133518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# UIControl.ContentHorizontalAlignment

<sub>Enumeration</sub>

The horizontal alignment of content (text and images) within a control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum ContentHorizontalAlignment
```

## Overview

You use these constants as the value of the [contentHorizontalAlignment](contenthorizontalalignment-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIControlContentHorizontalAlignmentCenter](contenthorizontalalignment-swift.enum/center.md) — Aligns the content horizontally in the center of the control.
- [UIControlContentHorizontalAlignmentLeft](contenthorizontalalignment-swift.enum/left.md) — Aligns the content horizontally from the left of the control (the default).
- [UIControlContentHorizontalAlignmentRight](contenthorizontalalignment-swift.enum/right.md) — Aligns the content horizontally from the right of the control.
- [UIControlContentHorizontalAlignmentFill](contenthorizontalalignment-swift.enum/fill.md) — Aligns the content horizontally to fill the content rectangles; text may wrap and images may be stretched.
- [UIControlContentHorizontalAlignmentLeading](contenthorizontalalignment-swift.enum/leading.md) — Aligns the content horizontally from the leading edge of the control.
- [UIControlContentHorizontalAlignmentTrailing](contenthorizontalalignment-swift.enum/trailing.md) — Aligns the content horizontally from the trailing edge of the control.

### Initializers

- [init(rawValue:)](<contenthorizontalalignment-swift.enum/init(rawvalue_).md>)

## See Also

### Specifying content alignment

- [contentVerticalAlignment](contentverticalalignment-swift.property.md) — The vertical alignment of content within the control’s bounds.
- [ContentVerticalAlignment](contentverticalalignment-swift.enum.md) — Constants for specifying the vertical alignment of content (text and images) in a control.
- [contentHorizontalAlignment](contenthorizontalalignment-swift.property.md) — The horizontal alignment of content within the control’s bounds.
- [effectiveContentHorizontalAlignment](effectivecontenthorizontalalignment.md) — The horizontal alignment currently in effect for the control.
