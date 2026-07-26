---
title: NSCollectionLayoutDecorationItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutdecorationitem
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutdecorationitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutdecorationitem.json'
content_hash: 'sha256:a5608f3c8de2e4d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutDecorationItem

<sub>Class</sub>

An object used to add a background to a section of a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutDecorationItem
```

## Overview

Each type of decoration item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

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

Add a background to a section by setting that section’s [decorationItems](nscollectionlayoutsection/decorationitems.md) property:

**Swift**

```swift
let sectionBackground = NSCollectionLayoutDecorationItem.background(
        elementKind: ElementKind.background)

section.decorationItems = [sectionBackground]

let layout = UICollectionViewCompositionalLayout(section: section)
layout.register(
    SectionBackgroundDecorationView.self,
    forDecorationViewOfKind: ElementKind.background)
return layout
```

**Objective-C**

```objc
NSCollectionLayoutDecorationItem *sectionBackground = [NSCollectionLayoutDecorationItem backgroundDecorationItemWithElementKind: ELEMENT_KIND_BACKGROUND];

[section setDecorationItems: @[sectionBackground]];

UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSection: section];
[layout registerClass: [SectionBackgroundDecorationView class] forDecorationViewOfKind: ELEMENT_KIND_BACKGROUND];
return layout;
```

## Relationships

- **Inherits From**: [NSCollectionLayoutItem](nscollectionlayoutitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a background

- [+ backgroundDecorationItemWithElementKind:](<nscollectionlayoutdecorationitem/background(elementkind_).md>) — Creates a section background with a string to identify the element kind.

### Getting the element kind

- [elementKind](nscollectionlayoutdecorationitem/elementkind.md) — A string that identifies the type of decoration item.

### Specifying stacking order

- [zIndex](nscollectionlayoutdecorationitem/zindex.md) — The vertical stacking order of the decoration item in relation to other items in the section.

## See Also

### Appearance

- [NSCollectionLayoutAnchor](nscollectionlayoutanchor.md) — An object that defines how to attach a supplementary item to an item in a collection view.
- [NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md) — An object used to add an extra visual decoration to an item in a collection view.
- [NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md) — An object used to add headers or footers to a collection view.
