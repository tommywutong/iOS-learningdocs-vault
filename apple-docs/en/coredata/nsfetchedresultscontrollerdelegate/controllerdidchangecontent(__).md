---
title: 'controllerDidChangeContent(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controllerdidchangecontent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controllerdidchangecontent%28_%3A%29.json'
content_hash: 'sha256:8269824d8abe1d42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controllerDidChangeContent(_:)

<sub>Instance Method</sub>

Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controllerDidChangeContent(_ controller: NSFetchedResultsController<any NSFetchRequestResult>)
```

## Parameters

- `controller` — The fetched results controller that sent the message.

## Discussion

This method is invoked after all invocations of [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<controller(__didchange_at_for_newindexpath_).md>) and [- controller:didChangeSection:atIndex:forChangeType:](<controller(__didchange_atsectionindex_for_).md>) have been sent for a given change event (such as the controller receiving a [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) notification).

## See Also

### Responding to Changes

- [- controller:didChangeContentWithSnapshot:](<controller(__didchangecontentwith_)-4kezq.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [- controller:didChangeContentWithDifference:](<controller(__didchangecontentwith_)-5ullb.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [- controllerWillChangeContent:](<controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<controller(__didchange_at_for_newindexpath_).md>) — Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [- controller:didChangeSection:atIndex:forChangeType:](<controller(__didchange_atsectionindex_for_).md>) — Notifies the receiver of the addition or removal of a section.
