---
title: AVAssetResourceLoaderDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloaderdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate.json'
content_hash: 'sha256:6d0e768f8c4e18d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoaderDelegate

<sub>Protocol</sub>

Methods you can implement to handle resource-loading requests coming from a URL asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVAssetResourceLoaderDelegate : NSObjectProtocol
```

## Overview

A class should adopt this protocol when associated with the asset’s resource loader—that is, an instance of the [AVAssetResourceLoader](avassetresourceloader.md) class. The resource loader works with your delegate to process the request.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Processing resource requests

- [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<avassetresourceloaderdelegate/resourceloader(__shouldwaitforloadingofrequestedresource_).md>) — Asks the delegate if it wants to load the requested resource.
- [- resourceLoader:shouldWaitForRenewalOfRequestedResource:](<avassetresourceloaderdelegate/resourceloader(__shouldwaitforrenewalofrequestedresource_).md>) — Tells the delegate when assistance is required of the application to renew a resource.
- [- resourceLoader:didCancelLoadingRequest:](<avassetresourceloaderdelegate/resourceloader(__didcancel_)-3nl51.md>) — Informs the delegate that a prior loading request has been cancelled.

### Processing authentication challenges

- [- resourceLoader:shouldWaitForResponseToAuthenticationChallenge:](<avassetresourceloaderdelegate/resourceloader(__shouldwaitforresponseto_).md>) — Tells the delegate that assistance is required of the application to respond to an authentication challenge.
- [- resourceLoader:didCancelAuthenticationChallenge:](<avassetresourceloaderdelegate/resourceloader(__didcancel_)-1wqin.md>) — Informs the delegate that a prior authentication challenge has been cancelled.

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md) — An object that encapsulates information about a resource request from a resource loader object.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
