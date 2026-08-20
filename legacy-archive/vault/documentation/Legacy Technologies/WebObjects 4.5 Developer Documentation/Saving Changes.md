---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/BehindSc3.html
archived_at: '2026-07-15T08:02:54.379176Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Behind%20the%20Scenes.md) [!Previous Section](How%20Changes%20are%20Distributed%20and%20Applied.md)

# Saving Changes

In a running application, the changes users make to objects are reflected in the object graph managed by an EOEditingContext and in the user interface. However, the database isn't updated to reflect these changes until there is an explicit request (typically issued by the user) to save. The sequence of events in a save operation is illustrated in [Figure 52](#apple-gq3da).

!

Figure 52. Saving to the Database

When an EOEditingContext receives a request to save in the form of a __saveChanges__ message, the following sequence of events occurs:

- The editing context sends it editors and delegates the message __editingContextWillSaveChanges__.
- The editing context processes, propagates, and validates deletes.
- The editing context processes and validates changes for saving.
- The editing context commits the changes made to its objects to its parent object store by sending the parent the message __saveChangesInEditingContext__ (__saveChangesInEditingContext:__ in Objective-C). If the editing context is not nested, its parent is typically an EOObjectStoreCoordinator. When an EOObjectStoreCoordinator receives this message, it guides its EOCooperatingObjectStores through a multi-pass save protocol in which each cooperating store saves its own changes and forwards remaining changes to other cooperating stores.
- After it receives the message __saveChangesInEditingContext__, the object store coordinator sends each of its cooperating stores a __prepareForSaveWithCoordinator__ message (__prepareForSaveWithCoordinator:editingContext:__ in Objective-C), which informs them that a multi-pass save operation is beginning. When the cooperating store is an EODatabaseContext, it takes this opportunity to generate primary keys for any new objects in the editing context.
- The coordinator sends each of its cooperating stores the message __recordChangesInEditingContext__, which prompts them to examine the changed objects in the editing context, record any operations that need to be performed, and notify the coordinator of any changes that need to be forwarded to other cooperating stores. For example, if in its __recordChangesInEditingContext__ method one cooperating store notices the removal of an object from an "owning" relationship but that object belongs to another cooperating store, it informs the other store by sending the coordinator a __forwardUpdateForObject__ message(__forwardUpdateForObject:changes:__ in Objective-C).
- The coordinator sends each of its cooperating stores the message __performChanges__. This tells the stores to transmit their changes to their underlying databases. When the cooperating store is an EODatabaseContext, it responds to this message by taking the EODatabaseOperations that were constructed in the previous step, constructing EOAdaptorOperations from them, and giving the EOAdaptorOperations to an available EOAdaptorChannel for execution.
- If __performChanges__ fails for any of the EOCooperatingObjectStores, all stores are sent the message __rollbackChanges__.
- If __performChanges__ succeeds for all EOCooperatingObjectStores, the receiver sends them the message __commitChanges__, which has the effect of telling the adaptor to commit the changes.
- If __commitChanges__ fails for a particular cooperating store, that store and all subsequent ones are sent the message __rollbackChanges__. However, the stores that have already committed their changes do not roll back. In other words, the EOObjectStoreCoordinator doesn't perform the two-phase commit protocol necessary to guarantee consistent distributed update.
- If the save operation was successful, the editing context updates its object snapshots.
- Once it has committed its changes to its parent object store, the editing context posts the EditingContextDidSaveChangesNotification (EOEditingContextDidSaveChangesNotification in Objective-C).

### Customizing Framework Behavior

You can customize the behavior a save operation by assigning delegates to EOEditingContext and EOAdaptorChannel, and implementing the any of the following delegate methods.

|  EOEditingContext Delegate Methods |  EOEditingContext Delegate Methods |  EOEditingContext Delegate Methods |
|  Java Method |  Objective-C Method |  Description |
|  editingContext ShouldValidateChanges |  editingContext ShouldValidateChanges: |  This method is invoked when an EOEditingContext receives a saveChanges message. If the delegate returns __false__ (NO), changes are saved without first performing validation. You can use this method to provide your own validation mechanism. |
|  editingContext WillSaveChanges |  editingContext WillSaveChanges: |  This method is invoked when an EOEditingContext receives a saveChanges message. You can use this method to perform other pre-save validation. |

```
```

