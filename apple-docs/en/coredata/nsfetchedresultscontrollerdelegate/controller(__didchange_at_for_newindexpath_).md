---
title: 'controller(_:didChange:at:for:newIndexPath:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchange:at:for:newindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controller%28_%3Adidchange%3Aat%3Afor%3Anewindexpath%3A%29.json'
content_hash: 'sha256:eb60811c527ec7ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controller(_:didChange:at:for:newIndexPath:)

<sub>Instance Method</sub>

Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChange anObject: Any, at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?)
```

## Parameters

- `controller` — The fetched results controller that sent the message.

- `anObject` — The object in controller’s fetched results that changed.

- `indexPath` — The index path of the changed object (this value is `nil` for insertions).

- `type` — The type of change. For valid values see [NSFetchedResultsChangeType](../nsfetchedresultschangetype.md).

- `newIndexPath` — The destination path for the object for insertions or moves (this value is `nil` for a deletion).

## Discussion

The fetched results controller reports changes to its section before changes to the fetch result objects.

Changes are reported with the following heuristics:

- On add and remove operations, only the added/removed object is reported.

It’s assumed that all objects that come after the affected object are also moved, but these moves are not reported.

- A move is reported when the changed attribute on the object is one of the sort descriptors used in the fetch request.

An update of the object is assumed in this case, but no separate update message is sent to the delegate.

- An update is reported when an object’s state changes, but the changed attributes aren’t part of the sort keys.

### Special Considerations

This method may be invoked many times during an update event (for example, if you are importing data on a background thread and adding them to the context in a batch). You should consider carefully whether you want to update the table view on receipt of each message.

## See Also

### Responding to Changes

- [- controller:didChangeContentWithSnapshot:](<controller(__didchangecontentwith_)-4kezq.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [- controller:didChangeContentWithDifference:](<controller(__didchangecontentwith_)-5ullb.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [- controllerWillChangeContent:](<controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeSection:atIndex:forChangeType:](<controller(__didchange_atsectionindex_for_).md>) — Notifies the receiver of the addition or removal of a section.
- [- controllerDidChangeContent:](<controllerdidchangecontent(__).md>) — Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.
