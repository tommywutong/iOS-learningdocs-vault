---
title: AVURLAssetAllowsConstrainedNetworkAccessKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlassetallowsconstrainednetworkaccesskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlassetallowsconstrainednetworkaccesskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlassetallowsconstrainednetworkaccesskey.json'
content_hash: 'sha256:ab2a6c4f8abb3828'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVURLAssetAllowsConstrainedNetworkAccessKey

<sub>Global Variable</sub>

A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the constrained interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVURLAssetAllowsConstrainedNetworkAccessKey: String
```

## Discussion

The default value for this key is [true](../swift/true.md).

## See Also

### Options

- [AVURLAssetAllowsCellularAccessKey](avurlassetallowscellularaccesskey.md) — A Boolean value that indicates whether the system can make network requests on behalf of the asset when connected to a cellular network.
- [AVURLAssetAllowsExpensiveNetworkAccessKey](avurlassetallowsexpensivenetworkaccesskey.md) — A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the expensive interface.
- [AVURLAssetHTTPCookiesKey](avurlassethttpcookieskey.md) — The HTTP cookies that a URL asset may send with HTTP requests.
- [AVURLAssetHTTPUserAgentKey](avurlassethttpuseragentkey.md) — A key that specifies the user agent of requests that an asset makes.
- [AVURLAssetOverrideMIMETypeKey](avurlassetoverridemimetypekey.md) — A key that specifies the MIME type to use to identify the format of a media resource.
- [AVURLAssetPreferPreciseDurationAndTimingKey](avurlassetpreferprecisedurationandtimingkey.md) — A Boolean value that indicates whether the asset should provide accurate duration and precise random access by time.
- [AVURLAssetPrimarySessionIdentifierKey](avurlassetprimarysessionidentifierkey.md) — Specifies a UUID to set as the session identifier for HTTP requests that the asset makes.
- [AVURLAssetReferenceRestrictionsKey](avurlassetreferencerestrictionskey.md) — A value that represents the restrictions used by the asset when resolving references to external media data.
- [AVURLAssetShouldSupportAliasDataReferencesKey](avurlassetshouldsupportaliasdatareferenceskey.md) — A Boolean value that indicates whether the system parses and resolves alias data references in the asset.
- [AVURLAssetURLRequestAttributionKey](avurlasseturlrequestattributionkey.md) — A value that specifies the attribution of the URLs that this asset requests.
- [AVURLAssetShouldParseExternalSphericalTagsKey](avurlassetshouldparseexternalsphericaltagskey.md) — Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions.
