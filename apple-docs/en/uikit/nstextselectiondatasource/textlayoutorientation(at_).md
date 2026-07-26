---
title: 'textLayoutOrientation(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/textlayoutorientation(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/textlayoutorientation(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/textlayoutorientation%28at%3A%29.json'
content_hash: 'sha256:44c40de4f874f983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# textLayoutOrientation(at:)

<sub>Instance Method</sub>

Returns the layout orientation at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutOrientation(at location: any NSTextLocation) -> NSTextSelectionNavigation.LayoutOrientation
```

## Parameters

- `location` — The location where you want to examine the text’s layout orientation.

## Return Value

Returns an [LayoutOrientation](../nstextselectionnavigation/layoutorientation.md) that describes the orientation of the layout.

## See Also

### Changing the characteristics of the selection

- [- baseWritingDirectionAtLocation:](<basewritingdirection(at_).md>) — Returns the base writing direction at the location you specify.
- [WritingDirection](../nstextselectionnavigation/writingdirection.md) — Values that describe the writing direction inside a text selection.
- [LayoutOrientation](../nstextselectionnavigation/layoutorientation.md) — Values that describe the possible layout orientations.
