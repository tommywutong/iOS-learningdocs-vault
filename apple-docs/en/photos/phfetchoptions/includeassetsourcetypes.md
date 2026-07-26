---
title: includeAssetSourceTypes
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phfetchoptions/includeassetsourcetypes
source_url: 'https://developer.apple.com/documentation/photos/phfetchoptions/includeassetsourcetypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phfetchoptions/includeassetsourcetypes.json'
content_hash: 'sha256:c1ff5e496358d7c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHFetchOptions](../phfetchoptions.md)

# includeAssetSourceTypes

<sub>Instance Property</sub>

The set of source types for which to include assets in the fetch result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var includeAssetSourceTypes: PHAssetSourceType { get set }
```

## Discussion

Asset source types identify the means by which an asset enters the Photos library, and affect the possible actions you can perform on an asset. For example, assets synced from iTunes cannot be edited or deleted.

The [PHAssetSourceType](../phassetsourcetype.md) type is an option set—to include multiple source types in the same query, combine type constants with the bitwise OR operator (Objective-C) or OptionSetType set syntax (Swift).

## See Also

### Limiting Fetch Results

- [fetchLimit](fetchlimit.md) — The maximum number of objects to include in the fetch result.
- [includeAllBurstAssets](includeallburstassets.md) — A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [includeHiddenAssets](includehiddenassets.md) — A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [prefetchAssetExtendedMetadata](prefetchassetextendedmetadata.md) — A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched. _(beta)_
