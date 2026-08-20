---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/More/EOEditingContext_m.html
archived_at: '2026-07-18T01:28:37.847594Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOEditingContext-3.md)
[!](EOFault.md)

---

# EOEditingContext

---

### Other Classes that Participate in Object Graph Management

EOEditingContexts work in conjunction with instances of other classes to manage the object graph. Two other classes that play a significant role in object graph management are NSUndoManager and EOObserverCenter. NSUndoManager objects provide a general-purpose undo stack. As a client of NSUndoManager, EOEditingContext registers undo events for all changes made the enterprise objects that it watches.

EOObserverCenter provides a notification mechanism for an observing object to find out when another object is about to change its state. "Observable" objects (typically all enterprise objects) are responsible for invoking their [__willChange__](EOEnterpriseObject-3.md)method prior to altering their state (in a "set" method, for instance). Objects (such as instances of EOEditingContext) can add themselves as observers to the objects they care about in the EOObserverCenter. They then receive a notification (as an [__objectWillChange:__](EOObserving-2.md)message) whenever an observed object invokes [__willChange__](EOEnterpriseObject-3.md).

The [__objectWillChange:__](EOObserving-2.md)method is defined in the EOObserving protocol. EOEditingContext implements the EOObserving interface. For more information about the object change notification mechanism, see the [EOObserving](EOObserving-2.md) protocol specification.

---

### Programmatically Creating an EOEditingContext

Typically, an EOEditingContext is created automatically for your application as a by product of some other operation. For example, the following operations result in the creation of network of objects that include an EOEditingContext:

- Running the EOF Wizard in Project Builder to create an OpenStep application with a graphical user interface
- Dragging an entity from EOModeler into a nib file in Interface Builder
- Accessing the default editing context of a WebObjects WOSession in a WebObjects application

Under certain circumstances, however, you may need to create an EOEditingContext programmatically-for example, if you're writing an application that doesn't include a graphical interface. To create an EOEditingContext, do this:
> ```
> EOEditingContext *editingContext = [[EOEditingContext alloc] init];
> ```

This creates an editing context that's connected to the default EOObjectStoreCoordinator. You can change this default setting by initializing an EOEditingContext with a particular parent EOObjectStore. This is useful if you want your EOEditingContext to use a different EOObjectStoreCoordinator than the default, or if your EOEditingContext is nested. For example, the following code excerpt initializes `childEditingContext` with a parent object store `parentEditingContext`:

> ```
> EOEditingContext *parentEditingContext;     // Assume this exists.
> EOEditingContext *childEditingContext = [[EOEditingContext alloc]
>     initWithParentObjectStore:parentEditingContext];
> ```

For more discussion of working programmatically with EOEditingContexts, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

---

#### Accessing An Editing Context's Adaptor Level Objects

You can use an EOEditingContext with any EOObjectStore. However, in a typical configuration, you use an EOEditingContext with the objects in the access layer. To access an EOEditingContext's adaptor level objects, you get the editing context's EOObjectStoreCoordinator from the editing context, you get an EODatabaseContext (EOAccess) from the object store coordinator, and you get the adaptor level objects from there. The following code demonstrates the process.

> ```
> EOEditingContext *editingContext;    // Assume this exists.
> NSString *myEntityName;              // Assume this exists.
> EOFetchSpecification *fspec;
> EOObjectStoreCoordinator *rootStore;
> EODatabaseContext *dbContext;
> EOAdaptor *adaptor;
> EOAdaptorContext *adContext;
>
> fspec = [EOFetchSpecification fetchSpecificationWithEntityName:myEntityName
>     qualifier:nil
>     sortOrderings:nil];
>
> rootStore = (EOCooperatingObjectStore *)[editingContext rootObjectStore];
>
> dbContext = [rootStore objectStoreForFetchSpecification:fspec];
>
> adaptor = [[dbContext database] adaptor];
> adContext = [dbContext adaptorContext];
> ```

