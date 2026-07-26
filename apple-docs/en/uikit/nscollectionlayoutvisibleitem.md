---
title: NSCollectionLayoutVisibleItem
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutvisibleitem
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutvisibleitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutvisibleitem.json'
content_hash: 'sha256:57e01b13c6808d59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutVisibleItem

<sub>Protocol</sub>

An item that’s currently visible within the bounds of a section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol NSCollectionLayoutVisibleItem : UIDynamicItem
```

## Overview

A visible item represents an item in a collection view that’s currently visible onscreen, such as a cell, supplementary view, or decoration. You access a specific section’s visible items in its visible item invalidation handler ([NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)), stored in the [visibleItemsInvalidationHandler](nscollectionlayoutsection/visibleitemsinvalidationhandler.md) property. The handler is called before each layout cycle, any time an animation occurs in that section due to changes such as adding or removing items, scrolling the section, or rotating the device.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UIDynamicItem](uidynamicitem.md)

## Topics

### Identifying the item

- [name](nscollectionlayoutvisibleitem/name.md) — The name of the item.
- [representedElementKind](nscollectionlayoutvisibleitem/representedelementkind.md) — A string that identifies the type of item.
- [representedElementCategory](nscollectionlayoutvisibleitem/representedelementcategory.md) — A category that identifies the item, such as decoration or supplementary view.

### Getting the index path

- [indexPath](nscollectionlayoutvisibleitem/indexpath.md) — The index path of the item.

### Configuring appearance

- [alpha](nscollectionlayoutvisibleitem/alpha.md) — The transparency of the item.
- [hidden](nscollectionlayoutvisibleitem/ishidden.md) — A Boolean value that determines whether the item is hidden.

### Configuring position

- [frame](nscollectionlayoutvisibleitem/frame.md) — The frame rectangle, which describes the item’s location and size in its section’s coordinate system.
- [bounds](nscollectionlayoutvisibleitem/bounds.md) — The bounds rectangle, which describes the item’s location and size in its own coordinate system.
- [center](nscollectionlayoutvisibleitem/center.md) — The center point of the item’s frame rectangle.
- [transform](nscollectionlayoutvisibleitem/transform.md) — The transform applied to the item, relative to the center of its bounds.
- [transform3D](nscollectionlayoutvisibleitem/transform3d.md) — The 3D transform applied to the item.

### Specifying stacking order

- [zIndex](nscollectionlayoutvisibleitem/zindex.md) — The vertical stacking order of the item in relation to other items in the section.

## See Also

### Layout updates

- [NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md) — A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [UICollectionViewUpdateItem](uicollectionviewupdateitem.md) — An object that describes a single change to make to an item in a collection view.
- [UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md) — A context object that stores information specific to a focus update in a collection view.
- [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md) — A context object that declares which parts of your layout need to be updated when the layout is invalidated.
