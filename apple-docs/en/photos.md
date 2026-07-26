---
title: Photos
framework: Photos
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos
source_url: 'https://developer.apple.com/documentation/photos'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos.json'
content_hash: 'sha256:89f82cbc1c735b42'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Photos

<sub>Framework</sub>

Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.

## Overview

Use PhotoKit to access image and video assets that the Photos app manages in iOS, macOS, tvOS, and visionOS. You might use this framework to edit or display a person’s photos, or to manage collections of assets such as albums, Moments, and Shared Albums. The framework provides access to photos on the person’s device and in iCloud.

> [!note] Note
> Photos is a [PhotoKit](photokit.md) framework.

## Topics

### Shared photo library

- [PHPhotoLibrary](photos/phphotolibrary.md) — An object that manages access and changes to the user’s photo library.

### Asset retrieval

- [Fetching Objects and Requesting Changes](photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](photos/phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHAssetCollection](photos/phassetcollection.md) — A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.
- [PHCollection](photos/phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHCollectionList](photos/phcollectionlist.md) — A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [PHObject](photos/phobject.md) — The abstract superclass for Photos model objects (assets and collections).
- [PHFetchResult](photos/phfetchresult.md) — An ordered list of assets or collections returned from a Photos fetch method.
- [PHFetchOptions](photos/phfetchoptions.md) — A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

### Asset loading

- [Loading and Caching Assets and Thumbnails](photokit/loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [PHImageManager](photos/phimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails and asset data.
- [PHCachingImageManager](photos/phcachingimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [PHImageRequestOptions](photos/phimagerequestoptions.md) — A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [PHVideoRequestOptions](photos/phvideorequestoptions.md) — A set of options affecting the delivery of video asset data that you request from an image manager.
- [PHLivePhotoRequestOptions](photos/phlivephotorequestoptions.md) — A set of options affecting the delivery of Live Photo assets you request from an image manager.

### Asset metadata

- [PHAssetExtendedMetadata](photos/phassetextendedmetadata.md) — Represents other asset attributes that are not included when fetching `PHAsset` directly. _(beta)_

### Asset resource management

- [PHAssetResource](photos/phassetresource.md) — An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [PHAssetCreationRequest](photos/phassetcreationrequest.md) — A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [PHAssetResourceCreationOptions](photos/phassetresourcecreationoptions.md) — A set of options affecting the creation of a new Photos asset from underlying resources.
- [PHAssetResourceManager](photos/phassetresourcemanager.md) — A resource manager for the data storage underlying a Photos asset.
- [PHAssetResourceRequestOptions](photos/phassetresourcerequestoptions.md) — A set of options affecting the delivery of underlying asset data that you request from the asset resource manager.

### Background resource upload extensions

- [Uploading asset resources in the background](photokit/uploading-asset-resources-in-the-background.md) — Enable reliable cloud backup for photo library assets with background processing.
- [PHBackgroundResourceUploadExtension](photos/phbackgroundresourceuploadextension.md) _(deprecated)_
- [PHAssetResourceUploadJob](photos/phassetresourceuploadjob.md) — An object that represents a request to upload an asset resource.
- [PHAssetResourceUploadJobChangeRequest](photos/phassetresourceuploadjobchangerequest.md) — Use within an application’s `com.apple.photos.background-upload` extension to create and change [PHAssetResourceUploadJob](photos/phassetresourceuploadjob.md) records.

### Live Photos

- [PHLivePhoto](photos/phlivephoto.md) — A displayable representation of a Live Photo—a picture that includes motion and sound from the moments just before and after its capture.

### Errors

- [PHPhotosError](photos/phphotoserror-swift.struct.md) — A structure that represents a framework error.
- [PHPhotosErrorDomain](photos/phphotoserrordomain.md) — A string representation of the error domain.

### Deprecated errors

- [Deprecated Errors](photokit/deprecated-errors.md) — Review unsupported errors and their replacements.

### Classes

- [PHProject](photos/phproject.md) — A representation of a Photos app project extension.
- [PHProjectChangeRequest](photos/phprojectchangerequest.md) — A request to change asset data in a Photos project extension.

### Protocols

- [PHBackgroundResourceUploadJobExtension](photos/phbackgroundresourceuploadjobextension.md) _(beta)_
- [PHPhotoLibraryPersistentChangesObserver](photos/phphotolibrarypersistentchangesobserver.md) _(beta)_

## See Also

### Frameworks

- [PhotosUI](photosui.md) — Present a person’s photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.
