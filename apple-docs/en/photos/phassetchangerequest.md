---
title: PHAssetChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest.json'
content_hash: 'sha256:5d643deb75a9b52f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetChangeRequest

<sub>Class</sub>

A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetChangeRequest
```

## Overview

You use the [PHAssetChangeRequest](phassetchangerequest.md) class to request changes for [PHAsset](phasset.md) objects. To make changes to assets in the Photos library, create a change request by using the appropriate class method for the change you want to perform.

- Call one of the methods listed in Adding New Assets to create a new asset from an image or video file.
- Call the [+ deleteAssets:](<phassetchangerequest/deleteassets(__).md>) method to delete existing assets.
- Call the [+ changeRequestForAsset:](<phassetchangerequest/init(for_).md>) method to modify an asset’s content or metadata.

A change request for creating or modifying an asset works like a mutable version of the asset object. Use the change request’s properties to request changes to the corresponding properties of the asset itself. For example, the following code uses the [favorite](phassetchangerequest/isfavorite.md) property of a change request to mark an asset as a favorite:

**Swift**

```swift
func toggleFavorite(for asset: PHAsset) {        
    PHPhotoLibrary.shared().performChanges {
        // Create a change request from the asset to be modified.
        let request = PHAssetChangeRequest(for: asset)
        // Set a property of the request to change the asset itself.
        request.isFavorite = !asset.isFavorite
    } completionHandler: { success, error in
        print("Finished updating asset. " + (success ? "Success." : error!.localizedDescription))
    }  
}
```

**Objective-C**

```objc
- (void)toggleFavoriteForAsset:(PHAsset *)asset {
    [[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        // Create a change request from the asset to be modified.
        PHAssetChangeRequest *request = [PHAssetChangeRequest changeRequestForAsset:asset];
        // Set a property of the request to change the asset itself.
        request.favorite = !asset.favorite;
    } completionHandler:^(BOOL success, NSError *error) {
        NSLog(@"Finished updating asset. %@", (success ? @"Success." : error));
    }];
}
```

After Photos runs the change block and calls your completion handler, the asset’s state reflects the changes that you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHChangeRequest](phchangerequest.md)

- **Inherited By**: [PHAssetCreationRequest](phassetcreationrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Adding New Assets

- [+ creationRequestForAssetFromImage:](<phassetchangerequest/creationrequestforasset(from_).md>) — Creates a request for adding a new image asset to the Photos library.
- [+ creationRequestForAssetFromImageAtFileURL:](<phassetchangerequest/creationrequestforassetfromimage(atfileurl_).md>) — Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [+ creationRequestForAssetFromVideoAtFileURL:](<phassetchangerequest/creationrequestforassetfromvideo(atfileurl_).md>) — Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.
- [placeholderForCreatedAsset](phassetchangerequest/placeholderforcreatedasset.md) — A placeholder object for the asset that the change request creates.

### Deleting Assets

- [+ deleteAssets:](<phassetchangerequest/deleteassets(__).md>) — Requests that the specified assets be deleted.

### Modifying Assets

- [+ changeRequestForAsset:](<phassetchangerequest/init(for_).md>) — Creates a request for modifying the specified asset.
- [creationDate](phassetchangerequest/creationdate.md) — The date and time at which the asset claims to have been originally created.
- [location](phassetchangerequest/location.md) — The location information saved with the asset.
- [favorite](phassetchangerequest/isfavorite.md) — A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [hidden](phassetchangerequest/ishidden.md) — A Boolean value that indicates whether the asset is hidden in collections.
- [caption](phassetchangerequest/caption.md) — An asset description to change to. Set to nil or an empty string to clear the caption. _(beta)_
- [- addKeyword:](<phassetchangerequest/addkeyword(__).md>) — Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored _(beta)_
- [- removeKeyword:](<phassetchangerequest/removekeyword(__).md>) _(beta)_
- [rating](phassetchangerequest/rating.md) _(beta)_
- [- setLivePhotoVideoPlaybackEnabled:](<phassetchangerequest/setlivephotovideoplaybackenabled(__).md>) — Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled) _(beta)_

### Editing Asset Content

- [contentEditingOutput](phassetchangerequest/contenteditingoutput.md) — The output of an asset content editing session.
- [- revertAssetContentToOriginal](<phassetchangerequest/revertassetcontenttooriginal().md>) — Request to revert any edits made to the asset’s content.
- [- revertAssetContentToOriginalResourceChoice:](<phassetchangerequest/revertassetcontent(to_).md>) — Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders. _(beta)_

### Initializers

- [init(forAsset:)](<phassetchangerequest/init(forasset_).md>)

## See Also

### Updating the Library

- [Requesting Changes to the Photo Library](../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHChangeRequest](phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.
