---
title: 'NSFetchedResultsController: Moved objects sometimes reported as updated'
apple_id: TP40009210
resource_type: Technical Note
platform: watchOS|iOS
topic: null
technology: CoreData
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/releasenotes/iPhone/NSFetchedResultsChangeMoveReportedAsNSFetchedResultsChangeUpdate/index.html
archived_at: '2026-07-26T19:54:16.213453Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# NSFetchedResultsController: Moved Objects Sometimes Reported as Updated

In some situations, an instance of [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller) may report moved objects using a [NSFetchedResultsChangeUpdate](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/nsfetchedresultschangeupdate) change notification instead of [NSFetchedResultsChangeMove](https://developer.apple.com/documentation/coredata/nsfetchedresultschangetype/nsfetchedresultschangemove).

A fetched results controller only sends object change notifications tagged as `NSFetchedResultsChangeMove` when the original index path is different from the new index path. It's possible that a series of object changes can result in an object being moved (such as moving to a new section), yet its relative index path remain the same (if other object changes happened in objects that appear before the moved object). This scenario will result in a `NSFetchedResultsChangeUpdate` notification being sent to the delegate.

A possible workaround is to maintain an extra (non modeled) instance variable in your object that indicates when an object has changed section (due to a change in its property that determines the section). For example, you might declare a custom class as follows:

```objc
@interface MyClass : NSManagedObject
{
    BOOL _changedSection;
}

// The modeled property that determines the object's section.
@property (nonatomic, retain) NSString *theSectionKey;

// The unmodeled property that tracks if a section was recently changed.
@property BOOL changedSection;

@end
```

The corresponding implementation might be:

```objc
@synthesize changedSection=_ changedSection;

- (void)setTheSectionKey:(id)value
{
    if (value != theSectionKey) {
        changedSection = YES;
    }

    [self willChangeValueForKey:@"theSectionKey"];
    [self setPrimitiveTheSectionKey:value];
    [self didChangeValueForKey:@"theSectionKey"];
}
```

You can then use this property to determine if a change flagged as `NSFetchedResultsChangeUpdate` should actually be treated as a `NSFetchedResultsChangeMove` by implementing [controller:didChangeObject:atIndexPath:forChangeType:newIndexPath:](https://developer.apple.com/documentation/coredata/nsfetchedresultscontrollerdelegate/1622296-controller) as illustrated in this example:

```objc
- (void)controller:(NSFetchedResultsController *)controller didChangeObject:(id)anObject atIndexPath:(NSIndexPath *)indexPath forChangeType:(NSFetchedResultsChangeType)type newIndexPath:(NSIndexPath *)newIndexPath {

    UITableView *tableView = self.tableView;

    // This is the workaround.
    MyClass *myInstance = (MyClass *)anObject;
    if ( (NSFetchedResultsChangeUpdate == type) && ([myInstance changedSection]) ) {
        [myInstance  setChangedSection:NO];
        type = NSFetchedResultsChangeMove;
        newIndexPath = indexPath;
    }
    switch(type) {
        case NSFetchedResultsChangeInsert:
            [tableView insertRowsAtIndexPaths:[NSArray arrayWithObject:newIndexPath] withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeDelete:
            [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
            break;
        case NSFetchedResultsChangeUpdate:
            [self configureCell:(ExpenseCell *)[self.tableView cellForRowAtIndexPath:indexPath] atIndexPath:indexPath];
            break;
        case NSFetchedResultsChangeMove:
            [tableView deleteRowsAtIndexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
            [tableView insertRowsAtIndexPaths:[NSArray arrayWithObject:newIndexPath] withRowAnimation:UITableViewRowAnimationFade];
            break;
    }
}
```
