---
title: contentType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contenttype
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest/contenttype.json'
content_hash: 'sha256:2abcde44b84846c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md)

# contentType

<sub>Instance Property</sub>

The UTI that specifies the type of data contained by the requested resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentType: String? { get set }
```

## Discussion

Before finishing loading an [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md) instance, if its [contentInformationRequest](../avassetresourceloadingrequest/contentinformationrequest.md) property is  not `nil`, set the value of this property to a UTI indicating the type of data contained by the requested resource.

When responding to an `AVAssetResourceLoadingRequest` for a FairPlay Streaming key, only set `contentType` to [AVStreamingKeyDeliveryContentKeyType](../avstreamingkeydeliverycontentkeytype.md), [AVStreamingKeyDeliveryPersistentContentKeyType](../avstreamingkeydeliverypersistentcontentkeytype.md), or `nil`. The value of contentType must be contained in the [allowedContentTypes](allowedcontenttypes.md) property or `nil`.

## See Also

### Configuring content information

- [allowedContentTypes](allowedcontenttypes.md) — The types of data that are accepted as a valid response for the requested resource.
- [contentLength](contentlength.md) — The length, in bytes, of the requested resource.
- [byteRangeAccessSupported](isbyterangeaccesssupported.md) — A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [renewalDate](renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [entireLengthAvailableOnDemand](isentirelengthavailableondemand.md) — A Boolean value that indicates whether asset data loading can expect data immediately.
