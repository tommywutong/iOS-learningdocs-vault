---
title: Core Data Snippets
apple_id: TP40008285
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2009-07-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CoreDataSnippets/Articles/stack.html
archived_at: '2026-07-15T07:23:47.166589Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Snippets](Introduction.md)


[Next](Fetching%20Managed%20Objects.md)[Previous](Introduction.md)

# Accessing the Core Data Stack

This article contains snippets for creating and accessing parts of the main pieces of infrastructure defined by the Core Data [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56).

How you access the parts of the Core Data stack may depend in part on the application architecture and platform.

Broadly-speaking, in OS X there are two basic application architectures for programs that use Core Data:

- Single-coordinator applications.

  These applications typically have a single Core Data stack (as defined by a single persistent store coordinator) managed by a single [controller object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11). They generally use a single persistent store for the whole application.
- Document-based applications.

  These applications typically use the Application Kit’s `NSPersistentDocument` class. There is a usually a persistent store coordinator and a single persistent store associated with each document.

This article uses the terms “single-coordinator application” and “document-based application” to differentiate between these architectures.

In iOS, the application [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) usually maintains a persistent store coordinator that manages the application’s store. It typically creates a managed object context, but it often doesn’t own it. This is explained in greater detail in [Getting a Managed Object Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq).

In OS X:

- In an single-coordinator applications, you can get the application’s context directly from the application [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14).
- In document-based applications, you can get the context directly from the document instance.

In iOS:

- _By convention_, you get a context from a view controller. You must implement your application appropriately, though, to follow this pattern.

  When you implement a view controller that integrates with Core Data, you can add an `NSManagedObjectContext` property.

  When you create a view controller, you pass it the context it should use. You pass an existing context, or (in a situation where you want the new controller to manage a discrete set of edits) a new context that you create for it. It’s typically the responsibility of the application delegate to create a context to pass to the first view controller that’s displayed.

  A view controller typically shouldn’t retrieve the context from a global object such as the application delegate—this makes the application architecture rigid. Neither should a view controller create a context for its own use (unless it’s a nested context). This may mean that operations performed using the controller’s context aren’t registered with other contexts, so different view controllers will have different perspectives on the data.

Sometimes, though, it’s easier or more appropriate to retrieve the context from somewhere other than application or the document, or the view controller. Several objects you might use in a Core Data-based application keep a reference to a managed object context. A managed object itself has a reference to its own context, as do the various [controller objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) that support Core Data such as array and object controllers (`NSArrayController` and `NSObjectController` in OS X, and `NSFetchedResultsController` in iOS).

Retrieving the context from one of these objects has the advantage that if you re-architect your application, for example to make use of multiple contexts, your code is likely to remain valid. For example, if you have a managed object, and you want to create a new managed object that will be related to it, you can ask original object for its managed object context and create the new object using that. This will ensure that the new object you create is in the same context as the original.

You sometimes need to create a new managed object context to contain a disjoint set of edits that you might want to discard without perturbing the main context (for example, if you’re presenting a modal view to add and edit a new object).

To create a new managed object context, you need a persistent store coordinator.

```
NSPersistentStoreCoordinator *psc = <#Get the coordinator#>;
NSManagedObjectContext *newContext = [[NSManagedObjectContext alloc] init];
[newContext setPersistentStoreCoordinator:psc];
```

If you already have a reference to an existing context, you can ask it for its persistent store coordinator. This way you can be sure that the new context is using the same coordinator as the existing one (assuming this is your intent):

```
NSManagedObjectContext *context = <#Get the context#>;
NSPersistentStoreCoordinator *psc = [context persistentStoreCoordinator];
NSManagedObjectContext *newContext = [[NSManagedObjectContext alloc] init];
[newContext setPersistentStoreCoordinator:psc];
```


You sometimes need to access a managed object model to get information about a particular entity.

Applications typically have just a single model (although it may have more than one configuration). In a single-coordinator application, you typically get the model directly from the application delegate. In a document-based application, you get the model directly from the document.

If you have access to a managed object context—directly or indirectly (see [Getting a Managed Object Context](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq))—you can get the model from the context’s persistent store coordinator. From the model, you can retrieve an entity using [entitiesByName](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/1506203-entitiesbyname):

```
NSManagedObjectContext *context = <#Get the context#>;
NSPersistentStoreCoordinator *psc = [context persistentStoreCoordinator];
NSManagedObjectModel *model = [psc managedObjectModel];
NSEntityDescription *entity = [[model entitiesByName] objectForKey:@"<#Entity name#>"];
```


In many applications, there is only one persistent store for each persistent store coordinator. In an single-coordinator application, the store is associated with the whole application. In a document-based application, each document has a separate store. Sometimes, however, you might want to add another store. You add the store to the persistent store coordinator. You have to specify the store’s type, location, and configuration (based on configurations present on the managed object model associated with the coordinator). You can also specify other options, such as whether an old version of the store should be migrated to a current version (see _[Core Data Model Versioning and Data Migration Programming Guide](../../Cocoa/Core%20Data%20Model%20Versioning%20and%20Data%20Migration%20Programming%20Guide/Core%20Data%20Model%20Versioning%20and%20Data%20Migration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dgojz)_).

In an single-coordinator applications, you can get the application’s coordinator directly from the application delegate.

In document-based applications, you can get the coordinator from the document’s managed object context.

```
NSPersistentStoreCoordinator *psc = <#Get the coordinator#>;
NSURL *storeUrl = [NSURL fileURLWithPath:@"<#Path to store#>"];
NSString *storeType = <#Store type#>; // A store type, such as NSSQLiteStoreType
NSError *error;
if (![psc addPersistentStoreWithType:storeType configuration:nil
    URL:storeUrl options:nil error:&error]) {
    // Handle the error.
}
```

[Next](Fetching%20Managed%20Objects.md)[Previous](Introduction.md)

