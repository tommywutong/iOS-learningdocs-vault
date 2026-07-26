---
title: UICollectionViewFocusUpdateContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewfocusupdatecontext
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewfocusupdatecontext.json'
content_hash: 'sha256:8b877ac7c410005b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewFocusUpdateContext

<sub>Class</sub>

A context object that stores information specific to a focus update in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewFocusUpdateContext
```

## Overview

When focus changes, the collection view delegate receives a context object with the relevant information. Your delegate methods use the information in this object to create animations or to perform other tasks related to the change in focus.

## Relationships

- **Inherits From**: [UIFocusUpdateContext](uifocusupdatecontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Locating focusable items in the collection view

- [previouslyFocusedIndexPath](uicollectionviewfocusupdatecontext/previouslyfocusedindexpath.md) — The index path of the collection view cell that previously had the focus.
- [nextFocusedIndexPath](uicollectionviewfocusupdatecontext/nextfocusedindexpath.md) — The index path of the collection view cell that’s receiving the focus.

## See Also

### Layout updates

- [NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md) — An item that’s currently visible within the bounds of a section.
- [NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md) — A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [UICollectionViewUpdateItem](uicollectionviewupdateitem.md) — An object that describes a single change to make to an item in a collection view.
- [UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md) — A context object that declares which parts of your layout need to be updated when the layout is invalidated.
