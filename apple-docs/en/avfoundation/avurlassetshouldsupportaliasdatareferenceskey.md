---
title: AVURLAssetShouldSupportAliasDataReferencesKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlassetshouldsupportaliasdatareferenceskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlassetshouldsupportaliasdatareferenceskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlassetshouldsupportaliasdatareferenceskey.json'
content_hash: 'sha256:680c8851aaa023c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVURLAssetShouldSupportAliasDataReferencesKey

<sub>Global Variable</sub>

A Boolean value that indicates whether the system parses and resolves alias data references in the asset.

<sub>macOS</sub>

```swift
let AVURLAssetShouldSupportAliasDataReferencesKey: String
```

## Discussion

Most QuickTime movie files contain all of the media data they require, but some contain references to media in other files. While AVFoundation and CoreMedia typically employ a URL reference for this purpose, older implementations commonly use a Macintosh alias instead, as the QuickTime File Format specification documents. Specify this option if your app must work with legacy QuickTime movie files that contain alias-based references to media data in other files.

If you provide a value for [AVURLAssetReferenceRestrictionsKey](avurlassetreferencerestrictionskey.md), the system observes restrictions for resolved alias references like it does for URL references.

## See Also

### Options

- [AVURLAssetAllowsCellularAccessKey](avurlassetallowscellularaccesskey.md) — A Boolean value that indicates whether the system can make network requests on behalf of the asset when connected to a cellular network.
- [AVURLAssetAllowsConstrainedNetworkAccessKey](avurlassetallowsconstrainednetworkaccesskey.md) — A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the constrained interface.
- [AVURLAssetAllowsExpensiveNetworkAccessKey](avurlassetallowsexpensivenetworkaccesskey.md) — A Boolean value that indicates whether the system allows network requests on behalf of this asset to use the expensive interface.
- [AVURLAssetHTTPCookiesKey](avurlassethttpcookieskey.md) — The HTTP cookies that a URL asset may send with HTTP requests.
- [AVURLAssetHTTPUserAgentKey](avurlassethttpuseragentkey.md) — A key that specifies the user agent of requests that an asset makes.
- [AVURLAssetOverrideMIMETypeKey](avurlassetoverridemimetypekey.md) — A key that specifies the MIME type to use to identify the format of a media resource.
- [AVURLAssetPreferPreciseDurationAndTimingKey](avurlassetpreferprecisedurationandtimingkey.md) — A Boolean value that indicates whether the asset should provide accurate duration and precise random access by time.
- [AVURLAssetPrimarySessionIdentifierKey](avurlassetprimarysessionidentifierkey.md) — Specifies a UUID to set as the session identifier for HTTP requests that the asset makes.
- [AVURLAssetReferenceRestrictionsKey](avurlassetreferencerestrictionskey.md) — A value that represents the restrictions used by the asset when resolving references to external media data.
- [AVURLAssetURLRequestAttributionKey](avurlasseturlrequestattributionkey.md) — A value that specifies the attribution of the URLs that this asset requests.
- [AVURLAssetShouldParseExternalSphericalTagsKey](avurlassetshouldparseexternalsphericaltagskey.md) — Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions.
