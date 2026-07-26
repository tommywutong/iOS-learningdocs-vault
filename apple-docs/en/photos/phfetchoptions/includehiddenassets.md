---
title: includeHiddenAssets
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions/includehiddenassets
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/includehiddenassets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/includehiddenassets.json'
content_hash: 'sha256:016d349bed4b4f5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# includeHiddenAssets

<sub>Instance Property</sub>

A Boolean value that determines whether the fetch result includes assets marked as hidden.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var includeHiddenAssets: Bool { get set }
```

## Discussion

If the value is `false` (the default), fetches exclude assets whose [hidden](../phasset/ishidden.md) property is `true`. If the value is `true`, fetches include all assets regardless of their hidden state.

## See Also

### Limiting Fetch Results

- [fetchLimit](fetchlimit.md) — The maximum number of objects to include in the fetch result.
- [includeAllBurstAssets](includeallburstassets.md) — A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [includeAssetSourceTypes](includeassetsourcetypes.md) — The set of source types for which to include assets in the fetch result.
- [prefetchAssetExtendedMetadata](prefetchassetextendedmetadata.md) — A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched. _(beta)_
