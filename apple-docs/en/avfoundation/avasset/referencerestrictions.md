---
title: referenceRestrictions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasset/referencerestrictions
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/referencerestrictions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/referencerestrictions.json'
content_hash: 'sha256:14de37debb8377ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# referenceRestrictions

<sub>Instance Property</sub>

The restrictions that an asset places on how it resolves references to external media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var referenceRestrictions: AVAssetReferenceRestrictions { get }
```

## Discussion

For [AVURLAsset](../avurlasset.md), this property reflects the value passed in for [AVURLAssetReferenceRestrictionsKey](../avurlassetreferencerestrictionskey.md), if any.

The default value for this property is [AVAssetReferenceRestrictionDefaultPolicy](../avassetreferencerestrictions/defaultpolicy.md). See [AVURLAssetReferenceRestrictionsKey](../avurlassetreferencerestrictionskey.md) for more information about reference restrictions.

## See Also

### Retrieving reference restrictions

- [AVAssetReferenceRestrictions](../avassetreferencerestrictions.md) — Restrictions to use when resolving references to external media data.
