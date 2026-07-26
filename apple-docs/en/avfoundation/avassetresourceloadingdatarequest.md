---
title: AVAssetResourceLoadingDataRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingdatarequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingdatarequest.json'
content_hash: 'sha256:91a04660938bd356'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoadingDataRequest

<sub>Class</sub>

An object for requesting data from a resource that an asset resource-loading request references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceLoadingDataRequest
```

## Overview

The [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) uses the `AVAssetResourceLoadingDataRequest` class to do the actual data reading, and its methods will be invoked, as necessary, to acquire data for the [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) instance.

When the resource loading delegate, which implements the [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) protocol, receives an instance of [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) as the second parameter of the delegate’s [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<avassetresourceloaderdelegate/resourceloader(__shouldwaitforloadingofrequestedresource_).md>) method, it has the option of accepting responsibility for loading the referenced resource. If it accepts that responsibility, by returning [true](../swift/true.md), it must check whether the [dataRequest](avassetresourceloadingrequest/datarequest.md) property of the [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) instance is not `nil`. If it is not `nil`, the resource loading delegate is informed of the range of bytes within the resource that are required by the underlying media system. In response, the data is provided by one or more invocations of [- respondWithData:](<avassetresourceloadingdatarequest/respond(with_).md>) as required to provide the requested data. The data can be provided in increments determined by the resource loading delegate according to convenience or efficiency.

When the [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) method [- finishLoading](<avassetresourceloadingrequest/finishloading().md>) is invoked, the data request is considered fully satisfied. If the entire range of bytes requested has not yet been provided, the underlying media system assumes that the resource’s length is limited to the provided content.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Providing data to a request

- [- respondWithData:](<avassetresourceloadingdatarequest/respond(with_).md>) — Provides data to the loading request.
- [requestedLength](avassetresourceloadingdatarequest/requestedlength.md) — The length, in bytes, of the data requested.
- [requestedOffset](avassetresourceloadingdatarequest/requestedoffset.md) — The position within the resource of the first byte requested.
- [currentOffset](avassetresourceloadingdatarequest/currentoffset.md) — The position within the resource of the next byte.
- [requestsAllDataToEndOfResource](avassetresourceloadingdatarequest/requestsalldatatoendofresource.md) — A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
