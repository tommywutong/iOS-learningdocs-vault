---
title: PHAssetCollection
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollection
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection.json'
content_hash: 'sha256:9571bb407ba3b148'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetCollection

<sub>Class</sub>

A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHAssetCollection
```

## Overview

In the Photos framework, collection objects (including asset collections) do not directly reference their member objects, and there are no other objects that directly reference collection objects. To retrieve the members of an asset collection, fetch them with a [PHAsset](phasset.md) class method such as [+ fetchAssetsInAssetCollection:options:](<phasset/fetchassets(in_options_).md>). To find asset collections, use one of the methods listed in the Fetching Asset Collections group below.

> [!important] Important
> Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in the Fetching Asset Collections group, Photos automatically prompts the user for authorization. (Alternatively, you can use the [PHPhotoLibrary](phphotolibrary.md)  [+ requestAuthorization:](<phphotolibrary/requestauthorization(__).md>) method to prompt the user at a time of your choosing.)
>
> Your app’s `Info.plist` file must provide a value for the [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) key that explains to the user why your app is requesting Photos access. Apps linked on or after iOS 10.0 will crash if this key is not present.

Like assets and collection lists, asset collections are immutable. To create, rename, or delete asset collections, or to add, remove, or rearrange members in an asset collection, create a [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) object within a photo library change block. For details on using change requests and change blocks to update the photo library, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHCollection](phcollection.md)

- **Inherited By**: [PHProject](phproject.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<phassetcollection/fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<phassetcollection/fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<phassetcollection/fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsInMomentList:options:](<phassetcollection/fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
- [+ fetchMomentsWithOptions:](<phassetcollection/fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_

### Reading Asset Collection Metadata

- [assetCollectionType](phassetcollection/assetcollectiontype.md) — The type of the asset collection, such as an album or a moment.
- [PHAssetCollectionType](phassetcollectiontype.md) — Major distinctions between kinds of asset collections, used by the [assetCollectionType](phassetcollection/assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<phassetcollection/fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) methods.
- [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) — The subtype of the asset collection.
- [PHAssetCollectionSubtype](phassetcollectionsubtype.md) — Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) method.
- [estimatedAssetCount](phassetcollection/estimatedassetcount.md) — The estimated number of assets in the asset collection.
- [startDate](phassetcollection/startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](phassetcollection/enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](phassetcollection/approximatelocation.md) — A location representing those of all assets in the collection.
- [localizedLocationNames](phassetcollection/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).

### Creating Temporary Asset Collections

- [+ transientAssetCollectionWithAssets:title:](<phassetcollection/transientassetcollection(with_title_).md>) — Creates a temporary asset collection containing the specified assets.
- [+ transientAssetCollectionWithAssetFetchResult:title:](<phassetcollection/transientassetcollection(withassetfetchresult_title_).md>) — Creates a temporary asset collection containing the assets from the specified fetch result.

## See Also

### Asset retrieval

- [Fetching Objects and Requesting Changes](../photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHCollection](phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHCollectionList](phcollectionlist.md) — A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [PHObject](phobject.md) — The abstract superclass for Photos model objects (assets and collections).
- [PHFetchResult](phfetchresult.md) — An ordered list of assets or collections returned from a Photos fetch method.
- [PHFetchOptions](phfetchoptions.md) — A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.
