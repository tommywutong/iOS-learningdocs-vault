---
title: 'fetchAssets(withBurstIdentifier:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phasset/fetchassets(withburstidentifier:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/fetchassets(withburstidentifier:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/fetchassets%28withburstidentifier%3Aoptions%3A%29.json'
content_hash: 'sha256:f49383b85b3ffdd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# fetchAssets(withBurstIdentifier:options:)

<sub>Type Method</sub>

Retrieves assets with the specified burst photo sequence identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssets(withBurstIdentifier burstIdentifier: String, options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

## Parameters

- `burstIdentifier` — A burst identifier string, as provided by the [burstIdentifier](burstidentifier.md) property of an asset.

- `options` — Options that specify a filter predicate and sort order for the fetched assets, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAsset](../phasset.md) objects, or an empty fetch result if no objects match the request.

## Discussion

A burst photo sequence, as seen in the Photos app, corresponds to a group of Photos assets that share the same [burstIdentifier](burstidentifier.md) string.

By default, the returned [PHFetchResult](../phfetchresult.md) object contains only the representative asset and any user-picked photos from the burst sequence. To retrieve all photos in the burst sequence, provide a [PHFetchOptions](../phfetchoptions.md) object containing a filter predicate.

## See Also

### Fetching Assets

- [Fetching Assets](../../photokit/fetching-assets.md) — Retrieve asset metadata or request full asset content.
- [+ fetchAssetsInAssetCollection:options:](<fetchassets(in_options_).md>) — Retrieves assets from the specified asset collection.
- [+ fetchAssetsWithMediaType:options:](<fetchassets(with_options_).md>) — Retrieves assets with the specified media type.
- [+ fetchAssetsWithLocalIdentifiers:options:](<fetchassets(withlocalidentifiers_options_).md>) — Retrieves assets with the specified local-device-specific unique identifiers.
- [+ fetchKeyAssetsInAssetCollection:options:](<fetchkeyassets(in_options_).md>) — Retrieves assets marked as key assets in the specified asset collection.
- [+ fetchAssetsWithOptions:](<fetchassets(with_).md>) — Retrieves all assets matching the specified options.
- [+ fetchAssetsWithALAssetURLs:options:](<fetchassets(withalasseturls_options_).md>) — Retrieves assets using URLs provided by the Assets Library framework. _(deprecated)_
