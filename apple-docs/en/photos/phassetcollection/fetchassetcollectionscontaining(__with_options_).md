---
title: 'fetchAssetCollectionsContaining(_:with:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollection/fetchassetcollectionscontaining(_:with:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollectionscontaining(_:with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchassetcollectionscontaining%28_%3Awith%3Aoptions%3A%29.json'
content_hash: 'sha256:15d3b60500cd8977'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchAssetCollectionsContaining(_:with:options:)

<sub>Type Method</sub>

Retrieves asset collections of the specified type containing the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssetCollectionsContaining(_ asset: PHAsset, with type: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `asset` — A Photos asset.

- `type` — An asset collection type, such as an album or a moment. See [PHAssetCollectionType](../phassetcollectiontype.md).

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsInMomentList:options:](<fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
- [+ fetchMomentsWithOptions:](<fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_
