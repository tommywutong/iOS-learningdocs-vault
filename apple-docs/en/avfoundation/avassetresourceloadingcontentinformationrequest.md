---
title: AVAssetResourceLoadingContentInformationRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingcontentinformationrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingcontentinformationrequest.json'
content_hash: 'sha256:517d3666e14ed95b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoadingContentInformationRequest

<sub>Class</sub>

A query for retrieving essential information about a resource that an asset resource-loading request references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceLoadingContentInformationRequest
```

## Overview

When a resource loading delegate, which must implement the [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) protocol, receives an instance of [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) when the [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<avassetresourceloaderdelegate/resourceloader(__shouldwaitforloadingofrequestedresource_).md>) is invoked and accepts responsibility for loading the resource, it must check whether the [contentInformationRequest](avassetresourceloadingrequest/contentinformationrequest.md) property of the [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) is not `nil`. Whenever the value is not `nil`, the request includes a query for the information that `AVAssetResourceLoadingContentInformationRequest` encapsulates. In response to such queries, the resource loading delegate should set the values of the content information request’s properties appropriately before invoking the [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) method [- finishLoading](<avassetresourceloadingrequest/finishloading().md>).

When [- finishLoading](<avassetresourceloadingrequest/finishloading().md>) is invoked, the values of the properties of its [contentInformationRequest](avassetresourceloadingrequest/contentinformationrequest.md) property will, in part, determine how the requested resource is processed. For example, if the requested resource’s URL is the URL of an [AVURLAsset](avurlasset.md) and [contentType](avassetresourceloadingcontentinformationrequest/contenttype.md) is set by the resource loading delegate to a value that the underlying media system doesn’t recognize as a supported media file type, operations on the `AVURLAsset`, such as playback, are likely to fail.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring content information

- [allowedContentTypes](avassetresourceloadingcontentinformationrequest/allowedcontenttypes.md) — The types of data that are accepted as a valid response for the requested resource.
- [contentType](avassetresourceloadingcontentinformationrequest/contenttype.md) — The UTI that specifies the type of data contained by the requested resource.
- [contentLength](avassetresourceloadingcontentinformationrequest/contentlength.md) — The length, in bytes, of the requested resource.
- [byteRangeAccessSupported](avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported.md) — A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [renewalDate](avassetresourceloadingcontentinformationrequest/renewaldate.md) — The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [entireLengthAvailableOnDemand](avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand.md) — A Boolean value that indicates whether asset data loading can expect data immediately.

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
