---
title: UICollectionViewFlowLayout
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout.json'
content_hash: 'sha256:68d1179bbd935ca1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewFlowLayout

<sub>Class</sub>

A layout object that organizes items into a grid with optional header and footer views for each section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewFlowLayout
```

## Overview

A flow layout is a type of collection view layout. Items in the collection view flow from one row or column (depending on the scrolling direction) to the next, with each row containing as many cells as will fit. Cells can be the same sizes or different sizes.

A flow layout works with the collection view’s delegate object to determine the size of items, headers, and footers in each section and grid. That delegate object must conform to the [UICollectionViewDelegateFlowLayout](uicollectionviewdelegateflowlayout.md) protocol. Use of the delegate allows you to adjust layout information dynamically. For example, you use a delegate object to specify different sizes for items in the grid. If you don’t provide a delegate, the flow layout uses the default values you set in the properties of this class.

Flow layouts lay out their content using a fixed distance in one direction and a scrollable distance in the other. For example, in a vertically scrolling grid, the width of the grid content is constrained to the width of the corresponding collection view while the height of the content adjusts dynamically to match the number of sections and items in the grid. The layout scrolls vertically by default, but you can configure the scrolling direction using the [scrollDirection](uicollectionviewflowlayout/scrolldirection.md) property.

Each section in a flow layout can have its own custom header and footer. To configure the header or footer for a view, configure the size of the header or footer to be non-zero. Implement the appropriate delegate methods or assign appropriate values to the [headerReferenceSize](uicollectionviewflowlayout/headerreferencesize.md) and [footerReferenceSize](uicollectionviewflowlayout/footerreferencesize.md) properties. If the header or footer size is `0`, the corresponding view isn’t added to the collection view.

## Relationships

- **Inherits From**: [UICollectionViewLayout](uicollectionviewlayout.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring the flow layout

- [UICollectionViewDelegateFlowLayout](uicollectionviewdelegateflowlayout.md) — The methods that let you coordinate with a flow layout object to implement a grid-based layout.

### Configuring the scroll direction

- [scrollDirection](uicollectionviewflowlayout/scrolldirection.md) — The scroll direction of the grid.
- [ScrollDirection](uicollectionview/scrolldirection.md) — Constants that indicate the direction of scrolling for the layout.

### Configuring item spacing

- [minimumLineSpacing](uicollectionviewflowlayout/minimumlinespacing.md) — The minimum spacing to use between lines of items in the grid.
- [minimumInteritemSpacing](uicollectionviewflowlayout/minimuminteritemspacing.md) — The minimum spacing to use between items in the same row.
- [itemSize](uicollectionviewflowlayout/itemsize.md) — The default size to use for cells.
- [estimatedItemSize](uicollectionviewflowlayout/estimateditemsize.md) — The estimated size of cells in the collection view.
- [UICollectionViewFlowLayoutAutomaticSize](uicollectionviewflowlayout/automaticsize.md) — A placeholder size for self-sizing cells.
- [sectionInset](uicollectionviewflowlayout/sectioninset.md) — The margins used to lay out content in a section.
- [sectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.property.md) — The boundary that section insets are defined in relation to.
- [SectionInsetReference](uicollectionviewflowlayout/sectioninsetreference-swift.enum.md) — Constants that describe the reference point of the section insets.

### Configuring headers and footers

- [headerReferenceSize](uicollectionviewflowlayout/headerreferencesize.md) — The default sizes to use for section headers.
- [footerReferenceSize](uicollectionviewflowlayout/footerreferencesize.md) — The default sizes to use for section footers.
- [Flow layout supplementary views](flow-layout-supplementary-views.md) — Constants that specify the types of supplementary views that can be presented using a flow layout.

### Pinning headers and footers

- [sectionHeadersPinToVisibleBounds](uicollectionviewflowlayout/sectionheaderspintovisiblebounds.md) — A Boolean value that indicates whether headers pin to the top of the collection view bounds during scrolling.
- [sectionFootersPinToVisibleBounds](uicollectionviewflowlayout/sectionfooterspintovisiblebounds.md) — A Boolean value that indicates whether footers pin to the bottom of the collection view bounds during scrolling.

## See Also

### Manual layouts

- [Customizing collection view layouts](customizing-collection-view-layouts.md) — Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [UICollectionViewLayout](uicollectionviewlayout.md) — An abstract base class for generating layout information for a collection view.
- [UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md) — A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md) — A layout object that manages the layout-related attributes for a given item in a collection view.
- [UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md) — A set of properties for determining whether to recompute the size of items or their position in the layout.
