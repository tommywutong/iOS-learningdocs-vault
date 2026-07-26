---
title: 'fetchAssetCollections(withALAssetGroupURLs:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）, tvOS 10.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phassetcollection/fetchassetcollections(withalassetgroupurls:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(withalassetgroupurls:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollection/fetchassetcollections%28withalassetgroupurls%3Aoptions%3A%29.json'
content_hash: 'sha256:dd5c9165b67dd37f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollection](../phassetcollection.md)

# fetchAssetCollections(withALAssetGroupURLs:options:)

<sub>Type Method</sub>

Retrieves asset collections using URLs provided by the Assets Library framework.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssetCollections(withALAssetGroupURLs assetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

## Parameters

- `assetGroupURLs` — An array of [NSURL](../../foundation/nsurl.md) objects, each an asset group URL that was previously retrieved from an [ALAssetsGroup](../../assetslibrary/alassetsgroup.md) object.

- `options` — Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAssetCollection](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Assets Library framework is deprecated in iOS 8.0 and later, replaced by the Photos framework. Use this method if your app has previously stored URLs from [ALAssetsGroup](../../assetslibrary/alassetsgroup.md) objects and you need to retrieve the corresponding Photos framework objects.

## See Also

### Fetching Asset Collections

- [+ fetchAssetCollectionsWithLocalIdentifiers:options:](<fetchassetcollections(withlocalidentifiers_options_).md>) — Retrieves asset collections with the specified unique identifiers.
- [+ fetchAssetCollectionsWithType:subtype:options:](<fetchassetcollections(with_subtype_options_).md>) — Retrieves asset collections of the specified type and subtype.
- [+ fetchAssetCollectionsContainingAsset:withType:options:](<fetchassetcollectionscontaining(__with_options_).md>) — Retrieves asset collections of the specified type containing the specified asset.
- [+ fetchMomentsInMomentList:options:](<fetchmoments(inmomentlist_options_).md>) — Retrieves asset collections in the specified moment list collection. _(deprecated)_
- [+ fetchMomentsWithOptions:](<fetchmoments(with_).md>) — Retrieves asset collections corresponding to moments seen in the Photos app. _(deprecated)_
