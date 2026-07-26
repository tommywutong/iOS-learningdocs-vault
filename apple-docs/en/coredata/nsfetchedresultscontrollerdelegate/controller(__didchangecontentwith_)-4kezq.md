---
title: 'controller(_:didChangeContentWith:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-4kezq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controller%28_%3Adidchangecontentwith%3A%29-4kezq.json'
content_hash: 'sha256:a16ce3a83c941e6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controller(_:didChangeContentWith:)

<sub>Instance Method</sub>

Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith snapshot: NSDiffableDataSourceSnapshot)
```

## Discussion

To apply the changes, call [applySnapshot(_:animatingDifferences:)](<../../uikit/uitableviewdiffabledatasourcereference/applysnapshot(__animatingdifferences_).md>) on the collection or table view’s data source.

If this method is implemented, no other delegate methods are invoked.

## See Also

### Responding to Changes

- [- controller:didChangeContentWithDifference:](<controller(__didchangecontentwith_)-5ullb.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [- controllerWillChangeContent:](<controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<controller(__didchange_at_for_newindexpath_).md>) — Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [- controller:didChangeSection:atIndex:forChangeType:](<controller(__didchange_atsectionindex_for_).md>) — Notifies the receiver of the addition or removal of a section.
- [- controllerDidChangeContent:](<controllerdidchangecontent(__).md>) — Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.
