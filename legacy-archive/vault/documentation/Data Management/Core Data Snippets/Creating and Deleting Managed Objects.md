---
title: Core Data Snippets
apple_id: TP40008285
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2009-07-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CoreDataSnippets/Articles/creating.html
archived_at: '2026-07-15T07:23:47.139332Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Snippets](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Fetching%20Specific%20Property%20Values.md)

# Creating and Deleting Managed Objects

This article contains snippets you use when creating or deleting a managed object.

When you create a new managed object, you need to specify its entity. Typically, however, you don’t actually need access to the model directly. Instead, you can `NSEntityDescription`’s class method [insertNewObjectForEntityForName:inManagedObjectContext:](https://developer.apple.com/documentation/coredata/nsentitydescription/1425093-insertnewobject) and pass the managed object context in which you want to create the new managed object. The method returns an instance of whatever class is defined in the managed object model to represent the entity, [initialized](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) with the default values given for its entity in the model.

To learn how to retrieve the managed object context, read [Getting a Managed Object Context](Accessing%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq).

```
NSManagedObjectContext *context = <#Get the context#>;
<#Managed Object Class#> *newObject = [NSEntityDescription
    insertNewObjectForEntityForName:@"<#Entity name#>"
    inManagedObjectContext:context];
```

It is typically important to cast the new instance to the managed object class so that you can use the appropriate [accessor methods](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) without the compiler generating a warning (or, if you’re using dot syntax, an error).

Simply creating a managed object does not cause it to be saved to a persistent store. It is simply associated with the managed object context. To commit changes to the store, you send the context a [save:](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506866-save) message.

To learn how to retrieve the managed object context, read [Getting a Managed Object Context](Accessing%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq).

```
NSManagedObjectContext *context = <#Get the context#>;
NSError *error;
if (![context save:&error]) {
    // Handle the error.
}
```


Simply being [deallocated](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27) does not cause a managed object to be deleted from the persistent store. To delete a managed object you have to delete it from the context then save the context.

To learn how to retrieve the managed object context, read [Getting a Managed Object Context](Accessing%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4deobtfvjvomq)—or you can simply ask the object itself what context it belongs to.

```
NSManagedObject *aManagedObject = <#Get the managed object#>;
NSManagedObjectContext *context = [aManagedObject managedObjectContext];
[context deleteObject:aManagedObject];
NSError *error;
if (![context save:&error]) {
    // Handle the error.
}
```

[Next](Document%20Revision%20History.md)[Previous](Fetching%20Specific%20Property%20Values.md)

