---
title: isEntireLengthAvailableOnDemand
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand.json'
content_hash: 'sha256:623d566b31856492'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md)

# isEntireLengthAvailableOnDemand

<sub>Instance Property</sub>

A Boolean value that indicates whether asset data loading can expect data immediately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isEntireLengthAvailableOnDemand: Bool { get set }
```

## Discussion

Before you finish loading an [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md), if its [contentInformationRequest](../avassetresourceloadingrequest/contentinformationrequest.md) isn’t `nil`, set the value to [true](../../swift/true.md) to indicate that all asset data is available. This may be [true](../../swift/true.md) because the data is fully cached, or because the custom URL scheme ultimately refers to files on local storage, which allows for significant data flow optimizations.

For backward compatibility, this property defaults to [false](../../swift/false.md).

## See Also

### Configuring content information

- [allowedContentTypes](allowedcontenttypes.md) — The types of data that are accepted as a valid response for the requested resource.
- [contentType](contenttype.md) — The UTI that specifies the type of data contained by the requested resource.
- [contentLength](contentlength.md) — The length, in bytes, of the requested resource.
- [byteRangeAccessSupported](isbyterangeaccesssupported.md) — A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [renewalDate](renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
