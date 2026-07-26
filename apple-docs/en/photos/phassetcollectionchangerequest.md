---
title: PHAssetCollectionChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollectionchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest.json'
content_hash: 'sha256:f467d6406f327380'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetCollectionChangeRequest

<sub>Class</sub>

A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetCollectionChangeRequest
```

## Overview

You use the [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) class to request changes for [PHAssetCollection](phassetcollection.md) objects. To make changes to asset collections (such as user-created albums) in the Photos library, create a change request using the appropriate class method for the change you want to perform.

- Call the [+ creationRequestForAssetCollectionWithTitle:](<phassetcollectionchangerequest/creationrequestforassetcollection(withtitle_).md>) method to create a new asset collection.
- Call the [+ deleteAssetCollections:](<phassetcollectionchangerequest/deleteassetcollections(__).md>) method to delete existing asset collections.
- Call the [+ changeRequestForAssetCollection:](<phassetcollectionchangerequest/init(for_).md>) or [+ changeRequestForAssetCollection:assets:](<phassetcollectionchangerequest/init(for_assets_).md>) method to modify a collection’s metadata or list of member assets.

Before creating a change request, use the [- canPerformEditOperation:](<phcollection/canperform(__).md>) method to verify that the collection allows the edit operation you’re requesting. If you attempt to perform an unsupported edit operation, Photos throws an exception.

A change request for creating or modifying an asset collection works like a mutable version of the asset collection object. Use the change request’s properties and instance methods to request changes to the asset collection itself. For example, the following code removes an asset from an album.

**Swift**

```swift
PHPhotoLibrary.shared().performChanges {

    let request = PHAssetCollectionChangeRequest(for: myAlbum,
                                                 assets: albumAssetsFetchResult)
    
    request!.removeAssets([asset] as NSFastEnumeration)

} completionHandler: { success, error in
    print("Finished removing the asset from the album. \(success ? "Success" : String(describing: error))")
}
```

**Objective-C**

```objc
[[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        
    PHAssetCollectionChangeRequest *request =
        [PHAssetCollectionChangeRequest changeRequestForAssetCollection:myAlbum
                                                                 assets:albumAssetsFetchResult];
        
    [request removeAssets:@[asset]];
     
} completionHandler:^(BOOL success, NSError *error) {
    NSLog(@"Finished removing the asset from the album. %@", (success ? @"Success" : error));
}];
```

After Photos runs the change block and calls your completion handler, the asset collection’s state reflects the changes you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHChangeRequest](phchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Adding New Asset Collections

- [+ creationRequestForAssetCollectionWithTitle:](<phassetcollectionchangerequest/creationrequestforassetcollection(withtitle_).md>) — Creates a request for adding a new asset collection to the Photos library.
- [placeholderForCreatedAssetCollection](phassetcollectionchangerequest/placeholderforcreatedassetcollection.md) — A placeholder object for the asset collection that the change request creates.

### Deleting Asset Collections

- [+ deleteAssetCollections:](<phassetcollectionchangerequest/deleteassetcollections(__).md>) — Requests that the specified asset collections be deleted.

### Modifying Asset Collections

- [+ changeRequestForAssetCollection:](<phassetcollectionchangerequest/init(for_).md>) — Creates a request for modifying the specified asset collection.
- [+ changeRequestForAssetCollection:assets:](<phassetcollectionchangerequest/init(for_assets_).md>) — Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [title](phassetcollectionchangerequest/title.md) — The displayed name of the asset collection.
- [- addAssets:](<phassetcollectionchangerequest/addassets(__).md>) — Adds the specified assets to the asset collection.
- [- insertAssets:atIndexes:](<phassetcollectionchangerequest/insertassets(__at_).md>) — Inserts the specified assets into the collection at the specified indexes.
- [- removeAssets:](<phassetcollectionchangerequest/removeassets(__).md>) — Removes the specified assets from the asset collection.
- [- removeAssetsAtIndexes:](<phassetcollectionchangerequest/removeassets(at_).md>) — Removes the assets at the specified indexes from the asset collection.
- [- replaceAssetsAtIndexes:withAssets:](<phassetcollectionchangerequest/replaceassets(at_withassets_).md>) — Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [- moveAssetsAtIndexes:toIndex:](<phassetcollectionchangerequest/moveassets(at_to_).md>) — Moves the assets at the specified indexes in the asset collection to a new index.

### Initializers

- [init(forAssetCollection:)](<phassetcollectionchangerequest/init(forassetcollection_).md>)
- [init(forAssetCollection:assets:)](<phassetcollectionchangerequest/init(forassetcollection_assets_).md>)

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHChangeRequest](phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetChangeRequest](phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.
