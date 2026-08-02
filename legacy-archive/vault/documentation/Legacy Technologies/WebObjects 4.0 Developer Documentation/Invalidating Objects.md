---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/invalidate.html
archived_at: '2026-07-15T08:01:39.445066Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Invalidating Objects

##  Synopsis

Describes when and how to invalidate objects to clear up the caches used by the Enterprise Objects Framework (EOF).

##  Description

Enterprise Objects Framework (EOF) automatically caches the raw dictionary of values and unique objects that are fetched from the database. The raw dictionary is cached in a set of snapshots based on a GlobalID derived from the primary keys of the database rows. All peer EOEditingContexts share this common cache of snapshots. Each EOEditingContext stores its own unique object instance for a given GlobalID. Whenever the common snapshots change, an EOObjectsChangedInStore notification is posted and all associated EOEditingContexts attempt to reconcile themselves with the new snapshot.

Sometimes you need to clear the snapshot caches to refresh the objects in your editing contexts. EOF provides object invalidation methods to clear the caches. These methods are also the only way to clear a database lock without saving your changes.

To understand how these methods work, consider the following objects subclassed from EOObjectStore: EODatabaseContext, EOObjectStoreCoordinator and EOEditingContext. EOObjectStores maintain collections of Enterprise Objects (EOs), and are organized in a multitiered tree with the EOObjectStores closest to the database at the bottom and those closest to the user interface at the top. Starting from the bottom, an application's EOObjectStore tree consists of:

· One or more EODatabaseContexts

· One EOObjectStoreCoordinator

· One or more EOEditingContexts

· Potentially some nested EOEditingContexts

The invalidating methods will have a different effect on the EOObjectStores in the EOObjectStore tree.

If you send _invalidateAllObjects_
to a nested EOEditingContext, it sends _invalidateObjectsWithGlobalIDs:_
to its parent EOEditingContext with the global IDs of its registered objects. The parent EOEditingContext propagates this message to the EOObjectStoreCoordinator, which propagates it to the EODatabaseContext(s). The EODatabaseContext throws away the snapshots corresponding to the global IDs and sends an _ObjectChangedInStoreNotification_
, which changes all of those objects to faults throughout your whole tree. The next time you examine one of these objects, it will be refetched from the database.

If you send the message _invalidateAllObjects_
directly to your EOObjectStoreCoordinator, it will send the _invalidateAllObjects_
to all of its EODatabaseContexts. As a consequence, all the snapshots in your application will be discarded and every enterprise object in every EOEditingContext will become a fault.

The following code shows how to invalidate an object in the default editing context.

#####  Figure 1. Java Code

```
// Invalidate the object, converting it back to a fault.
```



```
EOEditingContext ec=session().defaultEditingContext();
```



```
ec.invalidateObjectsWithGlobalIDs(new NSArray(
```



```
    ec.globalIDForObject(theObject)));
```


#####  Figure 2. Objective-C Code

```
// Invalidate the object, converting it back to a fault.
```



```
EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
[ec invalidateObjectsWithGlobalIDs:[NSArray arrayWithObject:
```



```
    [ec globalIDForObject:theObject]]];
```


You can also invalidate all objects in an editing context using _invalidateAllObjects_
.

#####  Figure 3. Java Code

```
// Invalidate all objects in the editing context, converting them to faults.
```



```
EOEditingContext ec=session().defaultEditingContext();
```



```
ec.invalidateAllObjects;
```


#####  Figure 4. Objective-C Code

```
// Invalidate all objects in an editing context, converting them to faults.
```



```
EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
[ec invalidateAllObjects];
```


####  Gotchas

The _setInvalidatesObjectsWhenFreed_
method defined in the EOEditingContext class does not free the object snapshots, even when it is called with the default value of _true/YES_
. Consequently, to avoid the memory leaks when an EOEditingContext is deallocated, you need to free the snapshots explicitly using the invalidating methods.

The snapshots associated with an EOEditingContext is never automatically released, even when the EOEditingContext is deallocated. This means that as data is fetched from the database, the number of snapshots, and hence your memory usage, will grow until you pull the whole database into memory.

This is a known problem with EOF that will be addressed in future releases.

##  See Also

· Refreshing Data by Refetching from the Database or Invalidating an Object

· Detecting Memory Leaks

· EOObjectStore

· EOEditingContext

##  Questions

· How can I prevent the memory from growing constantly in my application?

· When should I use _invalidateAllObjects_
?

##  Keywords

· _InvalidateAllObjects_

· _InvalidateObjectsWithGlobalIDs_

· _setInvalidatesObjectsWhenFreed_

##  Revision History

24 July, 1998. Mai Nguyen. First Draft.

19 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