|  EOAdaptorChannel Delegate Methods |  EOAdaptorChannel Delegate Methods |  EOAdaptorChannel Delegate Methods |
|  Java Method |  Java Method |  Description |
|  databaseContextWillOrder AdaptorOperations |  databaseContext: willOrder AdaptorOperations FromDatabaseOperations: |  This method is invoked when EODatabaseContext receives a performChanges message. You can use this method to construct your own adaptor operations, for instance, possibly transform a delete operation into an update, or a stored procedure invocation. |
|  databaseContext WillPerform AdaptorOperations |  databaseContext: willPerform AdaptorOperations: adaptorChannel: |  This method is invoked from the EODatabaseContext performChanges method. This method is useful for applications that need a special ordering of adaptor operations; for example, to avoid violating any database referential integrity constraints. |

```
```


You can also register to receive the notifications listed below

|  EOEditingContext Notifications |  EOEditingContext Notifications |
|  Notification |  Description |
|  EditingContextDidSaveChangesNotification  (EOEditingContextDidSaveChangesNotification in Objective-C) |  This notification is broadcast after changes are saved to the editing context's parent object store. |
|  ObjectsChangedInStoreNotification (EOObjectsChangedInStoreNotification in Objective-C) |  This notification is broadcast by the database context when object updates are committed to the database. |

```
```


## Locking and Update Strategies

An update operation includes the following ingredients:

- An enterprise object whose data values have been changed
- A means of identifying the row in the database that corresponds to the object
- A strategy for handling update conflicts-either by preventing them from occurring, or by detecting and handling them when they do occur.

There must also be a transaction in progress.
The "means of identifying" a row is the primary key or global ID.
An _update strategy_ determines how updates should be made in the face of changes by others. For example, one strategy is to lock a row when it is read so that no one else can change it until you're done with it; this is called _pessimistic locking_. Another strategy is to compare the state of a row as you fetched it-that is, the row's snapshot-with the database row at update time to confirm that the database row hasn't been changed by someone else. This is called _optimistic locking_, because it assumes a conflicting update won't occur, but does check at the last minute. You can set your update strategy using the EODatabaseContext method __setUpdateStrategy__ (__setUpdateStrategy:__ in Objective-C). Optimistic locking is the default.
Enterprise Objects Framework also supports "on-demand" locking, in which specific optimistic locks can be promoted to database locks during the course of program execution. In other words, you can lock single objects. There are three ways to use on-demand locking. Use the EODatabaseContext method __lockObjectWithGlobalID__ (__lockObjectWithGlobalID:editingContext:__ in Objective-C) to lock a database row for a particular object. Use the EODatabaseContext method __objectsWithFetchSpecification__ (__objectsWithFetchSpecification:editingContext:__ in Objective-C) with a fetch specification that's configured to lock rows as they're fetched. Or use the EOEditingContext method __lockObject__ (__lockObject:__ in Objective-C).

### Handling Conflicts

The locking approach you use determines at what point conflicts are detected and how you can handle them.

- Pessimistic locking

When you use pessimistic locking, conflicts are detected as soon as you fetch a row. This is because when you fetch a row with pessimistic locking, you attempt to put a lock on it. If someone else has a lock on the row, the lock (and hence, the fetch operation) is refused. Your application can display a panel at that point telling the user to try again later.

Since pessimistic locking puts a lock on a row when it fetches it, you can generally assume that you won't experience conflicts when you save changes. However, this behavior is ultimately dependent on how the database server handles locks.

- Optimistic locking

When you use optimistic locking, conflicts aren't detected until you attempt to save. At that point, the database row is checked against the snapshot to make sure the row hasn't changed. If the row and the snapshot don't match, the save operation is aborted, the transaction is rolled back, and an exception is thrown. To handle the error you can catch the exception, refresh the conflicted object from the updated database data, and save again.

- On-demand locking

On-demand locking mixes characteristics of both pessimistic and optimistic locking. With on-demand locking, you've already fetched the object, and you're trying to get a lock on it after the fact. When you try to get a lock on the object's corresponding database row, you can get a failure for one of two reasons: either because the row doesn't match the snapshot (optimistic locking), or because someone else has a lock on the row on the server (pessimistic locking).

When on-demand locking fails for either reason, it throws an exception. To handle the error you can catch the exception, refresh the conflicted object from the updated database data, and try to get a lock on it again.

As with pessimistic locking, because on-demand locking locks the row, you can generally assume that you won't experience conflicts when you save changes. Again, this behavior is ultimately dependent on how the database server handles locks.

[!Table of Contents](Behind%20the%20Scenes.md) [!Next Section](Transactions.md)
