---
title: request
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/request
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/request.json'
content_hash: 'sha256:719d53cd780e3a1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# request

<sub>Instance Property</sub>

The URL request object for the resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var request: URLRequest { get }
```

## Discussion

Use the value in this property to identify the requested resource and to formulate an appropriate response object.

## See Also

### Accessing the request data

- [requestor](requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](datarequest.md) — The range of requested resource data.
- [redirect](redirect.md) — An URL request instance if the loading request was redirected.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_
