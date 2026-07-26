---
title: 'baseWritingDirection(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/basewritingdirection(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/basewritingdirection(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/basewritingdirection%28at%3A%29.json'
content_hash: 'sha256:1687a88aa6f819bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# baseWritingDirection(at:)

<sub>Instance Method</sub>

Returns the base writing direction at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func baseWritingDirection(at location: any NSTextLocation) -> NSTextSelectionNavigation.WritingDirection
```

## Parameters

- `location` — The location where you want to examine the text’s writing direction.

## Return Value

The [NSWritingDirection](../nswritingdirection.md).

## See Also

### Changing the characteristics of the selection

- [WritingDirection](../nstextselectionnavigation/writingdirection.md) — Values that describe the writing direction inside a text selection.
- [- textLayoutOrientationAtLocation:](<textlayoutorientation(at_).md>) — Returns the layout orientation at the location you specify.
- [LayoutOrientation](../nstextselectionnavigation/layoutorientation.md) — Values that describe the possible layout orientations.
