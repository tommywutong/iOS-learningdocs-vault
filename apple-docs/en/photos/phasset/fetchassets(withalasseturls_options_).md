---
title: 'fetchAssets(withALAssetURLs:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 8.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/photos/phasset/fetchassets(withalasseturls:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/fetchassets(withalasseturls:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/fetchassets%28withalasseturls%3Aoptions%3A%29.json'
content_hash: 'sha256:e57a32b2f5429c99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# fetchAssets(withALAssetURLs:options:)

<sub>Type Method</sub>

Retrieves assets using URLs provided by the Assets Library framework.

> [!warning] Deprecated
> Will be removed in a future release

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func fetchAssets(withALAssetURLs assetURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

## Parameters

- `assetURLs` — An array of [NSURL](../../foundation/nsurl.md) objects, each an asset URL previously retrieved from an [ALAsset](../../assetslibrary/alasset.md) object.

- `options` — Options that specify a filter predicate and sort order for the fetched assets, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAsset](../phasset.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Assets Library framework is deprecated in iOS 8.0 and later, replaced by the Photos framework. Use this method if your app has previously stored URLs from [ALAsset](../../assetslibrary/alasset.md) objects and you need to retrieve the corresponding Photos framework objects.

## See Also

### Fetching Assets

- [Fetching Assets](../../photokit/fetching-assets.md) — Retrieve asset metadata or request full asset content.
- [+ fetchAssetsInAssetCollection:options:](<fetchassets(in_options_).md>) — Retrieves assets from the specified asset collection.
- [+ fetchAssetsWithMediaType:options:](<fetchassets(with_options_).md>) — Retrieves assets with the specified media type.
- [+ fetchAssetsWithLocalIdentifiers:options:](<fetchassets(withlocalidentifiers_options_).md>) — Retrieves assets with the specified local-device-specific unique identifiers.
- [+ fetchKeyAssetsInAssetCollection:options:](<fetchkeyassets(in_options_).md>) — Retrieves assets marked as key assets in the specified asset collection.
- [+ fetchAssetsWithOptions:](<fetchassets(with_).md>) — Retrieves all assets matching the specified options.
- [+ fetchAssetsWithBurstIdentifier:options:](<fetchassets(withburstidentifier_options_).md>) — Retrieves assets with the specified burst photo sequence identifier.
