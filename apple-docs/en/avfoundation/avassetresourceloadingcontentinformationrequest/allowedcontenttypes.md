---
title: allowedContentTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.2+, iPadOS 11.2+, Mac Catalyst 13.1+, macOS 10.13.2+, tvOS 11.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest/allowedcontenttypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/allowedcontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/allowedcontenttypes.json'
content_hash: 'sha256:1987f78bc19cc9ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md)

# allowedContentTypes

<sub>Instance Property</sub>

The types of data that are accepted as a valid response for the requested resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var allowedContentTypes: [String]? { get }
```

## Discussion

This property contains an array of file format UTIs. When `allowedContentTypes` is non-nil, the value of [contentType](contenttype.md) must be set to a value contained in `allowedContentTypes` or `nil`.

## See Also

### Configuring content information

- [contentType](contenttype.md) — The UTI that specifies the type of data contained by the requested resource.
- [contentLength](contentlength.md) — The length, in bytes, of the requested resource.
- [byteRangeAccessSupported](isbyterangeaccesssupported.md) — A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [renewalDate](renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [entireLengthAvailableOnDemand](isentirelengthavailableondemand.md) — A Boolean value that indicates whether asset data loading can expect data immediately.
