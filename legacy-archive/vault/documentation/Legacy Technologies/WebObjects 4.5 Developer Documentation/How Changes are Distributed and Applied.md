---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/BehindSc2.html
archived_at: '2026-07-15T08:02:53.265767Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Behind%20the%20Scenes.md) [!Previous Section](Fetching%20Objects.md)

# How Changes are Distributed and Applied

An EOEditingContext is responsible for managing the changes that occur to the objects in its object graph. For example, suppose the user edits a value in the user interface in an Application Kit application. This causes the sequence of events illustrated in [Figure 51](#apple-gqydemq).

!

Figure 51. Flow of Events When a User Edits Data

When a user edits data in the user interface:

- The EOAssociation passes the new value to its EODisplayGroup.
- The display group applies the changes to the affected enterprise object.
- The enterprise object notifies the EOEditingContext that it has changed. Specifically, the enterprise object invokes its __willChange__ method, which in turn invokes the editing context's __objectWillChange__ method (__objectWillChange:__ in Objective-C).
- The editing context records the object in its list of unprocessed changes. (How the editing context manages these changes is described in["How an EOEditingContext Manages Changes to Its Objects"](#apple-g4zdg).)

Then, at the end of the event loop:

- The editing context records undos.
- The editing context broadcasts an ObjectsChangedInStoreNotification and an ObjectsChangedInEditingContextNotification (EOObjectsChangedInStoreNotification and EOObjectsChangedInEditingContextNotification in Objective-C).
- The display group, which is registered to observe the ObjectsChangedInEditingContextNotification, receives the notification and updates the user interface.
- All views of the data in the application refresh themselves to reflect the change.

### Customizing Framework Behavior

During this process, you can customize the behavior of the EOEditingContext by registering for the following notifications and taking the appropriate action.

|  EOEditingContext Notifications |  EOEditingContext Notifications |
|  Notification |  Description |
|  ObjectsChangedInStoreNotification (EOObjectsChangedInStoreNotification in Objective-C) |  This notification is broadcast whenever objectWillChange observer notifications are processed, which is usually at the end of the event in which the changes occurred. |
|  ObjectsChangedInEditingContextNotification (EOObjectsChangedInEditingContextNotification in Objective-C) |  This notification is broadcast whenever changes are made in an EOEditingContext. It's similar to EOObjectsChangedInStoreNotification, except that it contains objects rather than globalIDs. EODisplayGroups listen for this notification to redisplay their contents. |

```
```


## How an EOEditingContext Manages Changes to Its Objects

From the standpoint of an EOEditingContext, the changes you make to objects in an application fall into one of three categories:

- Insertion of a new object
- Deletion of an existing object
- Modification (updating) of an existing object

Normally, when an editing context's objects change (for example, when they're deleted or their data is modified), the processing of changes is deferred until the end of the current event. In the meantime, the editing context buffers pending insertions, deletions, and updates as unprocessed changes.
__Note:__  When a source (master) object has an owning relationship to a destination object (as determined from the EOClassDescription) and the destination object is removed from the master, the destination object is marked for deletion from the EOEditingContext. For example, if a purchase order owns a line item and the line item is removed from the purchase order, the line item is marked for deletion from the editing context since the owning relationship implies that a line item can't exist without a purchase order.
When an EOEditingContext processes changes, typically at the end of an event, it does the following to the objects in its unprocessed changes list:

- Processes deleted objects.

For a more detailed description of what this entails, see the following section, "[How Deleted Objects are Processed](#apple-g44ti)."

- Moves each object to the context's inserted, deleted, or updated list, as appropriate.
- Snapshots the objects for undo.
- Posts ObjectsChangedInStoreNotification and ObjectsChangedInEditingContextNotification.

### How Deleted Objects are Processed

Just like inserted and updated objects, deleted objects are normally processed at the end of the event in which the change was made. However, you can use the method __setPropagatesDeletesAtEndOfEvent__ (__setPropagatesDeletesAtEndOfEvent:__ in Objective-C) to change this behavior so that the editing context only processes deletions right before you save to the database.
The processing of deleted objects entails these steps:

- Deletions are propagated by sending each object a __propagateDeleteWithEditingContext__ message(__propagateDeleteWithEditingContext:__ in Objective-C), which then invokes the EOClassDescription method __propagateDeleteForObject__ (__propagateDeleteForObject:editingContext:__ in Objective-C). By default, this method applies the delete rule of every relationship (Deny, Nullify, Cascade) to the source object's child objects.
- The deletion is validated by sending each object the message __validateForDelete__.

By default, each object forwards this message to its EOClassDescription. Based on the result, the operation is either allowed or refused. For example, referential integrity constraints in your model might state that you can't delete a Department object that still has employees. If a user attempts to delete a department that has employees, the deletion is refused. An enterprise object class can also implement its own version of __validateForDelete__ to do some additional processing before passing the check on to its EOClassDescription. For more discussion of validation, see the chapter["Designing Enterprise Objects"](Designing%20Enterprise%20Objects.md#apple-ge2daobr).

Instead of waiting until the end of the event, you can force the processing of inserted, updated, and deleted objects by invoking the EOEditingContext method __processRecentChanges__. EOEditingContext invokes this method on itself before performing certain operations such as __saveChanges__. The sequence of events that occurs when an editing context receives the message __saveChanges__ is described in the next section.

[!Table of Contents](Behind%20the%20Scenes.md) [!Next Section](Saving%20Changes.md)
