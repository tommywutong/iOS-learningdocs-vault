---
title: fetchLimit
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions/fetchlimit
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/fetchlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/fetchlimit.json'
content_hash: 'sha256:3e0da28bf429c9f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# fetchLimit

<sub>Instance Property</sub>

The maximum number of objects to include in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fetchLimit: Int { get set }
```

## Discussion

With the default fetch limit of zero, Photos returns all requested assets or collections in a fetch result. Change this value to fetch more efficiently in situations where a potentially very large result is not needed. For example, to fetch only the most recently captured asset, call the [+ fetchAssetsWithOptions:](<../phasset/fetchassets(with_).md>) method, using the [sortDescriptors](sortdescriptors.md) property to sort in descending date order, and setting a fetch limit of one.

## See Also

### Limiting Fetch Results

- [includeAllBurstAssets](includeallburstassets.md) — A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [includeHiddenAssets](includehiddenassets.md) — A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [includeAssetSourceTypes](includeassetsourcetypes.md) — The set of source types for which to include assets in the fetch result.
- [prefetchAssetExtendedMetadata](prefetchassetextendedmetadata.md) — A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched. _(beta)_
