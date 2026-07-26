---
title: redirect
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetresourceloadingrequest/redirect
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest/redirect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequest/redirect.json'
content_hash: 'sha256:18b5e6b4497760ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoadingRequest](../avassetresourceloadingrequest.md)

# redirect

<sub>Instance Property</sub>

An URL request instance if the loading request was redirected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var redirect: URLRequest? { get set }
```

## Discussion

Set this property to an instance of [NSURLRequest](../../foundation/nsurlrequest.md) indicating a redirection of the loading request to another URL.

If no redirection is needed, the value of this property must be `nil`, which is the default.

## See Also

### Accessing the request data

- [request](request.md) — The URL request object for the resource.
- [requestor](requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](datarequest.md) — The range of requested resource data.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
- [AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey](../avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md) — Specifies whether the content key request requires a persistable key to be returned from the key vendor. _(deprecated)_