This example first creates a fetch specification, providing just the entity name as an argument. Of course, you can use a fetch specification that has non-`nil` values for all of its arguments, but only the entity name is used by the EOObjectStore [__objectStoreForFetchSpecification:__](EOObjectStoreCoordinator-2.md)method. Next, the example gets the editing context's EOObjectStoreCoordinator using the EOEditingContext method [__rootObjectStore__](EOEditingContext-3.md). [__rootObjectStore__](EOEditingContext-3.md)returns an EOObjectStore and not an EOObjectStoreCoordinator, because it's possible to substitute a custom object store in place of an object store coordinator. Similarly, the EOObjectStoreCoordinator method [__objectStoreForFetchSpecification:__](EOObjectStoreCoordinator-2.md)returns an EOCooperatingObjectStore instead of an access layer EODatabaseContext because it's possible to substitute a custom cooperating object store in place of a database context. If your code performs any such substitutions, you should alter the above code example to match your custom object store's API. See the class specifications for EOObjectStore, EOObjectStoreCoordinator, and EOCooperatingObjectStore for more information.

An EOEditingContext's EOObjectStoreCoordinator can have more than one set of database and adaptor level objects. Consequently, to get a database context from the object store coordinator, you have to provide information that the coordinator can use to choose the correct database context. The code example above provides an EOFetchSpecification using the method [__objectStoreForFetchSpecification:__](EOObjectStoreCoordinator-2.md), but you could specify different criteria by using one of the following EOObjectStoreCoordinator methods instead:

| __Method__ | __Description__ |
| __cooperatingObjectStores__ | Returns an array of the EOObjectStoreCoordinator's cooperating object stores. |
| [__objectStoreForGlobalID:__](EOObjectStoreCoordinator-2.md) | Returns the cooperating object store for the enterprise object identified by the provided EOGlobalID_._ |
| [__objectStoreForObject:__](EOObjectStoreCoordinator-2.md) | Returns the cooperating object store for the provided enterprise object. |

```
```

After you have the EODatabaseContext, you can get the corresponding EOAdaptor and EOAdaptorContext as shown above. (EODatabaseContext, EOAdaptor, and EOAdaptorContext are all defined in EOAccess.)

---

### Using EOEditingContexts in Different Configurations

The fundamental relationship an EOEditingContext has is to its parent EOObjectStore, which creates the object graph the EOEditingContext monitors. EOObjectStore is an abstract class that defines a source and sink of objects for an EOEditingContext. The EOObjectStore is responsible for constructing and registering objects, servicing object faults, and committing changes made in an EOEditingContext.

You can augment the basic configuration of an EOEditingContext and its parent EOObjectStore in several different ways. For example, multiple EOEditingContexts can share the same EOObjectStore, one EOEditingContext can act as an EOObjectStore for another, and so on. The most commonly used scenarios are described in the following sections.

---

#### Peer EOEditingContexts

One or more "peer" EOEditingContexts can share a single EOObjectStore (Figure 1). Each EOEditingContext has its own object graph-so, for example, a given Employee row in a database can have separate object instances in each EOEditingContext. Changes to an object in one EOEditingContext don't affect the corresponding object in another EOEditingContext until all changes are successfully committed to the shared object store. At that time the objects in all EOEditingContexts are synchronized with the committed changes. This arrangement is useful when an application allows the user to edit multiple independent "documents."

!

__Figure 1__ Peer EOEditingContexts 

---

#### Nested EOEditingContexts

EOEditingContext is a subclass of EOObjectStore, which gives its instances the ability to act as EOObjectStores for other EOEditingContexts. In other words, EOEditingContexts can be nested (Figure 2), thereby allowing a user to make edits to an object graph in one EOEditingContext and then discard or commit those changes to another object graph (which, in turn, may commit them to an external store). This is useful in a "drill down" style of user interface where changes in a nested dialog can be okayed (committed) or canceled (rolled back) to the previous panel.

!

__Figure 2__ Nested EOEditingContexts When an object is fetched into a nested EOEditingContext, it incorporates any uncommitted changes that were made to it in its parent EOEditingContext. For example, suppose that in one panel you have a list of employees that allows you to edit salaries, and that the panel includes a button to display a nested panel where you can edit detail information. If you edit the salary in the parent panel, you see the modified salary in the nested panel, not the old (committed) salary from the database. Thus, conceptually, nested EOEditingContexts fetch through their parents.

EOEditingContext overrides several of EOObjectStore's methods:

