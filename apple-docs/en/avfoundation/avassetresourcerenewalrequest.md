---
title: AVAssetResourceRenewalRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourcerenewalrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourcerenewalrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourcerenewalrequest.json'
content_hash: 'sha256:386ea1d2aa997ad8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceRenewalRequest

<sub>Class</sub>

An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceRenewalRequest
```

## Overview

When an [AVURLAsset](avurlasset.md) needs to renew a resource, because the [renewalDate](avassetresourceloadingcontentinformationrequest/renewaldate.md) has been set on a previous loading request, it asks its [AVAssetResourceLoader](avassetresourceloader.md) object to assist. The resource loader encapsulates the request information by creating an instance of this object, which it then hands to its delegate for processing. The delegate uses the information in this object to perform the request and report on the success or failure of the operation.

The `AVAssetResourceRenewalRequest` class is a subclass of [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md).

## Relationships

- **Inherits From**: [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
