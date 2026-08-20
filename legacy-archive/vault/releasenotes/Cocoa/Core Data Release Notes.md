---
title: Core Data Release Notes
apple_id: TP40006503
resource_type: Release Note
platform: macOS
topic: null
technology: CoreData
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/CoreDataReleaseNotes/index.html
archived_at: '2026-07-18T02:50:22.461594Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Core Data Release Notes for OS X v10.5

This article summarizes some of the new features and changes in functionality in Core Data in OS X v10.5 (Leopard).

#### Contents:

- [Taking Advantage of New Features: Linking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomq)
- [Store Versioning and Migration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomy)
- [Persistent Store API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvona)
- [64-bit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvoni)
- [NSManagedObject](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvonq)
- [Fetching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjq)
- [Performance and Multi-Threading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjr)
- [Performance Analysis](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjs)
- [Deleting Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjt)
- [SQLite Store Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomju)
- [NSErrorMergePolicy and Optimistic Locking Records](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjv)
- [Managed Object Context, save:, and commitEditing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomjw)

### Taking Advantage of New Features: Linking

Core Data provides a number of major new features and enhancements in OS X v10.5. You can take advantage of these in OS X v10.5 while still maintaining backwards compatibility with OS X v10.4 provided that you link your application appropriately.

There are two ways you can build (in OS X v10.5) a project that runs on both OS X v10.4 and OS X v10.5:

1. Build a Tiger project against the OS X v10.4 SDK.
2. Build a Leopard project against the OS X v10.5 SDK and set the “OS X Deployment Target” to OS X v10.4.

The first option is what most developers do by default. This means, however, that even in OS X v10.5 the application runs as a OS X v10.4 application and cannot use new features or exclusive bug fixes. To take advantage of the new features and bug fixes, you must build your project against the OS X v10.5 SDK and set the “OS X Deployment Target” to OS X v10.4.

### Store Versioning and Migration

One of the major new Leopard features is an architecture to support versioning and migration—see _[Core Data Model Versioning and Data Migration Programming Guide](../../documentation/Cocoa/Core%20Data%20Model%20Versioning%20and%20Data%20Migration%20Programming%20Guide/Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojz)_ for more details.

### Persistent Store API

One of the major new Leopard features is a way that you can create your own persistent store type. You use the new `NSPersistentStore` and `NSAtomicStore` classes—see _[Atomic Store Programming Topics](../../documentation/Cocoa/Atomic%20Store%20Programming%20Topics/Introduction%20to%20Atomic%20Store%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrr)_ for more details. Persistent stores in general are discussed in Persistent Store Features and Using Persistent Stores.

### 64-bit

In OS X v10.5, Core Data is fully 64-bit compliant.

### NSManagedObject

In OS X v10.5, `NSManagedObject` is a class cluster. In practice, this should typically make no difference to the code you write. It does mean, however, that you _must_ use the proper Cocoa patterns if you override an initializer—that is, you must ensure that you set `self` to the return value from invocation of super’s implementation, as shown in the following example:

```objc
- (id)initWithEntity:(NSEntityDescription*)entityinsertIntoManagedObjectContext:(NSManagedObjectContext*)context {
    self = [super initWithEntity:entity insertIntoManagedObjectContext:context];
    if (self) {
        // Perform additional initialization.
    }
    return self;
}
```

[primitiveValueForKey:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506728-primitivevalueforkey) no longer supports unmodeled properties—there is no support for undefined keys.