- [- arrayFaultWithSourceGlobalID:relationshipName:editingContext:](EOEditingContext-3.md)
- [- faultForGlobalID:editingContext:](EOEditingContext-3.md)
- [- invalidateAllObjects](EOEditingContext-3.md)
- [- invalidateObjectsWithGlobalIDs:](EOEditingContext-3.md)
- [- objectsForSourceGlobalID:relationshipName:editingContext:](EOEditingContext-3.md)
- [- objectsWithFetchSpecification:editingContext:](EOEditingContext-3.md)
- [- refaultObject:withGlobalID:editingContext:](EOEditingContext-3.md)
- [- saveChangesInEditingContext:](EOEditingContext-3.md)

These methods are generally used when an EOEditingContext acts as an EOObjectStore for another EOEditingContext. For more information, see the individual method descriptions. For information on setting up this configuration for interfaces loaded from nib files, see the method description for [__setDefaultParentObjectStore:__](EOEditingContext-3.md).

For a description of how to implement nested EOEditingContexts, see the chapter "Application Configurations" in the _Enterprise Objects Framework Developer's Guide_.

---

#### Getting Data from Multiple Sources

An EOEditingContext's object graph can contain objects from more than one external store (Figure 3). In this scenario, the object store is an EOObjectStoreCoordinator, which provides the abstraction of a single object store by redirecting operations to one or more EOCooperatingObjectStores.

!

__Figure 3__ An EOEditingContext Containing Objects from Multiple Sources In writing an application, it's likely that you'll use combinations of the different scenarios described in the above sections.

---

### Fetching Objects

The most common way to explicitly fetch objects from an external store in an Enterprise Objects Framework application is to use EOEditingContext's [__objectsWithFetchSpecification:__](EOEditingContext-3.md)method. This method takes a fetch specification and returns an array of objects. A fetch specification includes the name of the entity for which you want to fetch objects, the qualifier (query) you want to use in the fetch, and the sort order in which you want the objects returned (if any). For example, the following code excerpt uses `objectsWithFetchSpecification:` to fetch all video store members who have Visa credit cards:

> ```
> EOFetchSpecification *fetchSpec;
> NSArray *results;
> fetchSpec = [EOFetchSpecification
>     fetchSpecificationWithEntityName:@"Member"
>     qualifier:[EOQualifier qualifierWithQualifierFormat:
>     @"cardType = 'Visa' "]
>     sortOrderings:nil];
> results = [editingContext objectsWithFetchSpecification:fetchSpec];
> ```

Note that objects are allocated in the same zone as the EOEditingContext into which they're fetched.

---

### Managing Changes in Your Application

EOEditingContext provides several methods for managing the changes made to objects in your application. You can use these methods to get information about objects that have changed, to selectively undo and redo changes, and to discard all changes made to objects before these changes are committed to the database. These methods are described in the following sections.

---

#### Getting Information About Changed Objects

An EOEditingContext maintains information about three different kinds of changes to objects in its object graph: insertions, deletions, and updates. After these changes have been made and before they're committed to the database, you can find out which objects have changes in each of these categories by using the [__insertedObjects__](EOEditingContext-3.md), [__deletedObjects__](EOEditingContext-3.md), and [__updatedObjects__](EOEditingContext-3.md)methods. Each method returns an array containing the objects that have been inserted, deleted, and updated, respectively. The [__hasChanges__](EOEditingContext-3.md)method returns YES or NO to indicate whether any of the objects in the object graph have been inserted, deleted, or updated.

---

#### Undo and Redo

EOEditingContext includes the ``__undo:__ , ``__redo:__ , and ``__revert:__ methods for managing changes to objects in the object graph. ``__undo:__ asks the EOEditingContext's NSUndoManager to reverse the latest changes to objects in the object graph. ``__redo:__ asks the NSUndoManager to reverse the latest undo operation. ``__revert:__ clears the undo stack, discards all insertions and deletions, and restores updated objects to their last committed (saved) values.

EOEditingContext's undo support is arbitrarily deep; you can undo an object repeatedly until you restore it to the state it was in when it was first created or fetched into its editing context. Even after saving, you can undo a change. To support this feature, the NSUndoManager can keep a lot of data in memory.

For example, whenever an object is removed from a relationship, the corresponding editing context creates a snapshot of the modified, source object. The snapshot, which retains the removed object, is retained by the editing context and by the undo manager. The editing context releases the snapshot when the change is saved, but the undo manager doesn't. It continues holding the snapshot, so it can undo the deletion if requested.

