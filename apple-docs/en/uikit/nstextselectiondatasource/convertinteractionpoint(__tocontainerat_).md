---
title: 'convertInteractionPoint(_:toContainerAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/convertinteractionpoint(_:tocontainerat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/convertinteractionpoint(_:tocontainerat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/convertinteractionpoint%28_%3Atocontainerat%3A%29.json'
content_hash: 'sha256:e0d49b24f098285f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# convertInteractionPoint(_:toContainerAt:)

<sub>Instance Method</sub>

Converts an interaction point from display space into the text container’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func convertInteractionPoint(_ point: CGPoint, toContainerAt containerLocation: any NSTextLocation) -> CGPoint
```

## Parameters

- `point` — The interaction point in display/view-space coordinates.

- `containerLocation` — The location identifying the text container the interaction occurred in.

## Return Value

The point mapped into the text container’s coordinate system. Return `point` unchanged when no transform is active.

## Discussion

`NSTextSelectionNavigation` calls this method before hit-testing to allow the data source to undo any display transform (rotation, flip, path layout, etc.) applied to the text.
