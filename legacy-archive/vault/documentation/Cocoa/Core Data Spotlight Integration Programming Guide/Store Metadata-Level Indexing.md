---
title: Core Data Spotlight Integration Programming Guide
apple_id: TP40008065
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreData
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Articles/storeMetadata.html
archived_at: '2026-07-15T07:19:21.198076Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data Spotlight Integration Programming Guide](Introduction.md)


[Next](Record-Level%20Indexing.md)[Previous](Introduction.md)

# Store Metadata-Level Indexing

In a document-based application, where the Spotlight data needs to be associated with individual files, you can add the data that needs to be indexed as metadata for the persistent store. Your importer adds the information from the metadata to the Spotlight index.

You can associate metadata with a persistent store. The template code for the Spotlight importer checks to see if the store file is what should be indexed. If so, it reads the relevant store metadata and passes appropriate values to the Spotlight indexer.

The metadata is a dictionary of key-value pairs. Core Data automatically sets values for `NSStoreType` and `NSStoreUUID`. To set custom keys and values, you make a mutable copy of the existing dictionary, add your own key-value pairs that will be read by the importer, and then set the updated dictionary as the metadata for the store.

You should be careful what information you put into metadata for two reasons:

- Spotlight imposes a limit to the size of metadata.
- Replicating an entire document in metadata is probably not useful.

Recall that it is possible to create a URL to identify a particular object in a store (using [URIRepresentation](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391689-urirepresentation))—the URL may be useful to include as metadata. Large metadata is best stored separately from the database file. For example, cached images for QuickLooks are much cheaper to store in a dedicated file on disk that can be memory mapped in, than stored in the database's metadata.

You set the metadata for a store using the `NSPersistentStore` method [setMetadata:forPersistentStoreWithURL:error:](https://developer.apple.com/documentation/coredata/nspersistentstore/1506824-setmetadata).

```
NSError *error = nil;
NSURL *storeURL = <#URL for persistent store#>;

NSDictionary *metadata =
    [NSPersistentStore metadataForPersistentStoreWithURL:storeURL error:&error];

if (metadata == nil) {
    /* Deal with the error. */
}
else {
    NSMutableDictionary *newMetadata = [metadata mutableCopy];
    [newMetadata setObject:@[@"MyKeyWord"] forKey:(__bridge id<NSCopying>)kMDItemKeywords];
    // Set additional key-value pairs as appropriate.
    [NSPersistentStore setMetadata:newMetadata
                       forPersistentStoreWithURL:storeURL
                       error:&error];
}
```

Note that setting the metadata for a store does not change the information on disk until the store is actually saved.

`NSPersistentStoreCoordinator` provides a class method, [metadataForPersistentStoreWithURL:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468915-metadataforpersistentstorewithur), that allows you to retrieve metadata from a store without the overhead of creating a Core Data stack. You can also use the `NSPersistentStore` method [metadataForPersistentStoreWithURL:error:](https://developer.apple.com/documentation/coredata/nspersistentstore/1506741-metadataforpersistentstore). You use these methods in the importer to extract the data to pass to the indexer.

[Next](Record-Level%20Indexing.md)[Previous](Introduction.md)

