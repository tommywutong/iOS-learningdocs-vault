---
title: PHCollectionListChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlistchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest.json'
content_hash: 'sha256:a719ad9544906dbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCollectionListChangeRequest

<sub>Class</sub>

A request to create, delete, or modify a Photos collection list, for use in a photo library change block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHCollectionListChangeRequest
```

## Overview

You use the [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) class to request changes for [PHCollectionList](phcollectionlist.md) objects. To make changes to collection lists (such as folders containing user-created albums) in the Photos library, create a change request using the appropriate class method for the change you want to perform.

- Call the [+ creationRequestForCollectionListWithTitle:](<phcollectionlistchangerequest/creationrequestforcollectionlist(withtitle_).md>) method to create a new asset collection.
- Call the [+ deleteCollectionLists:](<phcollectionlistchangerequest/deletecollectionlists(__).md>) method to delete existing asset collections.
- Call the [+ changeRequestForCollectionList:](<phcollectionlistchangerequest/init(for_).md>) or [+ changeRequestForCollectionList:childCollections:](<phcollectionlistchangerequest/init(for_childcollections_).md>) method to modify a collection’s metadata or its list of child collections.

Before creating a change request, use the [- canPerformEditOperation:](<phcollection/canperform(__).md>) method to verify that the collection allows the edit operation you’re requesting. If you attempt to perform an unsupported edit operation, Photos throws an exception.

A change request for creating or modifying a collection list works like a mutable version of the collection list object. Use the change request’s properties and instance methods to request changes to the collection list itself. For example, the following code removes an album from a folder.

**Swift**

```swift
PHPhotoLibrary.shared().performChanges {
            
    let request = PHCollectionListChangeRequest(for: folder,
                                                childCollections: folderContentsFetchResult)
            
    request!.removeChildCollections([album!] as NSFastEnumeration)
            
} completionHandler: { success, error in
    print("Finished removing the album from the folder. \(success ? "Success" : String(describing: error))")
}
```

**Objective-C**

```objc
[[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        
    PHCollectionListChangeRequest *request =
        [PHCollectionListChangeRequest changeRequestForCollectionList:folder
                                                     childCollections:folderContentsFetchResult];
        
    [request removeChildCollections:@[ album ]];
     
} completionHandler:^(BOOL success, NSError *error) {
    NSLog(@"Finished removing the album from the folder. %@", (success ? @"Success" : error));
}];
```

After Photos runs the change block and calls your completion handler, the collection list’s state reflects the changes you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHChangeRequest](phchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Change Request

- [+ changeRequestForCollectionList:](<phcollectionlistchangerequest/init(for_).md>) — Creates a request for modifying the specified collection list.
- [+ changeRequestForCollectionList:childCollections:](<phcollectionlistchangerequest/init(for_childcollections_).md>) — Creates a request for modifying the specified collection list, with a fetch result for tracking changes.
- [+ changeRequestForTopLevelCollectionListUserCollections:](<phcollectionlistchangerequest/init(fortoplevelcollectionlistusercollections_).md>) — Creates a request to add, remove, or rearrange child collections in the top-level collection list.

### Managing Collection Lists

- [+ creationRequestForCollectionListWithTitle:](<phcollectionlistchangerequest/creationrequestforcollectionlist(withtitle_).md>) — Creates a request for adding a new collection list to the Photos library.
- [placeholderForCreatedCollectionList](phcollectionlistchangerequest/placeholderforcreatedcollectionlist.md) — A placeholder object for the collection list that the change request creates.
- [+ deleteCollectionLists:](<phcollectionlistchangerequest/deletecollectionlists(__).md>) — Requests to delete the specified asset collections.

### Managing Collections

- [- addChildCollections:](<phcollectionlistchangerequest/addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- insertChildCollections:atIndexes:](<phcollectionlistchangerequest/insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- moveChildCollectionsAtIndexes:toIndex:](<phcollectionlistchangerequest/movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<phcollectionlistchangerequest/replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollections:](<phcollectionlistchangerequest/removechildcollections(__).md>) — Removes the specified child collections from the collection list.
- [- removeChildCollectionsAtIndexes:](<phcollectionlistchangerequest/removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.

### Inspecting the Request

- [title](phcollectionlistchangerequest/title.md) — The displayed name of the collection list.

### Initializers

- [init(forCollectionList:)](<phcollectionlistchangerequest/init(forcollectionlist_).md>)
- [init(forCollectionList:childCollections:)](<phcollectionlistchangerequest/init(forcollectionlist_childcollections_).md>)

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHChangeRequest](phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetChangeRequest](phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHObjectPlaceholder](phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.
