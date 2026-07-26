---
title: UICollectionViewUpdateItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewupdateitem
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewupdateitem.json'
content_hash: 'sha256:d6b5fee4fe0a8726'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewUpdateItem

<sub>Class</sub>

An object that describes a single change to make to an item in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewUpdateItem
```

## Overview

You don’t create instances of this class directly. When updating its content, the collection view object creates them and passes them to the layout object’s [- prepareForCollectionViewUpdates:](<uicollectionviewlayout/prepare(forcollectionviewupdates_).md>) method, which can use them to prepare the layout object for the upcoming changes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Accessing the item changes

- [indexPathBeforeUpdate](uicollectionviewupdateitem/indexpathbeforeupdate.md) — The index path of the item before the update.
- [indexPathAfterUpdate](uicollectionviewupdateitem/indexpathafterupdate.md) — The index path of the item after the update.
- [updateAction](uicollectionviewupdateitem/updateaction.md) — The action being performed on the item.
- [Action](uicollectionviewupdateitem/action.md) — Constants indicating the type of action being performed on an item.

## See Also

### Layout updates

- [NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md) — An item that’s currently visible within the bounds of a section.
- [NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md) — A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md) — A context object that stores information specific to a focus update in a collection view.
- [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md) — A context object that declares which parts of your layout need to be updated when the layout is invalidated.
