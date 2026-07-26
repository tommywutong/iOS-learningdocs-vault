---
title: There is a Bug in the NSFetchedResultsControllerDelegate Documentation
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/nsfetchedresultscontroller-documentation-bug/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:4b8a0e9d5a00fddd'
translated: false
---

> 原文：[There is a Bug in the NSFetchedResultsControllerDelegate Documentation](https://oleb.net/blog/2013/02/nsfetchedresultscontroller-documentation-bug/)　·　Ole Begemann

# There is a Bug in the NSFetchedResultsControllerDelegate Documentation

For the longest time, the documentation for the [`NSFetchedResultsControllerDelegate` protocol](http://developer.apple.com/library/ios/#documentation/CoreData/Reference/NSFetchedResultsControllerDelegate_Protocol) has included this “best practice” code sample:

```
- (void)controller:(NSFetchedResultsController *)controller
    didChangeObject:(id)anObject atIndexPath:(NSIndexPath *)indexPath
    forChangeType:(NSFetchedResultsChangeType)type
    newIndexPath:(NSIndexPath *)newIndexPath
{
    UITableView *tableView = self.tableView;

    switch(type) {

        case NSFetchedResultsChangeInsert:
            [tableView insertRowsAtIndexPaths:[NSArray arrayWithObject:newIndexPath]
                       withRowAnimation:UITableViewRowAnimationFade];
            break;

        case NSFetchedResultsChangeDelete:
            [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath]
                       withRowAnimation:UITableViewRowAnimationFade];
            break;

        case NSFetchedResultsChangeUpdate:
            [self configureCell:[tableView cellForRowAtIndexPath:indexPath]
                  atIndexPath:indexPath];
            break;

        case NSFetchedResultsChangeMove:
            [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath]
                       withRowAnimation:UITableViewRowAnimationFade];
            [tableView insertRowsAtIndexPaths:[NSArray arrayWithObject:newIndexPath]
                       withRowAnimation:UITableViewRowAnimationFade];
            break;
    }
}
```

Unfortunately, this code contains a bug that can lead to tables displaying wrong information after updates.

# Explanation

Inside a beginUpdates/endUpdates animation block, a table view can handle an arbitrary number of updates, including insertions, deletions, movements and content updates of table rows. [The documentation is very clear on the order](http://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/TableView_iPhone/ManageInsertDeleteRow/ManageInsertDeleteRow.html#//apple_ref/doc/uid/TP40007451-CH10-SW17) these updates are processed, regardless of the order they appear in the code:

> Deletion and reloading operations within an animation block specify which rows and sections in the original table should be removed or reloaded; insertions specify which rows and sections should be added to the resulting table. The index paths used to identify sections and rows follow this model. Inserting or removing an item in a mutable array, on the other hand, may affect the array index used for the successive insertion or removal operation; for example, if you insert an item at a certain index, the indexes of all subsequent items in the array are incremented.

In other words, when the table view finally performs the update animation and queries its data source for the updated cells (i.e., when you call `endUpdates`), it may have to adjust the actual index paths it is supposed to update. For example, consider a table view that receives the following update requests:

```
[tableView beginUpdates];
NSIndexPath *updatedIndexPath = [NSIndexPath indexPathForRow:2 inSection:0];
NSIndexPath *insertedIndexPath = [NSIndexPath indexPathForRow:0 inSection:0];
[tableView reloadRowsAtIndexPaths:@[updatedIndexPath]
    withRowAnimation:UITableViewRowAnimationAutomatic];
[tableView insertRowsAtIndexPaths:@[insertedIndexPath]
    withRowAnimation:UITableViewRowAnimationAutomatic];
[tableView endUpdates];
```

Here, the third row (row index 2) is being reloaded and another row is being inserted at the top of the table. When the table view performs the update (when we call `endUpdates`), it has to consider that the underlying data model already reflects the changes. Because of the insertion at the top, the cell that was at row index 2 is now at index 3. Therefore, the table view has to query the data source for the rows at indices 0 and 3 (as opposed to 0 and 2).

Now consider Apple’s sample code from above again. When the fetched results controller sees an update in a managed object (`case NSFetchedResultsChangeUpdate:`), it calls `configureCell:atIndexPath:`, a custom helper method that takes an existing cell and updates it in place. In this case, the cell that gets passed to the method is the cell that is currently at the index path that has been updated:

```
case NSFetchedResultsChangeUpdate:
    [self configureCell:[tableView cellForRowAtIndexPath:indexPath]
        atIndexPath:indexPath];
    break;
```

This approach ignores the possibility that other rows may have been inserted or deleted within the same beginUpdates/endUpdates block. Since the call to `configureCell:atIndexPath:` is synchronous, it happens before `endUpdates` is called – the table view is still in its _before_ state. This means that `[tableView cellForRowAtIndexPath:indexPath]` will always pass the correct cell to the configureCell:atIndexPath: method. But since the Core Data model may already have changed due to an insertion or deletion of a managed object, configureCell:atIndexPath: may receive a wrong index path in its second argument, which will cause it to update the (correct) cell with wrong data.

# Fix

Fixing the bug is easy. Just rely on the behavior of UITableView I described above and replace the call to `configureCell:atIndexPath:` with the `reloadRowsAtIndexPaths:withRowAnimation:` method, which will automatically do the right thing:

```
case NSFetchedResultsChangeUpdate:
    [tableView reloadRowsAtIndexPaths:@[indexPath]
        withRowAnimation:UITableViewRowAnimationAutomatic];
    break;
```

**Update February 27, 2013:** Fixed a typo in the bugfix code snippet.

So keep in mind not to update your cells directly when you are within an update block.

I have filed a documentation bug with Apple about this issue. If you want to help get this fixed, please [duplicate](https://bugreport.apple.com) bug ID rdar://13304722. **Update March 4, 2013:** Apple quickly closed my bug as a duplicate of bug ID rdar://13246496.
