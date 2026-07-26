---
title: AVAssetResourceLoadingRequestor
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequestor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequestor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequestor.json'
content_hash: 'sha256:3ceb9d3bf5e030a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoadingRequestor

<sub>Class</sub>

An object that contains information about the originator of a resource-loading request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceLoadingRequestor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Retrieving expired session reports

- [providesExpiredSessionReports](avassetresourceloadingrequestor/providesexpiredsessionreports.md) — A Boolean value that indicates whether the requestor provides expired session reports.

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
