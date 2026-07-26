---
title: 'controller(_:didChange:atSectionIndex:for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/controller(_:didchange:atsectionindex:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate/controller%28_%3Adidchange%3Aatsectionindex%3Afor%3A%29.json'
content_hash: 'sha256:966f8f8760ea9f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchedResultsControllerDelegate](../nsfetchedresultscontrollerdelegate.md)

# controller(_:didChange:atSectionIndex:for:)

<sub>Instance Method</sub>

Notifies the receiver of the addition or removal of a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func controller(_ controller: NSFetchedResultsController<any NSFetchRequestResult>, didChange sectionInfo: any NSFetchedResultsSectionInfo, atSectionIndex sectionIndex: Int, for type: NSFetchedResultsChangeType)
```

## Parameters

- `controller` — The fetched results controller that sent the message.

- `sectionInfo` — The section that changed.

- `sectionIndex` — The index of the changed section.

- `type` — The type of change (insert or delete). Valid values are [NSFetchedResultsChangeInsert](../nsfetchedresultschangetype/insert.md) and [NSFetchedResultsChangeDelete](../nsfetchedresultschangetype/delete.md).

## Discussion

The fetched results controller reports changes to its section before changes to the fetched result objects.

### Special Considerations

This method may be invoked many times during an update event (for example, if you are importing data on a background thread and adding them to the context in a batch). You should consider carefully whether you want to update the table view on receipt of each message.

## See Also

### Responding to Changes

- [- controller:didChangeContentWithSnapshot:](<controller(__didchangecontentwith_)-4kezq.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [- controller:didChangeContentWithDifference:](<controller(__didchangecontentwith_)-5ullb.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [- controllerWillChangeContent:](<controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<controller(__didchange_at_for_newindexpath_).md>) — Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [- controllerDidChangeContent:](<controllerdidchangecontent(__).md>) — Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.
