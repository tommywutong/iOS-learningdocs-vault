---
title: 'fetchAssetCollections(with:subtype:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollection/fetchassetcollections(with:subtype:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(with:subtype:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchassetcollections%28with%3Asubtype%3Aoptions%3A%29.json'
content_hash: 'sha256:0274e413744632eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchAssetCollections(with:subtype:options:)

<sub>Type Method</sub>

Retrieves asset collections of the specified type and subtype.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssetCollections(with type: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `type` — A type of asset collection, such as an album or a moment. See [PHAssetCollectionType](../phassetcollectiontype.md).

- `subtype` — A subtype of asset collection. See [PHAssetCollectionSubtype](../phassetcollectionsubtype.md).

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, the returned [PHFetchResult](../phfetchresult.md) object contains all asset collections with the specified type and subtype. To retrieve a more specific set of asset collections, provide a [PHFetchOptions](../phfetchoptions.md) object containing a filter predicate.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsInMomentList:options:](<fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
- [+ fetchMomentsWithOptions:](<fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_
