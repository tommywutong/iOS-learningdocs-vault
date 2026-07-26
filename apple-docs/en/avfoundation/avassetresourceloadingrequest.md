---
title: AVAssetResourceLoadingRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest.json'
content_hash: 'sha256:d5db0c6e5bd1f8c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoadingRequest

<sub>Class</sub>

An object that encapsulates information about a resource request from a resource loader object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetResourceLoadingRequest
```

## Overview

When an [AVURLAsset](avurlasset.md) object needs help loading a resource, it asks its [AVAssetResourceLoader](avassetresourceloader.md) object to assist. The resource loader encapsulates the request information by creating an instance of this object, which it then hands to its delegate object for processing. The delegate uses the information in this object to perform the request and report on the success or failure of the operation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the request data

- [request](avassetresourceloadingrequest/request.md) — The URL request object for the resource.
- [requestor](avassetresourceloadingrequest/requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](avassetresourceloadingrequest/contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](avassetresourceloadingrequest/datarequest.md) — The range of requested resource data.
- [redirect](avassetresourceloadingrequest/redirect.md) — An URL request instance if the loading request was redirected.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_

### Reporting the result of the request

- [response](avassetresourceloadingrequest/response.md) — The URL response for the loading request.
- [- finishLoading](<avassetresourceloadingrequest/finishloading().md>) — Causes the receiver to treat the processing of the request as complete.
- [cancelled](avassetresourceloadingrequest/iscancelled.md) — A Boolean value that indicates whether the request has been cancelled.
- [- finishLoadingWithError:](<avassetresourceloadingrequest/finishloading(with_).md>) — Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [finished](avassetresourceloadingrequest/isfinished.md) — A Boolean value that indicates whether loading of the resource has finished.
- [- finishLoadingWithResponse:data:redirect:](<avassetresourceloadingrequest/finishloading(with_data_redirect_).md>) — Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility . _(deprecated)_

## See Also

### Resource loading

- [AVAssetResourceLoader](avassetresourceloader.md) — An object that mediates resource requests from a URL asset.
- [AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md) — Methods you can implement to handle resource-loading requests coming from a URL asset.
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md) — An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md) — An object that contains information about the originator of a resource-loading request.
- [AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md) — An object for requesting data from a resource that an asset resource-loading request references.
- [AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md) — A query for retrieving essential information about a resource that an asset resource-loading request references.
