---
title: UIDataSourceTranslating
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatasourcetranslating
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcetranslating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcetranslating.json'
content_hash: 'sha256:f9e982136de3e38b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDataSourceTranslating

<sub>Protocol</sub>

An advanced interface for managing a data source object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIDataSourceTranslating : NSObjectProtocol
```

## Overview

Use the methods of this protocol to map between the positions of items and sections in your data source object and the positions of those same items and sections in your presented layout. Objects that adopt this protocol do so because the position of items in their data source object don’t always match the corresponding positions in their presented layout.

[UITableView](uitableview.md) and [UICollectionView](uicollectionview.md) adopt this protocol and use it in conjunction with drag and drop operations. For example, [UITableView](uitableview.md) must account for the presence of placeholder cells, which appear as rows in the table but don’t have a corresponding entry in the data source object. Typically, you don’t adopt this protocol in your own classes.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UICollectionView](uicollectionview.md), [UITableView](uitableview.md)

## Topics

### Managing item positions

- [- presentationIndexPathForDataSourceIndexPath:](<uidatasourcetranslating/presentationindexpath(fordatasourceindexpath_).md>) — Translates an index in your data source object to the equivalent index in your presented layout.
- [- dataSourceIndexPathForPresentationIndexPath:](<uidatasourcetranslating/datasourceindexpath(forpresentationindexpath_).md>) — Translates an index in your presented layout to the equivalent index in your data source object.

### Managing section positions

- [- presentationSectionIndexForDataSourceSectionIndex:](<uidatasourcetranslating/presentationsectionindex(fordatasourcesectionindex_).md>) — Translates a section index in your data source object to the equivalent section index in your presented layout.
- [- dataSourceSectionIndexForPresentationSectionIndex:](<uidatasourcetranslating/datasourcesectionindex(forpresentationsectionindex_).md>) — Translates a section index in your presented layout to the equivalent section index in your data source object.

### Performing actions

- [- performUsingPresentationValues:](<uidatasourcetranslating/performusingpresentationvalues(__).md>) — Performs actions on the current object using index paths that are relative to the presentation layer of that object.

## See Also

### Drag and drop

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md) — Initiate drags and handle drops from a collection view.
- [UICollectionViewDragDelegate](uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [UICollectionViewDropDelegate](uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md) — An interface for coordinating your custom drop-related actions with the collection view.
- [UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md) — A placeholder for an item dropped on a collection view.
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md) — Your proposed solution for handling a drop in a collection view.
- [UICollectionViewDropItem](uicollectionviewdropitem.md) — The data associated with an item being dropped into the collection view.
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md) — An object that contains information about a placeholder in the collection view.
- [UICollectionViewPlaceholder](uicollectionviewplaceholder.md) — A placeholder for an item dragged or dropped on a collection view.
