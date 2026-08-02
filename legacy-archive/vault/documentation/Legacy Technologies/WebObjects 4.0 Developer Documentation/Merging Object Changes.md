---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.09.html
archived_at: '2026-07-15T07:58:03.357480Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Binding%20to%20Complex%20Qualifiers.md)

# Merging Object Changes

A change has been made to how peer editing contexts (that is, editing contexts that share an object store) handle database modifications. WebObjects applications often use peer editing contexts since each session has an editing context and an application can run multiple sessions.
When an application has more than one editing context, it's possible for each editing context to have its own in-memory copy of the same enterprise object. Suppose the users of the editing contexts each make changes to their copies of that object. Which change wins? In prior releases of Enterprise Objects Framework, the editing context that saved its changes first overwrote the changes made by the second editing context.
For example, suppose two editing contexts each have a copy of a Customer object. Suppose the user of the first editing context changes the customer's address and at the same time, the user of the second editing context changes the customer's phone number. Then suppose the first user saved the change to the address. In previous releases of Enterprise Objects Framework, the change to the phone number was lost. When the first editing context's changes were saved, the customer object for the second editing context was turned back into a fault, losing any uncommitted changes in that object. The next time the customer was accessed, it was refetched from the object store, and the phone number retrieved from the database was the one committed by the first editing context.
In Enterprise Objects Framework release 3.0, the default behavior is not to lose the changed phone number. EOEditingContexts now keep track of uncommitted changes. When an object (such as the customer object) is refaulted in the second editing context (due to the EOObjectsChangeInStoreNotification posted after the first editing context saved changes), the second editing context checks to see if it has uncommitted changes for that object. If it does, it fires the fault (refetching the object from the database) and merges the uncommitted changes with the information retrieved from the database. Thus, in the example above, the second editing context would refetch the customer from the in-memory snapshot, thereby picking up the change to the address, and then overwrite the phone number retrieved from the database with the changed phone number.
Suppose, however, that the two users each change the same field. For example, suppose the first user changes the last name to "Primero" but doesn't save the change immediately, and the second user changes the last name to "Segundo" and immediately saves the change (before the first user saves). The first editing context refaults and refetches the customer object containing the last name "Segundo" and then overwrites that field with its uncommitted change of "Primero." You may not want this to happen. You may want the first user to decide whether to keep his uncommitted change or to replace it with the change made by the second user. If so, your editing context delegate should implement the method __editingContext:shouldMergeChangesForObject:__ (__editingContextShouldMergeChangesForObject__ in Java).
Remember that in a WebObjects application, the first editing context does not pick up the change until the first user submits a request. That is, the second user changes the last name to "Segundo" and clicks the submit button to save the change to the database. At this point, the first editing context refaults the customer object but has no way to update the user's browser with information that the object has changed until that user submits another request. This request is likely to be the action of submitting the last name change to "Primero." Thus, your application will probably have to display an alert component informing its user that the customer value in the database has changed and then prompt to see if its user wants to commit or discard his own changes.
The following tables describe the API added to support the change to the way peer editing contexts behave.

|  EOEditingContext Delegatation |  EOEditingContext Delegatation |
|  editingContext:shouldMergeChangesForObject: (Objective-C)  editingContextShouldMergeChangesForObject (Java) |  When an EOObjectsChangedInStoreNotification is received, the editing context sends this message to its delegate once for each of the objects that has both uncommitted changes and an update from the EOObjectStore. This method is invoked before any updates actually occur.  If this method returns YES or true, all of the uncommitted changes should be merged into the object after the update is applied, in effect preserving the uncommitted changes (the default behavior). The delegate method editingContext:shouldInvalidateObject:globalID: (editingContextShouldInvalidateObject in Java) will not be sent for the object in question.  If this method returns NO or false, no uncommitted changes are applied. Thus, the object is updated to reflect the values from the parent object store exactly. This method should not make any changes to the object since it is about to be invalidated. |
|  editingContextDidMergeChanges: |  Invoked once after a batch of objects has been updated from the database. A delegate might implement this method to define custom merging behavior, most likely in conjunction with editingContext:shouldMergeChangesForObject: (editingContextShouldMergeChangesForObject in Java). It is safe for this method to make changes to the objects in the editing context. |

```
```

|  EOEnterpriseObject Informal Protocol (Objective-C) or Interface (Java) |  EOEnterpriseObject Informal Protocol (Objective-C) or Interface (Java) |
|  changesFromSnapsot: |  Returns a dictionary similar to a snapshot except that the dictionary contains only those keys that refer to uncommitted changes in the enterprise object relative to the provided snapshot argument. For to-many keys, the uncommitted value is an array of two arrays: uncommitted additions and uncommitted deletions. |
|  reapplyChangesFromDictionary: |  Similar to takeValuesFromDictionary: but the dictionary argument can include values for to-many relationships as described above in the description of changesFromSnapshot:. Attribute and to-one keys refer to values that should replace the enterprise object's current value. An instance of EONull is used in the dictionary argument as a placeholder for nil or null. |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Raw%20Row%20Fetching.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
