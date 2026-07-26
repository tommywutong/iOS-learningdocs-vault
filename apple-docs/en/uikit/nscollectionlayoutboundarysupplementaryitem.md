---
title: NSCollectionLayoutBoundarySupplementaryItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutboundarysupplementaryitem
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutboundarysupplementaryitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutboundarysupplementaryitem.json'
content_hash: 'sha256:25b1efeac35717cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutBoundarySupplementaryItem

<sub>Class</sub>

An object used to add headers or footers to a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutBoundarySupplementaryItem
```

## Overview

A boundary supplementary item is a specialized type of supplementary item ([NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)). You use boundary supplementary items to add headers or footers to a section of a collection view or the entire collection view.

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

Add boundary supplementary items to a section by setting that section’s [boundarySupplementaryItems](nscollectionlayoutsection/boundarysupplementaryitems.md) property:

**Swift**

```swift
let section = NSCollectionLayoutSection(group: group)

let headerFooterSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                             heightDimension: .estimated(44))
    
let sectionHeader = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: headerFooterSize,
                                                               elementKind: ElementKind.sectionHeader,
                                                                 alignment: .top)
let sectionFooter = NSCollectionLayoutBoundarySupplementaryItem(layoutSize: headerFooterSize,
                                                               elementKind: ElementKind.sectionFooter,
                                                                 alignment: .bottom)
    
section.boundarySupplementaryItems = [sectionHeader, sectionFooter]
```

**Objective-C**

```objc
NSCollectionLayoutSection *section = [NSCollectionLayoutSection sectionWithGroup:group];

NSCollectionLayoutSize *headerFooterSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:1.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];

NSCollectionLayoutBoundarySupplementaryItem *sectionHeader = [NSCollectionLayoutBoundarySupplementaryItem boundarySupplementaryItemWithLayoutSize: headerFooterSize elementKind: ELEMENT_KIND_SECTION_HEADER alignment: NSRectAlignmentTop];

NSCollectionLayoutBoundarySupplementaryItem *sectionFooter = [NSCollectionLayoutBoundarySupplementaryItem boundarySupplementaryItemWithLayoutSize: headerFooterSize elementKind: ELEMENT_KIND_SECTION_FOOTER alignment: NSRectAlignmentBottom];

[section setBoundarySupplementaryItems: @[sectionHeader, sectionFooter]];
```

## Relationships

- **Inherits From**: [NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a boundary supplementary item

- [+ boundarySupplementaryItemWithLayoutSize:elementKind:alignment:](<nscollectionlayoutboundarysupplementaryitem/init(layoutsize_elementkind_alignment_).md>) — Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout.
- [+ boundarySupplementaryItemWithLayoutSize:elementKind:alignment:absoluteOffset:](<nscollectionlayoutboundarysupplementaryitem/init(layoutsize_elementkind_alignment_absoluteoffset_).md>) — Creates a boundary supplementary item of the specified size and element kind, with an alignment relative to a section or layout at an absolute offset.

### Specifying scrolling behavior

- [pinToVisibleBounds](nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds.md) — A Boolean value that indicates whether a header or footer is pinned to the top or bottom visible boundary of the section or layout it’s attached to.

### Specifying position

- [offset](nscollectionlayoutboundarysupplementaryitem/offset.md) — The floating-point value of the boundary supplementary item’s offset from the section or layout it’s attached to.
- [alignment](nscollectionlayoutboundarysupplementaryitem/alignment.md) — The alignment of the boundary supplementary item relative to the section or layout it’s attached to.
- [extendsBoundary](nscollectionlayoutboundarysupplementaryitem/extendsboundary.md) — A Boolean value that indicates whether a boundary supplementary item extends the content area of the section or layout it’s attached to.

## See Also

### Appearance

- [NSCollectionLayoutAnchor](nscollectionlayoutanchor.md) — An object that defines how to attach a supplementary item to an item in a collection view.
- [NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md) — An object used to add an extra visual decoration to an item in a collection view.
- [NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md) — An object used to add a background to a section of a collection view.
