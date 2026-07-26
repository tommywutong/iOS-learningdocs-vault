---
title: NSCollectionLayoutSupplementaryItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsupplementaryitem
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsupplementaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsupplementaryitem.json'
content_hash: 'sha256:83659ec8e130724a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutSupplementaryItem

<sub>Class</sub>

An object used to add an extra visual decoration to an item in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutSupplementaryItem
```

## Overview

You use supplementary items to attach additional views to your content. For example, you might attach a badge to an item or a frame around a group. A supplementary item follows the index path of the item it’s attached to.

If you want to create a header or footer for your layout or its sections, use a boundary supplementary item ([NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)) instead.

Each type of supplementary item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

**Swift**

```swift
struct ElementKind {
    static let badge = "badge-element-kind"
    static let background = "background-element-kind"
    static let sectionHeader = "section-header-element-kind"
    static let sectionFooter = "section-footer-element-kind"
    static let layoutHeader = "layout-header-element-kind"
    static let layoutFooter = "layout-footer-element-kind"
}
```

**Objective-C**

```objc
NSString* const ELEMENT_KIND_BADGE = @"badge-element-kind";
NSString* const ELEMENT_KIND_BACKGROUND = @"background-element-kind";
NSString* const ELEMENT_KIND_SECTION_HEADER = @"section-header-element-kind";
NSString* const ELEMENT_KIND_SECTION_FOOTER = @"section-footer-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_HEADER = @"layout-header-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_FOOTER = @"layout-footer-element-kind";
```

Add supplementary items to an item by passing in an array of supplementary items when you construct the item:

**Swift**

```swift
let itemSize = NSCollectionLayoutSize(widthDimension: .absolute(44),
                                     heightDimension: .absolute(44))
    
let badgeAnchor = NSCollectionLayoutAnchor(edges: [.top, .trailing],
                                fractionalOffset: CGPoint(x: 0.3, y: -0.3))
   
let badgeSize = NSCollectionLayoutSize(widthDimension: .absolute(20),
                                      heightDimension: .absolute(20))
    
let badge = NSCollectionLayoutSupplementaryItem(layoutSize: badgeSize,
                                               elementKind: ElementKind.badge,
                                           containerAnchor: badgeAnchor)
    
let item = NSCollectionLayoutItem(layoutSize: itemSize,
                          supplementaryItems: [badge])
```

**Objective-C**

```objc
NSCollectionLayoutSize *itemSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:44.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];

NSCollectionLayoutAnchor *badgeAnchor = [NSCollectionLayoutAnchor layoutAnchorWithEdges: NSDirectionalRectEdgeTop|NSDirectionalRectEdgeTrailing fractionalOffset:CGPointMake(0.3, -0.3)];

NSCollectionLayoutSize *badgeSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:20.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:20.0]];

NSCollectionLayoutSupplementaryItem *badge = [NSCollectionLayoutSupplementaryItem supplementaryItemWithLayoutSize:badgeSize elementKind:ELEMENT_KIND_BADGE containerAnchor:badgeAnchor];

NSCollectionLayoutItem *item = [NSCollectionLayoutItem itemWithLayoutSize:itemSize supplementaryItems:@[badge]];

```

## Relationships

- **Inherits From**: [NSCollectionLayoutItem](nscollectionlayoutitem.md)

- **Inherited By**: [NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a supplementary item

- [+ supplementaryItemWithLayoutSize:elementKind:containerAnchor:](<nscollectionlayoutsupplementaryitem/init(layoutsize_elementkind_containeranchor_).md>) — Creates a supplementary item of the specified size and element kind, with an anchor relative to a container.
- [+ supplementaryItemWithLayoutSize:elementKind:containerAnchor:itemAnchor:](<nscollectionlayoutsupplementaryitem/init(layoutsize_elementkind_containeranchor_itemanchor_).md>) — Creates a supplementary item of the specified size and element kind, an anchor relative to a container, and an anchor relative to an item.

### Getting the anchors

- [itemAnchor](nscollectionlayoutsupplementaryitem/itemanchor.md) — The anchor between the supplementary item and the item it’s attached to.
- [containerAnchor](nscollectionlayoutsupplementaryitem/containeranchor.md) — The anchor between the supplementary item and the container it’s attached to.

### Getting the element kind

- [elementKind](nscollectionlayoutsupplementaryitem/elementkind.md) — A string that identifies the type of supplementary item.

### Specifying stacking order

- [zIndex](nscollectionlayoutsupplementaryitem/zindex.md) — The vertical stacking order of the supplementary item in relation to other items in the section.

## See Also

### Appearance

- [NSCollectionLayoutAnchor](nscollectionlayoutanchor.md) — An object that defines how to attach a supplementary item to an item in a collection view.
- [NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md) — An object used to add headers or footers to a collection view.
- [NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md) — An object used to add a background to a section of a collection view.
