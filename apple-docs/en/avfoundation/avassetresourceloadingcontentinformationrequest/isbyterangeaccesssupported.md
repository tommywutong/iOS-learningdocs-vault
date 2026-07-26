---
title: isByteRangeAccessSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported.json'
content_hash: 'sha256:3f3c2e7508a88093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md)

# isByteRangeAccessSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isByteRangeAccessSupported: Bool { get set }
```

## Discussion

Before finishing loading an [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance, if its [contentInformationRequest](../avassetresourceloadingrequest/contentinformationrequest.md) property is not `nil`, set the value of this property to [true](../../swift/true.md) if it supports random access to arbitrary ranges of bytes of the resource.

If this property is not [true](../../swift/true.md) for resources that must be loaded incrementally, loading of the resource may fail. Such resources include anything that contains media data.

If byte range access is supported  portions of the resource can be requested more than once.

## See Also

### Configuring content information

- [allowedContentTypes](allowedcontenttypes.md) — The types of data that are accepted as a valid response for the requested resource.
- [contentType](contenttype.md) — The UTI that specifies the type of data contained by the requested resource.
- [contentLength](contentlength.md) — The length, in bytes, of the requested resource.
- [renewalDate](renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [entireLengthAvailableOnDemand](isentirelengthavailableondemand.md) — A Boolean value that indicates whether asset data loading can expect data immediately.
