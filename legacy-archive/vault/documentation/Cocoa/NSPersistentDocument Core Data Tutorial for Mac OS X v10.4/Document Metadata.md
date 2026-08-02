---
title: NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.
apple_id: TP40008168
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSPersistentDocumentTutorial104/07_Metadata/metadata.html
archived_at: '2026-07-15T07:16:51.594743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.](Introduction%20to%20NSPersistentDocument%20Core%20Data%20Tutorial%20for%20Mac%20OS%20X%20v10.4.md)


[Next](A%20Sheet%20for%20Creating%20a%20New%20Employee.md)[Previous](Localizing%20and%20Customizing%20Model%20Property%20Names%20and%20Error%20Messages.md)

This document will not be modified in the future.

# Document Metadata

Spotlight provides users with a means of searching for files quickly and easily. To support this, you need to associate metadata with your documents. Core Data makes it easy to do this and to write the necessary importer.

Note that setting the metadata only queues up the information to be saved when the store is next saved—it is not written out immediately.

1. You identify a store by its URL. Since there is more than one place that this code will be used, define a method in MyDocument to abstract the logic.

```objc
- (BOOL)setMetadataForStoreAtURL:(NSURL *)url {
    // implementation continues...
    return NO;
}
```
2. You retrieve a store from the persistent store coordinator, using the URL as an identifier. Objects that represent stores are opaque—they are defined as being of type `id` and have no API. You can use the ID to identify a store, but you can’t do anything else with it.

```
NSPersistentStoreCoordinator *psc = [[self managedObjectContext] persistentStoreCoordinator];
id pStore = [psc persistentStoreForURL:url];
```
3. If `pStore` is not `nil`, then you can set the metadata. The metadata is a dictionary of key-value pairs, where a key may be either custom for your application, or one of the standard set of Spotlight keys such as `kMDItemKeywords`. Core Data automatically sets values for `NSStoreType` and `NSStoreUUID`, so make a mutable copy of the existing metadata, and then add your own keys and values. In this example, simply set the department name as a keyword, then return `YES`.

   Note that the metadata may be set before validation methods are invoked, so even though the Department name is not optional, although unlikely it is possible for the value to be `nil` at this stage. You should therefore guard against attempting to insert a `nil` value into the array.

```
NSString *departmentName = [[self department] valueForKey:@"name"];

if ((pStore != nil) && (departmentName != nil)) {
    NSMutableDictionary *metadata = [[[psc metadataForPersistentStore:pStore] mutableCopy] autorelease];

    if (metadata == nil) {
         metadata = [NSMutableDictionary dictionary];

    [metadata setObject:[NSArray arrayWithObject:departmentName]
            forKey:(NSString *)kMDItemKeywords];

    [psc setMetadata:metadata forPersistentStore:pStore];
    return YES;
}
```


A complete listing for `setMetadataForStoreAtURL:` is shown in Listing 7-1.

__Listing 7-1__  Complete listing of the `setMetadataForStoreAtURL:` method

```objc
- (BOOL)setMetadataForStoreAtURL:(NSURL *)url {

    NSPersistentStoreCoordinator *psc = [[self managedObjectContext] persistentStoreCoordinator];
    id pStore = [psc persistentStoreForURL:url];
    NSString *departmentName = [[self department] valueForKey:@"name"];

    if ((pStore != nil) && (departmentName != nil)) {
        NSMutableDictionary *metadata = [[[psc metadataForPersistentStore:pStore] mutableCopy] autorelease];
        if (metadata == nil) {
            metadata = [NSMutableDictionary dictionary];
        }
        [metadata setObject:[NSArray arrayWithObject:departmentName]
                forKey:(NSString *)kMDItemKeywords];
        [psc setMetadata:metadata forPersistentStore:pStore];
        return YES;
    }
    return NO;
}
```


