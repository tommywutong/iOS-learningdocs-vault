---
title: 'fetchAssets(with:options:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phasset/fetchassets(with:options:)'
source_url: 'https://developer.apple.com/documentation/photos/phasset/fetchassets(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/fetchassets%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:7a323f4f9550f73c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# fetchAssets(with:options:)

<sub>Type Method</sub>

Retrieves assets with the specified media type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func fetchAssets(with mediaType: PHAssetMediaType, options: PHFetchOptions?) -> PHFetchResult<PHAsset>
```

## Parameters

- `mediaType` — A media type, such as image or video. See [PHAssetMediaType](../phassetmediatype.md).

- `options` — Options that specify a filter predicate and sort order for the fetched assets, or `nil` to use default options. For details, see [PHFetchOptions](../phfetchoptions.md).

## Return Value

A fetch result that contains the requested [PHAsset](../phasset.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, the returned [PHFetchResult](../phfetchresult.md) object contains all assets with the specified type. To retrieve a more specific set of assets, provide a [PHFetchOptions](../phfetchoptions.md) object containing a filter predicate.

By default, fetch results do not include photos synced to the device through iTunes or stored in iCloud Shared Albums. To change this behavior, use the [includeAssetSourceTypes](../phfetchoptions/includeassetsourcetypes.md) property in the `options` parameter.

## See Also

### Fetching Assets

- [Fetching Assets](../../photokit/fetching-assets.md) — Retrieve asset metadata or request full asset content.
- [+ fetchAssetsInAssetCollection:options:](<fetchassets(in_options_).md>) — Retrieves assets from the specified asset collection.
- [+ fetchAssetsWithLocalIdentifiers:options:](<fetchassets(withlocalidentifiers_options_).md>) — Retrieves assets with the specified local-device-specific unique identifiers.
- [+ fetchKeyAssetsInAssetCollection:options:](<fetchkeyassets(in_options_).md>) — Retrieves assets marked as key assets in the specified asset collection.
- [+ fetchAssetsWithOptions:](<fetchassets(with_).md>) — Retrieves all assets matching the specified options.
- [+ fetchAssetsWithBurstIdentifier:options:](<fetchassets(withburstidentifier_options_).md>) — Retrieves assets with the specified burst photo sequence identifier.
- [+ fetchAssetsWithALAssetURLs:options:](<fetchassets(withalasseturls_options_).md>) — Retrieves assets using URLs provided by the Assets Library framework. _(deprecated)_