If the typical usage patterns for your application generate a lot of change processing, you might want to limit the undo feature to keep its memory usage in check. For example, you could clear an undo manager whenever its editing context saves. To do so, simply send the undo manager a __removeAllActions__ message (or a __removeAllActionsWithTarget:__ message with the editing context as the argument). If your application doesn't need undo at all, you can avoid any undo overhead by setting the editing context's undo manager to __nil__ with [__setUndoManager:__](EOEditingContext-3.md).

---

#### Saving Changes

The [__saveChanges__](EOEditingContext-3.md)method commits changes made to objects in the object graph to an external store. When you save changes, EOEditingContext's lists of inserted, updated, and deleted objects are flushed.

Upon a successful save operation, the EOEditingContext's parent EOObjectStore broadcasts an [EOObjectsChangedInStoreNotification](EOEditingContext-3.md). Peers of the saved EOEditingContext receive this notification and respond by synchronizing their objects with the committed versions. See also

---

### Methods for Managing the Object Graph

EOEditingContext provides methods for managing the enterprise objects in the context's object graph. This section describes these methods, as well as other techniques you can use to manage the object graph.

At different points in your application, you might want to do the following:

- Break retain cycles between enterprise objects
- Discard changes that have been made to enterprise objects
- Make sure that when you refetch objects from the database, any changed database values are used instead of the original values
- Discard the view of objects cached in memory
- Work with objects across multiple editing contexts

These scenarios are discussed in the following sections.

---

#### Breaking Retain Cycles

You use the EOEditingContext methods [__refaultObjects__](EOEditingContext-3.md)and [__refaultObject:withGlobalID:editingContext:__](EOEditingContext-3.md)to break retain cycles between your enterprise objects. For example, suppose you have an Employee object that has a to-one relationship to its Department, and the Department object in turn has an array of Employee objects. This circular reference constitutes a retain cycle, which you can break using the `refault...` methods.

__Note:__ Retain cycles are automatically broken if you release the EOEditingContext.

You should use the `refault...` methods with caution, since refaulting an object doesn't remove the object snapshot from the undo stack. Objects that have been newly inserted or deleted should not be refaulted. In general, it's safer to use [__refaultObjects__](EOEditingContext-3.md)than it is to use [__refaultObject:withGlobalID:editingContext:__](EOEditingContext-3.md)since [__refaultObjects__](EOEditingContext-3.md)only refaults objects that haven't been inserted, deleted or updated. The method [__refaultObject:withGlobalID:editingContext:__](EOEditingContext-3.md)doesn't make this distinction, so you should only use it when you're sure you know what you're doing.

If you want to reset your EOEditingContext and free all of its objects, do the following:

> ```
> EOEditingContext *editingContext;     // Assume this exists.
> [editingContext revert];               // Discard uncommitted changes
> [editingContext refaultObjects];
> ```

Note that you must release any other retains on the enterprise objects in the EOEditingContext for them to actually be freed. For example, to clear a display group that references a list of enterprise objects, you'd do something like the following:

> ```
> [displayGroup setObjectArray:nil];
> ```

Releasing the EODisplayGroup (and any user interface objects that refer to it) also has the effect of releasing the object array.

Using the `invalidate...` methods (described below) also has the effect of breaking retain cycles, but these methods have a more far-reaching effect. It's not recommended that you use them simply to break retain cycles.

---

#### Discarding Changes to Enterprise Objects

EOEditingContext provides different techniques for discarding changes to enterprise objects. These techniques are as follows:

- Perform a simple ``__undo:__ , which reverses the latest uncommitted changes applied to objects in the object graph.
- Invoke the EOEditingContext method [__revert__](EOEditingContext-3.md), which removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values. If you just want to discard uncommitted changes but you don't want to sacrifice the original values from the database cached in memory, use the [__revert__](EOEditingContext-3.md)method.

A different approach is to use the `invalidate...` methods, described in ""Discarding the View of Objects Cached in Memory"."

---

#### Refreshing Objects

