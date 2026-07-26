---
title: 'default(color:size:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarview/decoration/default(color:size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/decoration/default(color:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/decoration/default%28color%3Asize%3A%29.json'
content_hash: 'sha256:889e345119814add'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICalendarView](../../uicalendarview.md) · [Decoration](../decoration.md)

# default(color:size:)

<sub>Type Method</sub>

Creates a default calendar view decoration with a filled circle image, using the color and size you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency static func `default`(color: UIColor? = nil, size: UICalendarView.DecorationSize = .medium) -> UICalendarView.Decoration
```

## Parameters

- `color` — A color for the decoration.

- `size` — A relative size for the decoration.

## Return Value

A calendar view decoration.

## See Also

### Creating a Default Decoration View

- [- init](<init().md>) — Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.
