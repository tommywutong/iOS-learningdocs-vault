---
title: multiple
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextselectionnavigation/modifier/multiple
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectionnavigation/modifier/multiple'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectionnavigation/modifier/multiple.json'
content_hash: 'sha256:3fb38d547678e19b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSTextSelectionNavigation](../../nstextselectionnavigation.md) · [Modifier](../modifier.md)

# multiple

<sub>Type Property</sub>

The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and dragged positions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var multiple: NSTextSelectionNavigation.Modifier { get }
```

## Discussion

This produces an [NSTextSelection](../../nstextselection.md) per line.

## See Also

### Navigation modifier characteristics

- [NSTextSelectionNavigationModifierExtend](extend.md) — The value that indicates the framework extends the selection by not moving the initial location while in a drag selection.
- [NSTextSelectionNavigationModifierVisual](visual.md) — The value that indicates the framework extends the selection visually inside the rectangular area defined by the anchor and drag positions.