One characteristic of an object graph is that it represents an internally consistent view of your application's data. By default, when you refetch data, Enterprise Objects Framework maintains the integrity of your object graph by not overwriting your object values with database values that have been changed by someone else. But what if you want your application to see those changes? You can accomplish this by using the EOFetchSpecification method __[setRefreshesRefetchedObjects:](EOFetchSpecification-2.md)__ . Invoking [__setRefreshesRefetchedObjects:__](EOFetchSpecification-2.md)with the argument YES causes existing objects to be overwritten with fetched values that have been changed. Alternatively, you can use the EODatabaseContext (EOAccess) delegate method __databaseContext:shouldUpdateCurrentSnapshot:newSnapshot:globalID:channel:__ .

Normally, when you set an EOFetchSpecification to refresh using [__setRefreshesRefetchedObjects:__](EOFetchSpecification-2.md), it only refreshes the objects you're fetching. For example, if you refetch employees, you don't also refetch the employees' departments. However, if you use the EOPrefetchingRelationshipHintKey with an EOFetchSpecification in the EODatabaseContext method __objectsWithFetchSpecification:editingContext:__ , the refetch is propagated for all of the fetched objects' relationships that are specified for the hint. For more discussion of this topic, see the EODatabaseContext class specification.

Refreshing refetched objects only affects the objects you specify. If you want to refetch your entire object graph, you can use the EOEditingContext `invalidate...` methods, described below.

---

#### Discarding the View of Objects Cached in Memory

As described in the section "Discarding Changes to Enterprise Objects," you can use [__undo:__](EOEditingContext-3.md)or [__revert__](EOEditingContext-3.md)to selectively discard the changes you've made to enterprise objects. Using these methods preserves the original cache of values fetched from the database. But what if you want to flush your in-memory object view all together-in the most likely scenario, to see changes someone else has made to the database? You can invalidate your enterprise objects using the [__invalidateAllObjects__](EOEditingContext-3.md)method or the [__invalidateObjectsWithGlobalIDs:__](EOEditingContext-3.md)method. (You can also use the action method [__refetch:__](EOEditingContext-3.md), which simply invokes [__invalidateAllObjects__](EOEditingContext-3.md)). Unlike fetching with the EOFetchSpecification method [__setRefreshesRefetchedObjects:__](EOFetchSpecification-2.md)set to YES (described above), the `invalidate...` methods result in the refetch of your entire object graph.

The effect of the[__invalidateAllObjects__](EOEditingContext-3.md)method depends on how you use it. For example, if you send[__invalidateAllObjects__](EOEditingContext-3.md)to an EOEditingContext, it sends ``__invalidateObjectsWithGlobalIDs:__ to its parent object store with all the globalIDs for the objects registered in it. If the EOEditingContext is nested, its parent object store is another EOEditingContext; otherwise its parent object store is typically an EOObjectStoreCoordinator. Regardless, the message is propagated down the object store hierarchy. Once it reaches the EOObjectStoreCoordinator, it's propagated to the EODatabaseContext(s). The EODatabaseContext discards the row snapshots for these globalIDs and sends an [EOObjectsChangedInStoreNotification](EOEditingContext-3.md), thereby refaulting all the enterprise objects in the object graph. This refaulting in turn releases all objects not retained by your application or by an EODisplayGroup. The next time you access one of these objects, it's refetched from the database.

Sending [__invalidateAllObjects__](EOEditingContext-3.md)to an EOEditingContext affects not only that context's objects, but objects with the same globalIDs in other EOEditingContexts. For example, suppose _editingContext1_ has _objectA_ and _objectB_, and _editingContext2_ has _objectA_, _objectB_, and _objectC_. When you send [__invalidateAllObjects__](EOEditingContext-3.md)to _editingContext1_, _objectA_ and _objectB_ are refaulted in both _editingContext1_ and _editingContext2_. However, _objectC_ in _editingContext2_ is left intact since _editingContext1_ doesn't have an _objectC_.

If you send[__invalidateAllObjects__](EOEditingContext-3.md)directly to the EOObjectStoreCoordinator, it sends ______invalidateAllObjects__ to all of its EODatabaseContexts, which then discard all of the snapshots in your application and refault every single enterprise object in all of your EOEditingContexts.

The `invalidate...` methods are the only way to get rid of a database lock without saving your changes.

---

#### Working with Objects Across Multiple EOEditingContexts

Any time your application is using more than one EOEditingContext (as described in the section ""Using EOEditingContexts in Different Configurations""), it's likely that one editing context will need to access objects in another.

