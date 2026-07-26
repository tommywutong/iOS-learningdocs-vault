---
title: contentLength
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contentlength
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contentlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contentlength.json'
content_hash: 'sha256:30ae4b20841957cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md)

# contentLength

<sub>Instance Property</sub>

The length, in bytes, of the requested resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentLength: Int64 { get set }
```

## Discussion

Before finishing loading an [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance, if its [contentInformationRequest](../avassetresourceloadingrequest/contentinformationrequest.md) property is not `nil`, set the value of the `contentLength` property to the number of bytes contained by the requested resource.

## See Also

### Configuring content information

- [allowedContentTypes](allowedcontenttypes.md) — The types of data that are accepted as a valid response for the requested resource.
- [contentType](contenttype.md) — The UTI that specifies the type of data contained by the requested resource.
- [byteRangeAccessSupported](isbyterangeaccesssupported.md) — A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [renewalDate](renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [entireLengthAvailableOnDemand](isentirelengthavailableondemand.md) — A Boolean value that indicates whether asset data loading can expect data immediately.
