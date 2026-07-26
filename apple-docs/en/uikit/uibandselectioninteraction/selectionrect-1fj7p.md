---
title: selectionRect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibandselectioninteraction/selectionrect-1fj7p
source_url: 'https://developer.apple.com/documentation/uikit/uibandselectioninteraction/selectionrect-1fj7p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibandselectioninteraction/selectionrect-1fj7p.json'
content_hash: 'sha256:56d96340f1992300'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBandSelectionInteraction](../uibandselectioninteraction.md)

# selectionRect

<sub>Instance Property</sub>

The selection rectangle for an in-progress interaction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CGRect selectionRect;
```

## Discussion

The rectangle is in the coordinate system of the view that owns the interaction object. If no interaction is active, the value of this propety is `nil`.