On the face of it, it may seem like the most reasonable solution would be for the first editing context to just get a pointer to the desired object in the second editing context and modify the object directly. But this would violate the cardinal rule of keeping each editing context's object graph internally consistent. Instead of modifying the second editing context's object, the first editing context needs to get its own copy of the object. It can then modify its copy without affecting the original. When it saves changes, they're propagated to the original object, down the object store hierarchy. The method that you use to give one editing context its own copy of an object that's in another editing context is [__faultForGlobalID:editingContext:__](EOEditingContext-3.md).

For example, suppose you have a nested editing context configuration in which a user interface displays a list of objects-this maps to the parent editing context. From the list, the user can select an object to inspect and modify in a "detail view"-this maps to the child editing context. To give the child its own copy of the object to modify in the detail view, you would do something like the following:

> ```
> EOEditingContext *childEC, *parentEC;      // Assume these exist.
> id newObject = [childEC faultForGlobalID:[parentEC globalIDForObject:origObject]
>     editingContext:childEC];
> ```

where `origObject` is the object the user selected for inspection from the list.

The child can make changes to `newObject` without affecting `origObject` in the parent. Then when the child saves changes, `origObject` is updated accordingly.

---

#### Updates from the Parent EOObjectStore

When changes are successfully saved in an EOObjectStore, it broadcasts an EOObjectsChangedInStoreNotification. An EOEditingContext receiving this notification will synchronize its objects with the committed values by refaulting objects needing updates so the new values will be retrieved from the EOObjectStore the next time they are needed. However, locally uncommitted changes to objects in the EOEditingContext are by default reapplied to the objects, in effect preserving the uncommitted changes in the object graph. After the update, the uncommitted changes remain uncommitted, but the committed snapshots have been updated to reflect the values in the EOObjectStore.

You can control this process by implementing two delegate methods. Before any updates have occurred, the delegate method [__editingContext:shouldMergeChangesForObject:__](EOEditingContextDelegate.md)will be invoked for each of the objects that has both uncommitted changes and an update in the EOObjectStore. If the delegate returns YES, the uncommitted chnages will be merged with the update (the default behavior). If it returns NO, then the object will be invalidated (and refaulted) without preserving ay uncommitted changes. As a side effect, the delgate might cache information about the object (globalID, snapshot, etc.) so that a specialized merging behavior could be implemented. At this point, the delegate should not make changes to the object becuse it is about to be invalidated. However, the delegate method [__editingContextDidMergeChanges:__](EOEditingContextDelegate.md)is invoked after all of the updates for the EOObjectsChangedInStoreNotification have been completed, including the merginf of all uncommitted changes. By default, it does nothing, but this delegate method might perform the customized merging behavior based on whatever information was cached in [__editingContext:shouldMergeChangesForObject:__](EOEditingContextDelegate.md)for each of the objects that needed an update. See the informal protocol [EOValueMerging](EOValueMerging.md) for the descriptions of the methods [__changesFromSnapshot:__](EOValueMerging.md)and [__reapplyChangesFromDictionary:__](EOValueMerging.md), which might be useful for implementing custom merging behaviors.

---

### General Guidelines for Managing the Object Graph

When you fetch objects into your application, you create a graph of objects instantiated from database data. From that point on, your focus should be on working with the object graph-not on interacting with your database. This distinction is an important key to working with Enterprise Objects Framework.

---

#### You don't have to worry about the database...

One of the primary benefits of Enterprise Objects Framework is that it insulates you from having to worry about database details. Once you've defined the mapping between your database and your enterprise objects in a model file, you don't need to think about issues such as foreign key propagation, how object deletions are handled, how operations in the object graph are reflected in your database tables, and so on.

This can be illustrated by considering the common scenario in which one object has a relationship to another. For example, suppose an Employee has a relationship to a Department. In the object graph, this relationship is simply expressed as an Employee object having a pointer to its Department object. The Department object might in turn have a pointer to an array of Employee objects. When you manipulate relationships in the object graph (for example, by moving an Employee to a different Department), Enterprise Objects Framework changes the appropriate relationship pointers. For example, moving an Employee to a different Department changes the Employee's department pointer and adds the Employee to the new Department's employee array. When you save your changes to the database, Enterprise Objects Framework knows how to translate these object graph manipulations into database operations.

