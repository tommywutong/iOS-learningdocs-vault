---
title: UICollectionViewDropProposal
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewdropproposal
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropproposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropproposal.json'
content_hash: 'sha256:67fb4f205b42830e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewDropProposal

<sub>Class</sub>

Your proposed solution for handling a drop in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UICollectionViewDropProposal
```

## Overview

Create instances of this class in the [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<uicollectionviewdropdelegate/collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) method of your drop delegate object. You create drop proposals to let the collection view know how you intend to handle a drop at the currently specified location. The collection view uses that information to provide appropriate visual feedback to the user.

## Relationships

- **Inherits From**: [UIDropProposal](uidropproposal.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Drop Proposal

- [- initWithDropOperation:intent:](<uicollectionviewdropproposal/init(operation_intent_).md>) — Creates a drop proposal object that specifies how to incorporate the dropped content.

### Getting the Proposed Drop Location

- [intent](uicollectionviewdropproposal/intent-swift.property.md) — The option to use when incorporating the dropped items into your content.
- [Intent](uicollectionviewdropproposal/intent-swift.enum.md) — Constants indicating how you intend to handle a drop.
- [UIDropOperation](uidropoperation.md) — Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

### Initializers

- [init(dropOperation:intent:)](<uicollectionviewdropproposal/init(dropoperation_intent_).md>)

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — The data associated with an item being dropped into the collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UIDataSourceTranslating](uidatasourcetranslating.md) — An advanced interface for managing a data source object.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
