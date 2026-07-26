---
title: AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（18.0 起废弃）, iPadOS 9.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.json'
content_hash: 'sha256:5ef7bb96ecf8ec7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey

<sub>Global Variable</sub>

Specifies whether the content key request requires a persistable key to be returned from the key vendor.

> [!warning] Deprecated
> Use -[AVPersistableContentKeyRequest persistableContentKeyFromKeyVendorResponse:options:error:] instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String
```

## See Also

### Accessing the request data

- [request](avassetresourceloadingrequest/request.md) — The URL request object for the resource.
- [requestor](avassetresourceloadingrequest/requestor.md) — The asset resource requestor that made the request.
- [contentInformationRequest](avassetresourceloadingrequest/contentinformationrequest.md) — The information for a requested resource.
- [dataRequest](avassetresourceloadingrequest/datarequest.md) — The range of requested resource data.
- [redirect](avassetresourceloadingrequest/redirect.md) — An URL request instance if the loading request was redirected.
- [- streamingContentKeyRequestDataForApp:contentIdentifier:options:error:](<avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp_contentidentifier_options_).md>) — Obtains key request data for a specific combination of application and content. _(deprecated)_
- [- persistentContentKeyFromKeyVendorResponse:options:error:](<avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse_options_).md>) — Obtains a persistable content key from a context. _(deprecated)_
