---
title: PHFetchOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions.json'
content_hash: 'sha256:327e714e2f6c34ea'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHFetchOptions

<sub>Class</sub>

A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHFetchOptions
```

## Overview

Using class methods on the [PHAsset](phasset.md), [PHCollection](phcollection.md), [PHAssetCollection](phassetcollection.md), and [PHCollectionList](phcollectionlist.md) classes to fetch assets or collections produces a [PHFetchResult](phfetchresult.md) object containing the requested objects. The options you specify control which objects the fetch result includes, how those objects are arranged in the fetch result, and how Photos should notify your app of changes to the fetch result.

Photos supports only a restricted set of keys for the [predicate](phfetchoptions/predicate.md) and [sortDescriptors](phfetchoptions/sortdescriptors.md) properties. The set of available keys depends on which class you’re using to fetch assets or collections. The following table lists the keys supported by each class:

| Class for Fetch Method | Supported Keys |
|---|---|
| [PHAsset](phasset.md) | `SELF`, [localIdentifier](phobject/localidentifier.md), [creationDate](phasset/creationdate.md), [modificationDate](phasset/modificationdate.md), [mediaType](phasset/mediatype.md), [mediaSubtypes](phasset/mediasubtypes.md), [duration](phasset/duration.md), [pixelWidth](phasset/pixelwidth.md), [pixelHeight](phasset/pixelheight.md), [favorite](phasset/isfavorite.md) (or `isFavorite`), [hidden](phasset/ishidden.md) (or `isHidden`), [burstIdentifier](phasset/burstidentifier.md) |
| [PHAssetCollection](phassetcollection.md) | `SELF`, [localIdentifier](phobject/localidentifier.md), [localizedTitle](phcollection/localizedtitle.md) (or `title`), [startDate](phassetcollection/startdate.md), [endDate](phassetcollection/enddate.md), [estimatedAssetCount](phassetcollection/estimatedassetcount.md) |
| [PHCollectionList](phcollectionlist.md) | `SELF`, [localIdentifier](phobject/localidentifier.md), [localizedTitle](phcollection/localizedtitle.md) (or `title`), [startDate](phcollectionlist/startdate.md), [endDate](phcollectionlist/enddate.md) |
| [PHCollection](phcollection.md) (can fetch a mix of [PHCollectionList](phcollectionlist.md) and [PHAssetCollection](phassetcollection.md) objects) | `SELF`, [localIdentifier](phobject/localidentifier.md), [localizedTitle](phcollection/localizedtitle.md) (or `title`), [startDate](phcollectionlist/startdate.md), [endDate](phcollectionlist/enddate.md) |

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Sorting and Filtering Fetch Results

- [predicate](phfetchoptions/predicate.md) — A predicate that specifies which properties to select results by and that also specifies any constraints on selection.
- [sortDescriptors](phfetchoptions/sortdescriptors.md) — A list of sort descriptors, specifying an order for the fetched objects.

### Subscribing to Changes

- [wantsIncrementalChangeDetails](phfetchoptions/wantsincrementalchangedetails.md) — A Boolean value that determines whether your app receives detailed change information for the objects in the fetch result.

### Limiting Fetch Results

- [fetchLimit](phfetchoptions/fetchlimit.md) — The maximum number of objects to include in the fetch result.
- [includeAllBurstAssets](phfetchoptions/includeallburstassets.md) — A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [includeHiddenAssets](phfetchoptions/includehiddenassets.md) — A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [includeAssetSourceTypes](phfetchoptions/includeassetsourcetypes.md) — The set of source types for which to include assets in the fetch result.
- [prefetchAssetExtendedMetadata](phfetchoptions/prefetchassetextendedmetadata.md) — A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched. _(beta)_

## See Also

### Asset retrieval

- [Fetching Objects and Requesting Changes](../photokit/fetching-objects-and-requesting-changes.md) — Get assets, asset collections, and collection lists matching a specified query.
- [PHAsset](phasset.md) — A representation of an image, video, or Live Photo in the Photos library.
- [PHAssetCollection](phassetcollection.md) — A representation of a Photos asset grouping, such as a moment, user-created album, or smart album.
- [PHCollection](phcollection.md) — The abstract superclass for Photos asset collections and collection lists.
- [PHCollectionList](phcollectionlist.md) — A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [PHObject](phobject.md) — The abstract superclass for Photos model objects (assets and collections).
- [PHFetchResult](phfetchresult.md) — An ordered list of assets or collections returned from a Photos fetch method.
