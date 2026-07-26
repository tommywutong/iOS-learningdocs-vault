---
title: prefetchAssetExtendedMetadata
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phfetchoptions/prefetchassetextendedmetadata
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/prefetchassetextendedmetadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/prefetchassetextendedmetadata.json'
content_hash: 'sha256:079b634357db3ebb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# prefetchAssetExtendedMetadata

<sub>Instance Property</sub>

A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var prefetchAssetExtendedMetadata: Bool { get set }
```

## Discussion

By default `extendedMetadata` is fetched on demand, with the dot accessor. Prefetching will fetch it as part of the `PHAsset` in a single fetch, rather than incurring fetch overhead for each `PHAsset`.

## See Also

### Limiting Fetch Results

- [fetchLimit](fetchlimit.md) — The maximum number of objects to include in the fetch result.
- [includeAllBurstAssets](includeallburstassets.md) — A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [includeHiddenAssets](includehiddenassets.md) — A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [includeAssetSourceTypes](includeassetsourcetypes.md) — The set of source types for which to include assets in the fetch result.
