---
title: AVAssetResourceLoader
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloader
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloader.json'
content_hash: 'sha256:a6228405362a16e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoader

<sub>Class</sub>

An object that mediates resource requests from a URL asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceLoader
```

## Overview

You do not create resource loader objects yourself. Instead, you retrieve a resource loader from the [resourceLoader](avurlasset/resourceloader.md) property of an [AVURLAsset](avurlasset.md) object and use it to assign your custom delegate object.

The delegate you associate with this object must adopt the [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) protocol. For more information, see [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the delegate

- [- setDelegate:queue:](<avassetresourceloader/setdelegate(__queue_).md>) — Sets the delegate and dispatch queue to use with the resource loader.
- [delegate](avassetresourceloader/delegate.md) — The delegate object to use when handling resource requests.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [delegateQueue](avassetresourceloader/delegatequeue.md) — The dispatch queue to use when handling resource requests.

### Loading content keys

- [preloadsEligibleContentKeys](avassetresourceloader/preloadseligiblecontentkeys.md) — A Boolean value that indicates whether content keys will be loaded as quickly as possible.

### Supporting Common Media Client Data

- [sendsCommonMediaClientDataAsHTTPHeaders](avassetresourceloader/sendscommonmediaclientdataashttpheaders.md) — A Boolean value that indicates whether to enable attaching Common Media Client Data as HTTP request headers.

## See Also

### Resource loading

- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
