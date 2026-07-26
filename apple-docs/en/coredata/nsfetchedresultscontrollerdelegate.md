---
title: NSFetchedResultsControllerDelegate
framework: Core Data
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchedresultscontrollerdelegate
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchedresultscontrollerdelegate.json'
content_hash: 'sha256:0606927652a5e12a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchedResultsControllerDelegate

<sub>Protocol</sub>

A delegate protocol that describes the methods that the associated fetched results controller calls when the fetch results change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSFetchedResultsControllerDelegate : NSObjectProtocol
```

## Overview

Consider whether to update the table view for each change. For a large number of simultaneous modifications simultaneously, such as if your app reads data on a background thread, it may be computationally expensive to animate all the changes. Rather than respond to changes individually (as illustrated in [Typical use](nsfetchedresultscontrollerdelegate.md#Typical-use)), implement [- controllerDidChangeContent:](<nsfetchedresultscontrollerdelegate/controllerdidchangecontent(__).md>) to reload the table view after the system processes all pending changes.

> [!note] Note
> The fetched results controller reports changes to its section before changes to the fetched objects themselves.

### Typical use

When a fetched results controller provides the content to a table view, you can use [- controllerWillChangeContent:](<nsfetchedresultscontrollerdelegate/controllerwillchangecontent(__).md>) and [- controllerDidChangeContent:](<nsfetchedresultscontrollerdelegate/controllerdidchangecontent(__).md>) to bracket updates to the table view, as shown in the following example:

```swift
// Find out when the fetched results controller is about to start making changes.
func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    // Start animating table view changes simultaneously.
    tableView.beginUpdates()
}

// Find out when the fetched results controller finishes making changes.
func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    // Stop animating table view changes simultaneously.
    tableView.endUpdates()
}

// Find out when the fetched results controller adds or removes a section.
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange sectionInfo: NSFetchedResultsSectionInfo,
                atSectionIndex sectionIndex: Int,
                for type: NSFetchedResultsChangeType) {
    switch type {
    case .insert:
        // Insert a new section with fade animation.
        tableView.insertSections(IndexSet(integer: sectionIndex), with: .fade)
    case .delete:
        // Delete a section with fade animation.
        tableView.deleteSections(IndexSet(integer: sectionIndex), with: .fade)
    default:
        break
    }
}

// Find out when the fetched results controller adds, removes, moves, or
// updates a fetched object.
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange anObject: Any,
                at indexPath: IndexPath?,
                for type: NSFetchedResultsChangeType,
                newIndexPath: IndexPath?) {
    switch type {
    case .insert:
        guard let newIndexPath else { return }
        // Insert a new row with fade animation when the fetched results
        // controller adds or moves an object to the specified index path.
        tableView.insertRows(at: [newIndexPath], with: .fade)
    case .delete:
        guard let indexPath else { return }
        // Delete the row with animation at the old index path when the fetched
        // results controller deletes or moves the associated object.
        tableView.deleteRows(at: [indexPath], with: .fade)
    case .update:
        guard let indexPath else { return }
        // Update the cell as the specified indexPath.
        if let cell = tableView.cellForRow(at: indexPath) {
            cell.textLabel?.text = fetchedResultsController?.object(at: indexPath).name
        }
    case .move:
        guard let indexPath, let newIndexPath else { return }
        // Move a row from the specified index path to the new index path.
        tableView.moveRow(at: indexPath, to: newIndexPath)
    @unknown default:
        break
    }
}
```

### User-driven updates

In general, [NSFetchedResultsControllerDelegate](nsfetchedresultscontrollerdelegate.md) responds to changes at the model layer. If you allow a user to reorder table rows, then your implementation of the delegate methods needs to take this into account.

Typically, if you allow the user to reorder table rows, your model object has an attribute that specifies its index. When the user moves a row, you update this attribute accordingly. This, however, has the side effect of causing the fetched results controller to also notice the change, which causes it to inform its delegate of the update (using [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<nsfetchedresultscontrollerdelegate/controller(__didchange_at_for_newindexpath_).md>)). If you use the implementation of this method shown in the section above, then the delegate attempts to update the table view. However, the table view is already in the appropriate state because of the user’s action.

Therefore, if you support user-driven updates, you should check if the user intitiated a move, such as by setting a flag. In the implementation of your delegate methods, bypass the method implementation if the user initiated the move, for example:

```objc
func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>,
                didChange anObject: Any,
                at indexPath: IndexPath?,
                for type: NSFetchedResultsChangeType,
                newIndexPath: IndexPath?) {
    // If you allow users to reorder table rows, bypass automated handling
    // of the change because the model layer already handles it.
    guard changeIsUserDriven == false else { return }
    
    switch type {
    case .insert:
        guard let newIndexPath else { return }
    // Remaining implementation.
}
```

> [!note] Note
> Prior to iOS 4.0, [NSFetchedResultsController](nsfetchedresultscontroller.md) doesn’t support deleting sections as a result of a UI-driven change.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Changes

- [- controller:didChangeContentWithSnapshot:](<nsfetchedresultscontrollerdelegate/controller(__didchangecontentwith_)-4kezq.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a diffable data source snapshot.
- [- controller:didChangeContentWithDifference:](<nsfetchedresultscontrollerdelegate/controller(__didchangecontentwith_)-5ullb.md>) — Notifies the receiver about changes to the content in the fetched results controller, by using a collection difference.
- [- controllerWillChangeContent:](<nsfetchedresultscontrollerdelegate/controllerwillchangecontent(__).md>) — Notifies the receiver that the fetched results controller is about to start processing of one or more changes due to an add, remove, move, or update.
- [- controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](<nsfetchedresultscontrollerdelegate/controller(__didchange_at_for_newindexpath_).md>) — Notifies the receiver that a fetched object has been changed due to an add, remove, move, or update.
- [- controller:didChangeSection:atIndex:forChangeType:](<nsfetchedresultscontrollerdelegate/controller(__didchange_atsectionindex_for_).md>) — Notifies the receiver of the addition or removal of a section.
- [- controllerDidChangeContent:](<nsfetchedresultscontrollerdelegate/controllerdidchangecontent(__).md>) — Notifies the receiver that the fetched results controller has completed processing of one or more changes due to an add, remove, move, or update.

### Customizing Section Names

- [- controller:sectionIndexTitleForSectionName:](<nsfetchedresultscontrollerdelegate/controller(__sectionindextitleforsectionname_).md>) — Returns the name for a given section.

### Constants

- [NSFetchedResultsChangeType](nsfetchedresultschangetype.md) — Constants that specify the possible types of changes that are reported.

## See Also

### Responding to Changes

- [NSFetchedResultsSectionInfo](nsfetchedresultssectioninfo.md) — A protocol that defines the interface for section objects vended by a fetched results controller.
- [NSFetchRequestResultType](nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
- [NSFetchedResultsChangeType](nsfetchedresultschangetype.md) — Constants that specify the possible types of changes that are reported.
