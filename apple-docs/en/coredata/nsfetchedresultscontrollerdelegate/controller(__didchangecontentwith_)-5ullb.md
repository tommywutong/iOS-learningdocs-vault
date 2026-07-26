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
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchangecontentwith:)-5ullb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controller%28_%3Adidchangecontentwith%3A%29-5ullb.json'
content_hash: 'sha256:ee4668cb4bdece54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controller(_:didChangeContentWith:)

<sub>Instance Method</sub>

Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChangeContentWith diff: CollectionDifference<NSManagedObjectID>)
```

## Discussion

This method is only invoked if the controller’s [sectionNameKeyPath](../nsfetchedresultscontroller/sectionnamekeypath.md) property is `nil` and [- controller:didChangeContentWithSnapshot:](<controller(__didchangecontentwith_)-4kezq.md>) is not implemented.

If this method is implemented, no other delegate methods are invoked.

## See Also

### Responding to Changes

- [- controller:didChangeContentWithSnapshot:](<controller(__didchangecontentwith_)-4kezq.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [- controllerWillChangeContent:](<controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<controller(__didchange_at_for_newindexpath_).md>) — Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [- controller:didChangeSection:atIndex:forChangeType:](<controller(__didchange_atsectionindex_for_).md>) — Notifies the receiver of the addition or removal of a section.
- [- controllerDidChangeContent:](<controllerdidchangecontent(__).md>) — Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.