`NSManagedObject` uses dynamic class generation to support the Objective-C 2 properties feature (see [Objective-C 2 Support](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmbtfvjvomi)) by automatically creating a subclass of your class appropriate for your entity. This is also typically transparent to you, however whereas `NSManagedObject`’s `class` method returns your class, the Objective-C function [object_getClass](https://developer.apple.com/documentation/objectivec/1418629-object_getclass) returns the dynamically-generated class.

As a class cluster, `NSManagedObject`'s `alloc`/`initWithEntity:insertIntoManagedObjectContext:` pair will always return an instance of correct class for the entity you pass as the parameter. The dynamically-generated subclass will be based on the class specified by the entity, so specifying a custom class in your model will supersede the class passed to `alloc`.

### Transformable Attributes

There's a new "transformable" type for `NSManagedObject` attributes that allows you more easily support attribute types that Core Data doesn't support natively. You access an attribute as a non-standard type, but behind the scenes Core Data uses an instance of [NSValueTransformer](https://developer.apple.com/documentation/foundation/valuetransformer) to convert the attribute to and from an instance of `NSData`. Core Data then stores the data instance to the persistent store.

If you don’t specify a transformer, transformable attributes to use keyed archiving ([NSKeyedUnarchiveFromDataTransformerName](https://developer.apple.com/documentation/foundation/nsvaluetransformername/1402008-keyedunarchivefromdatatransforme)).

For more details, see Non-Standard Persistent Attributes.

### Objective-C Feature Support

You can use Objective-C declared properties (see [Declared Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocProperties.html#//apple_ref/doc/uid/TP30001163-CH17)) in custom subclasses of `NSManagedObject`.

### Accessor methods

In OS X v10.5, Core Data will dynamically generate extremely efficient public and primitive get and set attribute accessor methods and relationship accessor methods for managed object classes. These are described in detail in Managed Object Accessor Methods, but this is a summary of the most important points:

- In OS X v10.5, an instance of `NSManagedObject` always responds to accessor methods for all its modeled properties. Accessor methods are the recommended way of accessing properties of a managed object.

  You are encouraged to use the `dynamic` declaration for compiler support and type checking, but this is not required to use this feature.
- If you do need to write custom accessor methods, instead of [primitiveValueForKey:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506728-primitivevalueforkey) and [setPrimitiveValue:forKey:](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506960-setprimitivevalue) you should use `primitive<PropertyName>` and `setPrimitive<PropertyName>:` (the latter are much more efficient).

  In OS X v10.5, `primitiveValueForKey:` no longer supports unmodeled keys.
- In addition to standard getter/setter methods, the accessors support the KVC mutable proxy names for to-many relationships.

### Subclassing

If you have two subclasses of `NSManagedObject`, and the parent class implements a dynamic property, and its subclass (the grandchild of `NSManagedObject`) overrides the methods for the property, those overrides cannot call super.

```objc
@interface Parent : NSManagedObject
@property(retain) NSString* foo;
@end

@implementation Parent
@dynamic foo;
@end

@interface Child : Parent
@end

@implementation Child
- (NSString*) foo {
    // This throws a "selector not found" exception.
    return super.foo;
}
@end
```


### Fetching

When you create a fetch request, you can use [setRelationshipKeyPathsForPrefetching:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506813-relationshipkeypathsforprefetchi) to specify key paths for relationships that should be fetched with the target entity. There are numerous other new configuration options for fetch requests—see [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) for full details.

### Performance and Multi-Threading

The new API for [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest) can be extremely helpful in working with data between threads. For example, you can configure a fetch request to return object IDs but exclude the row data (and update the row cache)—this can be useful if you're just going to pass those object IDs from a background thread to another thread. You can also pre-fetch relationships (which avoids the issue described in “Pre-fetching” in Core Data Performance) and pre-populate managed objects (that is, disable lazy initialization—which avoids the issue described in “Batch faulting” in Core Data Performance).

In OS X v10.5, [executeFetchRequest:error:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506672-fetch) intrinsically scales its behavior appropriately for the hardware and work load. If necessary, the Core Data will create additional private threads to optimize fetching performance. You will not now improve absolute fetching speed by creating background threads (although it may still be appropriate to fetch in a background thread for enhanced responsiveness—that is, to prevent your application from blocking).

Core Data now tries to optimize stack tear down (destruction of the persistent store coordinator, persistent stores, and so on). When a stack is torn down, the `dealloc` method of the component objects may not be called. You should therefore not do resource cleanup (such as removal of temporary files) in a `dealloc` method, instead you should invalidate resources when they are no longer needed.

Changes have been made to the merge policies to improve robustness and avoid resurrecting certain objects. In OS X v10.4, there were issues with objects that have with relationships to deleted objects, when the delete rules would have cascaded had all the changes been made in the same context. In OS X v10.5, merge policies handle delete propagation cascades correctly even between processes with disparate updates.

### Performance Analysis

Core Data now provides support for various `dtrace` probes, which can also be used with Instruments—see “Analyzing Performance” in Core Data Performance for more information.

### Deleting Objects

In OS X v10.4, you could not call [deleteObject:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506847-deleteobject) in a set accessor method; in OS X v10.5 you can.

In OS X v10.4, you could not delete an object if it was a fault that could not be fulfilled (that is, already deleted by another context or process). In OS X v10.5, you can always delete faults to missing records.

In OS X v10.5, Core Data won’t let you save the object graph if in the validation stage it contains a reference to a deleted object. For example, during a save operation Core Data will generate a deny error if a deleted object has a relationship to another object. This may happen especially if you haven’t specified a relationship without an inverse, or if after propagating deletions you add a reference to a deleted object. This is a change in behavior from OS X v10.4 (OS X v10.4 would not generate deny errors). If you manually perform validation, you may need to call [processPendingChanges](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506661-processpendingchanges) first so that deletions and other coalesced operations cascade completely to purge any references to pending deletions from the graph.

### SQLite Store Options

In OS X v10.4, there are only two settings to control the way in which data in a SQLite-based store is written to disk. In order to provide finer granularity of control over the tradeoff between performance and reliability, in OS X v10.5 Core Data uses two independent pragmas to control these options.

The default `fsync` behavior on OS X v10.4 was `fcntl(F_FULLFSYNC)` but on Leopard it is a standard `fsync`. (This affects all SQLite databases on Leopard, not just Core Data.) The pragma allows you to toggle this value. See “Configuring a SQLite Store’s Save Behavior” in Persistent Store Features for a full discussion.

In addition, the SQLite store now supports:

- Additional SQL generation for predicates including ANY and IN operators and sub-queries;
- A time-out option on the persistent store coordinator.

### NSErrorMergePolicy and Optimistic Locking Records

The [NSErrorMergePolicy](https://developer.apple.com/documentation/coredata/nserrormergepolicy) policy causes a save to fail if there are any merge conflicts (see “Conflict Detection and Optimistic Locking” and “Conflict Resolution” in Change Management). In the case of failure, the [save:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save) method returns with an error with a user info dictionary that contains the key `@"conflictList"`; the corresponding value is an array of conflict records.

In OS X v10.4, all relationship values in the records are managed objects; in OS X v10.5, all relationship values in the records to be objectIDs. This change is backwards binary compatible, so this only affects compiled in OS X v10.5 and using the `NSErrorMergePolicy` to perform some kind of custom recovery.

### Managed Object Context, save:, and commitEditing

The behavior of `NSManagedObjectContext`’s [save:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save) method has changed in OS X v10.5. In OS X v10.4, the `save:` method erroneously caused bound text views to commit their pending edits; in OS X v10.5 this error has been fixed.

This means that, for example, in Core Data non-document template based applications linked on or after OS X v10.5, to replicate the behavior of a OS X v10.4 application, the application delegate needs to send the managed object context a `commitEditing` message when saving.

The CoreData application template provided with Xcode includes an application delegate that implements some basic Core Data and application functionality, including a save action. The implementation of the `saveAction:` method is simple—it just tells the delegate's managed object context to save. For user interfaces created with Cocoa Bindings and linked on OS X v10.5, this has the effect of discarding editing before doing the actual save. For applications linked on OS X v10.4, this behavior triggered a bug where bound text views would have their pending edits _committed_ instead of discarded.

This has been fixed for applications linked on or after OS X v10.5. However, this does mean that if you want pending edits in bound text views to be committed during a save you need to modify the `saveAction:` method to first call `[[self managedObjectContext] commitEditing]` (or use the [commitEditingWithDelegate:didCommitSelector:contextInfo:](https://developer.apple.com/documentation/objectivec/nsobject/1458179-commiteditingwithdelegate) variant) before saving. Otherwise the pending edits will be discarded.
