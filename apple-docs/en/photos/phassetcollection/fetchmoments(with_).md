---
title: 'fetchMoments(with:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phassetcollection/fetchmoments(with:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchmoments(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchmoments%28with%3A%29.json'
content_hash: 'sha256:d84adec173247dda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchMoments(with:)

<sub>Type Method</sub>

Retrieves asset collections corresponding to moments seen in the Photos app.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func fetchMoments(with options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Photos app automatically creates moments to group assets by time and location.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchAssetCollectionsWithALAssetGroupURLs:options:](<fetchassetcollections(withalassetgroupurls_options_).md>) — Retrieves asset collections using URLs provided by the Assets Library framework. _(deprecated)_
- [+ fetchMomentsInMomentList:options:](<fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
