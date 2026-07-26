---
title: 'fetchKeyAssets(in:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phasset/fetchkeyassets(in:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/fetchkeyassets(in:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/fetchkeyassets%28in%3Aoptions%3A%29.json'
content_hash: 'sha256:f32ee8567bcf4902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# fetchKeyAssets(in:options:)

<sub>Type Method</sub>

Retrieves assets marked as key assets in the specified asset collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchKeyAssets(in assetCollection: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHAsset>?
```

## Parameters

- `assetCollection` — The asset collection from which to fetch assets.

- `options` — Options that specify a filter predicate and sort order for the fetched assets, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAsset](../phasset.md) objects, or an empty fetch result or `nil` if no objects match the request.

## Discussion

Most asset collections contain a _key asset_, which the Photos app displays as a proxy for the collection. Different types of asset collections have different ways of specifying one or more key assets. For example, in the Camera Roll collection, the most recently captured photo or video is the key asset.

This method returns `nil` if the `assetCollection` parameter references a transient asset collection (such as one created with the [+ transientAssetCollectionWithAssets:title:](<../phassetcollection/transientassetcollection(with_title_).md>) method).

## See Also

### Fetching Assets

- [Fetching Assets](../../photokit/fetching-assets.md) — Retrieve asset metadata or request full asset content.
- [+ fetchAssetsInAssetCollection:options:](<fetchassets(in_options_).md>) — Retrieves assets from the specified asset collection.
- [+ fetchAssetsWithMediaType:options:](<fetchassets(with_options_).md>) — Retrieves assets with the specified media type.
- [+ fetchAssetsWithLocalIdentifiers:options:](<fetchassets(withlocalidentifiers_options_).md>) — Retrieves assets with the specified local-device-specific unique identifiers.
- [+ fetchAssetsWithOptions:](<fetchassets(with_).md>) — Retrieves all assets matching the specified options.
- [+ fetchAssetsWithBurstIdentifier:options:](<fetchassets(withburstidentifier_options_).md>) — Retrieves assets with the specified burst photo sequence identifier.
- [+ fetchAssetsWithALAssetURLs:options:](<fetchassets(withalasseturls_options_).md>) — Retrieves assets using URLs provided by the Assets Library framework. _(deprecated)_
