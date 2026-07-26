---
title: NSCollectionLayoutSectionVisibleItemsInvalidationHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsectionvisibleitemsinvalidationhandler
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsectionvisibleitemsinvalidationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsectionvisibleitemsinvalidationhandler.json'
content_hash: 'sha256:1ccb91236791a067'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutSectionVisibleItemsInvalidationHandler

<sub>Type Alias</sub>

A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler = ([any NSCollectionLayoutVisibleItem], CGPoint, any NSCollectionLayoutEnvironment) -> Void
```

## Discussion

Each section of a collection view layout can have a visible items invalidation handler. You use this handler to perform custom animations on the items currently visible within the bounds of that section. The handler is called before each layout cycle, any time an animation occurs in that section due to changes such as adding or removing items, scrolling the section, or rotating the device.

**Swift**

```swift
let section = NSCollectionLayoutSection(group: group)
    
section.visibleItemsInvalidationHandler = { visibleItems, scrollOffset, layoutEnvironment in
    // Perform animations on the visible items.
}
```

**Objective-C**

```objc
NSCollectionLayoutSection *section = [NSCollectionLayoutSection sectionWithGroup:group];

[section setVisibleItemsInvalidationHandler:^(NSArray<id<NSCollectionLayoutVisibleItem>> *visibleItems, CGPoint contentOffset, id<NSCollectionLayoutEnvironment> layoutEnvironment) {
    // Perform animations on the visible items.
}];
```

## See Also

### Layout updates

- [NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md) — An item that’s currently visible within the bounds of a section.
- [UICollectionViewUpdateItem](uicollectionviewupdateitem.md) — An object that describes a single change to make to an item in a collection view.
- [UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md) — A context object that stores information specific to a focus update in a collection view.
- [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md) — A context object that declares which parts of your layout need to be updated when the layout is invalidated.
