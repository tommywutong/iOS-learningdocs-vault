---
title: PHCollectionList
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlist
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlist.json'
content_hash: 'sha256:44bf00640c0be587'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHCollectionList

<sub>Class</sub>

A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHCollectionList
```

## Overview

In the Photos framework, collection objects (including asset collections) do not directly reference their member objects, and there are no other objects that directly reference collection objects. To retrieve the members of a collection list, fetch them with a [PHCollection](phcollection.md) class method such as [+ fetchCollectionsInCollectionList:options:](<phcollection/fetchcollections(in_options_).md>). To find objects at the root of the collection list hierarchy (such as album folders with no parent folders), use the [+ fetchTopLevelUserCollectionsWithOptions:](<phcollection/fetchtoplevelusercollections(with_).md>) method.

> [!important] Important
> Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in the Fetching Collection Lists group, Photos automatically prompts the user for authorization. (Alternatively, you can use the [PHPhotoLibrary](phphotolibrary.md) [+ requestAuthorization:](<phphotolibrary/requestauthorization(__).md>) method to prompt the user at a time of your choosing.)
>
> Your app’s `Info.plist` file must provide a value for the [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) key that explains to the user why your app is requesting Photos access. Apps linked on or after iOS 10.0 will crash if this key is not present.

Like assets and asset collections, collection lists are immutable. To create, rename, or delete collection lists, or to add, remove, or rearrange members in a collection list, create a [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) object within a photo library change block. For details on using change requests and change blocks to update the photo library, see [PHPhotoLibrary](phphotolibrary.md).

## Relationships

- **Inherits From**: [PHCollection](phcollection.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Fetching Collection Lists

- [+ fetchCollectionListsContainingCollection:options:](<phcollectionlist/fetchcollectionlistscontaining(__options_).md>) — Retrieves collection lists that contain the specified collection.
- [+ fetchCollectionListsWithLocalIdentifiers:options:](<phcollectionlist/fetchcollectionlists(withlocalidentifiers_options_).md>) — Retrieves collection lists with the specified local-device-specific unique identifiers.
- [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>) — Retrieves collection lists of the specified type.
- [+ fetchMomentListsWithSubtype:containingMoment:options:](<phcollectionlist/fetchmomentlists(with_containingmoment_options_).md>) — Retrieves collection lists of the specified moment list type containing the specified moment. _(deprecated)_
- [+ fetchMomentListsWithSubtype:options:](<phcollectionlist/fetchmomentlists(with_options_).md>) — Retrieves collection lists of the specified moment list type. _(deprecated)_

### Reading Collection List Metadata

- [collectionListType](phcollectionlist/collectionlisttype.md) — The type of asset collection group that the collection list represents.
- [PHCollectionListType](phcollectionlisttype.md) — Major distinctions between kinds of collection list, used by the [collectionListType](phcollectionlist/collectionlisttype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>) method.
- [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) — The type of asset collection grouping the collection list represents.
- [PHCollectionListSubtype](phcollectionlistsubtype.md) — Major distinctions between kinds of collection list, used by the [collectionListSubtype](phcollectionlist/collectionlistsubtype.md) property and [+ fetchCollectionListsWithType:subtype:options:](<phcollectionlist/fetchcollectionlists(with_subtype_options_).md>), [+ fetchMomentListsWithSubtype:containingMoment:options:](<phcollectionlist/fetchmomentlists(with_containingmoment_options_).md>), and [+ fetchMomentListsWithSubtype:options:](<phcollectionlist/fetchmomentlists(with_options_).md>) methods.
- [startDate](phcollectionlist/startdate.md) — The earliest creation date among all assets in the collection list.
- [endDate](phcollectionlist/enddate.md) — The latest creation date among all assets in the collection list.
- [localizedLocationNames](phcollectionlist/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).

### Creating Temporary Collection Lists

- [+ transientCollectionListWithCollections:title:](<phcollectionlist/transientcollectionlist(with_title_).md>) — Creates a temporary collection list that contains the specified asset collections.
- [+ transientCollectionListWithCollectionsFetchResult:title:](<phcollectionlist/transientcollectionlist(withcollectionsfetchresult_title_).md>) — Creates a temporary collection list containing the asset collections in the specified fetch result.

## See Also

### Asset retrieval

- [Fetching Objects and Requesting Changes](../photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHAssetCollection](phassetcollection.md) — A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.
- [PHCollection](phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHObject](phobject.md) — The abstract superclass for Photos model objects (assets and collections).
- [PHFetchResult](phfetchresult.md) — An ordered list of assets or collections returned from a Photos fetch method.
- [PHFetchOptions](phfetchoptions.md) — A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.
