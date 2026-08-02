---
title: iCloud Programming Guide for Core Data
apple_id: TP40013491
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/UsingCoreDataWithiCloudPG/GuidanceforDocument-basedApplications/GuidanceforDocument-basedApplications.html
archived_at: '2026-07-15T07:24:01.230520Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Programming Guide for Core Data](About%20Using%20iCloud%20with%20Core%20Data.md)


[Next](Best%20Practices.md)[Previous](Using%20the%20SQLite%20Store%20with%20iCloud.md)

# Using Document Storage with iCloud

Core Data document-based iOS apps combine the power and flexibility of Core Data with a document-centric paradigm. You use [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument) objects that each manage an entire Core Data stack. Follow the implementation strategy in this chapter to persist managed documents to the cloud. Using these guidelines, you will learn how to:

- Create and open managed documents
- Use managed documents
- Save managed documents to iCloud
- Delete managed documents

By default, the `UIManagedDocument` class uses SQLite transactional persistent storage. Therefore after you create a managed document, see [Reacting to iCloud Events](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltk) to learn how to listen and respond to iCloud events.

A managed document is represented on disk as a file package, and it includes its own Core Data store within the package. You save managed documents to a ubiquity container to persist them to iCloud. Before using your app’s ubiquity container, see [Enabling iCloud Support](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknlte) to learn how to configure iCloud for your app.

To create or open a managed document, you initialize a `UIManagedDocument` object with a location outside of your app’s ubiquity container.

If you are creating a new managed document, choose a location to save your document inside the app’s `Documents` subdirectory. Otherwise, use the existing managed document’s location. Finally, use the `NSFileManager` class to decide whether you should create a new document or open the existing document.

```
NSURL *documentURL = <#path in the Documents directory#>
UIManagedDocument *document = [[UIManagedDocument alloc] initWithFileURL:documentURL];
NSDictionary *options = @{NSMigratePersistentStoresAutomaticallyOption: @YES,
                          NSInferMappingModelAutomaticallyOption: @YES};
document.persistentStoreOptions = options;

if ([[NSFileManager defaultManager] fileExistsAtPath:[documentURL path]]) {
    // Open existing document
} else {
    // Create new document
}
```


After you’ve configured your managed document object, invoke the [saveToURL:forSaveOperation:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619988-save) method on the document and pass the [UIDocumentSaveForCreating](https://developer.apple.com/documentation/uikit/uidocumentsaveoperation/uidocumentsaveforcreating) operation option. This method creates the managed document’s file package inside your app’s ubiquity container.

```
...
if ([[NSFileManager defaultManager] fileExistsAtPath:[documentURL path]]) {
    ...
} else {
    [document saveToURL:documentURL forSaveOperation:UIDocumentSaveForCreating completionHandler:^(BOOL success) {
        if (success) {
            // Begin using managed document.
        } else {
            // Handle the error.
        }
    }];
}
```


After you’ve configured your managed document object, call [openWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619977-open) to open it.

```
...
if ([[NSFileManager defaultManager] fileExistsAtPath:[documentURL path]]) {
    [document openWithCompletionHandler:^(BOOL success) {
        if (success) {
            // Begin using the managed document.
        } else {
            // Handle the error.
        }
    }];
} else {
    ...
}
```


To support asynchronous data writing, Core Data uses a pair of nested managed object contexts: The parent context is created on a private thread, and the child context is created on the main thread. You get the _child_ context from the [managedObjectContext](https://developer.apple.com/documentation/uikit/uimanageddocument/1622667-managedobjectcontext) property. Because you should typically work with the child context, perform all operations using that context on the main thread.

If appropriate, you can load data from a background thread directly to the _parent_ context.

You can get the parent context using [parentContext](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/1506529-parent). When you load data to the parent context, you avoid interrupting the child context’s operations. You can retrieve data loaded in the background simply by executing a fetch.

In addition to receiving the notifications typically posted by Core Data, apps that use iCloud receive additional, iCloud-specific state change notifications. You can register to receive these notifications when you need additional insight into the the iCloud persistence process. If your managed document is backed by a SQLite-type persistent store (the default), read [Reacting to iCloud Events](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltk) to learn about responding to SQLite persistent store events. If instead you have configured your managed document to use an atomic store, see [Use Core Data Atomic Stores for Small, Simple Storage](About%20Using%20iCloud%20with%20Core%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmjnknlti).

To save a managed document in iOS, you can use any of the following approaches, with the most recommended approach listed first:

- Use the inherited Auto Save behavior provided by the `UIDocument` superclass. For most apps, this approach provides good performance and low network traffic.
- If your app design requires explicit control over when pending changes are committed, use the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) method [saveToURL:forSaveOperation:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619988-save).

  If you perform an explicit save operation in an iCloud-enabled app, be aware that you are generating additional network traffic—multiplied by the number of devices connected to the iCloud account.

If you have a specific case in which neither of the two preceding approaches works, such as importing a large quantity of data in the background, you can explicitly save the document’s internal context. When you do, keep in mind that a managed document has two contexts. The one it presents to you is actually a child of a second context that the document uses internally to communicate with the document’s Core Data store.

If you save only the document’s public context, you’re not committing changes to the store; you still end up relying on Auto Save. To explicitly save a document’s internal context, explicitly save both contexts. For more information, read Saving Changes in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.

If you save the internal context directly, you sidestep other important operations that the document performs.

To delete a managed document, first close the document. Then delete the following two directories, using coordinated write operations:

- The directory for the Core Data change logs for the managed document
- The managed document’s file package

To obtain the location of the directory containing the change log files, view the document’s `DocumentMetadata.plist` property list file. Retrieve the name and URL that you set when creating the document.

[Next](Best%20Practices.md)[Previous](Using%20the%20SQLite%20Store%20with%20iCloud.md)

