---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewinteraction/view
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteraction/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteraction/view.json'
content_hash: 'sha256:5e1eb9e8860b30c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteraction](../uipreviewinteraction.md)

# view

<sub>Instance Property</sub>

The view from which the preview interaction receives touch events.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var view: UIView? { get }
```

## Discussion

A preview interaction operates on the view that’s provided at initialization time. Use this property to obtain a reference to that same view. Note that this is a weak property — the preview interaction doesn’t retain a reference to the view it’s provided.

## See Also

### Handling preview interactions

- [- cancelInteraction](<cancel().md>) — Cancels the current preview interaction.
- [- locationInCoordinateSpace:](<location(in_).md>) — Returns the location of the touch that started the interaction.