---

#### ...but you do have to worry about the object graph

As described above, you generally don't need to concern yourself with how changes to the object graph are saved to the database. However, you do need to concern yourself with managing the object graph itself. Since the object graph is intended to represent an internally consistent view of your application's data, one of your primary considerations should be maintaining its consistency. For example, suppose you have a relationship from Employee to Project, and from Employee to Manager. When you create a new Employee object, you must make sure that it has relationships to the appropriate Projects and to a Manager.

Just as you need to maintain the internal consistency of an EOEditingContext's object graph, you should never directly modify the objects in one EOEditingContext from another EOEditingContext. If you do so, you risk creating major synchronization problems in your application. If you need to access the objects in one EOEditingContext from another, use the method [__faultForGlobalID:editingContext:__](EOEditingContext-3.md), as described in "Working with Objects Across Multiple EOEditingContexts." This gives the receiving EOEditingContext its own copy of the object, which it can modify without affecting the original. Then when it saves its changes, the original is updated accordingly.

One of the implications of needing to maintain the consistency of your object graph is that you should never copy an enterprise object (though you can snapshot its properties), since this would be in conflict with uniquing. Uniquing dictates that an EOEditingContext can have one and only one copy of a particular object. For more discussion of uniquing, see the chapter "Behind the Scenes" in the _Enterprise Objects Framework Developer's Guide_. Similarly, your enterprise objects shouldn't override the `isEqual:` method. Enterprise Objects Framework relies on the default NSObject implementation which checks instance (pointer) equality rather than value equality.

---

### Using EOEditingContext to Archive Custom Objects in Web Objects Framework

In WebObjects, applications that use the Enterprise Objects Framework must enlist the help of the EOEditingContext to archive enterprise objects. The primary reason is so that the EOEditingContext can keep track, from one transaction to the next, of the objects it manages. But using an EOEditingContext for archiving also benefits your application in these other ways:

- During archiving, an EOEditingContext stores only as much information about its enterprise objects as is needed to reconstitute the object graph at a later time. For example, unmodified objects are stored as simple references (by globalID) that will allow the EOEditingContext to recreate the object from the database. Thus, your application can store state very efficiently by letting an EOEditingContext archive your enterprise objects.
- During unarchiving, an EOEditingContext can recreate individual objects in the graph only as they are needed by the application. This approach can significantly improve application performance.

An enterprise object (like any other object that uses the OpenStep archiving scheme) makes itself available for archiving by declaring that it conforms to the NSCoding protocol, by implementing the protocol's two methods, `encodeWithCoder:` and `initWithCoder:`. It implements these methods like this:
> ```
> - (void)encodeWithCoder:(NSCoder *)aCoder {
>     [EOEditingContext encodeObject:self withCoder:aCoder];
> }
>
> - (id)initWithCoder:(NSCoder *)aDecoder {
>     return [EditingContext initObject:self withCoder:aDecoder];
> }
> ```

The enterprise object simply passes on responsibility for archiving and unarchiving itself to the EOEditingContext class, by invoking the [__encodeObject:withCoder:__](EOEditingContext-3.md)and [__initObject:withCoder:__](EOEditingContext-3.md)class methods. The EOEditingContext takes care of the rest. For more discussion of `encodeWithCoder:` and `initWithCoder:`, see the NSCoding protocol specification in the _Foundation Framework Reference_.

EOEditingContext includes two additional methods that affect the archiving and unarchiving of objects: [__setUsesContextRelativeEncoding:__](EOEditingContext-3.md)and [__usesContextRelativeEncoding__](EOEditingContext-3.md). When you use context relative encoding, it means that enterprise objects that archive themselves using the EOEditingContext [__encodeObject:withCoder:__](EOEditingContext-3.md)method archive their current state (that is, all of their class properties) only if they (the objects) are marked as inserted or updated in the EOEditingContext. Otherwise, they archive just their globalID's since their state matches what's stored in the database and can be retrieved from there. If [__usesContextRelativeEncoding__](EOEditingContext-3.md)returns NO, it means the current state will always be archived, even if the enterprise object is unmodified. The default is NO for OpenStep applications, and YES for WebObjects applications.

---

[!](EOEditingContext-3.md)
[!](EOFault.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
