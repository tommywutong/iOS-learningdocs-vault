---
title: UICollectionViewFlowLayoutInvalidationContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayoutinvalidationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext.json'
content_hash: 'sha256:b1e31369c4a1f741'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewFlowLayoutInvalidationContext

<sub>Class</sub>

A set of properties for determining whether to recompute the size of items or their position in the layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewFlowLayoutInvalidationContext
```

## Overview

The flow layout object creates instances of this class when it needs to invalidate its contents in response to changes. You can also create instances when invalidating the flow layout manually.

## Relationships

- **Inherits From**: [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying what to invalidate

- [invalidateFlowLayoutDelegateMetrics](uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics.md) — A Boolean indicating whether to recompute the size of items and views in the layout.
- [invalidateFlowLayoutAttributes](uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes.md) — A Boolean indicating whether to recompute the layout attributes for items and views in the layout.

## See Also

### Manual layouts

- [Customizing collection view layouts](customizing-collection-view-layouts.md) — Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [UICollectionViewLayout](uicollectionviewlayout.md) — An abstract base class for generating layout information for a collection view.
- [UICollectionViewFlowLayout](uicollectionviewflowlayout.md) — A layout object that organizes items into a grid with optional header and footer views for each section.
- [UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md) — A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) — A layout object that manages the layout-related attributes for a given item in a collection view.
