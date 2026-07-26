---
title: AVURLAssetURLRequestAttributionKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avurlasseturlrequestattributionkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasseturlrequestattributionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasseturlrequestattributionkey.json'
content_hash: 'sha256:4e763cad85ddb23c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVURLAssetURLRequestAttributionKey

<sub>Global Variable</sub>

A value that specifies the attribution of the URLs that this asset requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVURLAssetURLRequestAttributionKey: String
```

## Discussion

The value is a number that represents an [NSURLRequest.Attribution](../foundation/nsurlrequest/attribution-swift.enum.md). URL requests that the system issues on behalf of the asset attribute this value and follow the App Privacy Policy accordingly.

The default value is [NSURLRequest.Attribution.developer](../foundation/nsurlrequest/attribution-swift.enum/developer.md).

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
- [AVURLAssetShouldSupportAliasDataReferencesKey](avurlassetshouldsupportaliasdatareferenceskey.md) — A Boolean value that indicates whether the system parses and resolves alias data references in the asset.
- [AVURLAssetShouldParseExternalSphericalTagsKey](avurlassetshouldparseexternalsphericaltagskey.md) — Indicates whether additional projected media signaling in the asset should be parsed and resolved as format description extensions.