When a new store is configured (whether for a new untitled document, or when an existing document is reopened), Core Data calls the `NSPersistentDocument` method [configurePersistentStoreCoordinatorForURL:ofType:error:](https://developer.apple.com/documentation/appkit/nspersistentdocument/1396158-configurepersistentstorecoordina). You can override this method to add metadata to a new store before it is saved.

1. In MyDocument, add an implementation for `configurePersistentStoreCoordinatorForURL:ofType:error:`. You first call the superclass’s implementation, and check the return value:

```objc
- (BOOL)configurePersistentStoreCoordinatorForURL:(NSURL *)url ofType:(NSString *)fileType error:(NSError **)error {

    BOOL ok = [super configurePersistentStoreCoordinatorForURL:url
                      ofType:fileType error:error];

    if (ok) {
        // implementation continues...
    }
    return ok;
}
```
2. If the return value for the superclass’s implementation is `YES`, then retrieve the persistent store for the specified URL from the persistent store coordinator:

```
NSPersistentStoreCoordinator *psc = [[self managedObjectContext] persistentStoreCoordinator];
id pStore = [psc persistentStoreForURL:url];
```
3. Since the configure method is also called when a document is reopened, you should check for existing custom metadata to avoid overwriting it unnecessarily. If your metadata is not present, set it using `setMetadataForStoreAtURL:`.

```
id existingMetadata = [[psc metadataForPersistentStore:pStore]
         objectForKey:(NSString *)kMDItemKeywords];
if (existingMetadata == nil) {
    ok = [self setMetadataForStoreAtURL:url];
}
```


A complete listing for `configurePersistentStoreCoordinatorForURL:ofType:error:` is shown in Listing 7-2.

__Listing 7-2__  Complete listing of the `configurePersistentStoreCoordinatorForURL:ofType:error:` method

```objc
- (BOOL)configurePersistentStoreCoordinatorForURL:(NSURL *)url
                ofType:(NSString *)fileType
                error:(NSError **)error
{
    BOOL ok = [super configurePersistentStoreCoordinatorForURL:url
                                                        ofType:fileType
                                                         error:error];
    if (ok)
    {
        NSPersistentStoreCoordinator *psc = [[self managedObjectContext]
                persistentStoreCoordinator];
        id pStore = [psc persistentStoreForURL:url];
        id existingMetadata = [[psc metadataForPersistentStore:pStore]
                objectForKey:(NSString *)kMDItemKeywords];
        if (existingMetadata == nil) {
            ok = [self setMetadataForStoreAtURL:url];
        }
    }
    return ok;}
```


When a document is saved, Core Data calls the `NSPersistentDocument` method `writeToURL:ofType:forSaveOperation:originalContentsURL:error:`. You can override this method to add metadata to the new store before it is saved. (Recall that setting the metadata for a store does not change the information on disk until the store is saved.)

1. In MyDocument, add an implementation for `writeToURL: ofType: forSaveOperation: originalContentsURL: error:`. The final step is to invoke and return the superclass’s implementation.

```objc
- (BOOL)writeToURL:(NSURL *)absoluteURL
    ofType:(NSString *)typeName
    forSaveOperation:(NSSaveOperationType)saveOperation
    originalContentsURL:(NSURL *)absoluteOriginalContentsURL
    error:(NSError **)error
{
    // implementation continues...

    return [super writeToURL:absoluteURL
                      ofType:typeName
            forSaveOperation:saveOperation
         originalContentsURL:absoluteOriginalContentsURL
                       error:error];
}
```
2. If the document’s URL is not `nil`, then it is possible to retrieve the persistent store for that URL from the persistent store coordinator. Invoke `setMetadataForStoreAtURL:` to set the metadata for the store.

```
if ([self fileURL] != nil) {
        [self setMetadataForStoreAtURL:[self fileURL]];
}
```

   Note that this also takes account of Save As operations. The metadata is associated with the persistent store before it is written to a new file.

A complete listing for `writeToURL:ofType:forSaveOperation:originalContentsURL:error:` is shown in Listing 7-3.

__Listing 7-3__  Complete listing of the `writeToURL:ofType:forSaveOperation:originalContentsURL:error:` method

```objc
- (BOOL)writeToURL:(NSURL *)absoluteURL
    ofType:(NSString *)typeName
    forSaveOperation:(NSSaveOperationType)saveOperation
    originalContentsURL:(NSURL *)absoluteOriginalContentsURL
    error:(NSError **)error
{
    if ([self fileURL] != nil) {
        [self setMetadataForStoreAtURL:[self fileURL]];
    }
    return [super writeToURL:absoluteURL
                      ofType:typeName
            forSaveOperation:saveOperation
         originalContentsURL:absoluteOriginalContentsURL
                       error:error];
}
```


Build and run the application again. Create and save several documents, giving the department a different name in each. Close and then reopen some of the documents, and save some to new locations.

If you open a document in a text editor (such as TextEdit), you should see that the correct metadata is appended to the file.

You used methods defined by `NSPersistentDocument` to set metadata for a store as it is saved. It is up to you to decide what information to store as metadata, and what keys to specify. You use the keys when writing your importer.

Details of how in general to write an importer are given in _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_. This section deals with aspects that are specific to writing an importer for Core Data.

To implement an importer, you first create a new Metadata Importer project in Xcode. Since a Core Data importer uses Objective-C, you should change the file type of the `GetMetadataForFile.c` file from `sourcecode.c.c` to `sourcecode.c.objc` using the Xcode inspector (Info window).

An important aspect of a Spotlight importer is that it should be efficient. A user may have many thousands of files, so any small inefficiency in an importer may have a serious impact on the time it takes to index their disk drive. One of the more expensive tasks in Core Data is creating the persistence stack—the object stores, the object store coordinator, the managed object context, and so on. So that you can avoid this overhead when reading metadata, `NSPersistentStoreCoordinator` provides a convenience method—`metadataForPersistentStoreWithURL:`—that retrieves the dictionary containing the metadata stored in an on-disk persistent store without initializing a persistence stack.

The main task when you write an importer is to implement the function `GetMetadataForFile`. The function must populate a mutable dictionary—supplied as one of the arguments—with the metadata for the specified file. Given the `NSPersistentStoreCoordinator` convenience method, the code is trivial, as shown here:

```
Boolean GetMetadataForFile(void* thisInterface,
    CFMutableDictionaryRef attributes,
    CFStringRef contentTypeUTI,
    CFStringRef pathToFile)
{
    NSURL *url = [NSURL fileURLWithPath:(NSString *)pathToFile];
    NSDictionary *metadata = [NSPersistentStoreCoordinator metadataForPersistentStoreWithURL:url error:nil];

    if (metadata != nil) {
        [(NSMutableDictionary *)attributes addEntriesFromDictionary:metadata];
        return TRUE;
    }
    return FALSE;
}
```

In addition to implementing the `GetMetadataForFile` function, you must (as with all importers) modify the CFBundleDocumentTypes entry in the importer project’s `Info.plist` file to contain an array of uniform type identifiers (UTIs) for the LSItemContentTypes that your importer can handle, and (if you have defined new attributes) update the `schema.xml` file. These are explained in detail in _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_.

[Next](A%20Sheet%20for%20Creating%20a%20New%20Employee.md)[Previous](Localizing%20and%20Customizing%20Model%20Property%20Names%20and%20Error%20Messages.md)

