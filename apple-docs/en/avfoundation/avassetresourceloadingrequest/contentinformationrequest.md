---
title: contentInformationRequest
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/contentinformationrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/contentinformationrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/contentinformationrequest.json'
content_hash: 'sha256:947c27e4ed85ae9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# contentInformationRequest

<sub>Instance Property</sub>

The information for a requested resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest? { get }
```

## Discussion

An instance of [AVAssetResourceLoadingContentInformationRequest](../avassetresourceloadingcontentinformationrequest.md) that you populate with information about the resource. The value of this property is `nil` if no such information is being requested.

## See Also

### Accessing the request data

- [request](request.md) — The URL request object for the resource.
- [requestor](requestor.md) — The asset resource requestor that made the request.
- [dataRequest](datarequest.md) — The range of requested resource data.
- [redirect](redirect.md) — An URL request instance if the loading request was redirected.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_
